from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
import random


class memberConnect:

    def __init__(self, root):
        self.root = root
        self.root.title("Insurance Services")
        self.root.resizable(True, True)
        self.root.geometry("1400x750+25+50")

        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="Kingmaker@2130",
            database="insurance_management"
        )

        self.cursor = self.connection.cursor()

        self.customerID = StringVar()
        self.Firstname = StringVar()
        self.Lastname = StringVar()
        self.DOB = StringVar()
        self.Gender = StringVar()
        self.PhoneNumber = StringVar()
        self.Email = StringVar()
        self.MaritalStatus = StringVar()

        self.Search = StringVar()
        self.Id = StringVar()

        MainFrame = Frame(self.root, bd=10, width=1350, height=668, relief=RIDGE, bg='cadetblue')
        MainFrame.grid()
        TitleFrames = Frame(MainFrame, bd=7, width=1320, height=100, relief=RIDGE)
        TitleFrames.grid(row=0, column=0)

        TitleFrame = Frame(TitleFrames, bd=7, width=1320, height=100, relief=RIDGE, bg='cadetblue')
        TitleFrame.grid(row=0, column=0)

        SearchFrame = Frame(MainFrame, bd=5, width=1340, height=50, relief=RIDGE)
        SearchFrame.grid(row=1, column=0)

        MidFrame = Frame(MainFrame, bd=5, width=1340, height=500, relief=RIDGE, bg='cadetblue')
        MidFrame.grid(row=3, column=0)

        InnerFrame = Frame(MidFrame, bd=5, width=1340, height=180, padx=24, pady=4, relief=RIDGE)
        InnerFrame.grid(row=0, column=0)

        ButtonFrame = Frame(MidFrame, bd=7, width=1340, height=50, relief=RIDGE, bg="cadetblue")
        ButtonFrame.grid(row=1, column=0)

        treeviewFrame = Frame(MidFrame, bd=5, width=1340, height=400, relief=RIDGE, padx=4)
        treeviewFrame.grid(row=2, column=0, padx=5, pady=0)

        self.labelTitle = Label(TitleFrames, font=('arial', 40, 'bold'), text="The XYZ Insurance Services",
                                bg="cadet blue", fg="white")
        self.labelTitle.grid(row=0, column=0, padx=90)

        self.txtSearch = Entry(SearchFrame, font=('Times new roman', 13), width=33, textvariable=self.Search,
                               justify='center')
        self.txtSearch.grid(row=0, column=2)
        self.btnSearch = Button(SearchFrame, pady=1, bd=4, font=('Times new roman', 12, 'bold'), text="Search",
                                width=9, height=1, bg='cadetblue', command=self.find_customer)
        self.btnSearch.grid(row=0, column=3, padx=1)

        self.labelcustomerID = Label(InnerFrame, font=('arial', 12, 'bold'), text="Customer ID", bd=7, anchor='w',
                                     justify=LEFT)
        self.labelcustomerID.grid(row=0, column=0, padx=4, sticky=W)

        self.txtcustomerID = Entry(InnerFrame, font=('Times new roman', 13), bd=5, width=33,
                                   textvariable=self.customerID, justify='left')
        self.txtcustomerID.grid(row=0, column=1)

        self.labelFirstname = Label(InnerFrame, font=('arial', 12, 'bold'), text="First Name", bd=7, anchor='w',
                                    justify=LEFT)
        self.labelFirstname.grid(row=1, column=0, padx=5, sticky=W)
        self.txtFirstname = Entry(InnerFrame, font=('Times new roman', 13), bd=5, width=33,
                                  textvariable=self.Firstname, justify='left')
        self.txtFirstname.grid(row=1, column=1)

        self.labelLastname = Label(InnerFrame, font=('arial', 12, 'bold'), text="Last Name", bd=7, justify=LEFT)
        self.labelLastname.grid(row=2, column=0, padx=5, sticky=W)
        self.txtLastname = Entry(InnerFrame, font=('Times new roman', 13), width=33, bd=5,
                                 textvariable=self.Lastname, justify='left')
        self.txtLastname.grid(row=2, column=1)

        self.labelGender = Label(InnerFrame, font=('arial', 12, 'bold'), text="Gender", bd=7)
        self.labelGender.grid(row=1, column=2, padx=5, sticky=W)
        self.cboGender = ttk.Combobox(InnerFrame, font=('Times new roman', 13), width=33,
                                      textvariable=self.Gender, state='readonly')
        self.cboGender['values'] = ('', 'Female', 'Male', 'Other')
        self.cboGender.current(0)
        self.cboGender.grid(row=1, column=3)

        self.labelEmail = Label(InnerFrame, font=('arial', 12, 'bold'), text="Email", bd=7)
        self.labelEmail.grid(row=0, column=4, padx=5, sticky=W)
        self.txtEmail = Entry(InnerFrame, font=('Times new roman', 13), width=33, bd=5,
                              textvariable=self.Email, justify='left')
        self.txtEmail.grid(row=0, column=5)

        self.labelPhoneNumber = Label(InnerFrame, font=('arial', 12, 'bold'), text="Phone Number", bd=7)
        self.labelPhoneNumber.grid(row=2, column=2, padx=5, sticky=W)
        self.txtPhoneNumber = Entry(InnerFrame, font=('Times new roman', 13), width=33, bd=5,
                                    textvariable=self.PhoneNumber, justify='left')
        self.txtPhoneNumber.grid(row=2, column=3, sticky=W)

        self.labelDOB = Label(InnerFrame, font=('arial', 12, 'bold'), text="DOB", bd=7)
        self.labelDOB.grid(row=0, column=2, padx=5, sticky=W)
        self.txtDOB = Entry(InnerFrame, font=('Times new roman', 13), width=33, bd=5,
                            textvariable=self.DOB, justify='left')
        self.txtDOB.grid(row=0, column=3)

        self.labelMaritalStatus = Label(InnerFrame, font=('arial', 12, 'bold'), text="Marital Status", bd=7)
        self.labelMaritalStatus.grid(row=1, column=4, padx=5, sticky=W)
        self.cboMaritalStatus = ttk.Combobox(InnerFrame, font=('Times new roman', 13), width=33,
                                             textvariable=self.MaritalStatus, state='readonly')
        self.cboMaritalStatus['values'] = ('', 'Single', 'Married', 'Divorced', 'Widowed', 'Other')
        self.cboMaritalStatus.current(0)
        self.cboMaritalStatus.grid(row=1, column=5)

        self.btnAddCustomer = Button(ButtonFrame, pady=1, bd=4, font=('Times new roman', 12, 'bold'),
                                     text="Add Customer", width=11, height=1, bg='cadetblue', command=self.add_customer)
        self.btnAddCustomer.grid(row=0, column=0, padx=10)
        self.btnFindCustomer = Button(ButtonFrame, pady=1, bd=4, font=('Times new roman', 12, 'bold'),
                                      text="Find Customer", width=11, height=1, bg='cadetblue', command=self.find_customer)
        self.btnFindCustomer.grid(row=0, column=1, padx=10)
        self.btnPolicy = Button(ButtonFrame, pady=1, bd=4, font=('Times new roman', 12, 'bold'), text="Show Policy",
                                width=11, height=1, bg='cadetblue', command=self.show_policy)
        self.btnPolicy.grid(row=0, column=2, padx=10)
        self.btnPolicyStatus = Button(ButtonFrame, pady=1, bd=4, font=('Times new roman', 12, 'bold'),
                                      text="Policy Status", width=11, height=1, bg='cadetblue', command=self.policy_status)
        self.btnPolicyStatus.grid(row=0, column=3, padx=10)
        self.btnPremiumStatus = Button(ButtonFrame, pady=1, bd=4, font=('Times new roman', 12, 'bold'),
                                       text="Premium Status", width=11, height=1, bg='cadetblue', command=self.premium_status)
        self.btnPremiumStatus.grid(row=0, column=4, padx=10)
        self.btnCarriers = Button(ButtonFrame, pady=1, bd=4, font=('Times new roman', 12, 'bold'),
                                  text="Available Carriers", width=16, height=1, bg='cadetblue', command=self.show_carriers)
        self.btnCarriers.grid(row=0, column=5, padx=10)

    def add_customer(self):
        try:
            # Get customer details from the entry fields
            first_name = self.Firstname.get()
            last_name = self.Lastname.get()
            dob = self.DOB.get()
            sex = self.Gender.get()
            marital_status = self.MaritalStatus.get()
            email = self.Email.get()
            phone_number = self.PhoneNumber.get()

            # Insert customer details into the database
            query = "INSERT INTO customers (CustomerID, FirstName, LastName, DOB, Sex, MaritalStatus, EmailID, PhoneNumber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (
                self.customerID.get(),
                first_name,
                last_name,
                dob,
                sex,
                marital_status,
                email,
                phone_number
            )
            self.cursor.execute(query, values)
            self.connection.commit()
            messagebox.showinfo("Success", "Customer added successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def find_customer(self):
        try:
            customer_id = self.Search.get()
            query = "SELECT * FROM customers WHERE CustomerID = %s"
            self.cursor.execute(query, (customer_id,))
            result = self.cursor.fetchone()
            if result:
                self.customerID.set(result[0])
                self.Firstname.set(result[1])
                self.Lastname.set(result[2])
                self.DOB.set(result[3])
                self.Gender.set(result[4])
                self.MaritalStatus.set(result[5])
                self.Email.set(result[6])
                self.PhoneNumber.set(result[7])
            else:
                messagebox.showinfo("Info", "Customer not found")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_policy(self):
        try:
           customer_id = self.customerID.get()
           query = "SELECT * FROM policies WHERE CustomerID = %s"
           self.cursor.execute(query, (customer_id,))
           result = self.cursor.fetchall()
           if result:
            policy_info = "\n".join([f"PolicyID: {row[0]}, PolicyType: {row[1]}, StartDate: {row[2]}, EndDate: {row[3]}, PremiumAmount: {row[4]}" for row in result])
            messagebox.showinfo("Policy Details", policy_info)
           else:
            messagebox.showinfo("Info", "No policies found for this customer")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def policy_status(self):
        try:
            policy_id = self.Id.get()
            query = "SELECT * FROM policies WHERE PolicyID = %s"
            self.cursor.execute(query, (policy_id,))
            result = self.cursor.fetchone()
            if result:
                status = result[5]
                messagebox.showinfo("Policy Status", f"Policy ID: {policy_id}\nStatus: {status}")
            else:
                messagebox.showinfo("Info", "Policy not found")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def premium_status(self):
        try:
            policy_id = self.Id.get()
            query = "SELECT * FROM premiums WHERE PolicyID = %s"
            self.cursor.execute(query, (policy_id,))
            result = self.cursor.fetchone()
            if result:
                premium_info = f"Policy ID: {policy_id}\nPremium Amount: {result[1]}\nPayment Status: {result[2]}"
                messagebox.showinfo("Premium Status", premium_info)
            else:
                messagebox.showinfo("Info", "Premium details not found for this policy")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_carriers(self):
        try:
            query = "SELECT * FROM Carrier"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            if result:
                carrier_info = "\n".join([f"{row[0]}: {row[1]}" for row in result])
                messagebox.showinfo("Available Carriers", carrier_info)
            else:
                messagebox.showinfo("Info", "No carriers found")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def __del__(self):
        if self.connection:
            self.connection.close()


if __name__ == '__main__':
    root = Tk()
    app = memberConnect(root)
    root.mainloop()