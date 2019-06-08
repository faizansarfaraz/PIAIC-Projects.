print("Marksheet")
print()
name=input("Enter Student Name:")
roll_num=input("Enter Roll Number:")
phy_marks=int(input("Enter Physics Marks:"))
chem_marks=int(input("Enter Chemistry Marks:"))
math_marks=int(input("Enter Math Marks:"))
urdu_marks=int(input("Enter Urdu Marks:"))
eng_marks=int(input("Enter English Marks:"))
islam_marks=int(input("Enter Islamiat Marks:"))
print()
print("_________________________________")
print()
obtained_marks= phy_marks + chem_marks + math_marks + urdu_marks + eng_marks + islam_marks
total_marks=550
percentage=((obtained_marks / total_marks) * 100)
if percentage >=80 and percentage <=100:
    print("Grade A")
if percentage >=65 and percentage <=79.99:
    print("Grade B")
if percentage >=50 and percentage <=64.99:
    print("Grade C")
if percentage >=40 and percentage <=49.99:
    print("Grade D")
if percentage >=0 and percentage <=39.99:
    print("Grade F")
