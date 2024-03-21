def unique_day(day, possible_birthdays):
    store = ()
    for birthday in possible_birthdays:
        if birthday[1] == day:
            store += (birthday[1],)
    n = len(store)
    if n >1:
        return False
    return True