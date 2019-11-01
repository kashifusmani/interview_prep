from __future__ import division
from math import floor


def cal_zak_year(principle_amt, years):
    zakat_amount_total = 0
    principle_amount_rem = principle_amt
    amortized_principle_by_year = principle_amt / years
    amortized_principle_total = amortized_principle_by_year
    for i in range(0, years):
        zak_amount_this = amortized_principle_total * 0.025
        amortized_principle_total = amortized_principle_total - zak_amount_this + amortized_principle_by_year

        zakat_amount_total += zak_amount_this
        principle_amount_rem -= zak_amount_this
    assert floor(principle_amt) == floor(principle_amount_rem + zakat_amount_total)
    return zakat_amount_total, principle_amount_rem


def test_cal_zak_year():
    years = 5
    principle_amt = 1000
    #year 1: amount = 200, zakat = 5 , remaining = 195
    #year 2: amount = 200 + 195, zakat = 9.875, remaining = 385.125
    #year 3: amount = 200 + 385.125, zakat = 14.628125, remaining = 570.496875
    #year 4: amount = 200 + 570.496875, zakat = 19.262421875, remaining = 751.234453125
    #year 5: amount = 200 + 751.234453125, zakat = 23.780861328125, remaining = 927.453591796875
    zakat_total, principle_rem = cal_zak_year(principle_amt, years)
    assert zakat_total == 72.546408203125
    assert floor(principle_rem) == floor(927.453591796875)
    assert floor(zakat_total + principle_rem) == floor(principle_amt)


if __name__ == '__main__':
    test_cal_zak_year()

    initial_principle_amount = 55000
    years = 1992 - 1972
    zak_1992, principle_1992 = cal_zak_year(initial_principle_amount, years)

    #assuming principle_rem is the only amount remaining at this point
    #year 2004
    raj_money = 70000 #Given in 2004
    dubai_apt_money = 37500 #purchased in 2005
    td_usd_money = 100000 #transferred in 2009
    year_2004_balance = raj_money + td_usd_money + dubai_apt_money + principle_1992

    years = 2004 - 1992
    zak_2004, principle_2004 = cal_zak_year(year_2004_balance, years)
    #print(zak_2004, principle_2004)


    years = 2005 - 2004
    year_2005_balance = principle_2004 - raj_money

    zak_2005, principle_2005 = cal_zak_year(year_2005_balance, years)

    years = 2006 - 2005
    year_2006_balance = principle_2005 - dubai_apt_money
    zak_2006, principle_2006 = cal_zak_year(year_2006_balance, years)

    #to 2019
    years = 2019 - 2006
    year_2019_balance = principle_2006 #+ plus may be a 5-6K CAD per year may be
    zak_2019, principle_2019 = cal_zak_year(year_2019_balance, years)

    total_zak = zak_1992 + zak_2004 + zak_2005 + zak_2006 + zak_2019
    print(total_zak)
    print(principle_2019)



