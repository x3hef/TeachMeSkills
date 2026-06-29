import os
import re
import json
import html
import asyncio

from dotenv import load_dotenv

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from handlers.states import PracticeState
from database.requests import add_xp, complete_lesson
from content.lessons_data import LESSONS

try:
    from google import genai
    from google.genai import types
except Exception:
    genai = None
    types = None


load_dotenv()

router = Router()


MENU_BUTTONS = {
    "🚀 Старт",
    "📚 Учиться",
    "🧠 Quiz",
    "🤖 AI Помощник",
    "🐍 Змейка",
    "🕹️ PyRunner",
    "🏆 Прогресс",
    "⚙️ Настройки",
}


SYSTEM_PROMPT = """
Ты AI Code Reviewer внутри Telegram-бота PyMaster Bot.

Твоя задача:
- проверять код ученика по Python;
- объяснять ошибки простым языком;
- не быть слишком строгим;
- давать оценку от 1 до 10;
- если код можно улучшить — показать улучшенный вариант;
- отвечать строго JSON.

Правила оценки:
10 — идеально
8-9 — хорошо, мелкие улучшения
6-7 — частично правильно, есть ошибки
4-5 — идея есть, но код слабый
1-3 — код почти не решает задачу

Верни строго JSON такого вида:
{
  "score": 8,
  "passed": true,
  "verdict": "Код в целом правильный",
  "feedback": [
    "Что хорошо",
    "Что исправить",
    "Почему это важно"
  ],
  "fixed_code": "исправленный код или пустая строка"
}
"""


def safe(value):
    return html.escape(str(value), quote=False)


def extract_json(text: str):
    text = text.strip()

    text = re.sub(r"^```json\s*", "", text)
    text = re.sub(r"^```\s*", "", text)
    text = re.sub(r"\s*```$", "", text)

    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1:
        raise ValueError("JSON не найден в ответе AI")

    json_text = text[start:end + 1]

    return json.loads(json_text)


def normalize_review(data: dict):
    score = data.get("score", 1)

    try:
        score = int(score)
    except Exception:
        score = 1

    if score < 1:
        score = 1

    if score > 10:
        score = 10

    passed = data.get("passed", score >= 7)

    verdict = data.get("verdict", "Код проверен.")

    feedback = data.get("feedback", [])

    if isinstance(feedback, str):
        feedback = [feedback]

    if not isinstance(feedback, list):
        feedback = ["AI не смог нормально оформить комментарии."]

    fixed_code = data.get("fixed_code", "")

    if fixed_code is None:
        fixed_code = ""

    return {
        "score": score,
        "passed": bool(passed),
        "verdict": str(verdict),
        "feedback": [str(item) for item in feedback],
        "fixed_code": str(fixed_code),
    }


