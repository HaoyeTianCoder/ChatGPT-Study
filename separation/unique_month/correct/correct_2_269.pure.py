def unique_month(month, possible_birthdays):
    counter = 0
    for x in possible_birthdays:
        x_month = x[0]
        if month == x_month:
            counter += 1
        else:
            counter = counter
    if counter == 1:
        return True
    else:
        return False