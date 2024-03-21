def unique_day(day, possible_birthdays):
    def map(fn,seq):
        if seq == ():
            return ()
        else:
            return (fn(seq[0]),) + map(fn,seq[1:])
    days = map(lambda x: x[1], possible_birthdays)
    filter1 = filter(lambda x:x == day, days)
    tup = tuple(filter1)
    return len(tup) == 1