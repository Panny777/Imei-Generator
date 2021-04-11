"""
Generates random IMEI numbers.
The user specifies the 8-digit TAC and up to 4-digits of the serial number.
The user also specifies the number of random IMEIs to generate.
"""
from tkinter import *
import tkinter as tk
from tkinter import ttk
import sys
import random


# Src: https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/luhn.py
def checksum(number, alphabet='0123456789'):
    """
    Calculate the Luhn checksum over the provided number.
    The checksum is returned as an int.
    Valid numbers should have a checksum of 0.
    """
    n = len(alphabet)
    number = tuple(alphabet.index(i)
                   for i in reversed(str(number)))
    return (sum(number[::2]) +
            sum(sum(divmod(i * 2, n))
                for i in number[1::2])) % n


def calc_check_digit(number, alphabet='0123456789'):
    """Calculate the extra digit."""
    check_digit = checksum(number + alphabet[0])
    return alphabet[-check_digit]

class Widget:
    def __init__(self):

        def clear():
            self.Output_text.delete(1.0, END)
            
        def main():
            """Ask for the base IMEI, how many to generate, then generate them."""
            # Loop until the first 8-12 digits have been received & are valid
            start = ''
            while True:
                try:
                    start = self.Imei_Entry.get()
                except KeyboardInterrupt:
                    sys.exit()

                # If all conditions are met, the input is valid
                if start.isdigit() and len(start) >= 8 and len(start) <= 12:
                    break

                # Tell the user why their input is invalid
                if not start.isdigit():
                    result = '*** Invalid input: you must enter digits only\n'
                    self.Output_text.delete(1.0, END)
                    self.Output_text.insert(END, result)
                    return result

                elif len(start) <= 8:
                    result = '*** Invalid input: you must enter at least 8 digits\n'
                    self.Output_text.delete(1.0, END)
                    self.Output_text.insert(END, result)
                    return result
                elif len(start) >= 12:
                    result = '*** Invalid input: you must enter no more than 12 digits\n'
                    self.Output_text.delete(1.0, END)
                    self.Output_text.insert(END, result)
                    return result

            # Loop until we know how many random numbers to generate
            count = 0
            while True:
                try:
                    count_input = self.Imei_No_Entry.get()
                except KeyboardInterrupt:
                    sys.exit()

                # If all conditions are met, the input is valid
                if count_input.isdigit() and int(count_input) > 0:
                    count = int(count_input)
                    break

                # Tell the user that they need to enter a number > 0

            # IMEIs will be generated based on the first 8 digits (TAC; the number
            #   used to identify the model) and the next 2-6 digits (partial serial #).
            #   The final, 15th digit, is the Luhn algorithm check digit.

            # Generate and print random IMEI numbers
            for _ in range(count):
                imei = start

                # Randomly compute the remaining serial number digits
                while len(imei) < 14:
                    imei += str(random.randint(0, 9))

                # Calculate the check digit with the Luhn algorithm
                imei += calc_check_digit(imei)
                self.Output_text.insert(END,'>' + imei + '\n')

        # Backwards compatibility (raw_input was renamed to input in Python 3.x)
        try:
            # Using Python 2.x; calls to input will be treated as calls to raw_input
            input = raw_input
        except NameError:
            # Using Python 3.x; no action required
            pass

        root = Tk()
        root.geometry('400x600')
        root.resizable(0, 0)
        root.config(bg='ghost white')
        root.title("HawaVunjaBei Imei Generator")

        self.Name_Label = Label(root, text="IMEI GENERATOR", font='verdana 18 bold', bg='ghost white', fg='blue')
        self.Name_Label.pack(side=TOP, fill=X)

        self.Imei_Label = Label(root, text="Trial IMEI Number", font='verdana', bg='ghost white', fg='black')
        self.Imei_Label.place(x=10, y=50)
        self.Imei_Entry = Entry(root, width=30, bd=2)
        self.Imei_Entry.place(x=10, y=80)

        Imei_No_Label = Label(root, text="Number of IMEI to Generate", font='verdana', bg='ghost white', fg='black')
        Imei_No_Label.place(x=10, y=120)
        self.Imei_No_Entry = Entry(root, width=10, bd=2)
        self.Imei_No_Entry.place(x=10, y=150)

        trans_btn = Button(root, text='Calculate', font='arial 12 bold', pady=5, command=main, bg='royal blue1',
                           activebackground='sky blue')
        trans_btn.place(x=10, y=180)
        

        clear_btn = Button(root, text='Clear', font='arial 12 bold', pady=5, command=clear, bg='red',
                           activebackground='red')
        clear_btn.place(x=320, y=180)
        

        self.Output_text = Text(root, font='arial 10', height=20, wrap=WORD, padx=5, pady=5, width=50, fg='blue')
        self.Output_text.place(x=10, y=220)

        self.Maker_Label = Label(root, text="Made By Panny Tech", font='verdana', bg='ghost white', fg='black')
        self.Maker_Label.pack(side=BOTTOM)

        root.mainloop()

# Bckwards compatibility (raw_input was renamed to input in Python 3.x)
try:
    # Using Python 2.x; calls to input will be treated as calls to raw_input
    input = raw_input
except NameError:
    # Using Python 3.x; no action required
    pass




if __name__ == '__main__':
    widget = Widget()
