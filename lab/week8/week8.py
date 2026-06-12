import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.optimize import curve_fit

plt.close("all")
#
data_ini_1 =np.loadtxt("simple harmonic oscillator.txt",encoding="utf-8-sig",skiprows=1)
t_1pre =data_ini_1[:,0]
x_1pre =data_ini_1[:,1]

data_ini_2 =np.loadtxt("damped harmonic oscillator.txt",encoding="utf-8-sig",skiprows=1)
t_2pre =data_ini_2[:,0]
x_2pre =data_ini_2[:,1]

'''get peaks'''
peaks_1 ,_ =find_peaks(x_1pre)
t_1 =t_1pre[peaks_1]
x_1 =x_1pre[peaks_1]

peaks_2 ,_ =find_peaks(x_2pre)
t_2 =t_2pre[peaks_2]
x_2 =x_2pre[peaks_2]

'''curve fitting function'''
def linear_decay(t, a, b):
    return a*t+ b

def exp_decay(t, A_0 ,gama):
    return A_0 * np.exp(-gama * t)

'''calculate R_sqr'''

def calculate_Rsqr(x,fit):
    y_mean=np.mean(x)
    ss_tot = np.sum((x-y_mean)**2)
    ss_res = np.sum((x-fit)**2)
    R_sqr=1-(ss_res / ss_tot)
    print(f"R={R_sqr:.4f}")
    return R_sqr
   
    


''' Exp_1 '''
plt.figure(1)
plt.xlabel("Time (s)", fontsize =12)
plt.ylabel("Position (m)", fontsize =12)
plt.plot(t_1pre, x_1pre,'.g' ,label='measured position' , color='green' )
plt.plot(t_1, x_1, 'o',label='peaks' , color='red')

#linear EXP_1
popt, pcov=curve_fit(linear_decay, t_1, x_1, p0=[x_1[0], 0.1])
plt.plot(t_1, linear_decay(t_1, *popt) ,'--' ,label='linear fit',color='blue')

plt.figure(2)#linear Residuals
x_fit = linear_decay(t_1, *popt)

R_sqr1 = calculate_Rsqr(x_1 ,x_fit)

residuals =x_1-x_fit
plt.plot(t_1, residuals , 'mo' ,label=f"linear Residuals(R^2={R_sqr1:.4f})")
plt.axhline(y=0 ,color='black' ,linestyle='--')
plt.xlabel('Time (s)')
plt.ylabel('Residuals (m)')
plt.legend()

#exp EXP_1
plt.figure(1)
popt, pcov=curve_fit(exp_decay, t_1, x_1, p0=[x_1[0], 0.1])
plt.plot(t_1, exp_decay(t_1, *popt) ,'--' ,label='exponential fit',color='black')
plt.legend()

plt.figure(3)#exponential Residuals
x_fit = exp_decay(t_1, *popt)

R_sqr2 = calculate_Rsqr(x_1 ,x_fit)

residuals =x_1-x_fit
plt.plot(t_1, residuals , 'mo' ,label=f"exponential Residuals(R^2={R_sqr2:.4f})")
plt.axhline(y=0 ,color='black' ,linestyle='--')
plt.xlabel('Time (s)')
plt.ylabel('Residuals (m)')

plt.legend()


'''Exp_2'''
plt.figure(4)
plt.xlabel("Time (s)", fontsize =12)
plt.ylabel("Position (m)", fontsize =12)
plt.plot(t_2pre, x_2pre,'.g' ,label='measured position' , color='green')
plt.plot(t_2, x_2, 'o',label='peaks' , color='red')
plt.legend()



#linear EXP_2
popt, pcov=curve_fit(linear_decay, t_2, x_2, p0=[x_2[0], 0.1])
plt.plot(t_2, linear_decay(t_2, *popt) ,'--' ,label='linear fit',color='blue')

plt.figure(5)#linear Residuals
x_fit = linear_decay(t_2, *popt)

R_sqr3 = calculate_Rsqr(x_2 ,x_fit)

residuals =x_2-x_fit
plt.plot(t_2, residuals , 'mo' ,label=f"linear Residuals(R^2={R_sqr3:.4f})")
plt.axhline(y=0 ,color='black' ,linestyle='--')
plt.xlabel('Time (s)')
plt.ylabel('Residuals (m)')
plt.legend()

#exp EXP_2
plt.figure(4)
popt, pcov=curve_fit(exp_decay, t_2, x_2, p0=[x_2[0], 0.1])
plt.plot(t_2, exp_decay(t_2, *popt) ,'--' ,label='exp fit',color='black')
plt.legend()
plt.figure(6)#linear Residuals
x_fit = exp_decay(t_2, *popt)

R_sqr4 = calculate_Rsqr(x_2 ,x_fit)

residuals =x_2-x_fit
plt.plot(t_2, residuals , 'mo' ,label=f"exponential Residuals(R^2={R_sqr4:.4f})")
plt.axhline(y=0 ,color='black' ,linestyle='--')
plt.xlabel('Time (s)')
plt.ylabel('Residuals (m)')

plt.legend()
plt.show()


