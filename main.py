import pandas as pd

def Buying_price(acc,unacc,good,vgood,df_Training):
    a = {}
    # p of Buying  pricesas(A) With acc

    A_vhigh_acc = ((df_Training['g'].values == 'acc') & (df_Training['a'].values == 'vhigh')).sum()
    p_A_vhigh_acc = A_vhigh_acc / acc
    a["p_vhigh_acc"] = p_A_vhigh_acc

    A_high_acc = ((df_Training['g'].values == 'acc') & (df_Training['a'].values == 'high')).sum()
    p_A_high_acc = A_high_acc / acc
    a["p_high_acc"] = p_A_high_acc

    A_med_acc = ((df_Training['g'].values == 'acc') & (df_Training['a'].values == 'med')).sum()
    p_A_med_acc = A_med_acc / acc
    a["p_med_acc"] = p_A_med_acc

    A_low_acc = ((df_Training['g'].values == 'acc') & (df_Training['a'].values == 'low')).sum()
    p_A_low_acc = A_low_acc / acc
    a["p_low_acc"] = p_A_low_acc

    # p of pricesas (A) With unacc

    A_vhigh_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['a'].values == 'vhigh')).sum()
    p_A_vhigh_unacc = A_vhigh_unacc / unacc
    a["p_vhigh_unacc"] = p_A_vhigh_unacc


    A_high_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['a'].values == 'high')).sum()
    p_A_high_unacc = A_high_unacc / unacc
    a["p_high_unacc"] = p_A_high_unacc


    A_med_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['a'].values == 'med')).sum()
    p_A_med_unacc = A_med_unacc / unacc
    a["p_med_unacc"] = p_A_med_unacc


    A_low_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['a'].values == 'low')).sum()
    p_A_low_unacc = A_low_unacc / unacc
    a["p_low_unacc"] = p_A_low_unacc


    # p of pricesas (A) With good

    A_vhigh_good = ((df_Training['g'].values == 'good') & (df_Training['a'].values == 'vhigh')).sum()
    p_A_vhigh_good = A_vhigh_good / good
    a["p_vhigh_good"] = p_A_vhigh_good

    A_high_good = ((df_Training['g'].values == 'good') & (df_Training['a'].values == 'high')).sum()
    p_A_high_good = A_high_good / good
    a["p_high_good"] = p_A_high_good


    A_med_good = ((df_Training['g'].values == 'good') & (df_Training['a'].values == 'med')).sum()
    p_A_med_good = A_med_good / good
    a["p_med_good"] = p_A_med_good


    A_low_good = ((df_Training['g'].values == 'good') & (df_Training['a'].values == 'low')).sum()
    p_A_low_good = A_low_good / good
    a["p_low_good"] = p_A_low_good

    # p of pricesas (A) With vgood

    A_vhigh_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['a'].values == 'vhigh')).sum()
    p_A_vhigh_vgood = A_vhigh_vgood / vgood
    a["p_vhigh_vgood"] = p_A_vhigh_vgood

    A_high_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['a'].values == 'high')).sum()
    p_A_high_vgood = A_high_vgood / vgood
    a["p_high_vgood"] = p_A_high_vgood

    A_med_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['a'].values == 'med')).sum()
    p_A_med_vgood = A_med_vgood / vgood
    a["p_med_vgood"] = p_A_med_vgood

    A_low_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['a'].values == 'low')).sum()
    p_A_low_vgood = A_low_vgood / vgood
    a["p_low_vgood"] = p_A_low_vgood
    return a

