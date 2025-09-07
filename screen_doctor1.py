from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
import ttkthemes
import mysql.connector
from tkinter import ttk


def fetch_appointments():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hospital"
        )
        cursor = connection.cursor()
        query = "SELECT appointment_id, patient_national_id, patient_name, start_time, end_time FROM Appointments"
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


doctor=ttkthemes.ThemedTk()
doctor.get_themes()
doctor.set_theme('breeze')
doctor.geometry('1920x1080')
doctor.title('MBA Hospital Dashboard - Doctor')
doctor.config(bg='#32acc7')

logout_img = Image.open("D:/Old/UFE/Materials/Year 2/Mini Project/Images/Log out button.png").resize((30,30))
logout_img = ImageTk.PhotoImage(logout_img)

logo_image = Image.open("D:/Old/UFE/Materials/Year 2/Mini Project/Images/Logo.png").resize((140,115))  # Open the image file
logo = ImageTk.PhotoImage(logo_image)  # Convert to Tkinter-compatible image
# Create a label to hold the image
logo_label = Label(doctor, image=logo, bg='#32acc7')  # Use same bg color for blending
logo_label.place(x=30, y=30)

def logout1():
    doctor.destroy()  # Close the current window
    import Choose
    Choose.mainloop()  # Import the Choose

def add_logout():
    # Adds a back button to the current frame
    logout_btn = Button(doctor, image=logout_img, bd=0, bg="#32acc7", cursor="hand2", command=logout1)
    logout_btn.place(x=1420,y=70)

add_logout()

leftframe=Frame(doctor,bg='#32acc7')
leftframe.place(x=0,y=200,width=293,height=252)
viewapp=Button(leftframe,text='View Appoinments',cursor="hand2",font=('times new roman' ,14 , 'bold'),width=20,fg='#006B82',command=fetch_appointments)
viewapp.grid(row=1,column=0,pady=100)


rightframe=Frame(doctor, bg="white")
rightframe.place(x=350,y=200,width=1110,height=630)

text_lbl = Label(rightframe, text = "Appointments")
text_lbl.config(font =('Roboto' ,24 , 'bold'), bg="white", fg="#006B82")
text_lbl.place(x=50, y=40)

table_frame = Frame(rightframe, bg="white")
table_frame.place(x=100, y=120, width=900, height=400)

scrollbarX=Scrollbar(table_frame,orient=HORIZONTAL)
scrollbarY=Scrollbar(table_frame,orient=VERTICAL)

doctortable=ttk.Treeview(table_frame,columns=('appointment_id','patient_national_id','patient_name','start_time','end_time'),xscrollcommand=scrollbarX.set,yscrollcommand=scrollbarY.set)
scrollbarX.config(command=doctortable.xview)
scrollbarY.config(command=doctortable.yview)
scrollbarX.pack(side=BOTTOM,fill=X)
scrollbarY.pack(side=RIGHT,fill=Y)
doctortable.pack(fill=BOTH,expand=True)
doctortable.heading('appointment_id',text='Appointment ID')
doctortable.heading('patient_national_id',text='Patient ID')
doctortable.heading('patient_name',text='Patient Name')
doctortable.heading('start_time',text='Start Time')
doctortable.heading('end_time',text='End Time')
doctortable.config(show='headings')
doctortable.column("appointment_id", width=100, anchor=CENTER)
doctortable.column("patient_national_id", width=100, anchor=CENTER)
doctortable.column("patient_name", width=100, anchor=CENTER)
doctortable.column("start_time", width=120, anchor=CENTER)
doctortable.column("end_time", width=120, anchor=CENTER)

style = ttk.Style()
style.configure("Treeview", font=("Helvetica", 12), rowheight=30, background="white", fieldbackground="lightgray")
style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"))


# Alternate row colors
doctortable.tag_configure("oddrow", background="lightblue")
doctortable.tag_configure("evenrow", background="white")


doctor.mainloop()