def unique_month(month, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if str(month) == i[0]:
            counter = counter + 1
    if counter > 1:
        return False
    else:
        return True