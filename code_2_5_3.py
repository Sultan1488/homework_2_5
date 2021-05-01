spendings = [140, 30, 999, 145, 538, 878, 901, 613, 471, 286, 147, 90]
income = [300, 40, 0, 4000, 8911, 73, 85, 0, 9000, 941, 658, 190]


def func(list_1, list_2):
    coeff_year = 0
    new_list = []
    for month in range(12):
        try:
            coeff = list_1[month] / list_2[month]
            new_list.append(coeff)
        except ZeroDivisionError:
            coeff = 0
            new_list.append(coeff)
        finally:
            coeff_year += coeff
    monthly_coefficient = {f'month {i + 1}': new_list[i] for i in range(12)}
    print(monthly_coefficient)
    print(f'Coefficient for the year: {coeff_year / 12}')
func(spendings, income)
