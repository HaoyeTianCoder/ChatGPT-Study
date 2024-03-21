def unique_day(day, possible_birthdays):
    product = 0
    for i in possible_birthdays:
        if i[1] == day:
            product +=1
    if product == 1:
        return True
    else:
        return False