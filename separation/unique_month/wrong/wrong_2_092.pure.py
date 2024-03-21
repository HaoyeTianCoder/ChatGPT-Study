def unique_month(month, possible_birthdays):
    counter = 0
    for dates in possible_birthdays:
        if month == dates[0]:
            possible_birthdays = possible_birthdays[1:]
            counter = counter + 1 
    if counter == 1:
        return True
    else:
        return False 