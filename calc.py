from tkinter import *

root = Tk()

currentText = ""

# def operations(value):
# 	if value == "=":
# 		mainInput.config(text=eval(currentText))
# 		currentText = mainInput.cget("text")
	

def main(value):
	global currentText

	if value == "=":
		currentText = eval(currentText)
		mainInput.config(text=currentText)
		return

	if value == "C":
		currentText = ""
		mainInput.config(text="0")

		return

	if value == "<x":
		currentText = currentText[:-1]

	else:
		currentText = str(currentText) + str(value)	
	
	mainInput.config(text=currentText)

root["bg"] = "#fafafa"
root.title("Калькулятор")
#root.wm_attributes("-alpha", 0.7)
root.geometry("300x250")

root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=250)
canvas.pack()

frameInput = Frame(root, bg="grey")
frameInput.place(relx=0, rely=0, relwidth=1, relheight=0.2)

# title = Label(frame, text="0", bg="grey", font=40)
# title.pack()

mainInput = Label(frameInput, text="0", anchor='e', bg="white", font=50)
mainInput.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.7)
#mainInput.pack(pady=(20,10))

frameBtn = Frame(root, bg="white")
frameBtn.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)


buttons = [
    Button(frameBtn, text=str(i), command=lambda x=i: main(x))  
    for i in range(10)  # Створюємо кнопки 0-9
]

buttons.extend([
    Button(frameBtn, text="+", command=lambda: main("+")),
    Button(frameBtn, text="-", command=lambda: main("-")),
    Button(frameBtn, text="*", command=lambda: main("*")),
    Button(frameBtn, text="/", command=lambda: main("/")),
    Button(frameBtn, text=".", command=lambda: main(".")),
    Button(frameBtn, text="=", command=lambda: main("=")),
    Button(frameBtn, text="C", command=lambda: main("C")),
    Button(frameBtn, text="<x", command=lambda: main("<x")),
])

button_config = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('<x', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('+', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('-', 2, 3),
    ('0', 3, 0), (".", 3, 1), ('/', 3, 2), ('*', 3, 3),
    ('=', 4, 0), ("C", 4, 1)
]

for text, row, col in button_config:
    button = Button(frameBtn, text=text, command=lambda t=text: main(t))
    button.grid(row=row, column=col, sticky='nsew')

frameBtn.grid_columnconfigure([0, 1, 2, 3], weight=1)  # Стовпці
frameBtn.grid_rowconfigure([0, 1, 2, 3], weight=1) 



root.mainloop()