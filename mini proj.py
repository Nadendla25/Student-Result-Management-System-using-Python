"Student Result Management System using Python"
import random
import math
name=input("Enter student name:")
phone_num=input("Enter valid Phone number: ")
if phone_num.isnumeric() and len(phone_num)==10:
    print("valid phone number")
else:
    print("invalid phone number")

otp=random.randint(1000,9999)
print("your otp is:",otp)
sub1=int(input("Enter marks of subject 1: "))
sub2=int(input("Enter marks of subject 2: "))
sub3=int(input("Enter marks of subject 3: "))
avg=(sub1+sub2+sub3)/3
print("average marks:",avg)
print(round(avg,2))

if avg>=75:
    print("pass")
else:
    print("fail")
