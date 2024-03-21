def contains_unique_day(month, possible_birthdays):
    correct_months = ()
    for birthday in possible_birthdays:
        if unique_day(birthday[1], possible_birthdays):
            correct_months = correct_months + (birthday[0],)
    if month in correct_months:
        return True
    return False 