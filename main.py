import tkinter as tk


window = tk.Tk()
window.title("Convert Roman to Integer")
window.minsize(width=300,height=300)

label = tk.Label(
    text="Please enter a roman number (1-4999)",
)

label.pack()

roman_number_entry= tk.Entry()
roman_number_entry.pack()

roman_numbers = {"M": 1000,
                 "CM": 900,
                 "D": 500,
                 "CD": 400,
                 "C": 100,
                 "XC": 90,
                 "L": 50,
                 "XL": 40,
                 "X": 10,
                 "V": 5,
                 "IV": 4,
                 "I": 1}

def calculate():
    result = 0
    prev_value = 0
    roman_entry = roman_number_entry.get().upper()
    for char in roman_entry:
        if char not in roman_numbers:
            label_answer.config(text="Invalid Roman number")
            return

    for key, value in roman_numbers.items():
        if roman_entry == key:
            label_answer.config(text="The answer: {}".format(value))

    for char in reversed(roman_entry):
        current_value = roman_numbers[char]
        if current_value >= prev_value:
            result += current_value
        else:
            result -= current_value
        prev_value = current_value
        label_answer.config(text="The answer: {}".format(result))







calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

label_answer = tk.Label(window, text="The answer: ")
label_answer.pack()

window.mainloop()