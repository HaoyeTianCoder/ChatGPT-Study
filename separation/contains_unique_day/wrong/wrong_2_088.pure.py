def contains_unique_day(month, possible_birthdays):
    for possiblemonth in possible_birthdays:
        if possiblemonth[0] == month:
            if unique_day(possiblemonth[1],possible_birthdays) == True:
                return True
            else:
                continue
    return False