def Maintenance_Price(acc,unacc,good,vgood,df_Training):
    b = {}
    # p of Maintenance_Price(b) With acc

    vhigh_acc = ((df_Training['g'].values == 'acc') & (df_Training['b'].values == 'vhigh')).sum()
    p_vhigh_acc = vhigh_acc / acc
    b["p_vhigh_acc"] = p_vhigh_acc

    high_acc = ((df_Training['g'].values == 'acc') & (df_Training['b'].values == 'high')).sum()
    p_b_high_acc = high_acc / acc
    b["p_high_acc"] = p_b_high_acc

    b_med_acc = ((df_Training['g'].values == 'acc') & (df_Training['b'].values == 'med')).sum()
    p_b_med_acc = b_med_acc / acc
    b["p_med_acc"] = p_b_med_acc

    b_low_acc = ((df_Training['g'].values == 'acc') & (df_Training['b'].values == 'low')).sum()
    p_b_low_acc = b_low_acc / acc
    b["p_low_acc"] = p_b_low_acc

    # p of pricesas (A) With unacc

    p_vhigh_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['b'].values == 'vhigh')).sum()
    p_p_vhigh_unacc = p_vhigh_unacc / unacc
    b["p_vhigh_unacc"] = p_p_vhigh_unacc


    A_high_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['b'].values == 'high')).sum()
    p_A_high_unacc = A_high_unacc / unacc
    b["p_high_unacc"] = p_A_high_unacc


    A_med_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['b'].values == 'med')).sum()
    p_A_med_unacc = A_med_unacc / unacc
    b["p_med_unacc"] = p_A_med_unacc


    A_low_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['b'].values == 'low')).sum()
    p_A_low_unacc = A_low_unacc / unacc
    b["p_low_unacc"] = p_A_low_unacc


    # p of pricesas (A) With good

    A_vhigh_good = ((df_Training['g'].values == 'good') & (df_Training['b'].values == 'vhigh')).sum()
    p_A_vhigh_good = A_vhigh_good / good
    b["p_vhigh_good"] = p_A_vhigh_good

    A_high_good = ((df_Training['g'].values == 'good') & (df_Training['b'].values == 'high')).sum()
    p_A_high_good = A_high_good / good
    b["p_high_good"] = p_A_high_good


    A_med_good = ((df_Training['g'].values == 'good') & (df_Training['b'].values == 'med')).sum()
    p_A_med_good = A_med_good / good
    b["p_med_good"] = p_A_med_good


    A_low_good = ((df_Training['g'].values == 'good') & (df_Training['b'].values == 'low')).sum()
    p_A_low_good = A_low_good / good
    b["p_low_good"] = p_A_low_good

    # p of pricesas (A) With vgood

    A_vhigh_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['b'].values == 'vhigh')).sum()
    p_A_vhigh_vgood = A_vhigh_vgood / vgood
    b["p_vhigh_vgood"] = p_A_vhigh_vgood

    A_high_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['b'].values == 'high')).sum()
    p_A_high_vgood = A_high_vgood / vgood
    b["p_high_vgood"] = p_A_high_vgood

    A_med_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['b'].values == 'med')).sum()
    p_A_med_vgood = A_med_vgood / vgood
    b["p_med_vgood"] = p_A_med_vgood

    A_low_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['b'].values == 'low')).sum()
    p_A_low_vgood = A_low_vgood / vgood
    b["p_low_vgood"] = p_A_low_vgood
    return b


