def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    q = 100 / (100 - percentLossByMonth)
    months = 0
    saved_money = 0
    while (startPriceOld + saved_money) <= startPriceNew:
        saved_money += savingperMonth
        startPriceOld = startPriceOld / 100 * (100 - percentLossByMonth)
        startPriceNew = startPriceNew / 100 * (100 - percentLossByMonth)
        months += 1
    return [months, startPriceNew - saved_money]

print(nbMonths(2000, 8000, 1000, 1.5))