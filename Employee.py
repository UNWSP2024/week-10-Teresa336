# Programmer: Teresa Fischer
# Date: 11/5/2024
# Program #4 Employee Class:

# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.

class Employee:

    def __init__(self, name, id_number, department, title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.title = title

    def __str__(self):
        return 'Name: {}, Id Number: {}, Department: {}, Title: {}'.format(self.name, self.id_number, self.department, self.title)


def main():

    employee1 = Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
    employee2 = Employee('Mark Jones', 39119, 'IT', 'Programmer')
    employee3 = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')

    print(employee1)
    print(employee2)
    print(employee3)

main()