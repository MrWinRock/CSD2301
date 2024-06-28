import random


def loop1():
    for _ in range(100):
        print("Pharthiwath")


def loop2():
    for i in range(100):
        print(i+1, "Pharthiwath")


def loop3():
    for i in range(1, 21):
        print(i, "---", i**2)


def loop4():
    for i in range(8, 90, 3):
        print(i, end=", ")


def loop5():
    for i in range(100, 0, -2):
        print(i, end=", ")


def loop6():
    str = "AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG"
    seq = ""
    for c in str:
        if c in seq:
            continue
        seq += c
    print(seq)


def loop7():
    n = int(input("Amount of users: "))
    users = []
    for i in range(n):
        users.append(input(f"Username {i+1}: "))
    for user in users:
        print(user)


def loop8():
    n = int(input("Amount if Fibbonacci: "))
    a, b = 1, 1
    for _ in range(n):
        print(a, end=", ")
        a, b = b, a + b  # a = b, b = a + b


def loop9():
    h = int(input("Height: "))
    for i in range(1, h + 1):
        print('*' * i)


def loop10():
    start = 3
    end = 6
    for _ in range(50):
        print(random.randint(start, end), end=", ")


def loop11():
    x, y = random.randint(1, 50), random.randint(2, 5)
    print(x**y)


def loop12():
    n = random.randint(1, 10)
    for _ in range(n):
        print("Pharthiwath")


def loop13():
    for i in range(1, 11):
        for j in range(1, i + 1):
            print(i * j, end=" ")
        print()


def loop14():
    for i in range(1, 6):
        for j in range(i, 6):
            print(j, end=" ")
        print()


def main():
    "Uncomment each line and comment other lines to run the code"
    loop1()
    # loop2()
    # loop3()
    # loop4()
    # loop5()
    # loop6()
    # loop7()
    # loop8()
    # loop9()
    # loop10()
    # loop11()
    # loop12()
    # loop13()
    # loop14()


main()
