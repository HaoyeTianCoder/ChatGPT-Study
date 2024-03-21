def contains_unique_day(month, possible_birthdays):
    datetup = ()
    for item in possible_birthdays:
        if item[0] == month:
            datetup = datetup + (item,)
    for item in datetup:
        if unique_day(item[1], possible_birthdays):
            return True
    return False