def unique_month(month, possible_birthdays):
    months = tuple(map(lambda x: x[0],possible_birthdays))
    count = 0
    for i in months:
        if i == month:
            count = count +1
    return count ==1