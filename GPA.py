import streamlit as st

grade_values = {
    "A+": 4.0,
    "A": 3.75,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "D+": 1.5,
    "D": 1.0,
    "F": 0.0
}

st.title("🎓 GPA Calculator")

num_courses = st.number_input("How many courses do you want to enter?", min_value=1, step=1)

total_hours = 0
total_points = 0

for i in range(1, num_courses + 1):
    st.markdown(f"### Course {i}")

    col1, col2 = st.columns(2)

    with col1:
        credit = st.number_input(f"Credit Hours", min_value=1, step=1, key=f"credit_{i}")

    with col2:
        grade = st.selectbox("Grade", options=grade_values.keys(), key=f"grade_{i}")

    total_hours += credit
    total_points += credit * grade_values[grade]

if total_hours > 0:
    gpa = round(total_points / total_hours, 3)
    st.success(f" Total Credits: {total_hours}")
    st.success(f" GPA: {gpa}")
