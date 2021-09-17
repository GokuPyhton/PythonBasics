#find second highest number in list
a = []
n = int(input("Enter the numbers to be entered : "))

for i in range(1, n+1):
        b = int(input("enter number :"))
        a.append(b)

a.sort()

print("second highest number = {}".format(a[-2]))