def local_code_review(user_code: str, lesson_key: str, task: str):
    """
    Запасная проверка без AI.
    Нужна, чтобы бот не ломался, если Gemini временно недоступен.
    """

    feedback = []
    score = 1
    passed = False

    code = user_code.strip()

    if not code:
        return {
            "score": 1,
            "passed": False,
            "verdict": "Ты отправил пустой ответ.",
            "feedback": [
                "Напиши Python-код для задания.",
                "После этого отправь его снова.",
            ],
            "fixed_code": "",
        }

    try:
        compile(code, "<student_code>", "exec")
        score += 3
        feedback.append("Синтаксис Python выглядит корректно.")
    except SyntaxError as error:
        return {
            "score": 3,
            "passed": False,
            "verdict": "В коде есть синтаксическая ошибка.",
            "feedback": [
                f"Python не может прочитать код: {error.msg}.",
                "Проверь двоеточия, скобки и отступы.",
                "Исправь код и отправь ещё раз.",
            ],
            "fixed_code": "",
        }

    lowered = code.lower()

    if lesson_key == "variables":
        if "=" in code:
            score += 3
            feedback.append("Ты используешь переменную через оператор =.")
        else:
            feedback.append("В задании по переменным обычно нужен оператор =.")

    elif lesson_key == "types":
        if any(word in lowered for word in ["int", "str", "bool", "float", "type"]):
            score += 3
            feedback.append("Ты используешь тему типов данных.")
        else:
            feedback.append("Попробуй явно показать тип данных или использовать type().")

    elif lesson_key == "strings":
        if '"' in code or "'" in code:
            score += 3
            feedback.append("В коде есть строковые значения.")
        else:
            feedback.append("Для темы строк нужно использовать текст в кавычках.")

    elif lesson_key == "numbers":
        if any(ch.isdigit() for ch in code):
            score += 3
            feedback.append("Ты используешь числа.")
        else:
            feedback.append("Для темы чисел стоит использовать числовые значения.")

    elif lesson_key == "input_output":
        if "print" in lowered or "input" in lowered:
            score += 3
            feedback.append("Ты используешь ввод/вывод через print() или input().")
        else:
            feedback.append("Для темы ввода/вывода обычно нужны print() или input().")

    elif lesson_key == "conditions":
        if "if " in lowered:
            score += 3
            feedback.append("Ты используешь условие if.")
        else:
            feedback.append("В задании по условиям обычно нужен if.")

    elif lesson_key == "logic":
        if any(word in lowered for word in ["and", "or", "not"]):
            score += 3
            feedback.append("Ты используешь логические операторы.")
        else:
            feedback.append("Для темы логики стоит использовать and / or / not.")

    elif lesson_key == "for_loop":
        if "for " in lowered and "range" in lowered:
            score += 4
            feedback.append("Ты используешь цикл for и range().")
        elif "for " in lowered:
            score += 3
            feedback.append("Ты используешь цикл for.")
        else:
            feedback.append("Для этого задания нужен цикл for.")

    elif lesson_key == "while_loop":
        if "while " in lowered:
            score += 4
            feedback.append("Ты используешь цикл while.")
        else:
            feedback.append("Для этого задания нужен цикл while.")

    elif lesson_key == "functions":
        if "def " in lowered:
            score += 4
            feedback.append("Ты объявляешь функцию через def.")
        else:
            feedback.append("Для темы функций обычно нужно использовать def.")

    elif lesson_key == "lists":
        if "[" in code and "]" in code:
            score += 3
            feedback.append("Ты используешь список.")
        else:
            feedback.append("Для темы списков нужен список в квадратных скобках.")

    elif lesson_key == "dicts":
        if "{" in code and "}" in code and ":" in code:
            score += 3
            feedback.append("Ты используешь словарь.")
        else:
            feedback.append("Для темы словарей нужен dict с ключами и значениями.")

    elif lesson_key == "tuples_sets":
        if "(" in code or "{" in code:
            score += 3
            feedback.append("Ты используешь структуру, похожую на tuple или set.")
        else:
            feedback.append("Для темы tuple/set стоит использовать круглые скобки или set().")

    elif lesson_key == "exceptions":
        if "try" in lowered and "except" in lowered:
            score += 4
            feedback.append("Ты используешь try/except.")
        else:
            feedback.append("Для темы исключений обычно нужен try/except.")

    elif lesson_key == "files":
        if "open(" in lowered or "with " in lowered:
            score += 4
            feedback.append("Ты используешь работу с файлами.")
        else:
            feedback.append("Для темы файлов обычно нужен open() или with open().")

    elif lesson_key == "modules":
        if "import " in lowered or "from " in lowered:
            score += 4
            feedback.append("Ты используешь импорт модуля.")
        else:
            feedback.append("Для темы модулей обычно нужен import.")

    elif lesson_key in {"oop_basics", "classes_objects", "inheritance"}:
        if "class " in lowered:
            score += 4
            feedback.append("Ты используешь класс.")
        else:
            feedback.append("Для ООП-задания обычно нужен class.")

    else:
        if "print" in lowered:
            score += 2
            feedback.append("Ты используешь print() для вывода результата.")

    if "print" in lowered:
        score += 1

    if len(code.splitlines()) >= 2:
        score += 1

    if score > 10:
        score = 10

    if score >= 7:
        passed = True

    if passed:
        verdict = "Код выглядит достаточно хорошо для зачёта практики."
    else:
        verdict = "Код частично подходит, но его лучше доработать."

    return {
        "score": score,
        "passed": passed,
        "verdict": verdict,
        "feedback": feedback,
        "fixed_code": "",
    }


async def gemini_code_review(user_code: str, lesson_key: str):
    if genai is None or types is None:
        raise RuntimeError("google-genai не установлен")

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY не найден в .env")

    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    lesson = LESSONS.get(lesson_key, {})
    title = lesson.get("title", lesson_key)
    text = lesson.get("text", "")
    example_code = lesson.get("code", "")

    practice = lesson.get("practice", {})
    task = practice.get("task", "Проверь код ученика по теме урока.")

    prompt = f"""
Урок: {title}

Краткая теория урока:
{text}

Пример из урока:
```python
{example_code}
```

Практическое задание:
{task}

Код ученика:
```python
{user_code}
```

Проверь код ученика.
Верни только JSON по схеме из system instruction.
"""

    client = genai.Client(api_key=api_key)

    response = await asyncio.to_thread(
        client.models.generate_content,
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=0.2,
            max_output_tokens=900,
            response_mime_type="application/json",
        ),
    )

    answer_text = getattr(response, "text", None)

    if not answer_text:
        raise RuntimeError("Gemini вернул пустой ответ")

    data = extract_json(answer_text)

    return normalize_review(data)


