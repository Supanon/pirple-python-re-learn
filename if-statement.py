# Homework 3 If statement

def compare(num1, num2, num3):
    if num1 == num2:
        return True
    if num2 == num3:
        return True
    if num3 == num1:
        return True
    else:
        return False
    
print(compare(6,5,6))
print(compare(5,6,6))
print(compare(6,5,6))
print(compare(6,5,"5"))
print(compare(6,5,int("5")))