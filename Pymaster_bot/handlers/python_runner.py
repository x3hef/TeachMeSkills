import asyncio
import random

from aiogram import Router, F, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from database.requests import add_xp

router = Router()

runner_games = {}

WIDTH = 12
HEIGHT = 5

PLAYER_X = 2
GROUND_Y = 3
JUMP_Y = 2

TICK_SECONDS = 0.75

EMPTY = "⬛"
GROUND = "🟫"
PLAYER = "🐍"
COIN = "🪙"
BUG = "🐞"
PYTHON_COIN = "💎"


def runner_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⬆️ Прыжок",
                    callback_data="pyrunner_jump",
                )
            ],
            [
                InlineKeyboardButton(
                    text="⏹ Закончить",
                    callback_data="pyrunner_stop",
                )
            ],
        ]
    )


def finish_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔁 Играть снова",
                    callback_data="pyrunner_start",
                )
            ],
            [
                InlineKeyboardButton(
                    text="❌ Выйти",
                    callback_data="pyrunner_exit",
                )
            ],
        ]
    )


def cancel_old_game(user_id: int):
    old_game = runner_games.get(user_id)

    if not old_game:
        return

    task = old_game.get("task")

    if task and not task.done():
        task.cancel()

    runner_games.pop(user_id, None)


def create_game(user_id: int, chat_id: int, message_id: int | None = None):
    cancel_old_game(user_id)

    game = {
        "chat_id": chat_id,
        "message_id": message_id,
        "tick": 0,
        "score": 0,
        "coins": 0,
        "python_coins": 0,
        "jump_ticks": 0,
        "entities": [],
        "task": None,
        "finished": False,
    }

    runner_games[user_id] = game
    return game


def get_player_y(game):
    if game["jump_ticks"] > 0:
        return JUMP_Y

    return GROUND_Y


def spawn_entity(game):
    tick = game["tick"]

    if tick < 3:
        return

    if tick % 3 != 0:
        return

    last_entities = [
        entity for entity in game["entities"]
        if entity["x"] >= WIDTH - 4
    ]

    if last_entities:
        return

    chance = random.randint(1, 100)

    if chance <= 45:
        game["entities"].append(
            {
                "type": "coin",
                "x": WIDTH - 1,
                "y": random.choice([JUMP_Y, GROUND_Y]),
            }
        )
    elif chance <= 70:
        game["entities"].append(
            {
                "type": "python_coin",
                "x": WIDTH - 1,
                "y": random.choice([JUMP_Y, GROUND_Y]),
            }
        )
    else:
        game["entities"].append(
            {
                "type": "bug",
                "x": WIDTH - 1,
                "y": GROUND_Y,
                "passed": False,
            }
        )


def move_entities(game):
    for entity in game["entities"]:
        entity["x"] -= 1

    game["entities"] = [
        entity for entity in game["entities"]
        if entity["x"] >= 0
    ]


def check_collisions(game):
    player_y = get_player_y(game)

    new_entities = []

    for entity in game["entities"]:
        same_cell = entity["x"] == PLAYER_X and entity["y"] == player_y

        if same_cell:
            if entity["type"] == "coin":
                game["coins"] += 1
                game["score"] += 10
                continue

            if entity["type"] == "python_coin":
                game["python_coins"] += 1
                game["score"] += 25
                continue

            if entity["type"] == "bug":
                return "game_over"

        if entity["type"] == "bug":
            if entity["x"] < PLAYER_X and not entity.get("passed"):
                entity["passed"] = True
                game["score"] += 5

        new_entities.append(entity)

    game["entities"] = new_entities

    return "continue"


def make_step(game):
    if game["finished"]:
        return "finished"

    game["tick"] += 1
    game["score"] += 1

    if game["jump_ticks"] > 0:
        game["jump_ticks"] -= 1

    move_entities(game)
    spawn_entity(game)

    result = check_collisions(game)

    if result == "game_over":
        return "game_over"

    if game["tick"] >= 80:
        return "win"

    return "continue"


def render_game(game):
    field = []

    for y in range(HEIGHT):
        row = []

        for x in range(WIDTH):
            if y == HEIGHT - 1:
                row.append(GROUND)
            else:
                row.append(EMPTY)

        field.append(row)

    player_y = get_player_y(game)
    field[player_y][PLAYER_X] = PLAYER

    for entity in game["entities"]:
        x = entity["x"]
        y = entity["y"]

        if 0 <= x < WIDTH and 0 <= y < HEIGHT:
            if entity["type"] == "coin":
                field[y][x] = COIN

            elif entity["type"] == "python_coin":
                field[y][x] = PYTHON_COIN

            elif entity["type"] == "bug":
                field[y][x] = BUG

    rows = ["".join(row) for row in field]
    game_map = "\n".join(rows)

    progress = min(game["tick"], 80)
    progress_blocks = progress // 8
    progress_bar = "🟨" * progress_blocks + "⬛" * (10 - progress_blocks)

    return (
        "🕹️ <b>PYRUNNER</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        f"{game_map}\n\n"
        f"🪙 Монеты: <b>{game['coins']}</b>\n"
        f"💎 Python-монеты: <b>{game['python_coins']}</b>\n"
        f"⭐ Очки: <b>{game['score']}</b>\n\n"
        f"🏁 Прогресс:\n{progress_bar}\n\n"
        "⬆️ Прыгай через багов 🐞\n"
        "🪙 Собирай монеты\n"
        "💎 Python-монеты дают больше очков"
    )


