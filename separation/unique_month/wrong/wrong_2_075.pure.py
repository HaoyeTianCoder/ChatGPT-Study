def unique_month(month, possible_birthdays):
    no_of_months = 0
    for i in possible_birthdays:
        if i[0] == month:
            no_of_months += 1
    if no_of_months != 1:
        return False
    return True