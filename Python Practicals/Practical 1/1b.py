# Enter the number from the user and depending on whether the number is even or odd, print out an appropriate message to the user.

print("11_KhushiTiwari")
number = int(input("Enter a number: "))
mod = number % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
