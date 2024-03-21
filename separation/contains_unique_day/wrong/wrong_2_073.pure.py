def contains_unique_day(month, possible_birthdays):
    birthdays_with_month = ()
    for i in possible_birthdays:
        if i[0] == month:
            birthdays_with_month += (i[1],)
    counter = 0
    for i in birthdays_with_month:
        if unique_day(i, possible_birthdays) == True:
            counter += 1
    if counter == 1:
        return True
    else:
        return False 