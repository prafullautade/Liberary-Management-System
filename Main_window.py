from tkinter import *

from ReturnBooks import *
from IssueBooks import *
from AddBooks import *
from DeleteBooks import *


root = Tk()

head = Label(root, text="Liberaty management system", font=('arial', 30, 'italic'))
head.grid(row=0, columnspan=3)

Add = Button(root, text="Add Book", command=addBooks, bg="DodgerBlue2", font=('arial', 15, 'bold'), fg="white")
Add.grid(row=3, columnspan=3, pady=5)

Delete = Button(root, text="Delete Book", command=deletebook, bg="DodgerBlue2", font=('arial', 15, 'bold'), fg="white")
Delete.grid(row=6, columnspan=3, pady=5)

Issue = Button(root, text="Issue Books", command=issueBooks, bg="DodgerBlue2", font=("arial", 15, "bold"), fg="white")
Issue.grid(row=9, columnspan=3, pady=5)

Return = Button(root, text="Return Books", command=returnBooks, bg="DodgerBlue2", font=("arial", 15, "bold"), fg="white")
Return.grid(row=12, columnspan=3, pady=5)

# View = Button(root, text="View Books", command=ViewBooks, bg="DodgerBlue2", font=("arial", 20, "bold"), fg="white")
# View.grid(row=15, columnspan=3)

last = Label(root, text="Thank You", fg="Black", font=("arial", 20, "italic"))
last.grid(row=14, column=1)

root.mainloop()
