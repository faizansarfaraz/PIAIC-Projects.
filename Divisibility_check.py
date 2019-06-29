print("Divisibility check of two numbers")
print("---------------------------------")
print()
numinator = int(input("Enter Numinator:"))
denominator = int(input("Enter Denominator:"))
print()
remainder = numinator % denominator
if remainder==0:
    print("Number", numinator, "is completely divisible by", denominator)
if remainder > 0:
    print("Number", numinator, "is not divisible by", denominator)
if remainder < 0:
    print("Number", numinator, "is not divisible by", denominator)
