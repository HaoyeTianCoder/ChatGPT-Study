def unique_day(date, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if date in i:
            counter +=1
    if counter >1:
        return False
    else:
        return True