def NumberOfDoors(acc,unacc,good,vgood,df_Training):
    c = {}
    # p of Maintenance_Price(c) With acc   2, 3, 4, 5more

    two_acc = ((df_Training['g'].values == 'acc') & (df_Training['c'].values == '2')).sum()
    p_two_acc = two_acc / acc
    c["p_2_acc"] = p_two_acc

    three_acc = ((df_Training['g'].values == 'acc') & (df_Training['c'].values == '3')).sum()
    p_three_acc = three_acc / acc
    c["p_3_acc"] = p_three_acc

    four_acc = ((df_Training['g'].values == 'acc') & (df_Training['c'].values == '4')).sum()
    p_four_acc = four_acc / acc
    c["p_4_acc"] = p_four_acc

    more_acc = ((df_Training['g'].values == 'acc') & (df_Training['c'].values == '5more')).sum()
    p_more_acc = more_acc/ acc
    c["p_5more_acc"] = p_more_acc

    # p  of Maintenance_Price(c) With unacc

    two_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['c'].values == '2')).sum()
    p_two_unacc = two_unacc / unacc
    c["p_2_unacc"] = p_two_unacc

    three_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['c'].values == '3')).sum()
    p_three_unacc = three_unacc / unacc
    c["p_3_unacc"] = p_three_unacc

    four_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['c'].values == '4')).sum()
    p_four_unacc = four_unacc / unacc
    c["p_4_unacc"] = p_four_acc

    more_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['c'].values == '5more')).sum()
    p_more_unacc = more_unacc / unacc
    c["p_5more_unacc"] = p_more_acc


    # p of pricesas (c) With good

    two_good = ((df_Training['g'].values == 'good') & (df_Training['c'].values == '2')).sum()
    p_two_good = two_good / good
    c["p_2_good"] = p_two_good

    three_good = ((df_Training['g'].values == 'good') & (df_Training['c'].values == '3')).sum()
    p_three_good = three_good / good
    c["p_3_good"] = p_three_good

    fourgood = ((df_Training['g'].values == 'good') & (df_Training['c'].values == '4')).sum()
    p_four_good = fourgood / good
    c["p_4_good"] = p_four_good

    more_good= ((df_Training['g'].values == 'good') & (df_Training['c'].values == '5more')).sum()
    p_more_good = more_good / good
    c["p_5more_good"] = p_more_good

    # p of pricesas (c) With vgood

    two_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['c'].values == '2')).sum()
    p_two_vgood = two_vgood / vgood
    c["p_2_vgood"] = p_two_vgood

    three_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['c'].values == '3')).sum()
    p_three_vgood = three_vgood / vgood
    c["p_3_vgood"] = p_three_vgood

    four_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['c'].values == '4')).sum()
    p_four_vgood = four_vgood / vgood
    c["p_4_vgood"] = p_four_vgood

    more_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['c'].values == '5more')).sum()
    p_more_vgood = more_vgood / vgood
    c["p_5more_vgood"] = p_more_vgood
    return c


def Capacityintermsofpersonstocarry(acc,unacc,good,vgood,df_Training):
    d = {}
    # p of Maintenance_Price(d) With acc   2, 4, more

    two_acc = ((df_Training['g'].values == 'acc') & (df_Training['d'].values == '2')).sum()
    p_two_acc = two_acc / acc
    d["p_2_acc"] = p_two_acc


    four_acc = ((df_Training['g'].values == 'acc') & (df_Training['d'].values == '4')).sum()
    p_four_acc = four_acc / acc
    d["p_4_acc"] = p_four_acc

    more_acc = ((df_Training['g'].values == 'acc') & (df_Training['d'].values == 'more')).sum()
    p_more_acc = more_acc/ acc
    d["p_more_acc"] = p_more_acc



    # p  of Maintenance_Price(d) With unacc

    two_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['d'].values == '2')).sum()
    p_two_unacc = two_unacc / unacc
    d["p_2_unacc"] = p_two_unacc



    four_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['d'].values == '4')).sum()
    p_four_unacc = four_unacc / unacc
    d["p_4_unacc"] = p_four_acc

    more_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['d'].values == 'more')).sum()
    p_more_unacc = more_unacc / unacc
    d["p_more_unacc"] = p_more_acc


    # p of pricesas (d) With good

    two_good = ((df_Training['g'].values == 'good') & (df_Training['d'].values == '2')).sum()
    p_two_good = two_good / good
    d["p_2_good"] = p_two_good



    fourgood = ((df_Training['g'].values == 'good') & (df_Training['d'].values == '4')).sum()
    p_four_good = fourgood / good
    d["p_4_good"] = p_four_good

    more_good= ((df_Training['g'].values == 'good') & (df_Training['d'].values == 'more')).sum()
    p_more_good = more_good / good
    d["p_more_good"] = p_more_good

    # p of pricesas (d) With vgood

    two_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['d'].values == '2')).sum()
    p_two_vgood = two_vgood / vgood
    d["p_2_vgood"] = p_two_vgood


    four_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['d'].values == '4')).sum()
    p_four_vgood = four_vgood / vgood
    d["p_4_vgood"] = p_four_vgood

    more_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['d'].values == 'more')).sum()
    p_more_vgood = more_vgood / vgood
    d["p_more_vgood"] = p_more_vgood
    return d


