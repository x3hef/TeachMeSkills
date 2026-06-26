# Операторы * и ** для упаковки и распаковки

x, *y = [1,2,4,5]
print(x)
print(y)
x, *y = [1,2,3,4,5]
print(x)
print(y)

*x, y = 1,2,3,4  # type: ignore[assignment]
print(x)
print(y)
print(*x)  # type: ignore[misc]
