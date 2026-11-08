# Course Information System

# Dictionary containing course room numbers
room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

# Dictionary containing course instructors
instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

# Dictionary containing course meeting times
meeting_times = {
    "CSC101": "8:00 AM",
    "CSC102": "9:30 AM",
    "CSC103": "11:00 AM",
    "NET110": "1:00 PM",
    "COM241": "3:30 PM"
}

# Function to retrieve course information
def get_course_information(course_number):

    if (course_number in room_numbers
            and course_number in instructors
            and course_number in meeting_times):

        return {
            "room": room_numbers[course_number],
            "instructor": instructors[course_number],
            "meeting_time": meeting_times[course_number]
        }

    else:
        return None


# Function to display course information
def display_course_information(course_number, course_info):

    if course_info is not None:
        print("\nCourse Information")
        print("--------------------------")
        print(f"Course Number: {course_number}")
        print(f"Room Number: {course_info['room']}")
        print(f"Instructor: {course_info['instructor']}")
        print(f"Meeting Time: {course_info['meeting_time']}")
        print("--------------------------")

    else:
        print(f"\nSorry, course {course_number} was not found.")
        print("Please check the course number and try again.")


# Main function
def main():

    print("Welcome to the Course Information System!")

    course_number = input(
        "\nEnter a course number (e.g., CSC101): "
    ).strip().upper()

    course_info = get_course_information(course_number)

    display_course_information(course_number, course_info)


# Run the program
if __name__ == "__main__":
    main()

