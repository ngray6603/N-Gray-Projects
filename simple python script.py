# This is a sample Python script.

#import the system module and decimal
import sys
from decimal import Decimal
#defining the class, its naming and most participants
class Class:
    def __init__(self, name, max_size):
        self.name = name
        self.max_size = max_size
        self.roster = []
#defining the student when they enroll
    def add_student(self, student):
        if len(self.roster) < self.max_size:
            self.roster.append(student)
#creating a kick back if the class if full
        else:
            print("Class is full")
#removing student from a class
    def remove_student(self, student):
        self.roster.remove(student)
#creating the definition to show student roster
    def get_students(self):
        return self.roster
#defining the student individually and assigning to class
class Student:
    def __init__(self, name):
        self.name = name
        self.classes = []
#allowing students to be added to a specific class
    def add_class(self, class_obj):
        if not any(c for c in class_obj.get_students() if c == self.name):  # check if the student is already enrolled in this class
            class_obj.add_student(self)
            self.classes.append(class_obj)
#removing student from a class
    def remove_class(self, class_obj):
        index = [i for i, c in enumerate(self.classes) if c == class_obj]  # find the index of the class to be removed from the student's schedule
        self.remove_student(class_obj)
        del self.classes[index[0]]
#returning the students schedule
    def get_schedule(self):
        return [c for c in self.classes if c != None]  # returns a list of classes the student is enrolled in, excluding any removed classes
#defining the entry that allows to add class, name and size
def main():
    while True:
        choice = input("Enter 'a' to add a class, 's' to switch to student mode, or 'q' to quit: ").lower()
        if choice == 'a':  # administrator mode
            name = input("Enter the class name: ")
            max_size = int(input("Enter maximum size of the class: "))
            new_class = Class(name, max_size)
            continue
#allowing the student to enroll in clases definied earlier
        elif choice == 's':  # student mode
            while True:
                command = input("Enter 'e' to enroll in a class, 'u' to un-enroll from a class, or 'p' to print your schedule: ").lower()
                if command == 'e':
                    name = input("Enter the class name you want to join: ")
                    new_class = Class(name)
                    student_name = input("What is your name? ")
                    stu = Student(student_name)
                    stu.add_class(new_class)
                elif command == 'u':
                    class_name = input("Enter the class you want to leave: ")
                    new_class = Class(class_name)
                    student_name = input("What is your name? ")
                    stu = Student(student_name)
                    stu.remove_class(new_class)
#allowing student to print newly created schedule
                elif command == 'p':
                    print("\nYour schedule:")
                    for c in stu.get_schedule():
                        print("{}".format(c))
                    break
                else:
                    continue
            break
#completion of scheduling
        elif choice == 'q':
            break

if __name__ == "__main__":
    main()