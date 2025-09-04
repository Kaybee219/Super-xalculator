import tkinter

button_Values = [
    ["+/-", "x!", "(", ")", "%", "AC", "CE"],
    ["inv", "sin", "ln", "7", "8", "9", "/"],
    ["pi", "cos", "log", "4", "5", "6", "*"],
    ["e", "tan", "sqrt", "1", "2", "3", "-"],
    ["ans", "EXP", "x^y", "0", ".", "=", "+"]
]

right_Symbols = ["CE", "/", "*", "-", "+"]
top_Symbols = ["+/-", "x!", "(", ")", "%", "AC", "CE"]
trig_Functions = ["sin", "cos", "tan"]
log_Functions = ["ln", "log"]
other_Buttons = ["inv", "pi", "e", "sqrt", "ans", "EXP", "x^y"]


row_Count = len(button_Values) #7
column_Count = len(button_Values[0]) #5

color_light_grey="#D3D3D2"
color_black="#1C1C1C"
color_dark_grey="#505050"
color_orange="#FF9500"
color_white="#FFFFFF"

#window setup
window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)
window.configure(bg=color_black)
frame=tkinter.Frame(window)
label=tkinter.Label(frame, text="0", bg=color_black, 
                    foreground=color_white,font=("Arial", 45), anchor="e", width=column_Count)
label.grid(row=0, column=0, columnspan=column_Count, sticky="we")#fill

for row in range(row_Count):
    for column in range(column_Count):
        value=button_Values[row][column]
        button=tkinter.Button(frame, text=value, font=("Arial", 30 ),
                               width=column_Count-1, height=1,
                               command=lambda value=value: button_click(value))
        button.grid(row=row+1, column=column)
        if value in top_Symbols:
            button.configure(foreground=color_black, background=color_light_grey)
        elif value in right_Symbols:
            button.configure(foreground=color_white, background=color_orange)
        else:
            button.configure(foreground=color_white, background=color_dark_grey)
frame.pack()

#A+B, A-B, A*B, A/B
A="0"
operator= None
B= None
c="="
def clear_all():
    global A, operator, B, c
    A = "0"
    operator = None
    B = None
    c = "="
def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)

def button_click(value):
    global right_Symbols, top_Symbols, label, A, operator, B ,c , trig_Functions, log_Functions, other_Buttons
    if value in right_Symbols:
        if operator is None:
            A = label["text"]
            label["text"] = "0"
            B = "0"
        operator = value
    if value == c:
        if A is not None and operator is not None:
            B = label["text"]
            numA = float(A)
            numB = float(B)
            if operator == "+":
               label["text"] = remove_zero_decimal(numA + numB)
            elif operator == "-":
               label["text"] = remove_zero_decimal(numA - numB) 
            elif operator == "*":
               label["text"] = remove_zero_decimal(numA * numB)
            elif operator == "/":
               if numB == 0:
                   label["text"] = "Error"
               else:
                   label["text"] = remove_zero_decimal(numA / numB)

            clear_all()
    elif value in top_Symbols:
        if value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        elif value == "x!":
            result = 1
            for i in range(1, int(label["text"]) + 1):
                result *= i
            label["text"] = remove_zero_decimal(result)
        elif value == "(":
            label["text"] += "("
        elif value == ")":
            label["text"] += ")"
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)

        elif value == "AC":
            clear_all()
        elif value == "CE":
            pass
    elif value in trig_Functions:
        import math
        num = float(label["text"])
        if value == "sin":
            result = math.sin(math.radians(num))
        elif value == "cos":
            result = math.cos(math.radians(num))
        elif value == "tan":
            result = math.tan(math.radians(num))
        label["text"] = remove_zero_decimal(result)
    elif value in log_Functions:
        import math
        num = float(label["text"])
        if value == "ln":
            result = math.log(num)
        elif value == "log":
            result = math.log10(num)
        label["text"] = remove_zero_decimal(result)
    elif value in other_Buttons:
        import math
        if value == "inv":
            result = 1 / float(label["text"])
            label["text"] = remove_zero_decimal(result)
        elif value == "pi":
            label["text"] = remove_zero_decimal(math.pi)
        elif value == "e":
            label["text"] = remove_zero_decimal(math.e)
        elif value == "sqrt":
            result = math.sqrt(float(label["text"]))
            label["text"] = remove_zero_decimal(result)
        elif value == "ans":
            label["text"] = A
        elif value == "EXP":
            label["text"] += "e"
        elif value == "x^y":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"
            operator = "^"
    else:
        if value ==".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value
#recenter the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.mainloop()