def unique_month(month, possible_birthdays):
    unique = False
    for i in possible_birthdays:
        if month == i[0]:
            if unique:
                return False
            else:
                unique = True
    return True