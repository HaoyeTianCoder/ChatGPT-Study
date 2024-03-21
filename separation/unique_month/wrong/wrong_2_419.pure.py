def unique_month(month, possible_birthdays):
    n=0
    for i in range (len(possible_birthdays)):
        if month == possible_birthdays[i][0]:
            n+=1
        else:
            n=n
    return n == 1