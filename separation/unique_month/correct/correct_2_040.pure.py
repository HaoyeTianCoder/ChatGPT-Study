def unique_month(month, possible_birthdays):
    month_count = 0
    for birthday in possible_birthdays:
        if birthday[0] == month:
            month_count = month_count + 1
        if month_count > 1:
            break
    if month_count == 1:
        return True
    else:
        return False