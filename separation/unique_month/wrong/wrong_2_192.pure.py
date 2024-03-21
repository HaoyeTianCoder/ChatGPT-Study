def unique_month(month, possible_birthdays):
    i=0
    for birthday in possible_birthdays:
        if month == birthday[0]:
            i+=1
            if i == 2:
                return False
    return True