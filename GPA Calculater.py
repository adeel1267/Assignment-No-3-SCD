class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course.course_name}")

    def calculate_gpa(self):
        total_credits = 0
        total_grade_points = 0

        for course in self.courses:
            total_credits += course.credits
            total_grade_points += course.credits * course.grade

        gpa = total_grade_points / total_credits
        return gpa

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")


class Professor(Person):
    def __init__(self, name, age, professor_id):
        super().__init__(name, age)
        self.professor_id = professor_id

    def assign_grade(self, student, course, grade):
        if course in student.courses:
            course.grade = grade
            print(f"{self.name} assigned grade {grade} to {student.name} in {course.course_name}")
        else:
            print(f"{student.name} is not enrolled in {course.course_name}")

    def display_info(self):
        super().display_info()
        print(f"Professor ID: {self.professor_id}")


class Course:
    def __init__(self, course_name, credits):
        self.course_name = course_name
        self.credits = credits
        self.grade = 0  # Initial grade is set to 0

    def display_info(self):
        print(f"Course: {self.course_name}, Credits: {self.credits}")


# Example usage
student1 = Student("Adeel Ashraf", 20, "12345")
professor1 = Professor("Naveed Ashraf", 35, "P001")
course1 = Course("Mathematics", 3)
course2 = Course("Computer Science", 4)

student1.enroll_course(course1)
student1.enroll_course(course2)
professor1.assign_grade(student1, course1, 85)
professor1.assign_grade(student1, course2, 92)

student1.display_info()
course1.display_info()
course2.display_info()

gpa = student1.calculate_gpa()
print(f"{student1.name}'s GPA: {gpa}")