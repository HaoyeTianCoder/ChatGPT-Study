def contains_unique_day(month, possible_birthdays):
    same_month_tuple = ()
    count = 0
    for i in possible_birthdays:
        if i[0] == month:
            same_month_tuple = same_month_tuple + (i,)
    for i in same_month_tuple:
        if unique_day(i[1], possible_birthdays):
            return True
    return False