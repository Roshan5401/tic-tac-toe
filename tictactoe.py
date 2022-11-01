from tkinter import *
import tkinter as tk
import time
from tkinter import ttk
win=Tk()
win.title("TicTacToe")#title at the top of the gui
lis=[None]*10
#canvas
#this is used to make a canvas
canvas1=Canvas(win,width=300,height=300,bd=0,bg="black")
canvas1.grid(row=0,column=0)
#lines on canvas
canvas1.create_line(100,0,100,300,fill="white",width=1)
canvas1.create_line(200,0,200,300,fill="white",width=1)
canvas1.create_line(0,100,300,100,fill="white",width=1)
canvas1.create_line(0,200,300,200,fill="white",width=1)
#action performed
ch=0
c=0
def winner(x):
    #123
    if(lis[1]==lis[2]==lis[3]==1):
        print("winner is 1")
        if(x==1):
            but1.configure(text="\nX\nwin",font=(None,15),height=4,fg="white")
        elif(x==2):
            but2.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
        elif(x==3):
            but3.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
    elif(lis[1]==lis[2]==lis[3]==0):
        print("winner is 0")
        if (x == 1):
            but1.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 2):
            but2.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 3):
            but3.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
    #456
    if (lis[4] == lis[5] == lis[6] == 1):
        print("winner is 1")
        if (x == 4):
            but4.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 5):
            but5.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 6):
            but6.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
    elif (lis[4] == lis[5] == lis[6] == 0):
        print("winner is 0")
        if (x == 4):
            but4.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 5):
            but5.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 6):
            but6.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
    #789
    if (lis[7] == lis[8] == lis[9] == 1):
        print("winner is 1")
        if (x == 7):
            but7.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 8):
            but8.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 9):
            but9.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
    elif (lis[7] == lis[8] == lis[9] == 0):
        print("winner is 0")
        if (x == 7):
            but7.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 8):
            but8.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 9):
            but9.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
    #147
    if (lis[1] == lis[4] == lis[7] == 1):
        print("winner is 1")
        if (x == 1):
            but1.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 4):
            but4.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 7):
            but7.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
    elif (lis[1] == lis[4] == lis[7] == 0):
        print("winner is 0")
        if (x == 1):
            but1.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 4):
            but4.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 7):
            but7.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
    #258
    if (lis[2] == lis[5] == lis[8] == 1):
        print("winner is 1")
        if (x == 2):
            but2.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 5):
            but5.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 8):
            but8.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
    elif (lis[2] == lis[5] == lis[8] == 0):
        print("winner is 0")
        if (x == 2):
            but2.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 5):
            but5.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 8):
            but8.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
    #369
    if (lis[3] == lis[6] == lis[9] == 1):
        print("winner is 1")
        if (x == 3):
            but3.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 6):
            but6.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 9):
            but9.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
    elif (lis[3] == lis[6] == lis[9] == 0):
        print("winner is 0")
        if (x == 3):
            but3.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 6):
            but6.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 9):
            but9.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
    #159
    if (lis[1] == lis[5] == lis[9] == 1):
        print("winner is 1")
        if (x == 1):
            but1.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 5):
            but5.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 9):
            but9.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
    elif (lis[1] == lis[5] == lis[9] == 0):
        print("winner is 0")
        if (x == 1):
            but1.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 5):
            but5.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 9):
            but9.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
    #357
    if (lis[3] == lis[5] == lis[7] == 1):
        print("winner is 1")
        if (x == 3):
            but3.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 5):
            but5.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 7):
            but7.configure(text="\nX\nwin", font=(None, 15), height=4, fg="white")
    elif (lis[3] == lis[5] == lis[7] == 0):
        print("winner is 0")
        if (x == 3):
            but3.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 5):
            but5.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")
        elif (x == 7):
            but7.configure(text="\nO\nwin", font=(None, 15), height=4, fg="white")

