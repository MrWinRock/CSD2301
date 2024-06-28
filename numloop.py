def loop1():
    count = 0
    for i in range(1, 10000):
        if i % 3 == 0:
            count += 1
    print("Loop 1: ", count)


def loop2():
    count = 0
    for i in range(1, 10000):
        if i % 5 == 0:
            count += 1
    print("Loop 2: ", count)


def loop3():
    count = 0
    for i in range(1, 10000):
        if i % 3 == 0 and i % 5 == 0:
            count += 1
    print("Loop 3: ", count)


def loop4():
    count = 0
    for i in range(1, 10000):
        if i % 3 == 0 or i % 5 == 0:
            count += 1
    print("Loop 4: ", count)


def loop5():
    count = 0
    for i in range(1, 10000):
        if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
            count += 1
    print("Loop 5: ", count)


def loop6():
    count = 0
    for i in range(1, 10000):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            count += 1
    print("Loop 6: ", count)


def loop7():
    sum = 0
    for i in range(1, 10000):
        if i % 3 == 0:
            sum += i
    print("Loop 7: ", sum)


def loop8():
    sum = 0
    for i in range(1, 10000):
        if i % 5 == 0:
            sum += i
    print("Loop 8: ", sum)


def loop9():
    print("Loop 9: หายยยยยยย")


def loop10():
    sum = 0
    for i in range(1, 10000):
        if i % 3 == 0 and i % 5 == 0:
            sum += i
    print("Loop 10: ", sum)


def loop11():
    sum = 0
    for i in range(1, 10000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print("Loop 11: ", sum)


def loop12():
    sum = 0
    for i in range(1, 10000):
        if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
            sum += i
    print("Loop 12: ", sum)


def loop13():
    sum = 0
    for i in range(1, 10000):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            sum += i
    print("Loop 13: ", sum)


def main():
    loop1()
    loop2()
    loop3()
    loop4()
    loop5()
    loop6()
    loop7()
    loop8()
    loop9()
    loop10()
    loop11()
    loop12()
    loop13()


main()
