from tkinter import *

def returnBooks():

    root = Tk()
    root.title('ProjectGurukul Library Management System')

    greet = Label(root, font=('arial', 30, 'bold'), text="Return Books")
    greet.grid(row=0, columnspan=3)

    L = Label(root, font=('arial', 15, 'bold'), text="Enter Book id: ")
    L.grid(row=2, column=1)

    L = Label(root, font=('arial', 15, 'bold'), text="   ")
    L.grid(row=2, column=2)

    id = Entry(root, width=5, font=('arial', 15, 'bold'))
    id.grid(row=2, column=3)

    submitbtn = Button(root, text="Submit", bg="DodgerBlue2", fg="white", font=('arial', 15, 'bold'))
    submitbtn.grid(row=8, columnspan=3)

    root.mainloop()

    print("return")
    pass

