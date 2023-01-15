# def average(a=5, b=3):
#     print("The average is ", (a + b) / 2)


# average()
# average(5, 63)
# average(5)
# average()
def average(*number):
    sum = 0
    for i in number:
        sum = sum + i
    print(sum / len(number))


average(3, 56, 63, 235, 6, 237, 456)


def name(**name):
    print("hello", name["fname"], name["mname"], name["lname"])


name(fname="siddharth", mname='ajay', lname="sharma")
