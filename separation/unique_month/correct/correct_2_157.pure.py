def unique_month(month, possible_birthdays):
    months = ()
    for elem in possible_birthdays:
        months += (elem[0],)
    times = months.count(month)
    if times == 1:
        return True
    else:
        return False