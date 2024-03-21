def unique_month(month, possible_birthdays):
    flag = 0
    for i in possible_birthdays:
        if i[0] == month:
            flag += 1
    return True if flag == 1 else False