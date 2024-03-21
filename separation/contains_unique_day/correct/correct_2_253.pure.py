def contains_unique_day(month, possible_birthdays):
    new_possible_birthdays = ()
    for i in range(len(possible_birthdays)):
        if month == possible_birthdays[i][0]:
           new_possible_birthdays += (possible_birthdays[i],)
    new_day = ""
    counter = 0
    for n in range(len(new_possible_birthdays)):
        new_day = new_possible_birthdays[n][1]
        if unique_day(new_day,possible_birthdays) == True:
            counter += 1
    if counter == 0:
        return False
    else:
        return True