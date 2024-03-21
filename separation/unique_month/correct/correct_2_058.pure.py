def unique_month(month, possible_birthdays):
    total_month = 0
    for birthday in possible_birthdays:
        if birthday[0] == month:
            total_month += 1
    if total_month == 1:
        return True
    else:
        return False