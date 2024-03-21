def contains_unique_day(month, possible_birthdays):
    result = ()
    for p in possible_birthdays:
        if month == p[0]:
            result = result + (p,)
    for r in result:
        if unique_day(r[1], possible_birthdays) == True:
            return True
    return False