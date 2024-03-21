def unique_month(month, possible_birthdays):
    count = 0
    months = map(lambda x:x[0], possible_birthdays)
    for i in months:
        if i == month:
            count += 1
    if count != 1:
        return False
    return True