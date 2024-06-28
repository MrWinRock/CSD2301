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
        print(i)


def loop5():
    for i in range(100, 0, -2):
        print(i)


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


def main():
    # loop1()
    # loop2()
    # loop3()
    # loop4()
    # loop5()
    loop6()
    # loop7()


main()
