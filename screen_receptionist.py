from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
import ttkthemes
import mysql.connector
from tkinter import ttk

dash_rec=ttkthemes.ThemedTk()
dash_rec.get_themes()
dash_rec.set_theme('breeze')
dash_rec.geometry('1920x1080')
dash_rec.title('MBA Hospital Dashboard - Receptionist')
dash_rec.config(bg='#32acc7')

logo_image = Image.open("D:/Old/UFE/Materials/Year 2/Mini Project/Images/Logo.png")  # Open the image file
logo_image = logo_image.resize((140,115))  # Resize the image (optional)
logo = ImageTk.PhotoImage(logo_image)  # Convert to Tkinter-compatible image

# Create a label to hold the image
logo_label = Label(dash_rec, image=logo, bg='#32acc7')  # Use same bg color for blending
logo_label.place(x=30, y=30)

rightframe=Frame(dash_rec, bg="white")
rightframe.place(x=350,y=200,width=1110,height=630)

back_image=Image.open("D:/Old/UFE/Materials/Year 2/Mini Project/Images/back_color.png").resize((30,30))
back_image=ImageTk.PhotoImage(back_image)
back_image_label=Label(rightframe, image=back_image, bd=0, bg="white")
back_image_label.place(x=700,y=40)

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def on_row_click_R(event):
    # Navigate to the patient information frame
    book_room()

def on_row_click_D(event):
    book_app()


logout_img = Image.open("D:/Old/UFE/Materials/Year 2/Mini Project/Images/Log out button.png").resize((30,30))
logout_img = ImageTk.PhotoImage(logout_img)

def add_back_button():
    back_btn = Button(rightframe, image=back_image, bd=0, bg="white", cursor="hand2", command=doctors)
    back_btn.place(x=1040, y=40)

def add_back_button_H():
    # Adds a back button to the current frame
    back_btn = Button(rightframe, image=back_image, bd=0, bg="white", cursor="hand2", command=home)
    back_btn.place(x=1040,y=40)

def add_back_button_R():
    # Adds a back button to the current frame
    back_btn = Button(rightframe, image=back_image, bd=0, bg="white", cursor="hand2", command=availbe_rooms)
    back_btn.place(x=1040,y=40)

def logout1(current_window):
    current_window.destroy()  # Close the current window
    import Choose  # Import the Choose screen
    Choose.mainloop() 

def add_logout():
    # Adds a back button to the current frame
    logout_btn = Button(dash_rec, image=logout_img, bd=0, bg="#32acc7", cursor="hand2", command=lambda:logout1(dash_rec))
    logout_btn.place(x=1420,y=70)

add_logout()


