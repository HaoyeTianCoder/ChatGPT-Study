def contains_unique_day(month, possible_birthdays):
    counter = 0
    birthdays = ()
    days = ()
    for i in range(len(possible_birthdays)):
        if month == possible_birthdays[i][0]:
            birthdays = birthdays + (possible_birthdays[i],)
        else:
            days = days + (possible_birthdays[i][1],)
    for i in range(len(birthdays)):
        if birthdays[i][1] in days:
            counter = counter + 1
    return (len(birthdays)> counter)