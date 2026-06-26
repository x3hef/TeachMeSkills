import time
import os
from colorama import Fore, init  # type: ignore[import-untyped]

init(autoreset=True)  # автоматический сброс цвета после каждой строки

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# эффект печатающегося текста
def type_text(text, speed=0.01):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()

# мигающий курсор
def cursor_blink(times=3):
    for _ in range(times):
        print("_", end="\r")
        time.sleep(0.2)
        print(" ", end="\r")
        time.sleep(0.2)

# анимированный прогресс бар
def progress_bar(duration=1.5, length=50):
    steps = int(duration / 0.01)
    for i in range(steps + 1):
        filled = int(i / steps * length)
        bar = "█" * filled + " " * (length - filled)
        print(Fore.GREEN + f"\r[{bar}] {int(i/steps*100)}%", end="")
        time.sleep(0.01)
    print()

def loading_screen():
    clear()
    print(Fore.GREEN)

    # Заголовки этапов
    type_text("ЗАПУСК СИСТЕМЫ...", 0.02)
    type_text("ПРОВЕРКА ФАЙЛОВ...", 0.015)
    type_text("ЗАГРУЗКА МОДУЛЕЙ...", 0.015)
    print()

    # Прогресс бар
    progress_bar(duration=1.5)

    # Название системы
    type_text("ИНИЦИАЛИЗАЦИЯ СИСТЕМЫ...", 0.02)
    print(r"""
███╗   ██╗███████╗    ███╗   ███╗ █████╗  ██████╗  █████╗ ███████╗██╗███╗   ██╗
████╗  ██║██╔════╝    ████╗ ████║██╔══██╗██╔════╝ ██╔══██╗╚══███╔╝██║████╗  ██║
██╔██╗ ██║█████╗      ██╔████╔██║███████║██║  ███╗███████║  ███╔╝ ██║██╔██╗ ██║
██║╚██╗██║██╔══╝      ██║╚██╔╝██║██╔══██║██║   ██║██╔══██║ ███╔╝  ██║██║╚██╗██║
██║ ╚████║███████╗    ██║ ╚═╝ ██║██║  ██║╚██████╔╝██║  ██║███████╗██║██║ ╚████║
╚═╝  ╚═══╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝
""")

    # Печатающийся приветственный текст
    type_text("ДОБРО ПОЖАЛОВАТЬ В СИСТЕМУ: НЕ МАГАЗИН", 0.02)
    cursor_blink(times=5)
    type_text("СИСТЕМА ГОТОВА К РАБОТЕ.", 0.02)
    time.sleep(0.5)

    clear()