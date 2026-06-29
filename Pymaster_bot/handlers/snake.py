import asyncio
import random

from aiogram import Router, F, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from database.requests import add_xp

router = Router()

snake_games = {}

FIELD_SIZE = 8
SPEED_SECONDS = 0.8

EMPTY = "⬛"
SNAKE_HEAD = "🟢"
SNAKE_BODY = "🟩"
FOOD = "🍎"


def create_snake_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="⬆️", callback_data="snake_move_up"),
            ],
            [
                InlineKeyboardButton(text="⬅️", callback_data="snake_move_left"),
                InlineKeyboardButton(text="⏹", callback_data="snake_stop"),
                InlineKeyboardButton(text="➡️", callback_data="snake_move_right"),
            ],
            [
                InlineKeyboardButton(text="⬇️", callback_data="snake_move_down"),
            ],
        ]
    )


def create_restart_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🔁 Играть снова", callback_data="snake_start"),
            ],
            [
                InlineKeyboardButton(text="❌ Выйти", callback_data="snake_exit"),
            ],
        ]
    )


def generate_food(snake):
    free_cells = []

    for y in range(FIELD_SIZE):
        for x in range(FIELD_SIZE):
            if (x, y) not in snake:
                free_cells.append((x, y))

    if not free_cells:
        return None

    return random.choice(free_cells)


def cancel_old_game(user_id: int):
    old_game = snake_games.get(user_id)

    if not old_game:
        return

    task = old_game.get("task")

    if task and not task.done():
        task.cancel()

    snake_games.pop(user_id, None)


def create_game(user_id: int, chat_id: int, message_id: int | None = None):
    cancel_old_game(user_id)

    snake = [
        (3, 4),
        (2, 4),
        (1, 4),
    ]

    food = generate_food(snake)

    snake_games[user_id] = {
        "snake": snake,
        "food": food,
        "direction": "right",
        "score": 0,
        "chat_id": chat_id,
        "message_id": message_id,
        "task": None,
    }

    return snake_games[user_id]


def render_game(game):
    snake = game["snake"]
    food = game["food"]
    score = game["score"]

    field = ""

    for y in range(FIELD_SIZE):
        row = ""

        for x in range(FIELD_SIZE):
            cell = (x, y)

            if cell == snake[0]:
                row += SNAKE_HEAD
            elif cell in snake:
                row += SNAKE_BODY
            elif cell == food:
                row += FOOD
            else:
                row += EMPTY

        field += row + "\n"

    return (
        "🐍 <b>SNAKE PYTHON</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        f"{field}\n"
        f"🍎 Очки: <b>{score}</b>\n\n"
        "Змейка идёт сама.\n"
        "Ты только меняешь направление 👇"
    )


def get_next_head(head, direction):
    x, y = head

    if direction == "up":
        return x, y - 1

    if direction == "down":
        return x, y + 1

    if direction == "left":
        return x - 1, y

    if direction == "right":
        return x + 1, y

    return x, y


def is_opposite_direction(old_direction, new_direction):
    opposites = {
        "up": "down",
        "down": "up",
        "left": "right",
        "right": "left",
    }

    return opposites.get(old_direction) == new_direction


def make_snake_step(game):
    snake = game["snake"]
    food = game["food"]
    direction = game["direction"]

    head = snake[0]
    new_head = get_next_head(head, direction)

    x, y = new_head

    if x < 0 or x >= FIELD_SIZE or y < 0 or y >= FIELD_SIZE:
        return "game_over"

    if new_head in snake:
        return "game_over"

    snake.insert(0, new_head)

    if new_head == food:
        game["score"] += 1
        game["food"] = generate_food(snake)

        if game["food"] is None:
            return "win"
    else:
        snake.pop()

    return "continue"


async def finish_game_by_bot(bot: Bot, user_id: int, game):
    score = game["score"]
    chat_id = game["chat_id"]
    message_id = game["message_id"]

    snake_games.pop(user_id, None)

    xp = score * 2

    user = None
    if xp > 0:
        user = await add_xp(user_id, xp)

    text = (
        "💀 <b>ИГРА ОКОНЧЕНА</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        f"🍎 Очки: <b>{score}</b>\n"
        f"⭐ XP за игру: <b>+{xp}</b>\n"
    )

    if user:
        text += (
            "\n"
            f"📈 Всего XP: <b>{user.xp}</b>\n"
            f"🏆 Уровень: <b>{user.level}</b>\n"
        )

    text += "\nХочешь сыграть ещё раз?"

    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=text,
        parse_mode="HTML",
        reply_markup=create_restart_keyboard(),
    )


async def snake_auto_loop(user_id: int, bot: Bot):
    while user_id in snake_games:
        await asyncio.sleep(SPEED_SECONDS)

        game = snake_games.get(user_id)

        if not game:
            return

        result = make_snake_step(game)

        if result in ("game_over", "win"):
            await finish_game_by_bot(bot, user_id, game)
            return

        try:
            await bot.edit_message_text(
                chat_id=game["chat_id"],
                message_id=game["message_id"],
                text=render_game(game),
                parse_mode="HTML",
                reply_markup=create_snake_keyboard(),
            )
        except TelegramBadRequest:
            pass
        except Exception:
            pass


@router.message(F.text == "🐍 Змейка")
async def start_snake_from_menu(message: Message, bot: Bot):
    game = create_game(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
    )

    sent_message = await message.answer(
        render_game(game),
        parse_mode="HTML",
        reply_markup=create_snake_keyboard(),
    )

    game["message_id"] = sent_message.message_id
    game["task"] = asyncio.create_task(
        snake_auto_loop(message.from_user.id, bot)
    )


@router.callback_query(F.data == "snake_start")
async def start_snake_from_button(callback: CallbackQuery, bot: Bot):
    game = create_game(
        user_id=callback.from_user.id,
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
    )

    await callback.message.edit_text(
        render_game(game),
        parse_mode="HTML",
        reply_markup=create_snake_keyboard(),
    )

    game["task"] = asyncio.create_task(
        snake_auto_loop(callback.from_user.id, bot)
    )

    await callback.answer()


@router.callback_query(F.data.startswith("snake_move_"))
async def change_direction(callback: CallbackQuery):
    user_id = callback.from_user.id

    if user_id not in snake_games:
        await callback.answer("Сначала начни игру 🐍", show_alert=True)
        return

    game = snake_games[user_id]

    new_direction = callback.data.replace("snake_move_", "")
    old_direction = game["direction"]

    if is_opposite_direction(old_direction, new_direction):
        await callback.answer("Назад резко нельзя 😄")
        return

    game["direction"] = new_direction

    await callback.answer("Направление изменено")


@router.callback_query(F.data == "snake_stop")
async def stop_snake(callback: CallbackQuery, bot: Bot):
    user_id = callback.from_user.id

    if user_id not in snake_games:
        await callback.answer("Игра уже остановлена", show_alert=True)
        return

    game = snake_games[user_id]

    task = game.get("task")
    if task and not task.done():
        task.cancel()

    await finish_game_by_bot(bot, user_id, game)
    await callback.answer()


@router.callback_query(F.data == "snake_exit")
async def exit_snake(callback: CallbackQuery):
    user_id = callback.from_user.id

    if user_id in snake_games:
        game = snake_games[user_id]

        task = game.get("task")
        if task and not task.done():
            task.cancel()

        snake_games.pop(user_id, None)

    await callback.message.edit_text(
        "🐍 Игра закрыта.\n\n"
        "Можешь вернуться к обучению 📚"
    )

    await callback.answer()
