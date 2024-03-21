def unique_month(month, possible_birthdays):
    j = 0
    for i in possible_birthdays:
        if month == i[0]:
            j = j+1
        else:
            j = j
    if j == 1:
        return True
    else:
        return False