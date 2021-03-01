import ChrisKellerQuiz1File1 as c


course1 = c.Course("Advanced Python", 125468, 25, "MIS4322")
course2 = c.Course("Database Development", 985474, 40, "MIS4340")


course_dict = {
    course1.get_crn(): course1.get_capacity(),
    course2.get_crn(): course2.get_capacity(),
}

print(course_dict)