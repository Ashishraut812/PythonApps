# first line
print('hello world!')

# changing assignments
a=20
b=30
print(a, b)
a, b=b, a
print(a, b)


#list - mutable datastructure - can be changed

my_list = [10,20,30,40]
type(my_list)

#to add no
my_list.append(50)
print(my_list)

#to add multiple values - extend
my_list.extend([60,70])
print(my_list)


#to sort - inline update - does not assignment
my_list.sort()
print(my_list)

#to insert - add at position
my_list.insert(1, 15)
print(my_list)