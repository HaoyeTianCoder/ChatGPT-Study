def contains_unique_day(month, possible_birthdays):
    days_in_month = ()
    for i in possible_birthdays:
        if i[0] == month:
            days_in_month += (i,)
    for x in range(len(days_in_month)):
        if unique_day(days_in_month[x][1], possible_birthdays) == False:
            return True
        else:
            return False