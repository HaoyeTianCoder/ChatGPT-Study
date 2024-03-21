def contains_unique_day(month, possible_birthdays):
    new_tup = ()
    edited_tup = ()
    for i in range (len(possible_birthdays)):
        if month == possible_birthdays [i][0]:
            new_tup = new_tup + ((possible_birthdays[i][0],possible_birthdays[i][1]),)
    for i in range (len(possible_birthdays)):
        if month != possible_birthdays [i][0]:
            edited_tup = edited_tup + ((possible_birthdays[i][0],possible_birthdays[i][1]),)