def unique_day(day, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if str(day) == i[1]:
            counter = counter + 1
    if counter > 1:
        return False
    else:
        return True