import random, datetime
def getBirthdays(number):
    Birthdays = []
    for a in range(number):
        start = datetime.date(2022,1,1)
        b = datetime.timedelta(random.randint(0, 364))
        Birthday = start + b
        Birthdays.append(Birthday)
    return Birthdays 
print(getBirthdays(10))    