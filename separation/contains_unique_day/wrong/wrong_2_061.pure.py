def contains_unique_day(month, possible_birthdays):
    dates = ()
    for date in possible_birthdays:
        if date[0] == month:
            dates += (date,)
    for dated in dates:
        if unique_day(dated[1], possible_birthdays) == True:
            return True
    else:
        return False