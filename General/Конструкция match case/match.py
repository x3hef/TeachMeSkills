# Конструкция match/case

cmd = 'top'

match cmd:
    case "top":
        print("top")
    case "left":
        print("left")
    case "right":
        print("right")


match cmd:
    case "top":
        print("top")
    case "left":
        print("left")
    case command:
        print(command)

match cmd:
    case "top":
        print("top")
    case _:
        print("1")


