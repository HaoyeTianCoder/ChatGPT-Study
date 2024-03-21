def contains_unique_day(month, possible_birthdays):
    b=0
    for i in range(len(possible_birthdays)):
        if month==possible_birthdays[i][0]:
            b+=unique_day(possible_birthdays[i][1],possible_birthdays)
    if b==0:
        return False
    else:
        return True