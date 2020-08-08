# For more information view https://www.youtube.com/watch?v=5K08WcjGV6c

def list_comp1():
    list = [1, 3, 5, 7, 9, 11]
    new_list = []

    # This simple for loop ...
    for num in list:
        new_list.append(num * 2)

    print(new_list)

    # ... is the same as this
    new_list = [num * 2 for num in list]
    print(new_list, '\n')

def list_comp2():
    list = []

    # This simple for loop...
    for i in range(1, 7):
        list.append(i ** 2)
    print(list)

    #...is the same as
    list = [i ** 2 for i in range(1, 7)]
    print(list, '\n')

def list_comp3():
    list = []

    # This simple for loop...
    for i in range(-6, 0):
        list.append(i ** 2)
    print(list)

    # ... is the same as this
    list = [i ** 2 for i in range(-6, 0)]
    print(list)

list_comp1()
list_comp2()
list_comp3()