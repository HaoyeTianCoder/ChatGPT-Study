def contains_unique_day(month, possible_birthdays):
    x = ()
    for i in possible_birthdays:
        if i[0] == month:
            x = x + (i, )
    for a in x:
        if unique_day(a[1], possible_birthdays):
            return True
        else:
            return False 