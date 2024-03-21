def contains_unique_day(month, possible_birthdays):
    data, outcome = (),()
    for birthday in possible_birthdays:
        if month == birthday[0]:
            data += (birthday,)
    for birthday in data:
        if unique_day(birthday[1], possible_birthdays) == True:
            outcome += birthday
        else:
            continue
    if outcome == ():
        return False
    else:
        return unique_day(outcome[1],possible_birthdays)