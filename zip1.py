# שתי רשימות פשוטות
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 30, 28]

# חיבור בין הרשימות
zipped = zip(names, ages)

# המרת האובייקט של zip לרשימה
print(list(zipped))
# Output: [('Alice', 24), ('Bob', 30), ('Charlie', 28)]

# שלוש רשימות
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]
grades = ['A', 'B', 'C']

# חיבור של שלוש רשימות
zipped = zip(names, scores, grades)

# המרת האובייקט של zip לרשימה
print(list(zipped))
# Output: [('Alice', 85, 'A'), ('Bob', 90, 'B'), ('Charlie', 78, 'C')]

# רשימות באורכים שונים
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90]

# חיבור בין הרשימות
zipped = zip(names, scores)

# המרת האובייקט של zip לרשימה
print(list(zipped))
# Output: [('Alice', 85), ('Bob', 90)]

# אובייקט zip
zipped = [('Alice', 24), ('Bob', 30), ('Charlie', 28)]

# פתיחת ה-zipped לרשימות נפרדות
names, ages = zip(*zipped)

print(names)
# Output: ('Alice', 'Bob', 'Charlie')
print(ages)
# Output: (24, 30, 28)

# רשימות לא שוות באורך
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']

# חיבור בין הרשימות
zipped = zip(list1, list2)

# המרת האובייקט של zip לרשימה
print(list(zipped))
# Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# דיקלרטים
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']

# חיבור בין הרשימות ויצירת דיקלרט
dictionary = dict(zip(keys, values))

print(dictionary)
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}



# יצירת מחלקה מותאמת אישית
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"


# רשימות עם נתונים
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 30, 28]

# יצירת אובייקטים Person עם zip
people = [Person(name, age) for name, age in zip(names, ages)]

print(people)
# Output: [Person(name=Alice, age=24), Person(name=Bob, age=30), Person(name=Charlie, age=28)]

# מטריצה (גריד של נתונים)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# חיבור של עמודות
transposed = zip(*matrix)

# המרת התוצאה לרשימה
print(list(transposed))
# Output: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]