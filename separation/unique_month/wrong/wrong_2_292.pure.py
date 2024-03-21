def unique_month(month, possible_birthdays):
    the_month = ()
    for i in possible_birthdays:
        if i[0] == month:
            the_month += (month,)
    return len(the_month) == 1