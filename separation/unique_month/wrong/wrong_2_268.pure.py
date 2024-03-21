def unique_month(month, possible_birthdays):
    count = 0
    for i in range(len(possible_birthdays)):
        check = possible_birthdays[i][0]
        if check == month:
            count = count+1
    if count >1:
        return False
    return True