import skfuzzy as fuzz
import numpy as np 
import matplotlib.pyplot as plt
from house_defuzz import house_defuzz
from applicant_defuzz import applicant_defuzz

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

input_mvh = 500
input_loc = 5
input_aa = 100
input_inc = 35


'''
    House eval rules
'''
market_values = [mvh_low,mvh_medium,mvh_high, mvh_vh]
location_values = [lh_bad, lh_fair, lh_exc]
defuzz_house = house_defuzz(market_values, x_market_value_house, location_values, x_location_house, input_mvh, input_loc)
#membership_res = fuzz.interp_membership(x_house, house_out, defuzz_house) içinde bulunma oranı
print(defuzz_house)


'''
    Applicant eval rules
'''

asset_values = [aa_low, aa_medium, aa_high]
income_values = [i_low,i_medium,i_high,i_vh]
defuzz_applicant = applicant_defuzz(asset_values, x_asset_application, income_values, x_income, input_aa, input_inc)
print(defuzz_applicant)










