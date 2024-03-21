def contains_unique_day(month, possible_birthdays):
    data = ()
    number = 0
    for datas in possible_birthdays:
        if month in datas:
            data += (datas,)
    for days in data:
        number += unique_day(days[1], possible_birthdays)
    if number >= 1:
        return True
    else:
        return False