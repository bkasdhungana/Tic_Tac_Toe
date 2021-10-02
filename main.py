import tkinter.messagebox
from tkinter import *
from tkmacosx import Button

root = Tk()
root.geometry("900x750")
root.title("Tic Tac Toe")
root.configure(background="Cadet Blue")

tops = Frame(root, bg="Red", pady=2, width=1350, height=100, relief=RIDGE)
tops.grid(row=0, column=0)

lblTitle = Label(tops, font=('arial', 50, 'bold'), text="Tic tac toe", bd=21, bg="Cadet Blue", fg="Cornsilk")
lblTitle.grid(row=0, column=0)

MainFrame = Frame(root, bg='White', bd=10, width=1350, height=600, relief=RIDGE)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame(MainFrame, bd=10, width=750, height=600, pady=5, padx=10, bg="Black", relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=10, width=560, height=500, pady=2, padx=10, bg="Black", relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width=560, height=400, pady=2, padx=5, bg="purple", relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=10, width=560, height=200, pady=2, padx=8, bg="Green", relief=RIDGE)
RightFrame2.grid(row=1, column=0)

PlayerX = IntVar()
PlayerO = IntVar()

PlayerX.set(0)
PlayerO.set(0)

button = StringVar()
click = True


def checker(buttons):
    global click
    if buttons['text'] == "" and click == True:
        buttons['text'] = "X"
        click = False
        scorekeeper()
    elif buttons["text"] == "" and click == False:
        buttons["text"] = "O"
        click = True
        scorekeeper()


def scorekeeper():
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        reset()
        tkinter.messagebox.showinfo("Information", "Player X win the game!!!")
    elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        reset()
        tkinter.messagebox.showinfo("Information", "Player X win the game!!!")
    elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        reset()
        tkinter.messagebox.showinfo("Information", "Player X win the game!!!")
    elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        reset()
        tkinter.messagebox.showinfo("Information", "Player X win the game!!!")
    elif button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        reset()
        tkinter.messagebox.showinfo("Information", "Player X win the game!!!")
    elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        reset()
        tkinter.messagebox.showinfo("Information", "Player X win the game!!!")
    elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        reset()
        tkinter.messagebox.showinfo("Information", "Player X win the game!!!")
    elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        reset()
        tkinter.messagebox.showinfo("Information", "Player X win the game!!!")

    elif button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        reset()
        tkinter.messagebox.showinfo("Information", "Player O win the game!!!")
    elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        reset()
        tkinter.messagebox.showinfo("Information", "Player O win the game!!!")
    elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        reset()
        tkinter.messagebox.showinfo("Information", "Player O win the game!!!")
    elif button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        reset()
        tkinter.messagebox.showinfo("Information", "Player O win the game!!!")
    elif button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        reset()
        tkinter.messagebox.showinfo("Information", "Player O win the game!!!")
    elif button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        reset()
        tkinter.messagebox.showinfo("Information", "Player O win the game!!!")
    elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        reset()
        tkinter.messagebox.showinfo("Information", "Player win the game!!!")
    elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        reset()
        tkinter.messagebox.showinfo("Information", "Player O win the game!!!")


def reset():
    button1['text'] = ""
    button2['text'] = ""
    button3['text'] = ""
    button4['text'] = ""
    button5['text'] = ""
    button6['text'] = ""
    button7['text'] = ""
    button8['text'] = ""
    button9['text'] = ""

    button1.configure(background="white")
    button2.configure(background="white")
    button3.configure(background="white")
    button4.configure(background="white")
    button5.configure(background="white")
    button6.configure(background="white")
    button7.configure(background="white")
    button8.configure(background="white")
    button9.configure(background="white")


def newgame():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)


def close():
    root.destroy()


lblPlayerX = Label(RightFrame1, font=('arial', 40, 'bold'), text="Player X:  ", padx=2, pady=2, bg="purple")
lblPlayerX.grid(row=0, column=0, sticky=W)
txtPlayerX = Entry(RightFrame1, font=('arial', 40, 'bold'), textvariable=PlayerX, width=14,
                   justify=LEFT).grid(row=0, column=1)

lblPlayerO = Label(RightFrame1, font=('arial', 40, 'bold'), text="PlayerO:  ", padx=2, pady=2, bg="purple")
lblPlayerO.grid(row=1, column=0, sticky=W)
txtPlayerO = Entry(RightFrame1, font=('arial', 40, 'bold'), textvariable=PlayerO, width=14,
                   justify=LEFT).grid(row=1, column=1)

btnreset = Button(RightFrame2, text='Reset', bg='Yellow', fg='black', borderless=1, height=100, command=reset)
btnreset.grid(row=1, column=0)

btnnew = Button(RightFrame2, text='New', bg='blue', fg='pink', borderless=1, height=100, command=newgame)
btnnew.grid(row=1, column=1)

btnquit = Button(RightFrame2, text='Quit', bg='red', fg='#00203F', borderless=1, height=100, command=close)
btnquit.grid(row=1, column=2)

button1 = Button(LeftFrame, text='', bg='white', fg='black', borderless=1, height=100,
                 command=lambda: checker(button1))
button1.grid(row=1, column=0)

button2 = Button(LeftFrame, text='', bg='white', fg='#00203F', borderless=1, height=100,
                 command=lambda: checker(button2))
button2.grid(row=1, column=1)

button3 = Button(LeftFrame, text='', bg='white', fg='#00203F', borderless=1, height=100,
                 command=lambda: checker(button3))
button3.grid(row=1, column=2, sticky=S + N + E + W)

button4 = Button(LeftFrame, text='', bg='white', fg='#00203F', borderless=1, height=100,
                 command=lambda: checker(button4))
button4.grid(row=2, column=0, sticky=S + N + E + W)

button5 = Button(LeftFrame, text='', bg='white', fg='#00203F', borderless=1, height=100,
                 command=lambda: checker(button5))
button5.grid(row=2, column=1, sticky=S + N + E + W)

button6 = Button(LeftFrame, text='', bg='white', fg='#00203F', borderless=1, height=100,
                 command=lambda: checker(button6))
button6.grid(row=2, column=2, sticky=S + N + E + W)

button7 = Button(LeftFrame, text='', bg='white', fg='#00203F', borderless=1, height=100,
                 command=lambda: checker(button7))
button7.grid(row=3, column=0, sticky=S + N + E + W)

button8 = Button(LeftFrame, text='', bg='white', fg='#00203F', borderless=1, height=100,
                 command=lambda: checker(button8))
button8.grid(row=3, column=1, sticky=S + N + E + W)

button9 = Button(LeftFrame, text='', bg='white', fg='#00203F', borderless=1, height=100,
                 command=lambda: checker(button9))
button9.grid(row=3, column=2, sticky=S + N + E + W)

root.mainloop()
