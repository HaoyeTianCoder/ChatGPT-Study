def unique_month(month, possible_birthdays):
    def map(fn,seq):
        if seq == ():
            return ()
        else:
            return (fn(seq[0]),) + map(fn,seq[1:])
    months = map(lambda x: x[0], possible_birthdays)
    filter2 = filter(lambda x:x == month, months)
    tup2 = tuple(filter2)
    return len(tup2) == 1