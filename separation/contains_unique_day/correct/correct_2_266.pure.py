def contains_unique_day(month, possible_birthdays):
    list_of_days = ()
    for x in possible_birthdays:
        if month == x[0]:
            x_day = x[1]
            if unique_day(x_day,possible_birthdays) == True:
                return True
    return False