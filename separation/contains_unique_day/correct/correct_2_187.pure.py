def contains_unique_day(month, possible_birthdays):
    unique = ()
    for i in possible_birthdays:
        if unique_day(i[1], possible_birthdays):
            unique += (i,)
    for i in unique:
        if month == i[0]:
            return True
    else:
        return False