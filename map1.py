

number = [1,2,3,4,5,6,7,8,9]

squared_number = map(lambda x: x**2,number)
print(list(squared_number))

ages =  [16,19,20,21,14,14,18,23,22]

can_drink_in_israel = list(map(_f,ages))

print(can_drink_in_israel)