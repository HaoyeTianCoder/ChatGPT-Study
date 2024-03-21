def unique_day(day, possible_birthdays):
    a= tuple(filter(lambda birthday: day == birthday[1], possible_birthdays))
    return (len(a) ==1) 