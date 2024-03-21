def unique_day(day, possible_birthdays):
    counter = 0
    for ele in possible_birthdays:
        birthday = ele[1]
        if birthday == day:
            counter += 1
    if counter == 1:
        return True
    else:
        return False