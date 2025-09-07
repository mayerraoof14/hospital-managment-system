from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
import ttkthemes
import mysql.connector
from tkinter import ttk


class MBAHospitalApp:
    def __init__(self, master):
        self.master = master
        self.master.title("MBA Hospital")
        self.master.geometry("1920x1080")
        self.master.configure(bg="#32acc7")

        # Main Frame
        self.main_frame = Frame(self.master, bg="#32acc7")
        self.main_frame.pack(fill=BOTH, expand=True)

        # Create the login frame
        self.login_frame = Frame(self.master, bg="#32acc7")

        # Show the main frame
        self.show_main_frame()

    def show_main_frame(self):
        self.login_frame.pack_forget()  # Hide the login frame
        self.main_frame.pack(fill=BOTH, expand=True)  # Show the main frame

        # Doctor Button
        doctor_button = Button(self.main_frame,
                               text="Doctor",
                               height=1,
                               width=13,
                               font=("Roboto", 28, "bold"),
                               background="#0088a6",
                               activebackground="#99cfdb",
                               highlightcolor="#0098B9",
                               border=0,
                               cursor="hand2",
                               foreground="white",
                               command=lambda: self.open_login_page("Doctor"))
        doctor_button.place(x=250, y=400)

        # Receptionist Button
        receptionist_button = Button(self.main_frame,
                                     text="Receptionist",
                                     height=1,
                                     width=13,
                                     font=("Roboto", 28, "bold"),
                                     background="#0088a6",
                                     foreground="white",
                                     activebackground="#99cfdb",
                                     border=0,
                                     cursor="hand2",
                                     command=lambda: self.open_login_page("Receptionist"))
        receptionist_button.place(x=250, y=500)

        # Adding Images
        self.add_images(self.main_frame)

    def open_login_page(self, role):
        self.main_frame.pack_forget()  # Hide the main frame
        self.show_login(role)

    def show_login(self, role):
        self.login_frame.pack(fill=BOTH, expand=True)  # Show the login frame

        # Adding Images
        self.add_images(self.login_frame)

        # Login logic
        def login():
            username=usernameEntry.get()
            password=PasswordEntry.get()
            # Check if username or password fields are empty
            if username == '' or password == '':
                messagebox.showerror('ERROR', 'Fields cannot be empty')
                return

            try:
            # Connect to the MySQL database
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",  # Replace with your MySQL username
                    password="1234",  # Replace with your MySQL password
                    database="hospital"  # Replace with your database name
                )
                cursor = conn.cursor()

            # Query the receptionists table
                query_receptionists = "SELECT * FROM receptionists WHERE user_name=%s AND pass_word=%s"
                cursor.execute(query_receptionists, (username, password))
                result_receptionists = cursor.fetchone()

                if result_receptionists:
                    self.master.destroy()  # Close the login window
                    import screen_receptionist  # Open the receptionist screen
                    return

        # Query the doctors table if not found in receptionists
                query_doctors = "SELECT * FROM doctors WHERE user_name=%s AND pass_word=%s"
                cursor.execute(query_doctors, (username, password))
                result_doctors = cursor.fetchone()

                if result_doctors:
                    self.master.destroy()  # Close the login window
                    import screen_doctor1  # Open the doctor screen
                    return

        # If no match in either table
                messagebox.showerror('Error', 'Invalid username or password')

                cursor.close()
                conn.close()

            except mysql.connector.Error as err:
                messagebox.showerror('Database Error', f'Error: {err}')
                print(f"Error: {err}")

        # Create login frame
        login_frame = Frame(self.login_frame, bg="#32acc7", width=350, height=350)
        login_frame.place(x=100, y=300)

        # Username entry
        def on_enter(e):
            usernameEntry.delete(0, "end")

        def on_leave(e):
            if usernameEntry.get() == "":
                usernameEntry.insert(0, "Username")

        usernameEntry = Entry(login_frame, width=25, fg="white", border=0, bg="#32acc7", font=("Roboto", 14))
        usernameEntry.place(x=30, y=80)
        usernameEntry.insert(0, "Username")
        usernameEntry.bind("<FocusIn>", on_enter)
        usernameEntry.bind("<FocusOut>", on_leave)
        Frame(login_frame, width=280, height=2, bg="white").place(x=30, y=107)

        # Password entry
        def on_enter_password(e):
            PasswordEntry.delete(0, "end")

        def on_leave_password(e):
            if PasswordEntry.get() == "":
                PasswordEntry.insert(0, "Password")

        PasswordEntry = Entry(login_frame, width=25, fg="white", border=0, bg="#32acc7", font=("Roboto", 14))
        PasswordEntry.place(x=30, y=150)
        PasswordEntry.insert(0, "Password")
        PasswordEntry.bind("<FocusIn>", on_enter_password)
        PasswordEntry.bind("<FocusOut>", on_leave_password)
        Frame(login_frame, width=280, height=2, bg="white").place(x=30, y=177)

        # Login Button
        Button(login_frame, width=12, pady=7, command=login, font=("Roboto", 14, "bold"), text="Login", bg="#0088a6",
               fg="white", border=0, cursor="hand2").place(x=200, y=215)


    def add_images(self, frame):
        # Adding Images
        # Back Button with an Image
        back_img = Image.open("D:/Old/UFE/Materials/Year 2/Mini Project/Images/back_white.png").resize((40, 40))
        back_img = ImageTk.PhotoImage(back_img)
        home = Image.open("D:/Old/UFE/Materials/Year 2/Mini Project/Images/Home page.png").resize((780, 580))
        home = ImageTk.PhotoImage(home)
        home_label = Label(frame, image=home, bd=0, bg="#32acc7")
        home_label.image = home  # Keep a reference to avoid garbage collection
        home_label.place(x=700, y=100)

        logo = Image.open("D:/Old/UFE/Materials/Year 2/Mini Project/Images/Logo.png").resize((140, 115))
        logo = ImageTk.PhotoImage(logo)
        logo_label = Label(frame, image=logo, bd=0, bg="#32acc7")
        logo_label.image = logo  # Keep a reference to avoid garbage collection
        logo_label.place(x=30, y=0)

        back_button = Button(self.login_frame, image=back_img, bg="#32acc7", command=self.show_main_frame, border=0, cursor="hand2")
        back_button.image = back_img  # Keep a reference to avoid garbage collection
        back_button.place(x=1420, y=70)


root = Tk()
app = MBAHospitalApp(root)
root.mainloop()