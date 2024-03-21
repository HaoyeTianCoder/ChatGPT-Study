def contains_unique_day(month, possible_birthdays):
    tup = ()
    for n in possible_birthdays:
        if n[0] == month:
            tup = tup + ((n), )
        else:
            continue
    for n in tup:
        if unique_day(n[1], possible_birthdays):
            return True
    return False