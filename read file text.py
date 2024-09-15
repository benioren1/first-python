import re
file_path = "text_to_read.txt"

with open(file_path, "r") as f:
    reader = f.read()

one_row = reader
y = re.sub(r'[^\w\s]', '', one_row)
x = y.split()
print(x)

my_dict = {}
count = 0
for i in range(len(x)):
    for j in range(len(x)):
        if x[i] == x[j]:
            count += 1

    my_dict[x[i]] = count
    count =0
print(my_dict)

inverse_dict = {v: k for k, v in my_dict.items()}

top_10_values = sorted(my_dict.values(), reverse=True)[:10]
print(top_10_values)
my_dict2 = {}

for i in range(len(top_10_values)):
    my_dict2[top_10_values[i]] = inverse_dict[top_10_values[i]]

print(my_dict2)