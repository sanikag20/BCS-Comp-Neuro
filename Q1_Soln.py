# Easter Egg at position 69
# Code will break at invalid input in S, A, R

import os


class task:
    arr = []
    duplicate = True

    def clear():
        os.system("cls")

    def task_print():
        print("P: print array")
        print("A: add number")
        print("S: sort array")
        print("R: number at rth position if the array is sorted")
        print("N: disallow/allow duplicate entries")
        print("Q: quit")

    def P():
        print(task.arr)
        input()

    def A():
        x = int(input("Enter A Number: "))
        if task.duplicate:
            task.arr.append(x)
        else:
            try:
                task.arr.index(x)
                print("Number Already Present")
                input()
            except:
                task.arr.append(x)

    def S():
        print("Sorting Options")
        print("1. Small to Large")
        print("2. Large to Small")
        x = int(input("Enter Choice: "))
        x -= 1
        task.arr.sort(reverse=x)
        print("Array was sorted")
        input()

    def R():
        x = int(input("Enter Position: "))
        if x == 69:
            print("YES DADDY")
        temp = task.arr.copy()
        temp.sort()
        print(temp[x - 1])
        input()

    def N():
        if task.duplicate:
            task.duplicate = False
        else:
            task.duplicate = True

    def Q():
        exit()


while True:
    task.clear()
    task.task_print()
    T = input()
    task.clear()

    if T == "P":
        task.P()

    elif T == "A":
        task.A()

    elif T == "S":
        task.S()

    elif T == "R":
        task.R()

    elif T == "N":
        task.N()

    elif T == "Q":
        task.Q()

    else:
        print("Invalid Input")
        input()
