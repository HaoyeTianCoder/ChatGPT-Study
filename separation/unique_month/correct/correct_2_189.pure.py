def unique_month(month, possible_birthdays):
    months = map(lambda x: x[0], possible_birthdays)
    counter = 0
    for i in months:
        if month == i:
            counter += 1
    if counter == 1:
        return True
    else:
        return False