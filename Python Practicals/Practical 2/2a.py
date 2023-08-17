# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

print("11_KhushiTiwari")
def check(c):
 if(c=="a" or c=="A" or
   c=="e" or c=="E" or
   c=="i" or c=="I" or
   c=="o" or c=="O" or
   c=="u" or c=="U"):
    return"True"
 else:
    return"False"
print("Enter the string to check: ")
c=input()
if check(c)=="True":
    print("The character is Vowel")
else:
    print("The character is not Vowel")
