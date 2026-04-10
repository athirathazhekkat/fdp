import streamlit as st
import pandas as pd
import os
import re

# 1. Page Configuration
st.set_page_config(page_title="Student Registration System", layout="centered")

# 2. Database Helper (Local CSV)
DB_FILE = "student_data.csv"

def save_data(data_dict):
    df = pd.DataFrame([data_dict])
    if not os.path.isfile(DB_FILE):
        df.to_csv(DB_FILE, index=False)
    else:
        df.to_csv(DB_FILE, mode='a', header=False, index=False)

# 3. Form Header
st.title("🎓 Student Registration Form")
st.markdown("Please fill out the form below to register for the upcoming semester.")

# 4. Registration Form
with st.form("student_reg_form", clear_on_submit=True):
    st.header("👤 Personal Information")
    
    # Using columns for a better layout
    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("First Name*", placeholder="e.g. John")
        dob = st.date_input("Date of Birth", min_value=pd.to_datetime("1980-01-01"))
    with col2:
        last_name = st.text_input("Last Name*", placeholder="e.g. Doe")
        gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])

    st.divider()
    st.header("📞 Contact Details")
    email = st.text_input("Email Address*", placeholder="name@university.edu")
    phone = st.text_input("Phone Number", placeholder="123-456-7890")

    st.divider()
    st.header("📚 Academic Information")
    course = st.selectbox("Preferred Course", ["Computer Science", "Data Science", "Physics", "Mathematics", "Biology"])
    enrol_type = st.radio("Enrollment Type", ["Full-time", "Part-time"])
    
    st.markdown("---")
    submitted = st.form_submit_button("Register Student")

    # 5. Form Logic & Validation
    if submitted:
        errors = []
        # Basic validation checks
        if not first_name or not last_name:
            errors.append("First and Last name are required.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Invalid email format.")
        if gender == "Select":
            errors.append("Please select a gender.")

        if errors:
            for err in errors:
                st.error(err)
        else:
            # Prepare data for storage
            student_record = {
                "First Name": first_name,
                "Last Name": last_name,
                "DOB": str(dob),
                "Gender": gender,
                "Email": email,
                "Phone": phone,
                "Course": course,
                "Enrollment": enrol_type
            }
            save_data(student_record)
            st.success(f"✅ Registration Successful for {first_name} {last_name}!")
            st.balloons()

# 6. Admin View (Optional)
if st.checkbox("Show registered students"):
    if os.path.exists(DB_FILE):
        df_view = pd.read_csv(DB_FILE)
        st.dataframe(df_view)
    else:
        st.info("No students registered yet.")
