def unique_day(day, possible_birthdays):
    the_day = ()
    for i in possible_birthdays:
        if i[1] == day:
            the_day += (day,)
    return len(the_day) == 1