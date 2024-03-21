def unique_month(month, possible_birthdays):
    i = 0
    for months in possible_birthdays:
        if month == months[0]:
            i += 1
    if counter == 1:
        return True
    else:
        return False