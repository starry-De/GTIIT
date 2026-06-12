**无序列表 (Unordered List):**
使用减号 `-` 或星号 `*` 加上空格：
- PASCO 实验小车
- 两个理想弹簧
- 磁阻尼装置

**有序列表 (Ordered List):**
直接使用数字加英文句号和空格：
1. 将小车放置在无摩擦轨道上。
2. 将小车从平衡位置拉开 10 厘米。
3. 释放小车并开始记录数据。


我们需要使用 `scipy.optimize` 中的 `curve_fit` 函数来进行拟合。

```python
import numpy as np
import matplotlib.pyplot as plt

# 计算阻尼系数
def damped_oscillation(t, A, gamma, omega, phi):
    return A * np.exp(-gamma * t) * np.cos(omega * t + phi)
```

| 物理量 (Quantity) | 符号 (Symbol) | 测量值 (Value) |
| :--- | :---: | ---: |
| 小车质量 (默认左对齐) | $m_{cart}$ (居中对齐) | 0.505 kg (右对齐) |
| 弹簧系数 | $k_1$ | 3.2 N/m |