def unique_month(month, possible_birthdays):
    index = 1
    for months in tuple(map(lambda x:x[0], possible_birthdays)):
        if month == months:
            index = index*(-1)
            if index == 1:
                return False
    return True