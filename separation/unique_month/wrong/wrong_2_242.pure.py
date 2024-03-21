def unique_month(month, possible_birthdays):
    months = ()
    for i in possible_birthdays:
        months += (i[0],)
    count = 0
    for ele in months:
        if ele == month:
            count += 1
    if count == 1:
        return True
    else:
        return False