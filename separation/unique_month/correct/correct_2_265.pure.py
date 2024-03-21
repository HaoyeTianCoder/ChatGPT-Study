def unique_month(month, possible_birthdays):
    def get_month(birthday):
        return birthday[0]
    count = 0
    for i in possible_birthdays:
        if get_month(i) == month:
            count +=1
        else:
            continue
    if count == 1:
        return True
    else:
        return False