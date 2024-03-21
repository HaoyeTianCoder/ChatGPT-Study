def unique_month(month, possible_birthdays):
    datetup = ()
    for item in possible_birthdays:
        if item[0] == month:
            datetup = datetup + (item[0],)
    if len(datetup) == 1:
        return True
    else:
        return False