def contains_unique_day(month, possible_birthdays):
    all_day_in_given_month = ()
    for i in possible_birthdays:
        if i[0] == month:
            all_day_in_given_month += (i[1],)
    for i in all_day_in_given_month:
        if unique_day(i, possible_birthdays):
            return True
    return False