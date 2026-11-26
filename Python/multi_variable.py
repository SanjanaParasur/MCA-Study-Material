class Student:
    def __init__(self):
        self.__name = ""  #private variable
        self.__rollno = 0
        self.__marks = 0

    def set_data(self, name, rollno, marks):
        self.__name = name
        self.__rollno = rollno
        
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")

    #Getter Methods
    def get_data(self):
       print("Name:", self.__name)
       print("Roll No:", self.__rollno)
       print("Marks:", self.__marks)

#Object Creation
s1 = Student()

#Accept multiple values
name = input("Enter Name: ")
rollno = int(input("Enter Roll No: "))
marks = int(input("Enter Marks: "))

#Set the data
s1.set_data(name, rollno, marks)

print("\nStudent Details:")
s1.get_data()