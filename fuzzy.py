import skfuzzy as fuzz
import numpy as np 
import matplotlib.pyplot as plt

x_market_value_house = np.arange(0, 1050, 50)
x_location_house = np.arange(0, 10.5, 0.5)
x_asset_application = np.arange(0, 1050, 50)
x_income = np.arange(0, 105, 5)
x_interest_rate = np.arange(0, 10.5, 0.5)

x_house = np.arange(0, 11, 1)
x_applicant = np.arange(0, 11, 1)
x_credit_amount = np.arange(0, 525, 25)

mvh_low = fuzz.membership.trapmf(x_market_value_house, [0, 0, 50, 100])
mvh_medium = fuzz.membership.trapmf(x_market_value_house, [50, 100, 200, 250])
mvh_high = fuzz.membership.trapmf(x_market_value_house, [200, 300, 650, 850])
mvh_vh = fuzz.membership.trapmf(x_market_value_house, [650, 850, 1000, 1000])

lh_bad = fuzz.membership.trapmf(x_location_house, [0, 0, 2, 4])
lh_fair = fuzz.membership.trapmf(x_location_house, [2.5, 5, 6, 8.5])
lh_exc = fuzz.membership.trapmf(x_location_house, [6, 8.5, 10, 10])

aa_low = fuzz.membership.trimf(x_asset_application, [0,0,150])
aa_medium = fuzz.membership.trapmf(x_asset_application, [50,250,450,650])
aa_high = fuzz.membership.trapmf(x_asset_application, [500,700,1000,1000])

i_low = fuzz.membership.trapmf(x_income, [0, 0, 10, 25])
i_medium = fuzz.membership.trimf(x_income, [15, 35, 55])
i_high = fuzz.membership.trimf(x_income, [40, 60, 80])
i_vh = fuzz.membership.trapmf(x_income, [60, 80, 100, 100])

int_low = fuzz.membership.trapmf(x_interest_rate, [0,0,2,5])
int_medium = fuzz.membership.trapmf(x_interest_rate, [2,4,6,8])
int_high = fuzz.membership.trapmf(x_interest_rate, [6,8.5,10,10])

house_vl = fuzz.membership.trimf(x_house, [0,0,3])
house_low = fuzz.membership.trimf(x_house, [0,3,6])
house_medium = fuzz.membership.trimf(x_house, [2,5,8])
house_high = fuzz.membership.trimf(x_house, [4,7,10])
house_vh = fuzz.membership.trimf(x_house, [7,10,10])

app_low = fuzz.membership.trapmf(x_applicant, [0, 0, 2, 4])
app_medium = fuzz.membership.trimf(x_applicant, [2, 5, 8])
app_high = fuzz.membership.trapmf(x_applicant, [6, 8, 10, 10])

ca_vl = fuzz.membership.trimf(x_credit_amount, [0, 0, 125])
ca_low = fuzz.membership.trimf(x_credit_amount, [0, 125, 250])
ca_medium = fuzz.membership.trimf(x_credit_amount, [125, 250, 375])
ca_high = fuzz.membership.trimf(x_credit_amount, [250, 375, 500])
ca_vh = fuzz.membership.trimf(x_credit_amount, [375, 500, 500])

'''
fig,  (ax0,ax1,ax2,ax3) = plt.subplots(nrows = 4, figsize = (20, 20))

ax0.plot(x_market_value_house, mvh_low)
ax0.plot(x_market_value_house, mvh_medium)
ax0.plot(x_market_value_house, mvh_high)
ax0.plot(x_market_value_house, mvh_vh)
ax0.set_title('Market Value')
ax0.legend()

ax1.plot(x_location_house, lh_bad)
ax1.plot(x_location_house, lh_fair)
ax1.plot(x_location_house, lh_exc)
ax1.set_title('Location of House')
ax1.legend()

ax2.plot(x_asset_application, aa_low)
ax2.plot(x_asset_application, aa_medium)
ax2.plot(x_asset_application, aa_high)
ax2.set_title('Asset Application')
ax2.legend()

ax3.plot(x_income, i_low)
ax3.plot(x_income, i_medium)
ax3.plot(x_income, i_high)
ax3.plot(x_income, i_vh)
ax3.set_title('Income of the Applicant')
ax3.legend()

plt.show()

fig,  (ax4,ax5,ax6,ax7) = plt.subplots(nrows = 4, figsize = (6, 12))

ax4.plot(x_interest_rate, int_low)
ax4.plot(x_interest_rate, int_medium)
ax4.plot(x_interest_rate, int_high)
ax4.set_title('Interest')
ax4.legend()

ax5.plot(x_house, house_vl)
ax5.plot(x_house, house_low)
ax5.plot(x_house, house_medium)
ax5.plot(x_house, house_high)
ax5.plot(x_house, house_vh)
ax5.set_title('House Quality')
ax5.legend()

ax6.plot(x_applicant, app_low)
ax6.plot(x_applicant, app_medium)
ax6.plot(x_applicant, app_high)
ax6.set_title('Applicant')
ax6.legend()

ax7.plot(x_credit_amount, ca_vl)
ax7.plot(x_credit_amount, ca_low)
ax7.plot(x_credit_amount, ca_medium)
ax7.plot(x_credit_amount, ca_high)
ax7.plot(x_credit_amount, ca_vh)
ax7.set_title('Credit Amount')
ax7.legend()

plt.show()
'''

input_mvh = 500
input_loc = 5
#input_aa = 5

#.append(fuzz.interp_membership(x_, , ))

market_values = [mvh_low,mvh_medium,mvh_high, mvh_vh]
market_fit = []
for value in market_values:
    market_fit.append(fuzz.interp_membership(x_market_value_house, value, input_mvh))

d = ['low', 'medium', 'high', 'vh']
mvh_dict = dict(zip(d, market_fit))
#print(temp_dict)


location_values = [lh_bad, lh_fair, lh_exc]
loc_fit = []
for loc in location_values:
    loc_fit.append(fuzz.interp_membership(x_location_house, loc, input_loc))
d = ['bad', 'fair', 'exc']

loc_dict = dict(zip(d, loc_fit))
#print(loc_dict)

'''
asset_applicants = [aa_low, aa_medium, aa_high]
asset_fit = []
for applicant in asset_applicants:
    asset_fit.append(fuzz.interp_membership(x_asset_application, applicant, input_aa))
'''

AND = min
OR = max

'''
    House eval rules
'''

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

'''
    Applicant eval rules
'''



plt.plot(x_house, house_out)
plt.plot(x_house, out_house_high)

defuzz_mom = fuzz.defuzz(x_house, house_out, 'mom')
#membership_res = fuzz.interp_membership(x_house, house_out, defuzz_mom) içinde bulunma oranı
print(defuzz_mom)

plt.show()









