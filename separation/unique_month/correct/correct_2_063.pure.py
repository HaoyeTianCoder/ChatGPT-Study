def unique_month(month, possible_birthdays):
    unique = ()
    for birthday in possible_birthdays:
        if month == birthday[0]:
            unique = unique + (month,)
    if len(unique) == 1:
        return True
    return False