class Student:
    def __init__(self):
        self.__marks = 0

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise ValueError("Marks must be between 0 and 100.")

# 1. Create a Student object
s1 = Student()

# 2. Set the marks
s1.set_marks(92)

# 3. Print the marks to see output
print(s1.get_marks())