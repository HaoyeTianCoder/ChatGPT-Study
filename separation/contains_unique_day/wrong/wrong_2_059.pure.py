def contains_unique_day(month, pb):
    new_pb = tuple(filter( lambda x: x[0] == month, pb))
    n = len(new_pb)
    for i in range(n):
        day = new_pb[i][1]
        if unique_day( day, pb):
            return True
    return False