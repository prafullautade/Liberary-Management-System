from tkinter import *


def addBooks():
    root = Tk()
    root.geometry("550x300")

    # global id
    # global title
    # global Author

    head = Label(root, text="Add Books", font=('arial', 30, 'bold'))
    head.grid(row=0, columnspan=3)

    #<------------------ id ------------------------>

    L = Label(root, text="Enter book id:", font=('arial', 15, 'bold'))
    L.grid(row=2, column=1)

    L = Label(root, text="  ", font=('arial', 15, 'bold'))
    L.grid(row=2, column=2)

    id = Entry(root, font=('arial', 15, 'bold'))
    id.grid(row=2, column=3)

    # <-----------------Title ------------------>

    T = Label(root, text="Enter Book title:", font=('arial', 15, 'bold'))
    T.grid(row=4, column=1)

    T = Label(root, text="  ", font=('arial', 15, 'bold'))
    T.grid(row=4, column=2)

    title = Entry(root, font=('arial', 15, 'bold'))
    title.grid(row=4, column=3)

    # <--------------------- Author ------------------>

    A = Label(root, text="Enter Author Name:", font=('arial', 15, 'bold'))
    A.grid(row=6, column=1)

    A = Label(root, text="  ", font=('arial', 15, 'bold'))
    A.grid(row=6, column=2)

    author = Entry(root, font=('arial', 15, 'bold'))
    author.grid(row=6, column=3)

    #<----------------- Submit Button ----------------->

    submit = Button(root, text="Submit", font=('arial', 15, 'bold'), bg="DodgerBlue2", fg="white")
    submit.grid(row=8, columnspan=10)

    print("add")
    pass

    root.mainloop()

