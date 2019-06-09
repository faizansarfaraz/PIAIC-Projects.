print("Determination of odd and even numbers")
print("=====================================")
print()
number=int(input("Enter Number:"))
x = number % 2
if x == 0:
    print(number, "is even.")
if x > 0:
    print(number, "is odd")
if x < 0:
    print(number,"is odd")
