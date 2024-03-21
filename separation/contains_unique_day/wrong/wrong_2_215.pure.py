def contains_unique_day(month, possible_birthdays):
    a = map(lambda x : x[0], possible_birthdays)
    b = map(lambda x : x[1], possible_birthdays)
    k = ()
    for i in range(len(a)):
        if month == a[i]:
                k += (b[i],)
    for f in range(len(k)):
        if len(filter(lambda x: x == k[f],b)) == 1:
            return True
    return False