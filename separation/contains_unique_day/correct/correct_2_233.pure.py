def contains_unique_day(month, possible_birthdays):
    b=[]
    for birthday in possible_birthdays:
        if month == birthday[0]:
            b.append(birthday[1])  
    for day in b:
        if unique_day(day,possible_birthdays)==True:
            return True
    return False