import streamlit as st

st.title("Student Marks")

# Initialize the list once per user session
if "students" not in st.session_state:
    st.session_state.students = []

with st.form("add"):
    name = st.text_input("Name")
    mark = st.number_input("Mark", min_value=0, max_value=100, step=1)

    submitted = st.form_submit_button("Add")

    if submitted:
        if name.strip():
            st.session_state.students.append({
                "Name": name.strip(),
                "Mark": int(mark),
            })
            st.success(f"Added {name.strip()}.")
        else:
            st.warning("Please enter a name.")

if st.session_state.students:
    st.subheader("Students")
    st.table(st.session_state.students)

    average_mark = sum(
        student["Mark"] for student in st.session_state.students
    ) / len(st.session_state.students)

    st.metric("Class average", f"{average_mark:.1f}")
else:
    st.info("No students added yet.")