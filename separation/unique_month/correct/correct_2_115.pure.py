def unique_month(month, possible_birthdays):
    product = 0
    for i in possible_birthdays:
        if i[0] == month:
            product +=1
    if product == 1:
        return True
    else:
        return False