import streamlit as st
import pandas as pd

# Title
st.title("🎓 School Report Card Generator")

# Student details input
st.header("Student Information")
student_name = st.text_input("Enter student's full name")
grade_level = st.selectbox("Select grade/class", ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12"])

# Subjects and marks
st.header("Enter Subject-wise Marks")
subjects = st.text_area("Enter subjects (one per line)", "Math\nScience\nEnglish\nHistory")
subject_list = subjects.splitlines()

marks = {}
for subject in subject_list:
    mark = st.number_input(f"Enter marks for {subject}", min_value=0, max_value=100, value=0)
    marks[subject] = mark

# Generate Report
if st.button("Generate Report Card"):
    st.subheader("📄 Report Card")
    st.write(f"**Student Name:** {student_name}")
    st.write(f"**Grade Level:** {grade_level}")
    
    df = pd.DataFrame({
        "Subject": list(marks.keys()),
        "Marks": list(marks.values())
    })
    df["Grade"] = df["Marks"].apply(lambda x: 
        "A" if x >= 90 else 
        "B" if x >= 80 else 
        "C" if x >= 70 else 
        "D" if x >= 60 else 
        "F"
    )
    st.table(df)

    average = sum(marks.values()) / len(marks) if marks else 0
    st.write(f"**Average Marks:** {average:.2f}")
    st.write(f"**Overall Grade:** {'A' if average >= 90 else 'B' if average >= 80 else 'C' if average >= 70 else 'D' if average >= 60 else 'F'}")
