def unique_month(month, possible_birthdays):
    store = 0
    for i in possible_birthdays:
        if i[0] == month:
            if store == 1:
                return False
            else:
                store += 1
    return True