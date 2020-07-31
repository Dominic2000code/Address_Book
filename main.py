from tkinter import *
from tkinter import messagebox

from db import Database

db = Database('try.sqlite')


class Application:
    def __init__(self, master):
        self.master = master
        master.geometry("500x550")
        master.resizable(width=False, height=False)
        master.title("Address Book")
        self.createWidgets()
        self.selected_items = 0
        self.populate_list()

    def createWidgets(self):
        self.header_label = Label(self.master, text="Address Book", font=('Courier', 20))
        self.header_label.grid(row=0, column=0, columnspan=2)

        # FirstName field
        self.firstName_text = StringVar()
        self.firstName_label = Label(self.master, text="First Name: ", font=('Courier', 14))
        self.firstName_entry = Entry(self.master, textvariable=self.firstName_text, font=('Courier', 12), width=25)
        self.firstName_label.grid(row=1, column=0, pady=4)
        self.firstName_entry.grid(row=1, column=1, pady=4)

        # LastName field
        self.lastName_text = StringVar()
        self.lastName_label = Label(self.master, text="Last Name: ", font=('Courier', 14))
        self.lastName_entry = Entry(self.master, textvariable=self.lastName_text, font=('Courier', 12), width=25)
        self.lastName_label.grid(row=2, column=0, pady=4)
        self.lastName_entry.grid(row=2, column=1, pady=4)

        # Company field
        self.company_text = StringVar()
        self.company_label = Label(self.master, text="Company: ", font=('Courier', 14))
        self.company_entry = Entry(self.master, textvariable=self.company_text, font=('Courier', 12), width=25)
        self.company_label.grid(row=3, column=0, pady=4)
        self.company_entry.grid(row=3, column=1, pady=4)

        # Phone field
        self.phone_text = StringVar()
        self.phone_label = Label(self.master, text="Phone: ", font=('Courier', 14))
        self.phone_entry = Entry(self.master, textvariable=self.phone_text, font=('Courier', 12), width=25)
        self.phone_label.grid(row=4, column=0, pady=4)
        self.phone_entry.grid(row=4, column=1, pady=4)

        # Email field
        self.email_text = StringVar()
        self.email_label = Label(self.master, text="Email: ", font=('Courier', 14))
        self.email_entry = Entry(self.master, textvariable=self.email_text, font=('Courier', 12), width=25)
        self.email_label.grid(row=5, column=0, pady=4)
        self.email_entry.grid(row=5, column=1, pady=4)

        # Address field
        self.address_text = StringVar()
        self.address_label = Label(self.master, text="Address: ", font=('Courier', 14))
        self.address_entry = Entry(self.master, textvariable=self.address_text, font=('Courier', 12), width=25)
        self.address_label.grid(row=6, column=0, pady=4)
        self.address_entry.grid(row=6, column=1, pady=4)

        # Birthday field
        self.birthday_text = StringVar()
        self.birthday_label = Label(self.master, text="Birthday: ", font=('Courier', 14))
        self.birthday_entry = Entry(self.master, textvariable=self.birthday_text, font=('Courier', 12), width=25)
        self.birthday_label.grid(row=7, column=0, pady=4)
        self.birthday_entry.grid(row=7, column=1, pady=4)

        # Search field
        self.search_text = StringVar()
        self.search_label = Label(self.master, text="Search: ", font=('Courier', 14))
        self.search_entry = Entry(self.master, textvariable=self.search_text, font=('Courier', 12), width=25)
        self.search_label.grid(row=8, column=0, pady=20)
        self.search_entry.grid(row=8, column=1, pady=15)

        # Contact list
        self.contact_list = Listbox(self.master, height=8, width=30)
        self.contact_list.grid(row=9, column=0, columnspan=2, rowspan=6, padx=20, pady=20, sticky=W + E)

        # Vertical scrollbar
        self.scrollbar = Scrollbar(self.master)
        self.scrollbar.grid(row=9, column=2, sticky=N + S, rowspan=6)

        # Horizontal scrollBar
        self.hscrollbar = Scrollbar(self.master, orient=HORIZONTAL)
        self.hscrollbar.grid(row=15, column=0, sticky=W + E, columnspan=2)

        # Set scrollbar to accounts
        self.contact_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.contact_list.yview)

        self.contact_list.configure(xscrollcommand=self.hscrollbar.set)
        self.hscrollbar.configure(command=self.contact_list.xview)

        # Bind select
        self.contact_list.bind('<<ListboxSelect>>', self.select_item)

        # Buttons
        self.add_button = Button(self.master, text="ADD", width=10, command=self.add_item)
        self.add_button.grid(row=1, column=2, padx=15)

        self.update_button = Button(self.master, text="UPDATE", width=10, command=self.update_item)
        self.update_button.grid(row=2, column=2)

        self.delete_button = Button(self.master, text="DELETE", width=10, command=self.delete_item)
        self.delete_button.grid(row=3, column=2)

        self.clear_button = Button(self.master, text="CLEAR", width=10, command=self.clear_item)
        self.clear_button.grid(row=4, column=2)

        self.search_button = Button(self.master, text="SEARCH", width=10, command=self.search_item)
        self.search_button.grid(row=8, column=2)

    def populate_list(self):
        self.contact_list.delete(0, END)
        for row in db.fetch():
            Id = row[0]
            # self.Fname = row[1]
            # self.Lname = row[2]
            # self.company = row[3]
            # self.phone = row[4]
            # self.email = row[5]
            # self.address = row[6]
            # self.birthday = row[7]
            # display = "Name: {} {}, Company: {}," \
            #         " Phone: {}, Email: {}, Address: {}, Birthday: {},".format(self.Fname, self.Lname, self.company,
            #                                                                   self.phone, self.email, self.address,
            #                                                                  self.birthday)
            self.contact_list.insert(END, row)
            # print(display)

    def select_item(self, event):
        try:
            # Get index
            index = self.contact_list.curselection()[0]
            # print(index)
            # Get selected item
            self.selected_item = self.contact_list.get(index)
            # print(self.selected_item)

            # Add text to entries
            self.firstName_entry.delete(0, END)
            self.firstName_entry.insert(END, self.selected_item[1])
            self.lastName_entry.delete(0, END)
            self.lastName_entry.insert(END, self.selected_item[2])
            self.company_entry.delete(0, END)
            self.company_entry.insert(END, self.selected_item[3])
            self.phone_entry.delete(0, END)
            self.phone_entry.insert(END, self.selected_item[4])
            self.email_entry.delete(0, END)
            self.email_entry.insert(END, self.selected_item[5])
            self.address_entry.delete(0, END)
            self.address_entry.insert(END, self.selected_item[6])
            self.birthday_entry.delete(0, END)
            self.birthday_entry.insert(END, self.selected_item[7])
            self.search_entry.delete(0, END)
            self.search_entry.insert(END, self.selected_item[8])

        except IndexError:
            pass

    def add_item(self):
        if self.firstName_text.get() == "" or self.lastName_text.get() == "" or self.company_text.get() == "" or self.phone_text.get() == "" or self.email_text.get() == "" or self.address_text.get() == "" or self.birthday_text.get() == "":
            messagebox.showerror("Required Fields", "Please include all fields")
            return

        else:
            db.insert(self.firstName_text.get(),
                      self.lastName_text.get(),
                      self.company_text.get(),
                      self.phone_text.get(),
                      self.email_text.get(),
                      self.address_text.get(),
                      self.birthday_text.get(),
                      )
            self.contact_list.delete(0, END)
            self.contact_list.insert(END, (
                self.firstName_text.get(),
                self.lastName_text.get(),
                self.company_text.get(),
                self.phone_text.get(),
                self.email_text.get(),
                self.address_text.get(),
                self.birthday_text.get(),
            )
                                     )
            self.clear_item()
            self.populate_list()

    def update_item(self):
        db.update(
            self.selected_item[0],
            self.firstName_text.get(),
            self.lastName_text.get(),
            self.company_text.get(),
            self.phone_text.get(),
            self.email_text.get(),
            self.address_text.get(),
            self.birthday_text.get(),
        )
        self.populate_list()

    def delete_item(self):
        db.remove(self.selected_item[0])
        self.clear_item()
        self.populate_list()

    def clear_item(self):
        self.firstName_entry.delete(0, END)
        self.lastName_entry.delete(0, END)
        self.company_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.birthday_entry.delete(0, END)
        self.search_entry.delete(0, END)

    def search_item(self):
        line = db.search(self.search_text.get())
        if line is None:
            messagebox.showerror("No Records Found", "No records found, try searching with First Name")
        else:
            self.clear_item()
            self.Fname = line[1]
            self.Lname = line[2]
            self.company = line[3]
            self.phone = line[4]
            self.email = line[5]
            self.address = line[6]
            self.birthday = line[7]

            self.firstName_entry.insert(END, self.Fname)
            self.lastName_entry.insert(END, self.Lname)
            self.company_entry.insert(END, self.company)
            self.phone_entry.insert(END, self.phone)
            self.email_entry.insert(END, self.email)
            self.address_entry.insert(END, self.address)
            self.birthday_entry.insert(END, self.birthday)

            # print(self.Fname)


root = Tk()
app = Application(root)
root.mainloop()