def Thesizeofluggageboot(acc,unacc,good,vgood,df_Training):
    e = {}
    # p of Maintenance_Price(e) With acc     small, med, big

    small_acc = ((df_Training['g'].values == 'acc') & (df_Training['e'].values == 'small')).sum()
    p_small_acc = small_acc / acc
    e["p_small_acc"] = p_small_acc

    big_acc = ((df_Training['g'].values == 'acc') & (df_Training['e'].values == 'big')).sum()
    p_big_acc = big_acc / acc
    e["p_big_acc"] = p_big_acc

    med_acc = ((df_Training['g'].values == 'acc') & (df_Training['e'].values == 'med')).sum()
    p_med_acc = med_acc / acc
    e["p_med_acc"] = p_med_acc



    # p of pricesas (A) With unacc

    small_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['e'].values == 'small')).sum()
    p_small_unacc = small_unacc / unacc
    e["p_small_unacc"] = p_small_unacc

    big_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['e'].values == 'big')).sum()
    p_big_unacc = big_unacc / unacc
    e["p_big_unacc"] = p_big_unacc

    med_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['e'].values == 'med')).sum()
    p_med_unacc = med_unacc / unacc
    e["p_med_unacc"] = p_med_unacc


    # p of pricesas (A) With good

    small_good = ((df_Training['g'].values == 'good') & (df_Training['e'].values == 'small')).sum()
    p_small_good = small_good / good
    e["p_small_good"] = p_small_good

    big_good = ((df_Training['g'].values == 'good') & (df_Training['e'].values == 'big')).sum()
    p_big_good = big_good / good
    e["p_big_good"] = p_big_good

    med_good = ((df_Training['g'].values == 'good') & (df_Training['e'].values == 'med')).sum()
    p_med_good = med_good / good
    e["p_med_good"] = p_med_good



    # p of pricesas (A) With vgood

    small_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['e'].values == 'small')).sum()
    p_small_vgood = small_vgood / vgood
    print(p_small_vgood)
    e["p_small_vgood"] = p_small_vgood

    big_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['e'].values == 'big')).sum()
    p_big_vgood = big_vgood / vgood
    e["p_big_vgood"] = p_big_vgood

    A_med_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['e'].values == 'med')).sum()
    p_A_med_vgood = A_med_vgood / vgood
    e["p_med_vgood"] = p_A_med_vgood
    return e


def EstimatedSafetofTheCar(acc,unacc,good,vgood,df_Training,):
    f = {}
    # p of Maintenance_Price(f) With acc


    high_acc = ((df_Training['g'].values == 'acc') & (df_Training['f'].values == 'high')).sum()
    p_high_acc = high_acc / acc
    f["p_high_acc"] = p_high_acc

    med_acc = ((df_Training['g'].values == 'acc') & (df_Training['f'].values == 'med')).sum()
    p_med_acc = med_acc / acc
    f["p_med_acc"] = p_med_acc

    low_acc = ((df_Training['g'].values == 'acc') & (df_Training['f'].values == 'low')).sum()
    p_low_acc = low_acc / acc
    f["p_low_acc"] = p_low_acc

    # p of pricesas (A) With unacc


    high_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['f'].values == 'high')).sum()
    p_high_unacc = high_unacc / unacc
    f["p_high_unacc"] = p_high_unacc


    med_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['f'].values == 'med')).sum()
    p_med_unacc = med_unacc / unacc
    f["p_med_unacc"] = p_med_unacc


    low_unacc = ((df_Training['g'].values == 'unacc') & (df_Training['f'].values == 'low')).sum()
    p_low_unacc = low_unacc / unacc
    f["p_low_unacc"] = p_low_unacc


    # p of pricesas (A) With good


    high_good = ((df_Training['g'].values == 'good') & (df_Training['f'].values == 'high')).sum()
    p_high_good = high_good / good
    f["p_high_good"] = p_high_good


    med_good = ((df_Training['g'].values == 'good') & (df_Training['f'].values == 'med')).sum()
    p_med_good = med_good / good
    f["p_med_good"] = p_med_good


    low_good = ((df_Training['g'].values == 'good') & (df_Training['f'].values == 'low')).sum()
    p_low_good = low_good / good
    f["p_low_good"] = p_low_good

    # p of pricesas (A) With vgood

    high_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['f'].values == 'high')).sum()
    p_high_vgood =high_vgood / vgood
    f["p_high_vgood"] = p_high_vgood

    med_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['f'].values == 'med')).sum()
    p_med_vgood = med_vgood / vgood
    f["p_med_vgood"] = p_med_vgood

    low_vgood = ((df_Training['g'].values == 'vgood') & (df_Training['f'].values == 'low')).sum()
    p_low_vgood = low_vgood / vgood
    f["p_low_vgood"] = p_low_vgood
    return f

