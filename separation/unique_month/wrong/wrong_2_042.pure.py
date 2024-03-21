def unique_month(month, possible_birthdays):
    months = ()
    for birthdays in possible_birthdays:
        months += (birthdays[0],)
    a = 0
    for dates in months:
        if month == dates:
            a +=1
    if a !=1:
        return False
    return True