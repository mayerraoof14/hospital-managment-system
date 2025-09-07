create database hospital; 
 
create table Specializations ( 
specialization_id int , 
specialization_name  varchar(20)  unique  not null  
,constraint specialization_id_1 
primary key(specialization_id) 
); 
    
 
create table DoctorSchedules (schedule_id int auto_increment,  
doctor_id  int , doctor_name varchar(30), 
start_time  time , 
end_time    time , 
constraint schedule_id_1 
primary key(schedule_id), 
constraint doctor_id_2 
foreign key ( doctor_id ) references Doctors (doctor_id)  
 on delete set null    on update cascade);  
     
     
CREATE TABLE patients ( 
    patient_full_name VARCHAR(30), 
    gender VARCHAR(10), 
    B_date DATE, 
    patient_contact_number VARCHAR(12), 
    patient_email VARCHAR(100) UNIQUE, 
    patient_national_id VARCHAR(14) UNIQUE, 
    patient_address VARCHAR(50) UNIQUE, 
    CONSTRAINT patient_national_id_1 PRIMARY KEY (patient_national_id) 
); 
 
CREATE TABLE Rooms ( 
    room_number INT, 
    room_address VARCHAR(40), 
    number_of_beds INT, 
    number_of_people_allowed INT, 
    start_time TIME, 
    end_time TIME, 
    patient_national_id VARCHAR(14), -- Change this to VARCHAR to match the patients 
table 
    CONSTRAINT room_number_1 PRIMARY KEY (room_number), 
    CONSTRAINT patient_national_id_2 FOREIGN KEY (patient_national_id)  
        REFERENCES patients (patient_national_id)  
        ON DELETE SET NULL  
        ON UPDATE CASCADE 
); 
 
create table Doctors ( doctor_name  varchar(20)  not null , doctor_id  int , specialization_id 
int , user_name  varchar(20) not null unique , 
pass_word varchar(20)  not null unique  
, constraint doctor_id_1 
primary key (doctor_id), 
constraint specialization_id_2 
foreign key (specialization_id) references Specializations(specialization_id)  
on delete set null    on update cascade); 
 
create table receptionists ( receptionist_name  varchar(20)  not null , receptionist_id  int , 
user_name  varchar(20) not null unique , 
pass_word varchar(20)  not null unique  
, constraint receptionist_id_1 
primary key (receptionist_id)); 
 
 
create table Appointments( appointment_id int not null auto_increment , 
patient_national_id varchar(14) , patient_name varchar(30), doctor_id int , start_time  time , 
end_time    time , 
constraint appointment_id_1  
primary key(appointment_id), 
constraint doctor_id_3 
foreign key (doctor_id ) references Doctors(doctor_id) 
     on delete set null    on update cascade, 
constraint patient_national_id_3 
foreign key (patient_national_id ) references Patients(patient_national_id) 
     on delete set null    on update cascade ); 
 
 
INSERT INTO Specializations (specialization_id, specialization_name)  
VALUES  
(101, 'Cardiology'), 
(102, 'Neurology'), 
(103, 'Dentistry'); 
 
INSERT INTO Doctors (doctor_name, doctor_id, specialization_id, user_name, pass_word)  
VALUES 
('Dr. John Smith', 1, 101, 'johnsmith', 'password123'), 
('Dr. Emily Davis', 2, 102, 'emilydavis', 'securepass456'), 
('Dr. Michael Brown', 3, 103, 'michaelbrown', 'mypassword789'); 
 
 
INSERT INTO receptionists (receptionist_name, receptionist_id, user_name, pass_word)  
VALUES 
('Alice Carter', 1, 'alicecarter', 'alicepass123'), 
('Bob Martin', 2, 'bobmartin', 'securebob456'), 
('Chloe Taylor', 3, 'chloetaylor', 'chloe789pass'), 
('David Wilson', 4, 'davidwilson', 'david2023pwd'); 
 
INSERT INTO Rooms (room_number, room_address, number_of_beds, 
number_of_people_allowed, start_time, end_time, patient_national_id) 
VALUES 
(101, 'First Floor, East Wing', 2, 4, '08:00:00', '16:00:00'), 
(102, 'First Floor, West Wing', 1, 2, '09:00:00', '15:00:00'), 
(201, 'Second Floor, North Wing', 3, 6, '10:00:00', '18:00:00'), 
(301, 'Third Floor, East Wing', 3, 2, '13:30:00', '20:30:00'); 
 
 
 
INSERT INTO patients (patient_full_name, gender, B_date, patient_contact_number, 
patient_email, patient_national_id, patient_address) 
VALUES 
('Ethan James', 'Male', '1995-02-18', '1122334455', 'ejames@mail.com', '123456789', '123 
Maple Street'), 
('Sophia Miller', 'Female', '1993-06-10', '2233445566', 'smiller@mail.com', '987654321', '456 
Oak Avenue'), 
('Liam Johnson', 'Male', '1988-09-25', '3344556677', 'ljohnson@mail.com', '543216789', '789 
Pine Road'), 
('Olivia Brown', 'Female', '2000-12-30', '4455667788', 'obrown@mail.com', '112358132','101 
Elm Boulevard'); 
 
INSERT INTO Appointments (patient_national_id, patient_name, doctor_id, start_time, 
end_time) 
VALUES 
('123456789', 'Ethan James', 1 ,'10:00:00', '10:30:00'), -- Appointment with Dr. John Smith 
('987654321', 'Sophia Miller', 2, '11:00:00', '11:30:00'), -- Appointment with Dr. Emily Davis 
('543216789', 'Liam Johnson', 3, '12:00:00', '12:45:00'); -- Appointment with Dr. Michael 
Brown 
 
INSERT INTO DoctorSchedules (doctor_id, doctor_name, start_time, end_time) 
VALUES 
(1, 'Dr. John Smith', '08:00:00', '12:00:00'), -- Morning shift 
(1, 'Dr. John Smith', '13:00:00', '17:00:00'), -- Afternoon shift 
(2, 'Dr. Emily Davis', '09:00:00', '13:00:00'), -- Morning shift 
(2, 'Dr. Emily Davis', '14:00:00', '18:00:00'), -- Afternoon shift 
(3, 'Dr. Michael Brown', '10:00:00', '14:00:00'), -- Midday shift 
(3, 'Dr. Michael Brown', '15:00:00', '19:00:00'); -- Evening shift