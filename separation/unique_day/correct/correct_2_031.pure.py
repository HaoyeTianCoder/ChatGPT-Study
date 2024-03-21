def unique_day(date, possible_birthdays):
    count = 0
    for tup in possible_birthdays:
        if tup[1] == date:
            count+=1
    return count == 1