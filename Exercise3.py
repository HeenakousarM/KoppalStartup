"""In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. 
You must add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.
You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator []. """

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")

for n in numbers:
    print(n)
for s in strings:
    print(s)

print("The second name on the names list is %s" % second_name)