def unique_day(day, possible_birthdays):
    store = 0
    for i in possible_birthdays:
        if i[1] == day:
            if store == 1:
                return False
            else:
                store += 1
    return True