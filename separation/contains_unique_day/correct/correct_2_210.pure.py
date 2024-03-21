def contains_unique_day(month, possible_birthdays):
    tup = ()
    for i in possible_birthdays:
        if month == i[0]:
           tup = tup + (i,)
    for j in tup:
        day = j[1]
        if unique_day(day, possible_birthdays) == True:
            return True
    else:
        return False