def action(x):
    global ch
    global lis
    global c
    if(ch==0):
        if(x==1):
            but1.configure(text="X        ",font=(None,15),height=4,fg="white")
            c=c+1
            lis[1] = 1
            if(c>=5):
                winner(1)
            ch=1
        elif(x==2):
            but2.configure(text="X        ", font=(None, 15),height=4, fg="white")
            c=c+1
            lis[2] = 1
            if (c>=5):
                winner(2)
            ch=1
        elif (x==3):
            but3.configure(text="X        ", font=(None, 15),height=4, fg="white")
            c=c+1
            lis[3] = 1
            if (c>=5):
                winner(3)
            ch=1
        elif (x==4):
            but4.configure(text="X        ", font=(None, 15),height=4, fg="white")
            c=c+1
            lis[4] = 1
            if (c>=5):
                winner(4)
            ch=1
        elif (x==5):
            but5.configure(text="X        ", font=(None, 15),height=4, fg="white")
            c=c+1
            lis[5] = 1
            if (c>=5):
                winner(5)
            ch=1
        elif (x==6):
            but6.configure(text="X        ", font=(None, 15),height=4, fg="white")
            c=c+1
            lis[6]=1
            if (c>=5):
                winner(6)
            ch=1
        elif (x==7):
            but7.configure(text="X        ", font=(None, 15),height=4, fg="white")
            c=c+1
            lis[7] = 1
            if (c>=5):
                winner(7)
            ch=1
        elif (x==8):
            but8.configure(text="X        ", font=(None, 15),height=4, fg="white")
            c=c+1
            lis[8] = 1
            if (c>=5):
                winner(8)
            ch=1
        elif (x==9):
            but9.configure(text="X        ", font=(None, 15),height=4, fg="white")
            c=c+1
            lis[9] = 1
            if (c>=5):
                winner(9)
            ch=1
    else:
        if (x == 1):
            but1.configure(text="O        ", font=(None, 15),height=4, fg="white")
            c=c+1
            lis[1] = 0
            if (c>=5):
                winner(1)
            ch=0
        elif (x == 2):
            but2.configure(text="O        ", font=(None, 15),height=4, fg="white")
            c = c + 1
            lis[2] = 0
            if (c >= 5):
                winner(2)
            ch = 0
        elif (x == 3):
            but3.configure(text="O        ", font=(None, 15),height=4, fg="white")
            c = c + 1
            lis[3] = 0
            if (c >= 5):
                winner(3)
            ch = 0
        elif (x == 4):
            but4.configure(text="O        ", font=(None, 15),height=4, fg="white")
            c = c + 1
            lis[4] = 0
            if (c >= 5):
                winner(4)
            ch = 0
        elif (x == 5):
            but5.configure(text="O        ", font=(None, 15),height=4, fg="white")
            c = c + 1
            lis[5] = 0
            if (c >= 5):
                winner(5)
            ch = 0
        elif (x == 6):
            but6.configure(text="O        ", font=(None, 15),height=4, fg="white")
            c = c + 1
            lis[6] = 0
            if (c >= 5):
                winner(6)
            ch = 0
        elif (x == 7):
            but7.configure(text="O        ", font=(None, 15),height=4, fg="white")
            c = c + 1
            lis[7] = 0
            if (c >= 5):
                winner(7)
            ch = 0
        elif (x == 8):
            but8.configure(text="O        ", font=(None, 15),height=4, fg="white")
            c = c + 1
            lis[8] = 0
            if (c >= 5):
                winner(8)
            ch = 0
        elif (x == 9):
            but9.configure(text="O        ", font=(None, 15),height=4, fg="white")
            c = c + 1
            lis[9] = 0
            if (c >= 5):
                winner(9)
            ch = 0
#buttons
but1=tk.Button(win,text="",width=13,height=6,bg="black",command=lambda: action(1))
but1.place(x=0,y=0)

but2=tk.Button(win,text="",width=13,height=6,bg="black",command=lambda: action(2))
but2.place(x=101,y=0)

but3=tk.Button(win,text="",width=13,height=6,bg="black",command=lambda: action(3))
but3.place(x=202,y=0)

but4=tk.Button(win,text="",width=13,height=6,bg="black",command=lambda: action(4))
but4.place(x=0,y=101)

but5=tk.Button(win,text="",width=13,height=6,bg="black",command=lambda: action(5))
but5.place(x=101,y=101)

but6=tk.Button(win,text="",width=13,height=6,bg="black",command=lambda: action(6))
but6.place(x=202,y=101)

but7=tk.Button(win,text="",width=13,height=6,bg="black",command=lambda: action(7))
but7.place(x=0,y=201)

but8=tk.Button(win,text="",width=13,height=6,bg="black",command=lambda: action(8))
but8.place(x=101,y=201)

but9=tk.Button(win,text="",width=13,height=6,bg="black",command=lambda: action(9))
but9.place(x=202,y=201)


win.mainloop()
