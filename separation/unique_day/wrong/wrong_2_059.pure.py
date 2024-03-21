def unique_day(day, pb):
    n = len(pb)
    for i in range(n):
        if day == pb[i][1]:
            k = pb[i+1:]
            for j in range(len(k)):
                if day == k[j][1]:
                    return False
    return True