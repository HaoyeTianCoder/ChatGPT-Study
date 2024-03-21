def contains_unique_day(month, possible_birthdays):
    b =()
    for p in possible_birthdays:
        if month == p[0]:
            b += (p[1],) 
    for d in b:
        if unique_day(d, possible_birthdays) == False:
            continue
        return True
    return False