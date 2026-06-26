
list = [1,2,3,4,5]

# for el in list
#===============================
index = 0
iterator = iter(list)
while True:
    try:
        el = next(iterator)
        #===============================

        print(el)

    except StopIteration:
        break


#===============================