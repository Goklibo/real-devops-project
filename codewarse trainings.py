def bacteria_growth(days):

    result = [5]

    if days <= 0:
        return []

    for i in range(days - 1):
        next_growth = result[-1] * 2

        if next_growth >= 1000:
            next_growth = 1000

            result.append(next_growth)


        return result


