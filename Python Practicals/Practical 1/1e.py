# Write a function to check the input value is Armstrong

print("11_KhushiTiwari")
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

# Write the function for palindrome

def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = (input('Enter a word: '))
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
