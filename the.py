from tkinter import *
from tkinter import ttk
import pymysql
import random
from datetime import datetime, timedelta
from tkinter import messagebox


from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql

class Authentication:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.root.title("Authentication Login")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.label_user = Label(self.root, text="Username:")
        self.label_user.pack()
        self.entry_user = Entry(self.root)
        self.entry_user.pack()

        self.label_password = Label(self.root, text="Password:")
        self.label_password.pack()
        self.entry_password = Entry(self.root, show="*")
        self.entry_password.pack()

        self.button_login = Button(self.root, text="Login", command=self.authenticate)
        self.button_login.pack()

    def authenticate(self):
        
        if self.entry_user.get() == "admin" and self.entry_password.get() == "password":
            messagebox.showinfo("Success", "Login Successful")
            self.app.enable_main_window()
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password")

class memberConnect:
    def __init__(self, root):
        self.root = root
        self.root.title("Insurance Services")
        self.root.resizable(True, True)
        self.root.geometry("1380x700+25+50")

        
        self.root.withdraw()

        
        self.auth_window = Toplevel()
        Authentication(self.auth_window, self)

        
        self.initialize_database_connection()

    def enable_main_window(self):
        self.root.deiconify()

    def initialize_database_connection(self):
        try:
            self.connection = pymysql.connect(
                host="localhost",
                user="root",
                password="Kingmaker@2130",
                database="insurance_data"
            )
            self.cursor = self.connection.cursor()
        except pymysql.Error as e:
            messagebox.showerror("Database Error", str(e))


