from aiogram.fsm.state import StatesGroup, State


class PracticeState(StatesGroup):
    waiting_variables_answer = State()