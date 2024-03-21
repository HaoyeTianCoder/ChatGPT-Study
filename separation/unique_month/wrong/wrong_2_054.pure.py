def unique_month(month, possible_birthdays):
    for i in range(0,len(possible_birthdays)):
        list = [x for x in possible_birthdays[i][0]]
        list = sorted(list)
        if month == list[i] and month != list[i+1] and month != list[i-1]:
            return True
        else:
            return False