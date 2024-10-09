from tkinter import *

def deletebook():
    root = Tk()
    root.geometry("400x250")

    head = Label(root, text="Delete Books", font=('arial', 30, 'bold'))
    head.grid(row=0, columnspan=3)

    # <------------------ id ---------------------->

    L = Label(root, font=('arial', 15, 'bold'), text="Enter Book id: ")
    L.grid(row=2, column=1)

    L = Label(root, font=('arial', 15, 'bold'), text="   ")
    L.grid(row=2, column=2)

    id = Entry(root, width=5, font=('arial', 15, 'bold'))
    id.grid(row=2, column=3)

    # <----------------- Submit ------------------->

    submitbtn = Button(root, text="Submit", bg="DodgerBlue2", fg="white", font=('arial', 15, 'bold'))
    submitbtn.grid(row=8, columnspan=7)

    root.mainloop()

