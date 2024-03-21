def unique_month(month, possible_birthdays):
    unique_month_counter = 0
    for i in possible_birthdays:
        if month == i[0]:
            unique_month_counter += 1
    if unique_month_counter != 1:
        return False
    return True