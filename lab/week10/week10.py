import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

plt.close("all")
#
data_B = np.loadtxt("lab/week10/dataB.txt", encoding="utf-8-sig", skiprows=1)
L_B =data_B[:,0]
T_B =data_B[:,1]

data_C =np.loadtxt("lab/week10/dataC.txt",encoding="utf-8-sig",skiprows=1)
A_C_degree =data_C[:,0]
T_C =data_C[:,1]
L_C=0.4#C的长度是固定的

A_C = np.deg2rad(A_C_degree)#弧度制角度

g_val = 9.59251 

'''curve fitting function'''
#Part_B
def linear_decay(x, a, b):
    return a*x+ b

#Part_C
def get_T0(l, g):
    # 最基础的小角度近似公式 [cite: 218, 630]
    return 2 * np.pi * np.sqrt(l / g)

def get_T_bernoulli(T0, theta_rad):
    # 伯努利一阶修正模型：T = T0 * (1 + theta^2 / 16) [cite: 642, 662]
    return T0 * (1 + (theta_rad**2 / 16))

def get_T_parwani(T0, theta_rad):
    # Parwani修正模型，据文献称在130度以内都很准 [cite: 636, 724]
    # 公式：T = T0 * [sin(sqrt(3)*theta/2) / (sqrt(3)*theta/2)]^(-0.5)
    term = (np.sqrt(3) * theta_rad / 2)
    return T0 * (np.sin(term) / term)**(-0.5)



'''Part_B'''
plt.figure(1)
plt.xlabel("Length Square root(√m)", fontsize =12)
plt.ylabel("Period (s)", fontsize =12)
plt.plot(L_B, T_B, 'o',label='measured period' , color='green' )


#linear Part_B
popt, pcov=curve_fit(linear_decay, L_B, T_B, p0=[T_B[0], 0.1])
plt.plot(L_B, linear_decay(L_B, *popt) ,'--' ,label='linear fit',color='blue')
plt.legend(loc='best')
print("--------------------------")
print(popt[0])#slope
print("--------------------------")

'''Part_C'''
plt.figure(2)
plt.xlabel("angle (radians)", fontsize =12)
plt.ylabel("Period (s)", fontsize =12)
plt.plot(A_C, T_C, 'o',label='measured period' , color='green')

# 生成从0度到90度的平滑角度序列
theta_smooth_deg = np.linspace(0, 90, 100)
theta_smooth_rad = np.deg2rad(theta_smooth_deg)

# 2. 计算理论小角度周期 T0 [cite: 218, 630]
# 注意：这里使用的是你在图片1中定义的固定摆长 L_C
T0_val = get_T0(L_C, g_val)

# 3. 计算理论修正模型的平滑曲线数据 [cite: 642, 636]
# 利用你生成的 theta_smooth_rad (0到90度的平滑弧度序列)
T_theory_B = get_T_bernoulli(T0_val, theta_smooth_rad)
T_theory_P = get_T_parwani(T0_val, theta_smooth_rad)

# 4. 继续完善图表 Figure(2) 的内容
# 绘制小角度近似线（一条红色的虚线，代表理想状态下周期不随角度改变）
plt.axhline(y=T0_val, color='red', linestyle='--', label='Theoretical T0 (Small Angle)')

# 绘制 Bernoulli 修正曲线 [cite: 662]
plt.plot(theta_smooth_rad, T_theory_B, color='blue', label='Bernoulli Correction', alpha=0.8)

# 绘制 Parwani 修正曲线 [cite: 724]
plt.plot(theta_smooth_rad, T_theory_P, color='orange', label='Parwani Correction', alpha=0.8)

# 5. 图表修饰
plt.title("Part C: Period vs Angle Analysis", fontsize=14)
plt.legend(loc='best')
plt.grid(True, which='both', linestyle=':', alpha=0.6)

# 6. 计算相对误差并输出到控制台 (用于回答实验指南中的“1%误差限制”问题) [cite: 101, 369]
# 计算实验测量周期 T_C 相对于理论 T0 的偏差百分比
relative_error = ((T_C - T0_val) / T0_val) * 100

print("\n" + "="*45)
print("             Part C 数据分析报告")
print(f"当前设定摆长 L_C = {L_C} m, 理论 T0 = {T0_val:.4f} s")
print("-" * 45)
print("角度 (deg) | 测量周期 (s) | 相对 T0 偏差 (%)")
for i in range(len(A_C_degree)):
    # 使用 A_C_degree 输出度数，读数更直观
    print(f"{A_C_degree[i]:<10.1f} | {T_C[i]:<12.4f} | {relative_error[i]:.2f}%")
print("="*45)



plt.legend()
plt.show()