async def finish_game_by_bot(bot: Bot, user_id: int, game, win: bool):
    game["finished"] = True

    task = game.get("task")
    current_task = asyncio.current_task()

    if task and not task.done() and task is not current_task:
        task.cancel()

    runner_games.pop(user_id, None)

    coins = game["coins"]
    python_coins = game["python_coins"]
    score = game["score"]

    xp = coins * 5 + python_coins * 15

    if win:
        xp += 30

    if xp > 150:
        xp = 150

    user = None

    if xp > 0:
        user = await add_xp(user_id, xp)

    if win:
        title = "🏁 <b>УРОВЕНЬ ПРОЙДЕН!</b>"
        comment = "🔥 Отлично! Ты добежал до конца Python-уровня."
    else:
        title = "💀 <b>ИГРА ОКОНЧЕНА</b>"
        comment = "🐞 Ты столкнулся с багом. Попробуй ещё раз."

    text = (
        f"{title}\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        f"🪙 Монеты: <b>{coins}</b>\n"
        f"💎 Python-монеты: <b>{python_coins}</b>\n"
        f"⭐ Очки: <b>{score}</b>\n"
        f"🎁 XP за игру: <b>+{xp}</b>\n\n"
        f"{comment}"
    )

    if user:
        text += (
            "\n\n"
            f"📈 Всего XP: <b>{user.xp}</b>\n"
            f"🏆 Уровень: <b>{user.level}</b>"
        )

    try:
        await bot.edit_message_text(
            chat_id=game["chat_id"],
            message_id=game["message_id"],
            text=text,
            parse_mode="HTML",
            reply_markup=finish_keyboard(),
        )
    except Exception:
        pass


async def runner_loop(user_id: int, bot: Bot):
    while user_id in runner_games:
        await asyncio.sleep(TICK_SECONDS)

        game = runner_games.get(user_id)

        if not game:
            return

        result = make_step(game)

        if result == "game_over":
            await finish_game_by_bot(bot, user_id, game, win=False)
            return

        if result == "win":
            await finish_game_by_bot(bot, user_id, game, win=True)
            return

        try:
            await bot.edit_message_text(
                chat_id=game["chat_id"],
                message_id=game["message_id"],
                text=render_game(game),
                parse_mode="HTML",
                reply_markup=runner_keyboard(),
            )
        except TelegramBadRequest:
            pass
        except Exception:
            pass


@router.message(F.text == "🕹️ PyRunner")
async def open_pyrunner(message: Message, bot: Bot):
    game = create_game(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
    )

    sent_message = await message.answer(
        render_game(game),
        parse_mode="HTML",
        reply_markup=runner_keyboard(),
    )

    game["message_id"] = sent_message.message_id

    game["task"] = asyncio.create_task(
        runner_loop(message.from_user.id, bot)
    )


@router.callback_query(F.data == "pyrunner_start")
async def restart_pyrunner(callback: CallbackQuery, bot: Bot):
    game = create_game(
        user_id=callback.from_user.id,
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
    )

    await callback.message.edit_text(
        render_game(game),
        parse_mode="HTML",
        reply_markup=runner_keyboard(),
    )

    game["task"] = asyncio.create_task(
        runner_loop(callback.from_user.id, bot)
    )

    await callback.answer()


@router.callback_query(F.data == "pyrunner_jump")
async def jump(callback: CallbackQuery):
    user_id = callback.from_user.id

    if user_id not in runner_games:
        await callback.answer("Сначала начни игру 🕹️", show_alert=True)
        return

    game = runner_games[user_id]

    if game["jump_ticks"] == 0:
        game["jump_ticks"] = 3
        await callback.answer("Прыжок!")
    else:
        await callback.answer("Ты уже в прыжке")


@router.callback_query(F.data == "pyrunner_stop")
async def stop_pyrunner(callback: CallbackQuery, bot: Bot):
    user_id = callback.from_user.id

    if user_id not in runner_games:
        await callback.answer("Игра уже остановлена", show_alert=True)
        return

    game = runner_games[user_id]

    await finish_game_by_bot(bot, user_id, game, win=False)
    await callback.answer()


@router.callback_query(F.data == "pyrunner_exit")
async def exit_pyrunner(callback: CallbackQuery):
    user_id = callback.from_user.id

    if user_id in runner_games:
        game = runner_games[user_id]

        task = game.get("task")

        if task and not task.done():
            task.cancel()

        runner_games.pop(user_id, None)

    await callback.message.edit_text(
        "🕹️ PyRunner закрыт.\n\n"
        "Можешь продолжать обучение 📚"
    )

    await callback.answer()
