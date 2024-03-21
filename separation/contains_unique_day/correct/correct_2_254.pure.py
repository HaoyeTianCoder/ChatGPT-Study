def contains_unique_day(month, possible_birthdays):
    month_tup = ()
    helper = 0
    for i in possible_birthdays:
        if month in i:
            month_tup = month_tup + possible_birthdays[helper]
        helper = helper + 1
    for i in range(1, 32):
        if unique_day(str(i), possible_birthdays) == True:
            if str(i) in month_tup:
                return True
    return False