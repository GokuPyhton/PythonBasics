import pdb


def order(num):
    n = 0
    while num != 0:
        n = n + 1
        num = int((num // 10))

    return n


def armstrong(num):
    n = order(num)
    print("number length :", n)
    arm = 0
    num1 = num
    rem = 0
    # pdb.set_trace()
    while num1 != 0:
        rem = num1 % 10
        arm = arm + pow(rem, n)
        # pdb.set_trace()
        num1 = num1 // 10

    print("Armstrong number :", arm)
    if num == arm:
        print("Number is armstrong number")
    else:
        print("Number is not armstrong number")


No = int(input("Enter number : "))
armstrong(No)
