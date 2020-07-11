class A:
    def name(self,data):# function returns name
        return data
class B(A):# Child class which inherits all parent functions
    def surname(self,data):
        return data

Fullname = B()
i = input("Enter your name:- ")
j = input("Enter your surname:- ")
# No need to add new function in class B for surname or make new function for name:)
print("Your full name is " + Fullname.name(i) +" "+ Fullname.surname(j))