def unique_day(day, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if day == i[1]:
            counter += 1
        else:
            continue
    if counter == 1:
        return True
    else:
        return False