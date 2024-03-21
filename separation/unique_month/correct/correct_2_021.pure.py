def unique_month(month, possible_birthdays):
    count_month = 0
    for i in possible_birthdays:
        if i[0] == month:
            count_month += 1
    if count_month == 1:
        return True
    return False