def cardiology():
    clear_frame(rightframe)
    text_lbl = Label(rightframe, text = "Available Doctors")
    text_lbl.config(font =('Roboto' ,24 , 'bold'), bg="white", fg="#006B82")
    text_lbl.place(x=50, y=40)

    table_frame = Frame(rightframe, bg="white")
    table_frame.place(x=100, y=120, width=900, height=400)

    scrollbarX = Scrollbar(table_frame, orient=HORIZONTAL)
    scrollbarY = Scrollbar(table_frame, orient=VERTICAL)
    doctortable = ttk.Treeview(table_frame, columns=('doctor_id', 'doctor_name', 'start_time', 'end_time'),xscrollcommand=scrollbarX.set, yscrollcommand=scrollbarY.set)
    scrollbarX.config(command=doctortable.xview)
    scrollbarY.config(command=doctortable.yview)
    scrollbarX.pack(side=BOTTOM, fill=X)
    scrollbarY.pack(side=RIGHT, fill=Y)
    doctortable.pack(fill=BOTH, expand=True)
    doctortable.heading('doctor_id', text='Doctor ID')
    doctortable.heading('doctor_name', text='Doctor Name')
    doctortable.heading('start_time', text='Start Time')
    doctortable.heading('end_time', text='End Time')
    doctortable.column("doctor_id", width=100, anchor=CENTER)
    doctortable.column("start_time", width=120, anchor=CENTER)
    doctortable.column("end_time", width=120, anchor=CENTER)
    doctortable.column("doctor_name", anchor=CENTER)

    doctortable.config(show='headings')


    style = ttk.Style()
    style.configure("Treeview", font=("Helvetica", 12), rowheight=30, background="white", fieldbackground="lightgray")
    style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"))

    # Alternate row colors
    doctortable.tag_configure("oddrow", background="lightblue")
    doctortable.tag_configure("evenrow", background="white")

    # Bind the row click event
    doctortable.bind("<Double-1>", on_row_click_D)
    add_back_button()


    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hospital"
        )
        cursor = connection.cursor()
        query = "select doctors.doctor_id,doctors.doctor_name,start_time,end_time from doctorschedules , doctors where doctorschedules.doctor_id=doctors.doctor_id and specialization_id=101"
        cursor.execute(query)
        appointments = cursor.fetchall()

        # Clear existing data in the Treeview
        doctortable.delete(*doctortable.get_children())

        # Insert data into the Treeview with alternate row colors
        for index, appointment in enumerate(appointments):
            tag = "oddrow" if index % 2 == 0 else "evenrow"
            doctortable.insert("", "end", values=appointment, tags=(tag,))

        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def neurology():
    clear_frame(rightframe)
    text_lbl = Label(rightframe, text = "Available Doctors")
    text_lbl.config(font =('Roboto' ,24 , 'bold'), bg="white", fg="#006B82")
    text_lbl.place(x=50, y=40)

    table_frame = Frame(rightframe, bg="white")
    table_frame.place(x=100, y=120, width=900, height=400)

    scrollbarX = Scrollbar(table_frame, orient=HORIZONTAL)
    scrollbarY = Scrollbar(table_frame, orient=VERTICAL)
    doctortable = ttk.Treeview(table_frame, columns=(
    'doctor_id', 'doctor_name', 'start_time', 'end_time'), xscrollcommand=scrollbarX.set, yscrollcommand=scrollbarY.set)
    scrollbarX.config(command=doctortable.xview)
    scrollbarY.config(command=doctortable.yview)
    scrollbarX.pack(side=BOTTOM, fill=X)
    scrollbarY.pack(side=RIGHT, fill=Y)
    doctortable.pack(fill=BOTH, expand=True)
    doctortable.heading('doctor_id', text='Doctor ID')
    doctortable.heading('doctor_name', text='Doctor Name')
    doctortable.heading('start_time', text='Start Time')
    doctortable.heading('end_time', text='End Time')
    doctortable.column("doctor_id", width=100, anchor=CENTER)
    doctortable.column("start_time", width=120, anchor=CENTER)
    doctortable.column("end_time", width=120, anchor=CENTER)
    doctortable.column("doctor_name", anchor=CENTER)

    doctortable.config(show='headings')


    style = ttk.Style()
    style.configure("Treeview", font=("Helvetica", 12), rowheight=30, background="white", fieldbackground="lightgray")
    style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"))


    # Alternate row colors
    doctortable.tag_configure("oddrow", background="lightblue")
    doctortable.tag_configure("evenrow", background="white")

    # Bind the row click event
    doctortable.bind("<Double-1>", on_row_click_D)
    add_back_button()


    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hospital"
        )
        cursor = connection.cursor()
        query = "select doctors.doctor_id,doctors.doctor_name,start_time,end_time from doctorschedules , doctors where doctorschedules.doctor_id=doctors.doctor_id and specialization_id=102"
        cursor.execute(query)
        appointments = cursor.fetchall()

        # Clear existing data in the Treeview
        doctortable.delete(*doctortable.get_children())

        # Insert data into the Treeview with alternate row colors
        for index, appointment in enumerate(appointments):
            tag = "oddrow" if index % 2 == 0 else "evenrow"
            doctortable.insert("", "end", values=appointment, tags=(tag,))

        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def dentistry():
    clear_frame(rightframe)
    text_lbl = Label(rightframe, text = "Available Doctors")
    text_lbl.config(font =('Roboto' ,24 , 'bold'), bg="white", fg="#006B82")
    text_lbl.place(x=50, y=40)

    table_frame = Frame(rightframe, bg="white")
    table_frame.place(x=100, y=120, width=900, height=400)

    scrollbarX = Scrollbar(table_frame, orient=HORIZONTAL)
    scrollbarY = Scrollbar(table_frame, orient=VERTICAL)
    doctortable = ttk.Treeview(table_frame, columns=(
    'doctor_id', 'doctor_name', 'start_time', 'end_time'), xscrollcommand=scrollbarX.set, yscrollcommand=scrollbarY.set)
    scrollbarX.config(command=doctortable.xview)
    scrollbarY.config(command=doctortable.yview)
    scrollbarX.pack(side=BOTTOM, fill=X)
    scrollbarY.pack(side=RIGHT, fill=Y)
    doctortable.pack(fill=BOTH, expand=True)
    doctortable.heading('doctor_id', text='Doctor ID')
    doctortable.heading('doctor_name', text='Doctor Name')
    doctortable.heading('start_time', text='Start Time')
    doctortable.heading('end_time', text='End Time')
    doctortable.column("doctor_id", width=100, anchor=CENTER)
    doctortable.column("start_time", width=120, anchor=CENTER)
    doctortable.column("end_time", width=120, anchor=CENTER)
    doctortable.column("doctor_name", anchor=CENTER)

    doctortable.config(show='headings')


    style = ttk.Style()
    style.configure("Treeview", font=("Helvetica", 12), rowheight=30, background="white", fieldbackground="lightgray")
    style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"))


    # Alternate row colors
    doctortable.tag_configure("oddrow", background="lightblue")
    doctortable.tag_configure("evenrow", background="white")

    # Bind the row click event
    doctortable.bind("<Double-1>", on_row_click_D)
    add_back_button()

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hospital"
        )
        cursor = connection.cursor()
        query = "select doctors.doctor_id, doctors.doctor_name,start_time,end_time from doctorschedules , doctors where doctorschedules.doctor_id=doctors.doctor_id and specialization_id=103"
        cursor.execute(query)
        appointments = cursor.fetchall()
        # Clear existing data in the Treeview
        doctortable.delete(*doctortable.get_children())
        # Insert data into the Treeview with alternate row colors
        for index, appointment in enumerate(appointments):
            tag = "oddrow" if index % 2 == 0 else "evenrow"
            doctortable.insert("", "end", values=appointment, tags=(tag,))
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def book_room():  
    clear_frame(rightframe)
    text_lbl = Label(rightframe, text="Patient Information")
    text_lbl.config(font=('Roboto', 24, 'bold'), bg="white", fg="#006B82")
    text_lbl.place(x=50, y=40)

    add_back_button_R()

    # Helper function for creating Entry fields
    def create_entry(x, y, placeholder):
        def on_enter(e):
            entry.delete(0, "end")

        def on_leave(e):
            if entry.get() == "":
                entry.insert(0, placeholder)

        entry = Entry(rightframe, width=25, fg="#006B82", border=0, bg="#E8E8E8", font=("Roboto", 14))
        entry.place(x=x, y=y, height=35)
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", on_enter)
        entry.bind("<FocusOut>", on_leave)
        return entry

    # Create fields for patient data
    Fname = create_entry(100, 150, "Full Name")
    Address = create_entry(100, 220, "Address")
    nationalID = create_entry(100, 290, "National ID")
    email = create_entry(100, 360, "Email")
    gender = create_entry(500, 150, "Gender")
    phone_no = create_entry(500, 220, "Phone Number")
    bd = create_entry(500, 290, "Birth Date")

    def display_patient_info():
        patient_info = f"""
        Patient Information:
        Full Name: {Fname.get()}
        Address: {Address.get()}
        National ID: {nationalID.get()}
        Email: {email.get()}
        Gender: {gender.get()}
        Phone Number: {phone_no.get()}
        Birth Date: {bd.get()}
        """
        print(patient_info)

    print_btn=Button(rightframe, text="Print", bd=0, bg="#0088a6", fg="white", font=("Roboto", 14, "bold"), cursor="hand2", width=10, height=1, command=display_patient_info)
    print_btn.place(x=950, y=550)

