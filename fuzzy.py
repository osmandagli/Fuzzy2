import skfuzzy as fuzz
import numpy as np 
import matplotlib.pyplot as plt

x_market_value_house = np.arange(0, 1050, 50)
x_location_house = np.arange(0, 11, 1)
x_asset_application = np.arange(0, 1100, 100)
x_income = np.arange(0, 110, 10)
x_interest_rate = np.arange(0, 11, 1)

x_house = np.arange(0, 11, 1)
x_appliant = np.arange(0, 11, 1)
x_credit_amount = np.arange(0, 550, 50)

mvh_low = fuzz.membership.trapmf(x_market_value_house, [0, 0, 50, 100])
mvh_medium = fuzz.membership.trapmf(x_market_value_house, [50, 100, 200, 250])
mvh_high = fuzz.membership.trapmf(x_market_value_house, [200, 300, 650, 850])
mvh_vh = fuzz.membership.trapmf(x_market_value_house, [650, 850, 1000, 1000])

plt.plot(x_market_value_house, mvh_low)
plt.plot(x_market_value_house, mvh_medium)
plt.plot(x_market_value_house, mvh_high)
plt.plot(x_market_value_house, mvh_vh)
plt.show()
