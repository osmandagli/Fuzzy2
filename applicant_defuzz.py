import skfuzzy as fuzz
import numpy as np 
import matplotlib.pyplot as plt

def applicant_defuzz(asset_values, x_asset_application, income_values, x_income, input_aa, input_inc):
    x_applicant = np.arange(0, 11, 1)

    app_low = fuzz.membership.trapmf(x_applicant, [0, 0, 2, 4])
    app_medium = fuzz.membership.trimf(x_applicant, [2, 5, 8])
    app_high = fuzz.membership.trapmf(x_applicant, [6, 8, 10, 10])

    asset_fit = []
    for applicant in asset_values:
        asset_fit.append(fuzz.interp_membership(x_asset_application, applicant, input_aa))

    d = ['low', 'medium', 'high']
    asset_dict = dict(zip(d, asset_fit))
    
    
    inc_fit = []
    for applicant in income_values:
        inc_fit.append(fuzz.interp_membership(x_income, applicant, input_inc))

    d = ['low', 'medium', 'high', 'vh']
    income_dict = dict(zip(d, inc_fit))

    AND = min
    OR = max
    #AND(loc_dict['bad'], mvh_dict['low']) * house_vl
    
    rule_n1 = AND(asset_dict['low'], income_dict['low']) * app_low
    rule_n2 = AND(asset_dict['low'], income_dict['medium']) * app_low
    rule_n3 = AND(asset_dict['low'], income_dict['high']) * app_medium
    rule_n4 = AND(asset_dict['low'], income_dict['vh']) * app_high
    rule_n5 = AND(asset_dict['medium'], income_dict['low']) * app_low
    rule_n6 = AND(asset_dict['medium'], income_dict['medium']) * app_medium
    rule_n7 = AND(asset_dict['medium'], income_dict['high']) * app_high
    rule_n8 = AND(asset_dict['medium'], income_dict['vh']) * app_high
    rule_n9 = AND(asset_dict['high'], income_dict['low']) * app_medium
    rule_n10 = AND(asset_dict['high'], income_dict['medium']) * app_medium
    rule_n11 = AND(asset_dict['high'], income_dict['high']) * app_high
    rule_n12 = AND(asset_dict['high'], income_dict['vh']) * app_high

    out_app_l = [max(a,b,c) for a,b,c in zip(rule_n1,rule_n2,rule_n5)] 
    out_app_m = [max(a,b,c,d) for a,b,c,d in zip(rule_n3,rule_n6,rule_n9,rule_n10)] 
    out_app_high = [max(a,b,c,d,e) for a,b,c,d,e in zip(rule_n4,rule_n7,rule_n8,rule_n11,rule_n12)]

    applicant_out = np.array([max(a,b,c) for a,b,c in zip(out_app_l, out_app_m, out_app_high)]) 

    defuzz_mom = fuzz.defuzz(x_applicant, applicant_out, 'mom')
    
    
    plt.plot(x_applicant, out_app_l, color = 'k')
    plt.plot(x_applicant, out_app_m, linestyle = '--',alpha = 0.35, color = 'r')
    plt.plot(x_applicant, out_app_high, linestyle = '--',alpha = 0.35, color = 'g')
    plt.plot(x_applicant, applicant_out, linestyle = '--',alpha = 0.35, color = 'b')
    plt.show()
    
    return defuzz_mom
    