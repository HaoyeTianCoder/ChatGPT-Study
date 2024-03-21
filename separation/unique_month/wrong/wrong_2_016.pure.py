def unique_month(month, possible_birthdays):
    months = map(lambda x: x[0], possible_birthdays)
    times = 0
    for i in months:
        if i==month:
            times = times+1
        else:
            continue
    if times>1:
        return False
    else:
        return True