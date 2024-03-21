def unique_day(day, possible_birthdays):
    b=[]  
    for birthday in possible_birthdays:
        b.append(birthday[1])
    if b.count(day)==1:
        return True
    return False