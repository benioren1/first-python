from datetime import datetime,date,time,timedelta,timezone
from itertools import count

from rsa.key import calculate_keys

current_date_time = datetime.now()
print(current_date_time)

current_date1 = datetime.now().date()
current_date2 = datetime.now().time()

print(current_date1)
print(current_date2)

spesipic_datetime = datetime(2024,9,10)

print(spesipic_datetime)

formated_datetime = spesipic_datetime.strftime("%d/%m/%y")
print(formated_datetime)
specific_datetime = datetime(2024, 9, 3)
print(specific_datetime.strftime("%d/%m/%y:%H-%M"))
print(specific_datetime.strftime("%A, %m %d, %Y"))
now = datetime.now()
futher_date1 = now + timedelta(days=2,hours=6,milliseconds=785)
futher_date2 = now - timedelta(days=2,hours=6,milliseconds=785)
print(futher_date1)
print(futher_date2)


utc_datetime = datetime.now(timezone.utc)
print(utc_datetime)

# start_date = '2024-08-01'
# end_date = '2024-08-10'

# Output: (7, [(1, datetime(2024, 8, 1)), (2, datetime(2024, 8, 2)), (3, datetime(2024, 8, 5)), ...])


def Calculate_Working(start_work,end_work):
    my_list =[]
    while start_work <= end_work:
        today = start_work.strftime("%A")
        if today != "Friday" and today != "Saturday":
            my_list.append(start_work)
        start_work += timedelta(days=1)
    return len(my_list), my_list


start_work = datetime(2024, 9, 4)  # Start date
end_work = datetime(2024, 9, 10)


print(Calculate_Working(start_work,end_work))

def calcolate_ribit(principal, rate, days):
    my_list = []
    new_principal = principal
    for i in range(days):
        my_list.append( (rate/365 +1)*new_principal)
        new_principal = ( (rate/365 +1)*new_principal)
    return my_list

print(calcolate_ribit(1000,0.05,31))