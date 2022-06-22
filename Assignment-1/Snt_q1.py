import numpy as np

array = [1, 2, 3, 4, 5, 6]
menu = 'P: print array (initially array is empty) \nA: add number \nS: sort array \nR: number at rth position if the array is sorted \nN: disallow/allow duplicate entries \nQ: quit '

print(menu)
print('\n')
ans = input('Select from menu: ')

# we will use a while loop here
while ans != 'Q':
    # print array
    if ans == 'P':
        print(array)
        print(menu)
        print('\n')

    # add number
    elif ans == 'A':
        num = int(input('Enter the number you wish to add: '))
        array = np.append(array, num)
        print('new array with added number is: ', array)
        print(menu)
        print('\n')


    # sort
    elif ans == 'S':
        choice = input('Choose increasing or decreasing: ')

        if choice == 'increasing':
            np.sort(array)
            print(array)
            print(menu)
            print('\n')
        else:
            np.sort(array)[::-1]
            print(array)
            print(menu)
            print('\n')

    # give Rth index
    elif ans == 'R':
        pos = int(input('which position: '))
        print(array[pos])
        print(menu)
        print('\n')

    # duplication check
    elif ans == 'N':
        choose = input('duplication allowed or not')
        print(menu)
        print('\n')

    # ensure the menu keeps running until Q is pressed
    ans = input('Select from menu: ')

