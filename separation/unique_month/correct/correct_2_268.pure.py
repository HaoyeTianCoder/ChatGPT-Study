def unique_month(month, possible_birthdays):
    total= 0
    for i in possible_birthdays:
        if month == i[0]:
            total= total + 1
    return total == 1