def book_app():  
    clear_frame(rightframe)
    
    # Label for Patient Information
    text_lbl = Label(rightframe, text="Patient Information")
    text_lbl.config(font=('Roboto', 24, 'bold'), bg="white", fg="#006B82")
    text_lbl.place(x=50, y=40)

    add_back_button()

    # Helper function for creating Entry fields
    def create_entry(x, y, placeholder):
        def on_enter(e):
            entry.delete(0, "end")

        def on_leave(e):
            if entry.get() == "":
                entry.insert(0, placeholder)

        entry = Entry(rightframe, width=25, fg="#006B82", border=0, bg="#E8E8E8", font=("Roboto", 14))
        entry.place(x=x, y=y, height=35)
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", on_enter)
        entry.bind("<FocusOut>", on_leave)
        return entry

    # Create fields for patient data
    Fname = create_entry(100, 150, "Full Name")
    Address = create_entry(100, 220, "Address")
    nationalID = create_entry(100, 290, "National ID")
    email = create_entry(100, 360, "Email")
    gender = StringVar(value="Gender")
    gender_types = ["Male", "Female"]
    gender_types_menu = OptionMenu(rightframe, gender, *gender_types)
    gender_types_menu.config(width=10, font=("Roboto", 14), bg="#E8E8E8")
    gender_types_menu.place(x=500, y=150)
    phone_no = create_entry(500, 220, "Phone Number")
    bd = create_entry(500, 290, "Birth Date (YYYY-MM-DD)")

    # Function to display and save information
    def display_info():


        from datetime import datetime

    # Inside your display_info function
        try:
            B_date = bd.get()
    
            # Validate the birth date format
            datetime.strptime(B_date, '%Y-%m-%d')  # Adjust format as necessary

        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter the date in YYYY-MM-DD format.")
            return  # Exit if the date is invalid
        try:
            # Retrieve data from the input fields
            patient_name = Fname.get()
            gender_value = gender.get()
            B_date = bd.get()
            patient_contact_number = phone_no.get()
            patient_email = email.get()
            patient_national_id = nationalID.get()
            patient_address = Address.get()

            # Confirmation dialog
            confirm = messagebox.askyesno("Confirm Save", "Are you sure you want to save this patient's information?")
            if not confirm:
                return  # Cancel the save operation if user clicks "No"

            # Connect to the MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",  # Replace with your MySQL username
                password="1234",  # Replace with your MySQL password
                database="hospital"  # Replace with your database name
            )
            cursor = conn.cursor()

            # Insert query
            query = """
            INSERT INTO patients (patient_full_name, gender, B_date, patient_contact_number, 
                                  patient_email, patient_national_id, patient_address)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (patient_name, gender_value, B_date, patient_contact_number, patient_email, patient_national_id, patient_address)

            # Execute the query
            cursor.execute(query, values)
            conn.commit()

            # Show success message
            messagebox.showinfo("Success", "Patient information saved successfully!")

        except mysql.connector.Error as err:
            # Show error message if there is an issue with the database
            messagebox.showerror("Database Error", f"Error: {err}")

        finally:
            # Close the database connection
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

    # Print button to trigger saving patient data
    print_btn = Button(rightframe, text="Print", bd=0, bg="#0088a6", fg="white", font=("Roboto", 14, "bold"), cursor="hand2", width=10, height=1, command=display_info)
    print_btn.place(x=950, y=550)



def doctors():
    clear_frame(rightframe)
    text_lbl = Label(rightframe, text = "Spectialities")
    text_lbl.config(font =('Roboto' ,24 , 'bold'), bg="white", fg="#006B82")
    text_lbl.place(x=50, y=40)

    cardiology_btn= Button(rightframe, text="Cardiology", bd=0, bg="#E8E8E8", font=("Roboto", 24, "bold"), cursor="hand2", fg="#006B82",command=cardiology)
    cardiology_btn.place(x=50, y=150, width=300, height=200)

    neurology_btn=Button(rightframe, text="Neurology", bd=0, bg="#E8E8E8", font=("Roboto", 24, "bold"), cursor="hand2", fg="#006B82",command=neurology)
    neurology_btn.place(x=400, y=150, width=300, height=200)

    dentistry_btn=Button(rightframe, text="Dentistry", bd=0, bg="#E8E8E8", font=("Roboto", 24, "bold"), cursor="hand2", fg="#006B82",command=dentistry)
    dentistry_btn.place(x=750, y=150, width=300, height=200)
    add_back_button_H()

def booked_app():
    clear_frame(rightframe)
    text_lbl = Label(rightframe, text = "Booked Appointments")
    text_lbl.config(font =('Roboto' ,24 , 'bold'), bg="white", fg="#006B82")
    text_lbl.place(x=50, y=40)
    table_frame = Frame(rightframe, bg="white")
    table_frame.place(x=50, y=100, width=1000, height=500)


    scrollbarX=Scrollbar(table_frame,orient=HORIZONTAL)
    scrollbarY=Scrollbar(table_frame,orient=VERTICAL)

    doctortable=ttk.Treeview(table_frame,columns=('appointment_id','patient_national_id','patient_name','doctor_id','doctor_name','start_time', 'end_time'),xscrollcommand=scrollbarX.set,yscrollcommand=scrollbarY.set)
    scrollbarX.config(command=doctortable.xview)
    scrollbarY.config(command=doctortable.yview)
    scrollbarX.pack(side=BOTTOM,fill=X)
    scrollbarY.pack(side=RIGHT,fill=Y)
    doctortable.pack(fill=BOTH, expand=True)
    doctortable.heading('appointment_id',text='Appointment ID')
    doctortable.heading('patient_national_id',text='Patient ID')
    doctortable.heading('patient_name',text='Patient Name')
    doctortable.heading('doctor_name',text='Doctor Name')
    doctortable.heading('doctor_id',text='Doctor ID')
    doctortable.heading('start_time',text='Start ime')
    doctortable.heading('end_time',text='End time')
    doctortable.config(show='headings')
    doctortable.column("patient_national_id", width=100, anchor=CENTER)
    doctortable.column("start_time", width=120, anchor=CENTER)
    doctortable.column("end_time", width=120, anchor=CENTER)
    doctortable.column("appointment_id", anchor=CENTER)
    doctortable.column("doctor_id", anchor=CENTER)
    doctortable.column("patient_name", anchor=CENTER)
    doctortable.column("doctor_name", anchor=CENTER)

    style = ttk.Style()
    style.configure("Treeview", font=("Helvetica", 12), rowheight=30, background="white", fieldbackground="lightgray")
    style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"))


    # Alternate row colors
    doctortable.tag_configure("oddrow", background="lightblue")
    doctortable.tag_configure("evenrow", background="white")
    add_back_button_H()


    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hospital"
        )
        cursor = connection.cursor()
        query = "select appointment_id,patient_national_id, patient_name, appointments.doctor_id, doctor_name, start_time, end_time from appointments, doctors where appointments.doctor_id=doctors.doctor_id"
        cursor.execute(query)
        appointments = cursor.fetchall()

        # Clear existing data in the Treeview
        doctortable.delete(*doctortable.get_children())

        # Insert data into the Treeview with alternate row colors
        for index, appointment in enumerate(appointments):
            tag = "oddrow" if index % 2 == 0 else "evenrow"
            doctortable.insert("", "end", values=appointment, tags=(tag,))

        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def availbe_rooms():
    clear_frame(rightframe)
    text_lbl = Label(rightframe, text = "Available Rooms")
    text_lbl.config(font =('Roboto' ,24 , 'bold'), bg="white", fg="#006B82")
    text_lbl.place(x=50, y=40)
    table_frame = Frame(rightframe, bg="white")
    table_frame.place(x=50, y=100, width=1000, height=500)

    scrollbarX=Scrollbar(table_frame,orient=HORIZONTAL)
    scrollbarY=Scrollbar(table_frame,orient=VERTICAL)

    roomtable=ttk.Treeview(table_frame,columns=('room_number','room_address','number_of_beds','number_of_people_allowed','start_time', 'end_time'),xscrollcommand=scrollbarX.set,yscrollcommand=scrollbarY.set)
    scrollbarX.config(command=roomtable.xview)
    scrollbarY.config(command=roomtable.yview)
    scrollbarX.pack(side=BOTTOM,fill=X)
    scrollbarY.pack(side=RIGHT,fill=Y)
    roomtable.pack(fill=BOTH, expand=True)
    roomtable.heading('room_number',text='Room Number')
    roomtable.heading('room_address',text='Floor')
    roomtable.heading('number_of_beds',text='Beds')
    roomtable.heading('number_of_people_allowed',text='People Allowed')
    roomtable.heading('start_time',text='Start time')
    roomtable.heading('end_time',text='End time')
    roomtable.config(show='headings')
    roomtable.column("number_of_beds", width=70, anchor=CENTER)
    roomtable.column("number_of_people_allowed", anchor=CENTER)
    roomtable.column("room_number", anchor=CENTER)
    roomtable.column("room_address", anchor=CENTER)
    roomtable.column("start_time", width=100, anchor=CENTER)
    roomtable.column('end_time', width=100, anchor=CENTER)


    style = ttk.Style()
    style.configure("Treeview", font=("Roboto", 11), rowheight=30, background="white", fieldbackground="lightgray")
    style.configure("Treeview.Heading", font=("Roboto", 14, "bold"))

    roomtable.bind("<Double-1>", on_row_click_R)

    # Alternate row colors
    roomtable.tag_configure("oddrow", background="lightblue")
    roomtable.tag_configure("evenrow", background="white")
    add_back_button_H()

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hospital"
        )
        cursor = connection.cursor()
        query = "SELECT * FROM rooms"
        cursor.execute(query)
        rooms = cursor.fetchall()

        # Clear existing data in the Treeview
        roomtable.delete(*roomtable.get_children())

        # Insert data into the Treeview with alternate row colors
        for index, room in enumerate(rooms):
            tag = "oddrow" if index % 2 == 0 else "evenrow"
            roomtable.insert("", "end", values=room, tags=(tag,))

        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def home():
    clear_frame(rightframe)

    doctors_btn= Button(rightframe, text="Doctors", bd=0, bg="#E8E8E8", font=("Roboto", 24, "bold"), cursor="hand2", fg="#006B82", command=doctors)
    doctors_btn.place(x=50, y=150, width=300, height=200)

    booked_app_btn=Button(rightframe, text="Booked\nAppointments", bd=0, bg="#E8E8E8", font=("Roboto", 24, "bold"), cursor="hand2", fg="#006B82", command=booked_app)
    booked_app_btn.place(x=400, y=150, width=300, height=200)

    rooms_btn=Button(rightframe, text="Rooms", bd=0, bg="#E8E8E8", font=("Roboto", 24, "bold"), cursor="hand2", fg="#006B82", command=availbe_rooms)
    rooms_btn.place(x=750, y=150, width=300, height=200)

home()
def main():
    leftframe=Frame(dash_rec,bg='#32acc7')
    leftframe.place(x=0,y=200,width=293,height=252)

    home_btn=Button(leftframe,text='Home',font=('Roboto' ,14 , 'bold'),width=20,fg='#006B82', bg="white", activeforeground="yellow", command=home)
    home_btn.place(x=0, y=50)

    doctors_btn= Button(leftframe,text='Doctors',font=('Roboto' ,14 , 'bold'),width=20,fg='#006B82', bg="white", activeforeground="yellow", command=doctors)
    doctors_btn.place(x=0, y=100)

    booked_app_btn= Button(leftframe,text='Booked Appointments',font=('Roboto' ,14 , 'bold'),width=20,fg='#006B82', bg="white", activeforeground="yellow", command=booked_app)
    booked_app_btn.place(x=0, y=150)
    rooms_btn= Button(leftframe,text='Rooms',font=('Roboto' ,14 , 'bold'),width=20,fg='#006B82', bg="white", activeforeground="yellow", command=availbe_rooms)
    rooms_btn.place(x=0, y=200)

main()


dash_rec.mainloop()