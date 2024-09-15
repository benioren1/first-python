data = [
    {'Name': 'Alice', 'Category': 'A', 'Amount': 100},
    {'Name': 'Bob', 'Category': 'B', 'Amount': 150},
    {'Name': 'Charlie', 'Category': 'A', 'Amount': 200},
    {'Name': 'David', 'Category': 'B', 'Amount': 50},
    {'Name': 'Eve', 'Category': 'A', 'Amount': 300}
]

# קיבוץ לפי קטגוריה
grouped_data = {}
for item in data:
    key = item['Category']
    if key not in grouped_data:
        grouped_data[key] = []
    grouped_data[key].append(item)

print(grouped_data)
הסבר: אנו מקבצים את הפריטים לפי הערך שבקטגוריה (מפתח Category). התוצאה היא מילון שבו המפתחות הם הקטגוריות והערכים הם רשימות של פריטים השייכים לכל קטגוריה.

חישוב סיכום לפי קטגוריה
python
Copy code
# חישוב סכום של Amount לפי קטגוריה
sums = {}
for item in data:
    key = item['Category']
    if key not in sums:
        sums[key] = 0
    sums[key] += item['Amount']

print(sums)
הסבר: כאן אנו מחשבים את הסכום הכולל של Amount לכל קטגוריה.

קיבוץ לפי שדה של רשימה ומניפולציה על תוצאות
python
Copy code
from itertools import groupby
from operator import itemgetter

# סדר את הרשימה לפי קטגוריה
data_sorted = sorted(data, key=itemgetter('Category'))

# קיבוץ לפי קטגוריה
grouped = groupby(data_sorted, key=itemgetter('Category'))

# הצגת התוצאה
for key, group in grouped:
    print(f'Category: {key}')
    for item in group:
        print(f'  {item}')
הסבר: קודם אנו ממיינים את הנתונים לפי הקטגוריה ואז מקבצים את הנתונים באמצעות groupby. תוצאת הקיבוץ היא סדרה של קבוצות לפי המפתח.

2. קיבוץ נתונים עם קובץ CSV
קריאה וקיבוץ נתונים מקובץ CSV
python
Copy code
import csv
from collections import defaultdict

# קריאת הנתונים מקובץ CSV
filename = 'data.csv'  # שים כאן את שם הקובץ שלך
data = []

with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

# קיבוץ לפי קטגוריה
grouped_data = defaultdict(list)
for item in data:
    key = item['Category']
    grouped_data[key].append(item)

print(grouped_data)
הסבר: קראנו את הנתונים מקובץ CSV תוך שימוש ב-csv.DictReader שהופך כל שורה למילון. לאחר מכן, קיבצנו את הנתונים לפי הקטגוריה בעזרת מילון defaultdict שמייצרת רשימות אוטומטית.

חישוב סיכום לפי קטגוריה מתוך CSV
python
Copy code
# חישוב סכום של Amount לפי קטגוריה
sums = defaultdict(int)
for item in data:
    key = item['Category']
    sums[key] += float(item['Amount'])  # המרה למספר צף כדי לחשב את הסכום

print(sums)
הסבר: אנחנו סופרים את הסכומים לפי קטגוריה תוך המרה של Amount למספר צף.

3. קיבוץ נתונים עם pandas
קיבוץ לפי עמודה עם pandas
python
Copy code
import pandas as pd

# יצירת DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Amount': [100, 150, 200, 50, 300]
})

# קיבוץ לפי קטגוריה וסיכום של Amount
grouped = df.groupby('Category')['Amount'].sum()

print(grouped)
הסבר: כאן אנו מקבצים את הנתונים לפי הקטגוריה (Category) ומבצעים חישוב סכום של Amount לכל קטגוריה.

חישוב ממוצע וסטיית תקן
python
Copy code
# קיבוץ לפי קטגוריה וחישוב ממוצע וסטיית תקן של Amount
grouped_stats = df.groupby('Category')['Amount'].agg(['mean', 'std'])

print(grouped_stats)
הסבר: אנו מקבצים את הנתונים לפי קטגוריה ומבצעים חישוב ממוצע וסטיית תקן של Amount.

קיבוץ לפי מספר עמודות
python
Copy code
# יצירת DataFrame עם מספר עמודות לקיבוץ
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Subcategory': ['X', 'Y', 'X', 'Y', 'X'],
    'Amount': [100, 150, 200, 50, 300]
})

# קיבוץ לפי קטגוריה ו-Subcategory
grouped = df.groupby(['Category', 'Subcategory'])['Amount'].sum()

print(grouped)