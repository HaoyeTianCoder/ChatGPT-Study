def contains_unique_day(month, possible_birthdays):
    tup=tuple(filter(lambda x: x[0]==month,possible_birthdays))
    for i in range(len(tup)):
        if unique_day(tup[i][1],possible_birthdays)==True:
            return True
    return False