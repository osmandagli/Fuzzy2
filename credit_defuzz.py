import skfuzzy as fuzz
import numpy as np 
import matplotlib.pyplot as plt

def credit_defuzz(int_tuple, inc_tuple, house_tuple, app_tuple):
    
    x_credit_amount = np.arange(0, 525, 25)
    
    ca_vl = fuzz.membership.trimf(x_credit_amount, [0, 0, 125])
    ca_low = fuzz.membership.trimf(x_credit_amount, [0, 125, 250])
    ca_medium = fuzz.membership.trimf(x_credit_amount, [125, 250, 375])
    ca_high = fuzz.membership.trimf(x_credit_amount, [250, 375, 500])
    ca_vh = fuzz.membership.trimf(x_credit_amount, [375, 500, 500])
    
    int_fit = []
    for value in int_tuple[1]:
        int_fit.append(fuzz.interp_membership(int_tuple[0], value, int_tuple[2]))
    
    d = ['low', 'medium', 'high']
    int_dict = dict(zip(d, int_fit))
    
    inc_fit = []
    for value in inc_tuple[1]:
        inc_fit.append(fuzz.interp_membership(inc_tuple[0], value, inc_tuple[2]))
    
    d = ['low', 'medium', 'high', 'vh']
    inc_dict = dict(zip(d, inc_fit))
    
    house_fit = []
    for value in house_tuple[1]:
        house_fit.append(fuzz.interp_membership(house_tuple[0], value, house_tuple[2]))
    
    d = ['vl', 'low', 'medium', 'high', 'vh']
    house_dict = dict(zip(d, house_fit))
    
    app_fit = []
    for value in app_tuple[1]:
        app_fit.append(fuzz.interp_membership(app_tuple[0], value, app_tuple[2]))
    
    d = ['low', 'medium', 'high']
    app_dict = dict(zip(d, app_fit))
    
    AND = min
    OR = max
    
    rule_n1 = AND(inc_dict['low'], int_dict['medium']) * ca_vl
    rule_n2 = AND(inc_dict['low'], int_dict['high']) * ca_vl
    rule_n4 = app_dict['low'] * ca_vl
    rule_n5 = house_dict['vl'] * ca_vl
    
    rule_n3 = AND(inc_dict['medium'], int_dict['high']) * ca_low  
    rule_n6 = AND(app_dict['medium'], house_dict['vl']) * ca_low    
    rule_n7 = AND(app_dict['medium'], house_dict['low']) * ca_low
    rule_n11 = AND(app_dict['high'], house_dict['vl']) * ca_low
    
    rule_n8 = AND(app_dict['medium'], house_dict['medium']) * ca_medium
    rule_n12 = AND(app_dict['high'], house_dict['low']) * ca_medium
    
    rule_n9 = AND(app_dict['medium'], house_dict['high']) * ca_high
    rule_n10 = AND(app_dict['medium'], house_dict['vh']) * ca_high
    rule_n13 = AND(app_dict['high'], house_dict['medium']) * ca_high
    rule_n14 = AND(app_dict['high'], house_dict['high']) * ca_high
    
    rule_n15 = AND(app_dict['high'], house_dict['vh']) * ca_vh
    
    out_credit_vl = [max(a,b,c,d) for a,b,c,d in zip(rule_n1,rule_n2,rule_n4,rule_n5)]
    out_credit_low = [max(a,b,c,d) for a,b,c,d in zip(rule_n3,rule_n6,rule_n7,rule_n11)]
    out_credit_medium = [max(a,b) for a,b in zip(rule_n8,rule_n12)]
    out_credit_high = [max(a,b,c,d) for a,b,c,d in zip(rule_n9,rule_n10,rule_n13,rule_n14)]
    out_credit_vh = rule_n15
    
    credit_out = np.array([max(a,b,c,d,e) for a,b,c,d,e in zip(out_credit_vl,out_credit_low,out_credit_medium,out_credit_high,out_credit_vh)])
    
    defuzz_cen = fuzz.defuzz(x_credit_amount, credit_out, 'centroid')
    
    print(defuzz_cen)
    
    return defuzz_cen
    
    
    
    
    
    
    
    
    
    
    
    
    