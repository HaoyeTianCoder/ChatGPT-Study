def contains_unique_day(month, possible_birthdays):
    days=()
    for birthday in possible_birthdays:
        if month== birthday[0]:
            days += (birthday[1],)
    for day in days:
        if unique_day(day, possible_birthdays)== False:
            continue
        else:
            return unique_day(day, possible_birthdays)
    return False