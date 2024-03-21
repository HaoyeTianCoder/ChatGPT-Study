def unique_month(month, possible_birthdays):
    counter = 0
    for mth in range(len(possible_birthdays)):
        if month == possible_birthdays[mth][0]:
            counter += 1
    return True if counter == 1 else False