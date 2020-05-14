import math
import pyinputplus as pyip


def copies(count, word):
    if count <= 1:
        return word
    return word + copies(count-1, word)


def copies_interface():
    print("-----")
    count = pyip.inputNum("How many times would you like this word printed? ")
    word = pyip.inputStr("What word would you like printed? ")
    print("Output:", copies(count, word))
    print("-----")


def fib(count, dp):
    if dp[count] != 0:
        return dp[count]
    if count == 0:
        return 0
    if count == 1:
        return 1
    dp[count] = fib(count-1, dp) + fib(count-2, dp)
    return dp[count]


def fib_interface():
    print("-----")
    count = pyip.inputNum("Which number in the fibonacci sequence would you like printed? ")
    print("Output:", fib(count, [0 for i in range(count+1)]))
    print("-----")


def initials(words):
    if words == "":
        return ""
    arr = words.split()
    remaining = ' '.join(arr[1:])
    return arr[0][0] + initials(remaining)


def initials_interface():
    print("-----")
    words = pyip.inputStr("Enter a sentence you would like the initials of! ")
    print("Output:", initials(words))
    print("-----")


def pascal(row, col, dp):
    if dp[row][col] != -1:
        return dp[row][col]
    if col == 0:
        return 1
    if row == col:
        return 1
    dp[row][col] = pascal(row-1, col, dp) + pascal(row-1, col-1, dp)
    return dp[row][col]


def pascal_interface():
    print("-----")
    row = pyip.inputNum("Which row of the pascal triangle are you interested in? ")
    col = pyip.inputNum("Which column of the pascal triangle are you interested in? ")
    print("Output:", pascal(row, col, [[-1 for i in range(col+1)] for j in range(row+1)]))
    print("-----")


def to_binary(dec):
    if dec == 0:
        return ""
    return ''.join([to_binary(dec//2), str(dec % 2)])


def to_binary_interface():
    print("-----")
    dec = pyip.inputNum("Enter a decimal you would like to convert to binary! ")
    print("Output:", to_binary(dec))
    print("-----")


def user_interface():
    print("-----")
    print("1. Copies")
    print("2. Fibonacci")
    print("3. Initials")
    print("4. Pascals")
    print("5. Decimal to Binary")
    print("6. Quit")
    response = pyip.inputNum("Enter the number of the program you would like to use! ")

    if response == 1:
        copies_interface()
    elif response == 2:
        fib_interface()
    elif response == 3:
        initials_interface()
    elif response == 4:
        pascal_interface()
    elif response == 5:
        to_binary_interface()
    elif response != 6:
        print("Invalid program number!")

    if response != 6:
        user_interface()
    else:
        print("Exiting..., thanks for playing!")


if __name__ == '__main__':
    user_interface()
