def unique_month(month, possible_birthdays):
    store= ()
    for birthday in possible_birthdays:
        if birthday[0] == month:
            store += (birthday[0],)
    n = len(store)
    if n >1:
        return False
    return True