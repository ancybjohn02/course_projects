import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="ancybjohn02",
        password="@Hosanna2014",
        database="hospital_management_system"
    )

import streamlit as st
import pandas as pd

# Main title and navigation
st.title("Hospital Management System")

menu = ["Patients", "Doctors", "Appointments", "Billing", "Wards", "Inventory"]
choice = st.sidebar.selectbox("Navigation", menu)

# Database Connection
conn = get_connection()
cursor = conn.cursor()

def add_patient():
    st.subheader("Add New Patient")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    contact = st.text_input("Contact Info")
    address = st.text_input("Address")
    email = st.text_input("Email")
    blood_group = st.text_input("Blood Group")
    emergency_contact = st.text_input("Emergency Contact")
    admission_date = st.date_input("Admission Date")
    
    if st.button("Add Patient"):
        query = """INSERT INTO patients (name, age, gender, contact_info, address, email, blood_group, emergency_contact, admission_date)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (name, age, gender, contact, address, email, blood_group, emergency_contact, admission_date)
        cursor.execute(query, values)
        conn.commit()
        st.success("Patient added successfully!")

def view_patients():
    st.subheader("View All Patients")
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    df = pd.DataFrame(patients, columns=[col[0] for col in cursor.description])
    st.dataframe(df)

if choice == "Patients":
    st.write("Manage Patients")
    if st.button("View All Patients"):
        view_patients()
    add_patient()

def add_doctor():
    st.subheader("Add New Doctor")
    name = st.text_input("Doctor's Name")
    specialization = st.text_input("Specialization")
    education = st.text_input("Education Level")
    experience = st.number_input("Years of Experience", min_value=0)
    contact = st.text_input("Contact Info")
    email = st.text_input("Email")
    work_schedule = st.text_input("Work Schedule")
    salary = st.number_input("Salary", min_value=0.0)

    if st.button("Add Doctor"):
        query = """INSERT INTO doctors (name, specialization, education_level, years_of_experience, contact_info, email, work_schedule, salary)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (name, specialization, education, experience, contact, email, work_schedule, salary)
        cursor.execute(query, values)
        conn.commit()
        st.success("Doctor added successfully!")

if choice == "Doctors":
    add_doctor()

def book_appointment():
    st.subheader("Book Appointment")
    patient_id = st.number_input("Patient ID", min_value=1)
    doctor_id = st.number_input("Doctor ID", min_value=1)
    appointment_date = st.date_input("Appointment Date")
    reason = st.text_area("Reason for Appointment")

    if st.button("Book Appointment"):
        query = """INSERT INTO appointments (patient_id, doctor_id, appointment_date, reason, status)
                   VALUES (%s, %s, %s, %s, %s)"""
        values = (patient_id, doctor_id, appointment_date, reason, "Pending")
        cursor.execute(query, values)
        conn.commit()
        st.success("Appointment booked successfully!")

if choice == "Appointments":
    book_appointment()

def view_bills():
    st.subheader("Billing Information")
    cursor.execute("SELECT * FROM billing")
    bills = cursor.fetchall()
    df = pd.DataFrame(bills, columns=[col[0] for col in cursor.description])
    st.dataframe(df)

if choice == "Billing":
    view_bills()

def view_inventory():
    st.subheader("Medicine Inventory")
    cursor.execute("SELECT * FROM medicine_stock")
    inventory = cursor.fetchall()
    df = pd.DataFrame(inventory, columns=[col[0] for col in cursor.description])
    st.dataframe(df)

if choice == "Inventory":
    view_inventory()

conn.close()
