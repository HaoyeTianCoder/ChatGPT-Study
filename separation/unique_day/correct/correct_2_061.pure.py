def unique_day(day, possible_birthdays):
    unique = ()
    for birthday in possible_birthdays:
        if day == birthday[1]:
            unique = unique + (day,)
    if len(unique) == 1:        
        return True
    return False