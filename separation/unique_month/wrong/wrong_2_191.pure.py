def unique_month(month, possible_birthdays):
    counter = 0
    for i in range(0,len(possible_birthdays)):
        if possible_birthdays[i][0] == month:
            counter = counter + 1
    if counter == 1:
        return True
    else:
        return False