number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x:  x% 2 ==0,number))

print(even_numbers)



vet = ["sdrrg","aregregqe","ergrqegqerg",'rgeq',"geqge","eq","gerqggreg"]


even_max_5 = list(filter(lambda x: len(x) <= 5, vet))
print(even_max_5)