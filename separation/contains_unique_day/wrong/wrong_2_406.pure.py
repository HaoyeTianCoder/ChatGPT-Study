def contains_unique_day(month, possible_birthdays):
    for i in possible_birthdays:
        if unique_day(i[1], possible_birthdays) == True:
            ans = False
            if i[0] == month:
                ans = True
                break
            else:
                continue
        else:
            continue
    return ans