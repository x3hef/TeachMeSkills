from content.lessons_data import LESSON_ORDER


def get_available_lessons(completed: set[str]) -> list[str]:
    if not LESSON_ORDER:
        return []

    available = []

    for index, lesson_key in enumerate(LESSON_ORDER):
        if index == 0:
            available.append(lesson_key)
            continue

        previous_lesson = LESSON_ORDER[index - 1]

        if previous_lesson in completed:
            available.append(lesson_key)
        else:
            break

    return available


def is_lesson_locked(lesson_key: str, completed: set[str]) -> bool:
    if lesson_key not in LESSON_ORDER:
        return True

    if lesson_key == LESSON_ORDER[0]:
        return False

    index = LESSON_ORDER.index(lesson_key)
    previous_lesson = LESSON_ORDER[index - 1]

    return previous_lesson not in completed
