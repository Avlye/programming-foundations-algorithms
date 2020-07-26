def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        countdown(x - 1)


def upto(x, limit):
    if x == limit:
        print("Done!")
        return
    else:
        print(x, "...")
        upto(x + 1, limit)


countdown(5)
upto(0, 20)