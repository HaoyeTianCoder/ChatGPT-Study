def unique_day(day, possible_birthdays):
    a = map(lambda x : x[1], possible_birthdays)
    for i in  a:
        if i == day:
            b = filter(lambda x: x == i, a)
            if len(b) > 1:
                return False
            else:
                return True