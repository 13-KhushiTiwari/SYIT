# Take a list, say for example this one : a = [1,1,2,3,5,8,13,21,34,55,89]
# And write a program that prints out all the elements of the list that are less than 5

print("11_KhushTiwari")
a = [1, 1, 2, 3, 5, 8,  13, 21, 34, 55, 89]

number = int(input("Enter the number: "))

new_list = []

for i in a:
    if i < number:
        new_list.append(i)
print(new_list)
