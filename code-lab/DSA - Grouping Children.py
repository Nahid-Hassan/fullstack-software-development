# For 4 children of ages 3 years 2 months, 3 years 8 months, 4 years 6 months and 5 years, what is the smallest number of such groups that for any two children in the same group their ages differ by at most one year?

children_ages = [3.2, 3.2, 3.3, 3.8, 4.6, 5.0]


def points_cover_sorted(points: list) -> set:
    """
        Grouping Children:

        For 4 children of ages 3 years 2 months, 3 years 8 months, 4 years 6 months and 5 years, what is the smallest number of such groups that for any two children in the same group their ages differ by at most one year?

        We can assume 3 year 2 months => 3.2, 3 year 8 month => 3.8 and set it on the line.
                3.2  3.8
        |--------|----|------------------------------------
    """
    points.sort()

    result = []
    i = 0
    while i < len(points):
        point = points[i]    
        temp = []
        temp.append(point)
        i += 1
        while i < len(points) and (point + 1.0) >= points[i]:
            temp.append(points[i])
            i += 1
        result.append(temp)
    return result

out = points_cover_sorted(children_ages)
print(out)
print(len(out))