def getTheClass(item,a,b,c,d,e,f,acc,unacc,good,vgood):
    Class={}

    #p(acc)
    buying_acc="p_"+item[0]+"_acc"
    p_buying_acc=a[buying_acc]


    Maintenance_acc="p_"+item[1]+"_acc"
    p_Maintenance_acc=b[Maintenance_acc]


    door_acc = "p_" + item[2] + "_acc"
    p_door_acc = c[door_acc]

    persons_acc = "p_" + item[3] + "_acc"
    p_persons_acc = d[persons_acc]



    luggage_acc = "p_" + item[4] + "_acc"
    p_luggage_acc = e[luggage_acc]

    safety_acc = "p_" + item[5] + "_acc"
    p_safety_acc = f[safety_acc]

    acc=p_safety_acc*p_luggage_acc*p_persons_acc*p_door_acc*p_Maintenance_acc*p_buying_acc*(acc/431)
    Class["acc"]=acc
####//////////////////////////////////////////////////////////////////////////////////////////////////////////

    #p(unacc)
    buying_unacc="p_"+item[0]+"_unacc"
    p_buying_unacc=a[buying_unacc]


    Maintenance_unacc="p_"+item[1]+"_unacc"
    p_Maintenance_unacc=b[Maintenance_unacc]


    door_unacc = "p_" + item[2] + "_unacc"
    p_door_unacc = c[door_unacc]

    persons_unacc = "p_" + item[3] + "_unacc"
    p_persons_unacc = d[persons_unacc]



    luggage_unacc = "p_" + item[4] + "_unacc"
    p_luggage_unacc = e[luggage_unacc]

    safety_unacc = "p_" + item[5] + "_unacc"
    p_safety_unacc = f[safety_unacc]

    unacc=p_safety_unacc*p_luggage_unacc*p_persons_unacc*p_door_unacc*p_Maintenance_unacc*p_buying_unacc*(unacc/431)
    Class["unacc"] = unacc

####//////////////////////////////////////////////////////////////////////////////////////////////////////////

    #p(good)
    buying_good="p_"+item[0]+"_good"
    p_buying_good=a[buying_good]


    Maintenance_good="p_"+item[1]+"_good"
    p_Maintenance_good=b[Maintenance_good]


    door_good = "p_" + item[2] + "_good"
    p_door_good = c[door_good]

    persons_good = "p_" + item[3] + "_good"
    p_persons_good = d[persons_good]



    luggage_good = "p_" + item[4] + "_good"
    p_luggage_good = e[luggage_good]

    safety_good = "p_" + item[5] + "_good"
    p_safety_good = f[safety_good]

    good=p_safety_good*p_luggage_good*p_persons_good*p_door_good*p_Maintenance_good*p_buying_good*(good/431)
    Class["good"] = good

    ##///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # p(vgood)
    buying_vgood = "p_" + item[0] + "_vgood"
    p_buying_vgood= a[buying_vgood]

    Maintenance_vgood= "p_" + item[1] + "_vgood"
    p_Maintenance_vgood= b[Maintenance_vgood]

    door_vgood = "p_" + item[2] + "_vgood"
    p_door_vgood = c[door_vgood]

    persons_vgood= "p_" + item[3] + "_vgood"
    p_persons_vgood= d[persons_vgood]

    luggage_vgood= "p_" + item[4] + "_vgood"
    p_luggage_vgood = e[luggage_vgood]

    safety_vgood = "p_" + item[5] + "_vgood"
    p_safety_vgood = f[safety_vgood]

    vgood = p_safety_vgood * p_luggage_vgood * p_persons_vgood * p_door_vgood * p_Maintenance_vgood * p_buying_vgood * (
                vgood / 431)
    Class["vgood"] = vgood

    return Class


