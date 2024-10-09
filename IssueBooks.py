from tkinter import *

def issueBooks():


    root = Tk()
    title = Label(root, text="Issue book", font=('arial', 30, 'bold'))

    greet = Label(root, font=('arial', 30, 'bold'), text="Issue Books")
    greet.grid(row=0, columnspan=3)

    # ----------id-------------------

    L = Label(root, font=('arial', 15, 'bold'), text="Enter Book id: ")
    L.grid(row=2, column=1)

    L = Label(root, font=('arial', 15, 'bold'), text="   ")
    L.grid(row=2, column=2)

    id = Entry(root, width=5, font=('arial', 15, 'bold'))
    id.grid(row=2, column=3)

    # ----------StudentName-------------------

    L = Label(root, font=('arial', 15, 'bold'), text="Enter StudentName: ")
    L.grid(row=4, column=1)

    L = Label(root, font=('arial', 15, 'bold'), text="   ")
    L.grid(row=4, column=2)

    StudentName = Entry(root, width=5, font=('arial', 15, 'bold'))
    StudentName.grid(row=4, column=3)

    submitbtn = Button(root, text="Submit", bg="DodgerBlue2", fg="white", font=('arial', 15, 'bold'))
    submitbtn.grid(row=8, columnspan=3)

    root.mainloop()

    print("issue")
    pass

