def unique_day(date, possible_birthdays):
    for i in range(0,len(possible_birthdays)):
        list_final = [x for x in possible_birthdays[i][1]]
        list_final = sorted(list_final)
        if date == list_final[i] and date != list_final[i+1] and date != list_final[i-1]:
            return True
        else:
            return False