import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

plt.close('all')#close all open windows in each run
#set font size 14 for all figures
font = {'size' :14}
plt.rc('font',**font)

'''prepare datas'''
B_data=np.loadtxt("PartB_vt.txt", encoding="utf-8-sig")
B_data_t=B_data[:,0]
B_data_v=B_data[:,1]

C_data=np.loadtxt("PartC_Fv.txt", encoding="utf-8-sig")
C_data_v=C_data[:,0]
C_data_F=C_data[:,1]

C_data1=np.loadtxt("PartC_vt.txt", encoding="utf-8-sig")
C_data_t1=C_data1[:,0]
C_data_v1=C_data1[:,1]

D_data = np.loadtxt('PartD_vt.txt', encoding="utf-8-sig")
D_data_t=D_data[:,0]
D_data_v=D_data[:,1]
'''plot figures - friction'''

plt.figure(1)#pingheng Qian

plt.xlabel("time (s)", fontsize=12)
plt.ylabel("velocity (m/s)", fontsize=12)
plt.legend()
plt.grid(True ,which='both' ,linestyle=':' ,alpha=0.7)

plt.plot(B_data_t - B_data_t[0] ,B_data_v ,
         label='Before Adjustment (Friction dominates)' ,
         color='green' )


'''plot figures - drag force'''

plt.figure(2)#calculate b form F-v figure

plt.xlabel("velocity (m/s)", fontsize=12)
plt.ylabel("Force (N)", fontsize=12)

plt.grid(True ,which='both' ,linestyle=':' ,alpha=0.7)

plt.scatter(C_data_v, C_data_F, s=20 ,c='blue' ,marker='o')

def fit_func(x, a, b):
    return a * x + b
popt, pcov = curve_fit(fit_func, C_data_v, C_data_F)

plt.legend()
a_fit = popt[0]  # slope
b_fit = popt[1]  # incerment

b_drag_coefficient = abs(a_fit)

# === 1. Calculate R2 of F-v ===
y_true_F = C_data_F
y_pred_F = fit_func(C_data_v, *popt)

ss_res_F = np.sum((y_true_F - y_pred_F)**2)
ss_tot_F = np.sum((y_true_F - np.mean(y_true_F))**2)
r_squared_F = 1 - (ss_res_F / ss_tot_F)

plt.plot(C_data_v, y_pred_F, color='red', linewidth=2, label=f'Fit Line ($R^2$={r_squared_F:.4f})')
plt.legend()
#: F = {a_fit:.4f}v + {b_fit:.4f}


plt.figure(3)#calculate b form v-t figure

m = 0.8491
plt.xlabel("time (s)", fontsize=12)
plt.ylabel("ln(velocity)", fontsize=12)
plt.grid(visible=True, which='both', linestyle=':', alpha=0.7)

ln_v1 = np.log(np.abs(C_data_v1))

plt.scatter(C_data_t1, ln_v1, s=20, c='blue', marker='o', label='ln(v) Data')

# define linear function: y = at + c
def lin_func(t, a, c):
    return a * t + c

# linear fitting
popt_lin, _ = curve_fit(lin_func, C_data_t1, ln_v1)
a_fit = popt_lin[0] # slope
c_fit = popt_lin[1] # intercept

b_fit_linear = -a_fit * m

# === 2. calculate  ln(v)-t fi  ===
y_true_v = ln_v1

y_pred_v = a_fit * C_data_t1 + c_fit

ss_res_v = np.sum((y_true_v - y_pred_v)**2)
ss_tot_v = np.sum((y_true_v - np.mean(y_true_v))**2)
r_squared_v = 1 - (ss_res_v / ss_tot_v)

plt.plot(C_data_t1, y_pred_v, 'r-', linewidth=2, label=f'Linear Fit ($R^2$={r_squared_v:.4f})')
plt.legend()



'''plot figures - D'''
plt.figure(4)#calculate b form v-t figure

plt.xlabel("time (s)", fontsize=12)
plt.ylabel("velocity (m/s)", fontsize=12)
plt.grid(visible=True, which='both', linestyle=':', alpha=0.7)

v_abs = np.abs(D_data_v)

# draw spots on the figures
plt.scatter(D_data_t, v_abs, s=15, c='blue', marker='o', label='Experimental Data')


vT_exp = np.mean(v_abs[200:])#use datas after 2.0s

# show the fitting curves
plt.axhline(vT_exp, color='red', linestyle='--', linewidth=2, label=f'Exp $v_T$ = {vT_exp:.4f} m/s')

plt.legend()

# Part D
m_partD = 0.3446      # mass without clump weight
theta_deg = 2.0

b_final = 0.5903      # final b from PartC

g = 9.8

theta_rad = np.radians(theta_deg)

# Calculate the theoretical vT: v_T = (mg * sin(theta)) / b
vT_theo = (m_partD * g * np.sin(theta_rad)) / b_final

print("================ Part D Results ================")
print(f"tV from figures = {vT_exp:.4f} m/s")
print(f"tV from theoretical formula= {vT_theo:.4f} m/s")

#show the relative error rate
error = abs(vT_exp - vT_theo) / vT_theo * 100
print(f"relative error rate between experiment and theoretical v = {error:.2f}%")
print("=============================================")

#shwo all the figures
plt.show()



