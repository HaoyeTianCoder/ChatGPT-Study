def contains_unique_day(month, possible_birthdays):
    daystoconsider = ()
    i = 0
    while i < len(possible_birthdays):
        if month == possible_birthdays[i][0]:
            daystoconsider += (possible_birthdays[i][1],)
        i += 1
    monthcontaininguniqueday = ()
    for a in range(len(possible_birthdays)):
        if possible_birthdays[a][1] in daystoconsider:
            monthcontaininguniqueday += (possible_birthdays[a][0],)
    for mth in range(len(monthcontaininguniqueday)):
        if monthcontaininguniqueday[mth] == month:
            return True
            break
        return False