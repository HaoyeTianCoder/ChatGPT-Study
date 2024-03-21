def contains_unique_day(month, possible_birthdays):
    x = ()
    for birthday in possible_birthdays:
        mn,dy = birthday
        if mn == month:
            x = x + (dy,)
    for i in x:
        if unique_day(i,possible_birthdays) == True:
            return True
    return False