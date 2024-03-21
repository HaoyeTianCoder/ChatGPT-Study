def unique_month(month, possible_birthdays):
    counter = 0
    for dates in possible_birthdays:
        if month in dates:
            counter += 1
    if counter == 1:
        return True
    else:
        return False