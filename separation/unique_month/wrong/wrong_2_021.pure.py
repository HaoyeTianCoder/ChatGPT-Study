def unique_month(month, possible_birthdays):
    possible_months = tuple(map(lambda x: x[0], possible_birthdays))
    counter = 0
    for possible_month in possible_months:
        if month == possible_month:
            counter = counter + 1
    if counter == 1:
        return True
    elif counter > 1:
        return False
    else:
        return "Not a month in possible_birthdays"  