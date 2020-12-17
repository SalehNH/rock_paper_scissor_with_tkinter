from tkinter import *
import tkinter.messagebox as tm
import random

root = Tk()
root.title('Rock / Paper / Scissor')
root.geometry('800x200+400+150')
Label(root, text="Write (r) for Rock, (p) for Paper & (s) for scissor. then press the button,\nThe Computer will choose as well.",
 font=('Arial', 25, 'italic')).pack()
choice = Entry(root)
choice.pack(pady=20)
Button(root, text='PLAY',command=lambda:play(choice.get())).pack()

def play(choice):
    flag = True
    if choice.lower() == 'r':
        choice = 'rock'
    elif choice.lower() == 'p':
        choice = 'paper'
    elif choice.lower() == 's':
        choice = 'scissor'
    else:
        tm.showerror('ERROR', 'PLEASE ENTER r OR p OR s')
        flag = False
        
    if flag:
        computer = random.choice(['rock', 'paper', 'scissor'])
        if choice == computer:
            tm.showinfo('.:: RESULT ::.', f'Your choice: {choice}.\nComputer Choice: {computer}\n\n (IT\'S A TIE)')
        if (choice == 'rock' and computer == 'scissor') or (choice == 'paper' and computer == 'rock') or (choice == 'scissor' and computer == 'paper'):
            tm.showinfo('.:: RESULT ::.', f'Your choice: {choice}.\nComputer Choice: {computer}\n\n (You WON)')
        else:
            tm.showinfo('.:: RESULT ::.', f'Your choice: {choice}.\nComputer Choice: {computer}\n\n (You LOST)')

    



root.mainloop()