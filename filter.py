number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x:  x% 2 ==0,number))

print(even_numbers)



vet = ["sdrrg","aregregqe","ergrqegqerg",'rgeq',"geqge","eq","gerqggreg"]


even_max_5 = list(filter(lambda x: len(x) <= 5, vet))
print(even_max_5)

# דוגמאות לשימוש ב-filter בפייתון

# פונקציה לעיכול
def is_even(n):
    return n % 2 == 0

# 1. **דוגמה קלה: סינון מספרים זוגיים מתוך רשימה**

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
print("Even numbers:", even_numbers)
# Output: Even numbers: [2, 4, 6]

# 2. **דוגמה קלה: סינון מיתרים באורך מסוים**

strings = ['apple', 'banana', 'cherry', 'date']
short_strings = list(filter(lambda s: len(s) <= 5, strings))
print("Short strings:", short_strings)
# Output: Short strings: ['apple', 'date']

# 3. **דוגמה בינונית: סינון מספרים חיוביים מתוך רשימה**

numbers = [-10, -5, 0, 5, 10]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print("Positive numbers:", positive_numbers)
# Output: Positive numbers: [5, 10]

# 4. **דוגמה בינונית: סינון אובייקטים לפי תכונה**

# יצירת מחלקה
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# רשימת אובייקטים
people = [Person('Alice', 24), Person('Bob', 30), Person('Charlie', 28)]

# סינון אנשים מעל גיל 25
older_than_25 = list(filter(lambda p: p.age > 25, people))
print("People older than 25:", [p.name for p in older_than_25])
# Output: People older than 25: ['Bob', 'Charlie']

# 5. **דוגמה קשה: סינון רשימות של רשימות לפי סכום**

lists_of_numbers = [[1, 2], [3, 4, 5], [6]]
non_empty_sums = list(filter(lambda lst: sum(lst) > 5, lists_of_numbers))
print("Lists with sum greater than 5:", non_empty_sums)
# Output: Lists with sum greater than 5: [[3, 4, 5], [6]]

# 6. **דוגמה קשה: סינון מיתרים לפי אם הם מכילים תו מסוים**

# רשימת מיתרים
strings = ['apple', 'banana', 'cherry', 'date']

# סינון מיתרים שמכילים את התו 'a'
contains_a = list(filter(lambda s: 'a' in s, strings))
print("Strings containing 'a':", contains_a)
# Output: Strings containing 'a': ['apple', 'banana', 'date']

# 7. **דוגמה מתקדמת: סינון של אובייקטים לפי תנאים מורכבים**

# יצירת מחלקה
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

# רשימת מוצרים
products = [
    Product('Laptop', 1200, 5),
    Product('Smartphone', 800, 0),
    Product('Tablet', 300, 15)
]

# סינון מוצרים במחיר מעל 500 ושיש להם מלאי
expensive_in_stock = list(filter(lambda p: p.price > 500 and p.stock > 0, products))
print("Expensive products in stock:", [p.name for p in expensive_in_stock])
# Output: Expensive products in stock: ['Laptop']

# 8. **דוגמה מתקדמת: סינון של תאריכים לפי אם הם בשנה מסוימת**

from datetime import datetime

# רשימת תאריכים
dates = [
    datetime(2023, 1, 15),
    datetime(2024, 5, 10),
    datetime(2023, 12, 25),
    datetime(2024, 7, 19)
]

# סינון תאריכים לשנת 2023
dates_2023 = list(filter(lambda d: d.year == 2023, dates))
print("Dates in 2023:", dates_2023)
# Output: Dates in 2023: [datetime.datetime(2023, 1, 15, 0, 0), datetime.datetime(2023, 12, 25, 0, 0)]
