def unique_month(month, possible_birthdays):
    b=[] 
    for birthday in possible_birthdays:
        b.append(birthday[0])
    if b.count(month)==1:
        return True
    return False