import skfuzzy as fuzz
import numpy as np 
import matplotlib.pyplot as plt

x_temp = np.arange(7,17,1)
x_press = np.arange(1.75, 4.25, 0.25)
x_co2 = np.arange(2, 6.5, 0.5)

temp_vc = fuzz.membership.trimf(x_temp, [1,7,9])
temp_c = fuzz.membership.trimf(x_temp, [7,9,11])
temp_n = fuzz.membership.trimf(x_temp, [10, 12, 14])
temp_h = fuzz.membership.trimf(x_temp, [12, 14, 16])
temp_vh = fuzz.membership.trimf(x_temp, [13, 16, 16])

press_vb = fuzz.membership.trimf(x_press, [1, 1.75, 2.25])
press_b = fuzz.membership.trimf(x_press, [1.75, 2.25, 2.50])
press_n = fuzz.membership.trimf(x_press, [2.25, 2.75, 3.25])
press_g = fuzz.membership.trimf(x_press, [ 2.50, 3.25, 3.50])
press_vg = fuzz.membership.trimf(x_press, [2.75, 4.00, 4.00])

co2_vb = fuzz.membership.trimf(x_co2, [1,2,3])
co2_b = fuzz.membership.trimf(x_co2, [2,3,4])
co2_n = fuzz.membership.trimf(x_co2, [3,4,5])
co2_g = fuzz.membership.trimf(x_co2, [4,5,6])
co2_vg = fuzz.membership.trimf(x_co2, [5,6,6])


fig,  (ax0, ax1, ax2) = plt.subplots(nrows = 3, figsize = (6, 10))

ax0.plot(x_temp, temp_vc, 'b', linewidth = 2, label = 'VC')
ax0.plot(x_temp, temp_c, 'b', linewidth = 2, label = 'C')
ax0.plot(x_temp, temp_n, 'b', linewidth = 2, label = 'N')
ax0.plot(x_temp, temp_h, 'b', linewidth = 2, label = 'H')
ax0.plot(x_temp, temp_vh, 'b', linewidth = 2, label = 'VH')
ax0.set_title('Temperature')
ax0.legend()

ax1.plot(x_press, press_vb, 'b', linewidth = 2, label = 'VB')
ax1.plot(x_press, press_b, 'b', linewidth = 2, label = 'B')
ax1.plot(x_press, press_n, 'b', linewidth = 2, label = 'N')
ax1.plot(x_press, press_g, 'b', linewidth = 2, label = 'G')
ax1.plot(x_press, press_vg, 'b', linewidth = 2, label = 'VG')
ax1.set_title('Pressure')
ax1.legend()

ax2.plot(x_co2, co2_vb, 'b', linewidth = 2, label = 'VB')
ax2.plot(x_co2, co2_b, 'b', linewidth = 2, label = 'B')
ax2.plot(x_co2, co2_n, 'b', linewidth = 2, label = 'N')
ax2.plot(x_co2, co2_g, 'b', linewidth = 2, label = 'G')
ax2.plot(x_co2, co2_vg, 'b', linewidth = 2, label = 'VG')
ax2.set_title('Percentage of CO2')
ax2.legend()

input_temp = 13.50
input_press = 3.25

temps = [temp_vc, temp_c, temp_n, temp_h, temp_vh]
temp_fit = []
d = ['vc', 'c', 'n', 'h', 'vh']
for temp in temps:
    temp_fit.append(fuzz.interp_membership(x_temp, temp, input_temp))

temp_dict = dict(zip(d, temp_fit))

presses = [press_vb, press_b, press_n, press_g, press_vg]
press_fit = []
d = ['vb','b', 'n', 'g', 'vg']
for press in presses:
    press_fit.append(fuzz.interp_membership(x_press, press, input_press))

press_dict = dict((zip(d, press_fit)))

AND = np.fmin
OR = np.fmax


rule_n1 = AND(AND(temp_dict['vc'], OR(press_dict['vb'], press_dict['b'])),                     co2_n)
rule_n2 = AND(AND(temp_dict['n'],  OR(press_dict['b'], press_dict['n'])) ,                     co2_n)
rule_n3 = AND(AND(OR (temp_dict['h'], temp_dict['vh']), OR(press_dict['n'], press_dict['g'])), co2_n)


out_normal = OR(OR(rule_n1, rule_n2), rule_n3)

rule_g1 = AND(AND(OR(temp_dict['vc'], temp_dict['c']), press_dict['n']), co2_g)
rule_g2 = AND(AND(temp_dict['c'], OR(press_dict['b'], press_dict['g'])), co2_g)
rule_g3 = AND(AND(temp_dict['n'], press_dict['g']),                      co2_g)
rule_g4 = AND(AND(press_dict['vg'], OR(temp_dict['h'],temp_dict['vh'])), co2_g)

rule_g =  OR(rule_g1, rule_g2)
rule_gg = OR(rule_g3, rule_g4)

out_good = OR(rule_g, rule_gg)

rule_vg1 = AND(AND(temp_dict['vc'], OR(press_dict['g'], press_dict['vg'])), co2_vg)
rule_vg2 = AND(AND(press_dict['vg'],OR(temp_dict['c'],  temp_dict['n'])),   co2_vg)

out_very_good = OR(rule_vg1, rule_vg2)

rule_b1 = AND(AND(press_dict['vb'], OR(OR(temp_dict['c'], temp_dict['n']), temp_dict['h'])), co2_b)
rule_b2 = AND(AND(press_dict['b'], OR(temp_dict['h'], temp_dict['vh'])),                     co2_b)

out_bad = OR(rule_b1, rule_b2)

out_very_bad = AND(AND(temp_dict['vh'], press_dict['vb']), co2_vb)

plt.tight_layout()


co2_0 = np.zeros_like(x_co2)
fig, ax0 = plt.subplots(figsize = (10,5))
ax0.fill_between(x_co2, co2_0, out_bad, facecolor = 'k',alpha = 0.5)
ax0.plot(x_co2, co2_b, 'r', linestyle = '--')
ax0.fill_between(x_co2, co2_0, out_very_bad, facecolor = 'k',alpha = 0.5)
ax0.plot(x_co2, co2_vb, 'b', linestyle = '--')
ax0.fill_between(x_co2, co2_0, out_good, facecolor = 'k',alpha = 0.5)
ax0.plot(x_co2, co2_g, 'g', linestyle = '--')
ax0.fill_between(x_co2, co2_0, out_very_good, facecolor = 'k',alpha = 0.5)
ax0.plot(x_co2, co2_vg, 'c', linestyle = '--')
ax0.fill_between(x_co2, co2_0, out_normal, facecolor = 'k',alpha = 0.5)
ax0.plot(x_co2, co2_n, 'y', linestyle = '--')
plt.show()

out_co2 = OR(out_very_bad, OR(out_bad, OR(out_normal, OR(out_good, out_very_good))))
defuzz = fuzz.defuzz(x_co2, out_co2, 'centroid')
membership_res = fuzz.interp_membership(x_co2, out_co2, defuzz)

print(membership_res, defuzz)