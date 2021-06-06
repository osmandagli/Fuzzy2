import skfuzzy as fuzz
import numpy as np 
import matplotlib.pyplot as plt

def house_defuzz(market_values, x_market_value_house, location_values, x_location_house, input_mvh, input_loc):
    
    x_house = np.arange(0, 11, 1)
    
    house_vl = fuzz.membership.trimf(x_house, [0,0,3])
    house_low = fuzz.membership.trimf(x_house, [0,3,6])
    house_medium = fuzz.membership.trimf(x_house, [2,5,8])
    house_high = fuzz.membership.trimf(x_house, [4,7,10])
    house_vh = fuzz.membership.trimf(x_house, [7,10,10])
    
    market_fit = []
    for value in market_values:
        market_fit.append(fuzz.interp_membership(x_market_value_house, value, input_mvh))
    
    d = ['low', 'medium', 'high', 'vh']
    mvh_dict = dict(zip(d, market_fit))
    #print(temp_dict)
    
    loc_fit = []
    for loc in location_values:
        loc_fit.append(fuzz.interp_membership(x_location_house, loc, input_loc))
    d = ['bad', 'fair', 'exc']
    
    loc_dict = dict(zip(d, loc_fit))
    
    AND = min
    OR = max
    
    rule_n3 = AND(loc_dict['bad'], mvh_dict['low']) * house_vl
    
    rule_n1 = mvh_dict['low'] * house_low
    rule_n2 = loc_dict['bad'] * house_low
    rule_n4 = AND(loc_dict['bad'], mvh_dict['medium']) * house_low
    rule_n7 = AND(loc_dict['fair'], mvh_dict['low']) * house_low
    
    rule_n5 = AND(loc_dict['bad'], mvh_dict['high']) * house_medium
    rule_n8 = AND(loc_dict['fair'], mvh_dict['medium']) * house_medium
    rule_n11 = AND(loc_dict['exc'] , mvh_dict['low']) * house_medium
    
    rule_n9 = AND(loc_dict['fair'], mvh_dict['high']) * house_high
    rule_n12 = AND(loc_dict['exc'] , mvh_dict['medium']) * house_high
    rule_n6 = AND(loc_dict['bad'], mvh_dict['vh']) * house_high
    
    rule_n10 = AND(loc_dict['fair'] , mvh_dict['vh']) * house_vh
    rule_n13 = AND(loc_dict['exc'] , mvh_dict['high']) * house_vh
    rule_n14 = AND(loc_dict['exc'] , mvh_dict['vh']) * house_vh
    
    out_house_vl = rule_n3
    out_house_low = [max(a,b,c,d) for a,b,c,d in zip(rule_n1,rule_n2,rule_n4,rule_n7)] 
    out_house_medium = [max(a,b,c) for a,b,c in zip(rule_n5,rule_n8,rule_n11)] 
    out_house_high = [max(a,b,c) for a,b,c in zip(rule_n6,rule_n9,rule_n12)] 
    out_house_vh = [max(a,b,c) for a,b,c in zip(rule_n10,rule_n13,rule_n14)] 
    
    house_out = np.array([max(a,b,c,d,e) for a,b,c,d,e in zip(out_house_vl, out_house_low, out_house_medium, out_house_high, out_house_vh)])
    
    defuzz_lom = fuzz.defuzz(x_house, house_out, 'lom')
    
    #plt.plot(x_house, house_out)
    #plt.plot(x_house, out_house_high)
    
    return defuzz_lom
    