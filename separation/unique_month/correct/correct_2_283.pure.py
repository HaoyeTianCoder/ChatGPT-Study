def unique_month(month, possible_birthdays):
    get_possible_months = map(lambda bdays:bdays[0],possible_birthdays)
    count = 0
    for months in get_possible_months:
        if months == month:
            count = count + 1
    if count == 1:
        return True
    else:
        return False