class memberConnect:
    def __init__(self, root):
        self.root = root
        self.root.title("Insurance Services")
        self.root.resizable(True, True)
        self.root.geometry("1380x700+25+50")

        
        self.root.withdraw()

        
        self.auth_window = Toplevel()
        Authentication(self.auth_window, self)

        
        self.initialize_database_connection()
        

    def enable_main_window(self):
        self.root.deiconify()

    def initialize_database_connection(self):
        try:
            self.connection = pymysql.connect(
                host="localhost",
                user="root",
                password="Kingmaker@2130",
                database="insurance_data"
            )
            self.cursor = self.connection.cursor()
        except pymysql.Error as e:
            messagebox.showerror("Database Error", str(e))


            self.cursor = self.connection.cursor()

        self.customerID = StringVar()
        self.Firstname = StringVar()
        self.Lastname = StringVar()
        self.DOB = StringVar()
        self.Gender = StringVar()
        self.PhoneNumber = StringVar()
        self.Email = StringVar()
        self.MaritalStatus = StringVar()
        self.PolicyNumber = StringVar()

        self.Search = StringVar()
        self.Id = StringVar()

        MainFrame = Frame(self.root, bd=1, width=1350, height=668, pady=9, relief=RIDGE, bg='sky blue')
        MainFrame.grid()
        TitleFrames = Frame(MainFrame, bd=1, width=1320, height=50, pady=9, relief=RIDGE)
        TitleFrames.grid(row=0, column=0)

        TitleFrame = Frame(TitleFrames, bd=7, width=1320, height=300, pady=9, relief=RIDGE, bg='dark green')
        TitleFrame.grid(row=0, column=0)

        SearchFrame = Frame(MainFrame, bd=5, width=1340, pady=9, height=300, relief=RIDGE)
        SearchFrame.grid(row=3, column=0)

        MidFrame = Frame(MainFrame, bd=5, width=1340, height=800,  pady=9,relief=RIDGE, bg='sky blue')
        MidFrame.grid(row=5, column=0)

        InnerFrame = Frame(MidFrame, bd=5, width=1340, height=1340,  pady=4, relief=RIDGE)
        InnerFrame.grid(row=0, column=0)

        ButtonFrame = Frame(MidFrame, bd=7, width=1340, height=500,  pady=9,relief=RIDGE, bg="sky blue")
        ButtonFrame.grid(row=1, column=0)

       

        self.labelTitle = Label(TitleFrames, font=('arial', 70, 'bold'), text="The XYZ Insurance Services",
                                bg="green", fg="white")
        self.labelTitle.grid(row=0, column=0, padx=90)

        self.txtSearch = Entry(SearchFrame, font=('Times new roman', 17), width=33, textvariable=self.Search,
                               justify='center')
        self.txtSearch.grid(row=0, column=2)
        self.btnSearch = Button(SearchFrame, pady=1, bd=4, font=('Times new roman', 17, 'bold'), text="Search",
                                width=9, height=1, bg='sky blue', command=self.find_customer)
        self.btnSearch.grid(row=0, column=3, padx=1)

        self.labelcustomerID = Label(InnerFrame, font=('arial', 15, 'bold'), text="Customer ID", bd=7, anchor='w',
                                     justify=LEFT)
        self.labelcustomerID.grid(row=0, column=0, padx=4, sticky=W)

        self.txtcustomerID = Entry(InnerFrame, font=('Times new roman', 15), bd=5, width=33,
                                   textvariable=self.customerID, justify='left')
        self.txtcustomerID.grid(row=0, column=1)

        self.labelFirstname = Label(InnerFrame, font=('arial', 15, 'bold'), text="First Name", bd=7, anchor='w',
                                    justify=LEFT)
        self.labelFirstname.grid(row=1, column=0, padx=5, sticky=W)
        self.txtFirstname = Entry(InnerFrame, font=('Times new roman', 15), bd=5, width=33,
                                  textvariable=self.Firstname, justify='left')
        self.txtFirstname.grid(row=1, column=1)

        self.labelLastname = Label(InnerFrame, font=('arial', 15, 'bold'), text="Last Name", bd=7, justify=LEFT)
        self.labelLastname.grid(row=2, column=0, padx=5, sticky=W)
        self.txtLastname = Entry(InnerFrame, font=('Times new roman', 15), width=33, bd=5,
                                 textvariable=self.Lastname, justify='left')
        self.txtLastname.grid(row=2, column=1)

        self.labelGender = Label(InnerFrame, font=('arial', 15, 'bold'), text="Gender", bd=7)
        self.labelGender.grid(row=1, column=2, padx=5, sticky=W)
        self.cboGender = ttk.Combobox(InnerFrame, font=('Times new roman', 15), width=33,
                                      textvariable=self.Gender, state='readonly')
        self.cboGender['values'] = ('', 'Female', 'Male', 'Other')
        self.cboGender.current(0)
        self.cboGender.grid(row=1, column=3)

        self.labelEmail = Label(InnerFrame, font=('arial', 15, 'bold'), text="Email", bd=7)
        self.labelEmail.grid(row=0, column=4, padx=5, sticky=W)
        self.txtEmail = Entry(InnerFrame, font=('Times new roman', 15), width=33, bd=5,
                              textvariable=self.Email, justify='left')
        self.txtEmail.grid(row=0, column=5)

        self.labelPhoneNumber = Label(InnerFrame, font=('arial', 15, 'bold'), text="Phone Number", bd=7)
        self.labelPhoneNumber.grid(row=2, column=2, padx=5, sticky=W)
        self.txtPhoneNumber = Entry(InnerFrame, font=('Times new roman', 15), width=33, bd=5,
                                    textvariable=self.PhoneNumber, justify='left')
        self.txtPhoneNumber.grid(row=2, column=3, sticky=W)

        self.labelDOB = Label(InnerFrame, font=('arial', 15, 'bold'), text="DOB", bd=7)
        self.labelDOB.grid(row=0, column=2, padx=5, sticky=W)
        self.txtDOB = Entry(InnerFrame, font=('Times new roman', 15), width=33, bd=5,
                            textvariable=self.DOB, justify='left')
        self.txtDOB.grid(row=0, column=3)

        self.labelMaritalStatus = Label(InnerFrame, font=('arial', 15, 'bold'), text="Marital Status", bd=7)
        self.labelMaritalStatus.grid(row=1, column=4, padx=5, sticky=W)
        self.cboMaritalStatus = ttk.Combobox(InnerFrame, font=('Times new roman', 15), width=33,
                                             textvariable=self.MaritalStatus, state='readonly')
        self.cboMaritalStatus['values'] = ('', 'Single', 'Married', 'Divorced', 'Widowed', 'Other')
        self.cboMaritalStatus.current(0)
        self.cboMaritalStatus.grid(row=1, column=5)

        self.btnAddCustomer = Button(ButtonFrame, pady=1, bd=4, font=('Times new roman', 17, 'bold'),
                                     text="Add Customer", width=11, height=1, bg='sky blue', command=self.add_customer)
        self.btnAddCustomer.grid(row=0, column=0, padx=10)
        self.btnFindCustomer = Button(ButtonFrame, pady=1, bd=4, font=('Times new roman', 17, 'bold'),
                                      text="Find Customer", width=11, height=1, bg='sky blue', command=self.find_customer)
        self.btnFindCustomer.grid(row=0, column=1, padx=10)
        self.btnPolicy = Button(ButtonFrame, pady=1, bd=4, font=('Times new roman', 17, 'bold'), text="Show Policy",
                                width=11, height=1, bg='sky blue', command=self.show_policy)
        self.btnPolicy.grid(row=0, column=2, padx=10)
        self.btnPolicyStatus = Button(ButtonFrame, pady=1, bd=4, font=('Times new roman', 17, 'bold'),
                                      text="Policy Status", width=11, height=1, bg='sky blue', command=self.policy_status)
        self.btnPolicyStatus.grid(row=0, column=3, padx=10)
        self.btnPremiumStatus = Button(ButtonFrame, pady=1, bd=4, font=('Times new roman', 17, 'bold'),
                                       text="Premium Status", width=11, height=1, bg='sky blue', command=self.premium_status)
        self.btnPremiumStatus.grid(row=0, column=4, padx=10)
        self.btnCarriers = Button(ButtonFrame, pady=1, bd=4, font=('Times new roman', 17, 'bold'),
                                  text="Available Carriers", width=11, height=1, bg='sky blue', command=self.show_carriers)
        self.btnCarriers.grid(row=0, column=5, padx=10)
        self.btnRemoveCustomer = Button(ButtonFrame, pady=1, bd=4, font=('Times new roman', 17, 'bold'),
                                        text="Remove Customer", width=11, height=1, bg='sky blue',
                                        command=self.remove_customer)
        self.btnRemoveCustomer.grid(row=0, column=6, padx=10)
        self.btnAddPolicy = Button(ButtonFrame, pady=1, bd=4, font=('Times new roman', 17, 'bold'),
                                   text="Issue Policy", width=11, height=1, bg='sky blue', command=self.add_customer_and_issue_policy)
        self.btnAddPolicy.grid(row=0, column=7, padx=10)

        
        lblSpace = Label(ButtonFrame, text=" ", bg='sky blue')
        lblSpace.grid(row=1, column=0, columnspan=8)

        self.btnPaidCustomers = Button(ButtonFrame, pady=1, bd=4, font=('Times new roman', 17, 'bold'),
                                       text="Paid Customers", width=15, height=1, bg='sky blue',
                                       command=self.find_paid_customers)
        self.btnPaidCustomers.grid(row=2, column=2, padx=10)

        self.btnUnpaidCustomers = Button(ButtonFrame, pady=1, bd=4, font=('Times new roman', 17, 'bold'),
                                         text="Unpaid Customers", width=15, height=1, bg='sky blue',
                                         command=self.find_unpaid_customers)
        self.btnUnpaidCustomers.grid(row=2, column=5, padx=10)


        self.txtFilterCriteria = Entry(SearchFrame, font=('Times new roman', 17), width=33, textvariable=self.Search,
                               justify='center')
        self.txtFilterCriteria.grid(row=0, column=4)

    def add_customer(self):
        try:
            
            first_name = self.Firstname.get()
            last_name = self.Lastname.get()
            dob = self.DOB.get()
            sex = self.Gender.get()
            marital_status = self.MaritalStatus.get()
            email = self.Email.get()
            phone_number = self.PhoneNumber.get()

            
            query = "INSERT INTO customers (CustomerID, FirstName, LastName, DOB, Sex, MaritalStatus, E python3 -m pip install pandasmailID, PhoneNumber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
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
            search_criteria = self.Search.get()
        
            query = "SELECT * FROM customers WHERE CustomerID = %s OR FirstName = %s OR LastName = %s OR EmailID = %s OR PhoneNumber = %s"
            self.cursor.execute(query, (search_criteria, search_criteria, search_criteria, search_criteria, search_criteria))
            result = self.cursor.fetchall()
            if result:
            
                self.customerID.set(result[0][0])
                self.Firstname.set(result[0][1])
                self.Lastname.set(result[0][2])
                self.DOB.set(result[0][3])
                self.Gender.set(result[0][4])
                self.MaritalStatus.set(result[0][5])
                self.Email.set(result[0][6])
                self.PhoneNumber.set(result[0][7])
            else:
                messagebox.showinfo("Info", "Customer not found")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_policy(self):
        try:
           customer_id = self.customerID.get()
           query = "SELECT * FROM PolicyDetail WHERE CustomerID = %s"
           self.cursor.execute(query, (customer_id,))
           result = self.cursor.fetchall()
           if result:
            policy_info = "\n".join([f"PolicyID: {row[0]}, PolicyType: {row[2]}, CarrierName: {row[4]}, PolicyStatus: {row[5]}" for row in result])
            messagebox.showinfo("PolicyDetails", policy_info)
           
           else:
            messagebox.showinfo("Info", "No policies found for this customer")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def policy_status(self):
        try:
            policy_number = self.Search.get()  
            query = "SELECT PolicyNumber, PolicyStatus FROM PolicyDetail WHERE CustomerID = %s"
            self.cursor.execute(query, (policy_number,))
            result = self.cursor.fetchone()
            if result:
                policy_number = result[0]
                policy_status = result[1]
                messagebox.showinfo("Policy Status", f"Policy Number: {policy_number}\nStatus: {policy_status}")
            else:
                messagebox.showinfo("Info", "Policy not found")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def premium_status(self):
        try:
            policy_number = self.Search.get()  
            query = "SELECT * FROM Premiums WHERE CustomerID = %s"
            self.cursor.execute(query, (policy_number,))
            result = self.cursor.fetchone()
            if result:
                premium_info = f"Policy Number: {result[1]}\nPremium Amount: {result[3]}\nPayment Status: {result[5]}"
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

    def add_customer_and_issue_policy(self):
        try:
        
            self.add_customer()

        
            policy_number = ''.join(random.choices('0123456789', k=4))

        
            query_policy = "INSERT INTO PolicyDetail (PolicyNumber, CustomerID, Type, CarrierName, PolicyStatus) VALUES (%s, %s, %s, %s, %s)"
            values_policy = (policy_number, self.customerID.get(), "auto", "Safeco", "Active")
            self.cursor.execute(query_policy, values_policy)

        
            premium_amount = round(random.uniform(300, 1000), 2)

        
            today = datetime.now()
            premium_due_date = (today + timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d')

        
            query_premium = "INSERT INTO Premiums (PolicyNumber, CustomerID, PremiumAmount, PremiumDueDate, PaymentStatus, PolicyType, StatusName) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values_premium = (policy_number, self.customerID.get(), premium_amount, premium_due_date, "Unpaid", "auto", "Active")
            self.cursor.execute(query_premium, values_premium)

        
            self.connection.commit()

        
            messagebox.showinfo("Success", "Customer added and policy issued successfully")
        except Exception as e:
        
            self.connection.rollback()
            messagebox.showerror("Error", str(e))

    def remove_customer(self):
        try:
            customer_id = self.customerID.get()

        
            query_check_policy = "SELECT COUNT(*) FROM PolicyDetail WHERE CustomerID = %s"
            self.cursor.execute(query_check_policy, (customer_id,))
            policy_count = self.cursor.fetchone()[0]

            if policy_count > 0:
                messagebox.showwarning("Warning", "Cannot remove customer with active policies")
                return

        
            query_delete_premium = "DELETE FROM Premiums WHERE CustomerID = %s"
            self.cursor.execute(query_delete_premium, (customer_id,))

        
            query_delete_customer = "DELETE FROM customers WHERE CustomerID = %s"
            self.cursor.execute(query_delete_customer, (customer_id,))

        
            self.connection.commit()

        
            messagebox.showinfo("Success", "Customer removed successfully")
        
        
            self.customerID.set("")
            self.Firstname.set("")
            self.Lastname.set("")
            self.DOB.set("")
            self.Gender.set("")
            self.MaritalStatus.set("")
            self.Email.set("")
            self.PhoneNumber.set("")
        except Exception as e:
        
            self.connection.rollback()
            messagebox.showerror("Error", str(e))

    def find_paid_customers(self):
        try:
            query = "SELECT c.*, pd.*, p.PaymentStatus FROM customers c INNER JOIN PolicyDetail pd ON c.CustomerID = pd.CustomerID INNER JOIN Premiums p ON pd.PolicyNumber = p.PolicyNumber WHERE p.PaymentStatus = 'Paid'"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.display_customers(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def find_unpaid_customers(self):
        try:
            query = "SELECT c.*, pd.*, p.PaymentStatus FROM customers c INNER JOIN PolicyDetail pd ON c.CustomerID = pd.CustomerID INNER JOIN Premiums p ON pd.PolicyNumber = p.PolicyNumber WHERE p.PaymentStatus = 'Unpaid'"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.display_customers(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_customers(self, result):
    
        
        self.Firstname.set("")
        self.Lastname.set("")
        self.Email.set("")
        self.PhoneNumber.set("")

        if result:
        
            customer_list = []
            for row in result:
                customer_info = f" Name: {row[1]} {row[2]}, Email: {row[6]}, Phone Number: {row[7]}\n"
                customer_list.append(customer_info)

            messagebox.showinfo("Customer List", "\n".join(customer_list))
        else:
            messagebox.showinfo("Info", "No customers found")

    def __del__(self):
        if self.connection:
            self.connection.close()


       

if __name__ == '__main__':
    root = Tk()
    app = memberConnect(root)
    root.mainloop()