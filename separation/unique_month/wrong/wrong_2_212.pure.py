def unique_month(month, possible_birthdays):
    count=0
    for i in range(len(possible_birthdays)):
        if month==possible_birthdays[i][0]:
            count=count+1
    if count>=2:
        return False
    return True