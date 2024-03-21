def unique_month(month, possible_birthdays):
    a = map(lambda x : x[0], possible_birthdays)
    for i in  a:
        if i == month:
            b = filter(lambda x: x == i, a)
            if len(b) > 1:
                return False
            else:
                return True