def unique_month(month, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if month == i[0]:
            count += 1
        else:
            continue
    if count == 1:
        return True
    else:
        return False