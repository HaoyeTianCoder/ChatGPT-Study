def contains_unique_day(month, possible_birthdays):
    days = ()
    for a in possible_birthdays:        
        if a[0] == month:
            days = days + (a[1],)
    for b in days:
        if unique_day(b, possible_birthdays):
            return True
    return False