def contains_unique_day(month, possible_birthdays):
    results = ()
    for birthday in possible_birthdays:
        if month == birthday[0]:
            results += (unique_day(birthday[1], possible_birthdays),)
    if True in results:
        return True
    else:
        return False