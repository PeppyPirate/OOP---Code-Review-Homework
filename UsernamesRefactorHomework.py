from tabulate import tabulate

class Student:
    #Define class Student, give name and surname to begin with, default status is True (meaning active) and if no special username is given, it is created
    def __init__(self, name: str, surname: str, status = True, username = "") -> None:
        self.name = name
        self.surname = surname
        self.status = status #If adding new student, default will be active status
        self.username = username
        if self.username == "": #If no special username is given, create it
            self.username = self._create_username()

    def __repr__(self) -> str:
        return self.name + " " + self.surname

    def _create_username(self) -> str:
        #Take the first 5 letters from surname and 3 from name and joint them
        surname_part = self.surname.lower()[:5]
        name_part = self.name.lower()[:3]
        username = surname_part + name_part
        return username 
        
class Database: #Create a database for storing student information

    def __init__(self) -> None:
        self.students = []
        self.status = []
        self.usernames = []

    def __repr__(self) -> str:
        table = tabulate({"Name": self.students,
                         "Status": self.status,
                         "Usernames": self.usernames},
                         headers="keys")
        return table 

    def _check_for_status(self, student: Student) -> bool:
        if student.status == False:
            print(f"{student} does not have active status, cannot add to database.")
            return 0
        else:
            return 1

    def _check_for_duplicit_username(self, student: Student):
        if student.username in self.usernames: #If the username is already in the database, change the last letter to increasing numbers
            last_letter = student.username[-1]            

            if last_letter.isnumeric():
                last_letter = int(last_letter) + 1                
            else:                
                last_letter = "0"

            new_username =  student.username[:-1]+str(last_letter)            
            student.username = new_username  
            self._check_for_duplicit_username(student)   


    def add_student(self, student: Student):
        if student in self.students:
            print(f"{student} is already in the database.")
        if student.status == False:
           print(f"{student} in inactive, cannot add to the database.")
        else:
            self.students.append(student)
            self.status.append(student.status)
            self._check_for_duplicit_username(student)
            self.usernames.append(student.username)

    def remove_student(self, student: Student):
        if student in self.students:
            self.students.remove(student)
            self.status.remove(student.status)
            self.usernames.remove(student.username)


StudentDatabase = Database()

student1 = Student("Adam", "Levine")
student2 = Student("Monica", "Muller")
student3 = Student("John", "Deere")
student4 = Student("John", "Deere")
student5 = Student("John", "Deere")
student6 = Student("Adam", "Levine", username="Admin")
student7 = Student("John", "Deere", False)


StudentDatabase.add_student(student1)
StudentDatabase.add_student(student2)
StudentDatabase.add_student(student3)
StudentDatabase.add_student(student4)
StudentDatabase.add_student(student5)
StudentDatabase.add_student(student6)
StudentDatabase.add_student(student7)
print(StudentDatabase)

StudentDatabase.remove_student(student5)
StudentDatabase.remove_student(student3)
print(StudentDatabase)

