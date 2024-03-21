def unique_month(month, possible_birthdays):
    months = tuple(map(lambda x: x[0], possible_birthdays))
    count = 0
    for temp_month in months:
        if temp_month==month:
            count+=1
    return True if count == 1 else False