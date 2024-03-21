def unique_day(day, possible_birthdays):
    def get_day(birthday):
        return birthday[1]
    count = 0
    for i in possible_birthdays:
        if get_day(i) == day:
            count +=1
        else:
            continue
    if count == 1:
        return True
    else:
        return False