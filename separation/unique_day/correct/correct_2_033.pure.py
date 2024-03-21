def unique_day(date, possible_birthdays):
    flag = 0
    for i in possible_birthdays:
        if i[1] == date:
            flag += 1
    return True if flag == 1 else False