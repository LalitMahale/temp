import streamlit as st
from datetime import datetime, timedelta

import streamlit as st

st.title("hellow")
st.write("Hellow")
st.success("success")
st.info("info")
st.error("error")


def date_difference(date1, date2):
    # Convert string dates to datetime objects
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")

    # Calculate the difference in days
    difference = abs((date2 - date1).days)

    return difference


def main():
    st.title("Date Difference Calculator")

    # Get user input for two dates using the calendar
    start_date = st.date_input("Select the start date")
    end_date = st.date_input("Select the end date")

    # Display the selected dates
    st.write(f"Start Date: {start_date}")
    st.write(f"End Date: {end_date}")

    # Calculate and display the difference in days
    if start_date and end_date:
        difference = date_difference(str(start_date), str(end_date))
        st.write(f"Difference in days: {difference} days")


if __name__ == "__main__":
    main()