def calculate_xp(score: int, passed: bool):
    if not passed:
        return 0

    if score >= 10:
        return 20

    if score >= 9:
        return 18

    if score >= 8:
        return 15

    if score >= 7:
        return 12

    return 0


def build_review_message(review: dict, user_code: str, lesson_key: str, source: str, xp: int, user):
    lesson = LESSONS.get(lesson_key, {})
    title = lesson.get("title", lesson_key)

    score = review["score"]
    passed = review["passed"]
    verdict = review["verdict"]
    feedback = review["feedback"]
    fixed_code = review["fixed_code"]

    if passed:
        status = "✅ <b>ПРАКТИКА ЗАСЧИТАНА</b>"
    else:
        status = "❌ <b>НУЖНО ДОРАБОТАТЬ</b>"

    feedback_text = ""

    for item in feedback[:6]:
        feedback_text += f"• {safe(item)}\n"

    if not feedback_text:
        feedback_text = "• Комментарии отсутствуют.\n"

    if source == "gemini":
        source_text = "🤖 Проверка: <b>Gemini AI</b>"
    else:
        source_text = "🧠 Проверка: <b>локальный fallback</b>"

    text = (
        "🤖 <b>AI CODE REVIEW</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        f"📘 Урок: <b>{safe(title)}</b>\n"
        f"{source_text}\n\n"
        f"{status}\n"
        f"Оценка: <b>{score} / 10</b>\n\n"
        f"💬 <b>Вердикт</b>\n"
        f"{safe(verdict)}\n\n"
        f"📌 <b>Разбор</b>\n"
        f"{feedback_text}\n"
        f"💻 <b>Твой код</b>\n"
        f"<pre><code>{safe(user_code)}</code></pre>"
    )

    if fixed_code.strip():
        text += (
            "\n\n"
            "✅ <b>Вариант исправления</b>\n"
            f"<pre><code>{safe(fixed_code)}</code></pre>"
        )

    if passed:
        text += (
            "\n\n"
            f"⭐ XP за практику: <b>+{xp}</b>"
        )

        if user:
            text += (
                "\n"
                f"📈 Всего XP: <b>{user.xp}</b>\n"
                f"🏆 Уровень: <b>{user.level}</b>"
            )

        text += (
            "\n\n"
            "🔥 Отлично. Можешь переходить к следующему уроку."
        )
    else:
        text += (
            "\n\n"
            "✍️ Исправь код и отправь его ещё раз."
        )

    return text


@router.message(PracticeState.waiting_variables_answer)
async def check_practice_answer(message: Message, state: FSMContext):
    if not message.text:
        await message.answer("Отправь ответ текстом с Python-кодом.")
        return

    if message.text in MENU_BUTTONS:
        await state.clear()
        await message.answer(
            "Практика остановлена.\n\n"
            "Нажми кнопку меню ещё раз."
        )
        return

    data = await state.get_data()
    lesson_key = data.get("lesson", "variables")

    lesson = LESSONS.get(lesson_key, {})
    practice = lesson.get("practice", {})
    task = practice.get("task", "Практическое задание")

    user_code = message.text.strip()

    thinking_message = await message.answer(
        "🤖 Проверяю твой код через AI Code Review..."
    )

    source = "gemini"

    try:
        review = await gemini_code_review(
            user_code=user_code,
            lesson_key=lesson_key,
        )

    except Exception as error:
        print("AI CODE REVIEW ERROR:", f"{type(error).__name__}: {error}")

        review = local_code_review(
            user_code=user_code,
            lesson_key=lesson_key,
            task=task,
        )

        source = "local"

    xp = calculate_xp(
        score=review["score"],
        passed=review["passed"],
    )

    user = None

    if review["passed"]:
        await complete_lesson(
            message.from_user.id,
            lesson_key,
        )

        if xp > 0:
            user = await add_xp(
                message.from_user.id,
                xp,
            )

        await state.clear()

    try:
        await thinking_message.delete()
    except Exception:
        pass

    await message.answer(
        build_review_message(
            review=review,
            user_code=user_code,
            lesson_key=lesson_key,
            source=source,
            xp=xp,
            user=user,
        ),
        parse_mode="HTML",
    )
