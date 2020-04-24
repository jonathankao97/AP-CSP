import tkinter
import math
import re

def base_to_decimal(base_input):
    base_input = int(base_input)
    counter = 0
    returnValue = 0
    while base_input / (pow(2,counter)) != 0:
        returnValue += int(pow(2,counter))*(base_input % 10)
        counter += 1
        base_input = int(base_input/10)
    return returnValue

def decimal_to_base(base_output):
    base_output = int(base_output)
    string_output = ""
    while (base_output / 2) != 0:
        string_output += str(base_output%2)
        base_output = int(base_output/2)
    string_reverse = ""
    for x in range (0, len(string_output)):
        string_reverse += string_output[len(string_output)-x-1]
    return string_reverse

def letter_to_num(letter):
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    for i in range(len(list)):
        if str(list[i]) == letter:
            return i
    return -1

def num_to_letter(number):
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    return str(list[number])

def hex_to_dec(hex):
    dec = 0
    for i in range(len(hex)):
        dec += 16**(len(hex)-i-1) * letter_to_num(hex[i])
    return dec

def dec_to_hex(dec):
    hex = ""
    dec = int(dec)
    while dec/16 != 0:
        hex = num_to_letter(dec%16) + hex
        dec = math.floor(dec/16)
    return hex


def userInput():
    outField.delete(1.0,tkinter.END)
    checkboxes = [baseToDec.get(), decToBase.get(), hexToDec.get(), decToHex.get(), hexToBin.get(), binToHex.get()]
    seen = False
    for num in checkboxes:
        if num==1 and seen:
            outField.insert(tkinter.INSERT, 'You can only pick one option')
            return
        elif num==1 and not seen:
            seen = True
    if not seen:
        outField.insert(tkinter.INSERT, 'You must pick at least one option')

    binaryValidator = r'[0-1]'
    if (binToHex.get()==1 or baseToDec.get()==1) and not re.match(binaryValidator, str(entry.get())):
        outField.insert(tkinter.INSERT, 'Invalid Input (Allowed Input: 0-1)')
        return
    if binToHex.get()==1:
        outField.insert(tkinter.INSERT, dec_to_hex(base_to_decimal(entry.get())))
    if baseToDec.get()==1:
        outField.insert(tkinter.INSERT, base_to_decimal(entry.get()))

    decimalValidator = r'[0-9]'
    if (decToBase.get()==1 or decToHex.get()==1) and not re.match(decimalValidator, str(entry.get())):
        outField.insert(tkinter.INSERT, 'Invalid Input (Allowed Input: 0-9)')
        return
    if decToBase.get()==1:
        outField.insert(tkinter.INSERT, decimal_to_base(entry.get()))
    if decToHex.get()==1:
        outField.insert(tkinter.INSERT, dec_to_hex(entry.get()))

    hexValidator = r'[A-Fa-f0-9]'
    print(entry.get())
    print(re.match(hexValidator, str(entry.get())))
    if (hexToDec.get()==1 or hexToBin.get()==1) and not re.match(hexValidator, str(entry.get())):
        outField.insert(tkinter.INSERT, 'Invalid Input (Allowed Input: 0-9, a-f, A-F)')
        return
    if hexToDec.get()==1:
        outField.insert(tkinter.INSERT, hex_to_dec(entry.get()))
    if hexToBin.get()==1:
        outField.insert(tkinter.INSERT, decimal_to_base(hex_to_dec(entry.get())))

window = tkinter.Tk()
prompt = tkinter.Label(window, text = 'Input')
prompt.pack()

entry = tkinter.Entry(window)
entry.pack()

baseToDec = tkinter.IntVar()
checkButton1 = tkinter.Checkbutton(window, text = 'Convert from Binary to Decimal', variable = baseToDec)
checkButton1.pack()

decToBase = tkinter.IntVar()
checkButton2 = tkinter.Checkbutton(window, text = 'Convert from Decimal to Binary', variable = decToBase)
checkButton2.pack()

hexToDec = tkinter.IntVar()
checkButton3 = tkinter.Checkbutton(window, text = 'Convert from Hexadecimal to Decimal', variable = hexToDec)
checkButton3.pack()

decToHex = tkinter.IntVar()
checkButton4 = tkinter.Checkbutton(window, text = 'Convert from Decimal to Hexadecimal', variable = decToHex)
checkButton4.pack()

hexToBin = tkinter.IntVar()
checkButton5 = tkinter.Checkbutton(window, text = 'Convert from Hexadecimal to Binary', variable = hexToBin)
checkButton5.pack()

binToHex = tkinter.IntVar()
checkButton6 = tkinter.Checkbutton(window, text = 'Convert from Binary to Hexadecimal', variable = binToHex)
checkButton6.pack()

submitButton = tkinter.Button(window, text = 'submit', command = userInput)
submitButton.pack()

outField = tkinter.Text(window)
outField.pack()

window.mainloop()
