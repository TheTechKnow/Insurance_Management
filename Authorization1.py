from tkinter import *
from tkinter import messagebox
from PIL import ImageTk 
from PIL import Image, ImageTk

class Authentication:
    def __init__(self, root):
        self.root = root
        self.root.title("Authentication Login")
        self.root.geometry("1260x750+50+50")
        self.root.resizable(True, True)

        # Load the background image
        self.bg = Image.open("/Users/gursimrankaur/Desktop/insurance Small.png")
        self.bg = ImageTk.PhotoImage(self.bg)

        # Create a Label to display the background image
        self.bg_image = Label(self.root, image=self.bg)
        #self.bg_image = Label(self.root, image=self.bg)
        self.bg_image.pack(fill=BOTH, expand=YES)
        #self.bg_image.place(x=0, y=0, relwidth=0.99, relheight=0.99)

        frame_authentication = Frame(self.root, bg="white")
        frame_authentication.place(relx=0.60, rely=0.3, relwidth=0.3, relheight=0.6)

        title = Label(frame_authentication, text="Sign in", font=("Microsoft YaHei UI Light", 27, "bold"), fg="#57a1f8", bg="white")
        title.place(relx=0.2, rely=0.05)
        description = Label(frame_authentication, text="Welcome to xyz Insurance", font=("times new roman", 15, "bold"), fg="#57a1f8", bg="white")
        description.place(relx=0.2, rely=0.15)

        label_username = Label(frame_authentication, text="Username", font=("Merriweather", 15, "bold"), fg="gray", bg="white")
        label_username.place(relx=0.1, rely=0.3)
        self.text_username = Entry(frame_authentication, font=("Merriweather", 15))
        self.text_username.place(relx=0.1, rely=0.38, relwidth=0.8, relheight=0.1)

        label_password = Label(frame_authentication, text="Password", font=("Merriweather", 15, "bold"), fg="gray", bg="white")
        label_password.place(relx=0.1, rely=0.5)
        self.text_password = Entry(frame_authentication, font=("Merriweather", 15))
        self.text_password.place(relx=0.1, rely=0.58, relwidth=0.8, relheight=0.1)

        forget_button = Button(frame_authentication, text="Forget Password?", bg="white", fg="#57a1f8", bd=0, font=("Merriweather", 12))
        forget_button.place(relx=0.1, rely=0.7)

        sign_in_button = Button(frame_authentication, command=self.sign_in, text="Sign In", fg='#57a1f8', bg='white',bd=0.0,  font=("Merriweather", 12))
        sign_in_button.place(relx=0.3, rely=0.85, relwidth=0.4, relheight=0.1)

    def sign_in(self):
        if self.text_password.get() == "" or self.text_username.get() == "":
            messagebox.showerror("Error", "Please Enter the login credentials", parent=self.root)
        
        elif self.text_password.get() != "Services@213" or self.text_username.get() != "xyzinsuranceservices":
            messagebox.showerror("Invalid Credentials", "Enter the correct Credentials", parent=self.root)

        else:
            messagebox.showinfo("Welcome to xyz Insurance")

root = Tk()
app = Authentication(root)
root.mainloop()