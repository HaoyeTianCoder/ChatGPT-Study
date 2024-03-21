def unique_month(month, possible_birthdays):
    months = ()
    for a in possible_birthdays:
        months += (a[0],)
    if months.count(month) == 1:
        return True
    else:
        return False