def contains_unique_day(month, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if month == i[0]:
            if unique_day(i[1], possible_birthdays):
                counter += 1
    if counter != 0:
        return True
    return False