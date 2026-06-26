import pathlib

base_dir_path = pathlib.Path(__file__).resolve().parent.parent


print(pathlib.Path("file.txt"))


def check_path(path: pathlib.Path):
    text = str(path)
    if path.exists():
        text += " | exists"
    else:
        text += " | does not exist"

    if path.is_dir():
        text += " | is a directory"
    elif path.is_file():
        text += " | is a file"

    print(text)


check_path(base_dir_path)

file_name = "test.txt"

file_path = base_dir_path / file_name

check_path(file_path)

print("Создаём папку")
file_path.mkdir(parents=True, exist_ok=True)

check_path(file_path)