def Naive (df_Training,df_Testing_copy,df_Testing):
    acc = (df_Training['g'].values == 'acc').sum()
    unacc = (df_Training['g'].values == 'unacc').sum()
    good = (df_Training['g'].values == 'good').sum()
    vgood = (df_Training['g'].values == 'vgood').sum()

    a = Buying_price(acc, unacc, good, vgood, df_Training)
    b = Maintenance_Price(acc, unacc, good, vgood, df_Training)
    c = NumberOfDoors(acc, unacc, good, vgood, df_Training)
    d = Capacityintermsofpersonstocarry(acc, unacc, good, vgood, df_Training)
    e = Thesizeofluggageboot(acc, unacc, good, vgood, df_Training)
    f = EstimatedSafetofTheCar(acc, unacc, good, vgood, df_Training)
    #    print(a)
    #   print(b)
    #  print(c)
    # print(d)
    # print(e)
    # print(f)

    count = 0
    len = 0
    for i in range(431):
        item = [df_Testing_copy.values[i - 1, j] for j in range(0, 6)]
        Class = getTheClass(item, a, b, c, d, e, f, acc, unacc, good, vgood)
        max_class = max(Class, key=Class.get)
        df_Testing_copy.values[i - 1, -1] = max_class
        if (df_Testing_copy.values[i - 1, -1] == df_Testing.values[i - 1, -1]):
            count += 1
        len += 1

    accurancy = (count / len) * 100
    print("accurancy of Naive=", accurancy)


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def transform (df):
    df_copy=df.copy()
    df_copy['a'] = df_copy['a'].map({'vhigh': 4, 'high': 3,  'med':2, 'low': 1})
    df_copy['b'] = df_copy['b'].map({'vhigh': 4, 'high': 3, 'med': 2, 'low': 1})
    df_copy['c'] = df_copy['c'].map({'5more': 5, '3': 3, '2': 2, '4': 4})
    df_copy['d'] = df_copy['d'].map({'more': 5, '2': 2, '4': 4})
    df_copy['e'] = df_copy['e'].map({'small': 3, 'med': 2, 'big': 1})
    df_copy['f'] = df_copy['f'].map({'high': 3, 'med': 2, 'low': 1})

    return df_copy



def ManhattanDistance(x, y):
    S = 0;
    for i in range(len(x)):
        S += abs(int(x[i])- int(y[i]))

    return S

def getClass(item,df_Training):
    distance= {}
    index={}
    for i in range(1296):
        item1 = [df_Training.values[i - 1, j] for j in range(0, 6)]
        d=ManhattanDistance(item1, item)
        distance[i]=d
    res=[] #to get the indixes
    while(len(res)<5):
        temp = min(distance.values())
        r=[key for key in distance if distance[key] == temp]
        for k in r:
            res.append(k)
            distance.pop(k)
    classes=[]
    for i in range(5):
        ind=res[i]
        Class = df_Training.values[i - 1, 6]
        classes.append(Class)

    predict= max(set(classes), key = classes.count)
    return predict




   # C = df_Training.values[227 - 1, 6]
    #print("Class", Class)
    #print("item1",item1)


if __name__ == '__main__':

    df = pd.read_csv('car.data.csv', names=["a", "b", "c", "d", "e", "f", "g"], header=0)

    df_Training= df.iloc[:1296, :]
    df_Testing= df.iloc[1297:, :]
    df_Testing_copy = df_Testing.copy()
    df_Testing_copy['g'] = 'null'


    Naive (df_Training,df_Testing_copy,df_Testing)

"""
    df_copy =transform(df)
    df_Training = df_copy.iloc[:1296, :]
    df_Testing = df_copy.iloc[1297:, :]
    df_Testing_copy = df_Testing.copy()
    df_Testing_copy['g'] = 'null'
   # print(df_Training.head(227))
    print(df_Testing_copy.head(5))
    for i in range(431):
        item = [df_Testing_copy.values[i - 1, j] for j in range(0, 6)]
        Class=getClass(item,df_Training)

        df_Testing_copy.values[i - 1, 6]=Class
    print (df_Testing_copy.head(5))

"""









