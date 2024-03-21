def unique_month(month, possible_birthdays):
    result = ()
    for p in possible_birthdays:
        pm = p[0]
        if month == pm:
            result = result + (month,)
    if len(result) > 1:
        return False
    return True