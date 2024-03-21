def unique_day(day, possible_birthdays):
    days = ()
    for birthday in possible_birthdays:
        if birthday[1] != day:
            continue
        elif birthday[1] not in days:
            days += (birthday[1],)
        else:
            return False
    return True