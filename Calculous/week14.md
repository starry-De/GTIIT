# 向量微积分笔记：三维曲面与第一类曲面积分
*(Surfaces in $\mathbb{R}^3$ & Surface Integrals of Scalar Functions)*

---

## 1. 核心概念升维：从曲线到曲面

### 1.1 一维曲线 (Curves) 的回顾
* **本质：** 三维空间中的单参数子集 (1-parameter subsets)。
* **参数化：** $\gamma(t) = (x(t), y(t), z(t)), \quad t \in [a, b]$
* **切向量：** $\gamma'(t) = (x'(t), y'(t), z'(t))$

### 1.2 二维曲面 (Surfaces) 的定义
* **本质：** 三维空间中的双参数子集 (2-parameter subsets)。记为 $\Sigma$。
* **参数化：** $\sigma: D \subseteq \mathbb{R}^2 \to \mathbb{R}^3$
    $$\sigma(u,v) = (x(u,v), y(u,v), z(u,v))$$
* **两个切向量：** 沿着网格线求偏导
    1.  $\sigma_u = \frac{\partial \sigma}{\partial u} = (x_u, y_u, z_u)$
    2.  $\sigma_v = \frac{\partial \sigma}{\partial v} = (x_v, y_v, z_v)$

### 1.3 切平面与曲面的“光滑”判定 (Smoothness)
由两个切向量叉乘得到**法向量 (Normal Vector)** $\vec{N}$：
$$\vec{N} = \sigma_u \times \sigma_v$$
* **光滑判定：** 若在定义域 $D$ 内恒有 $\vec{N} \neq \vec{0}$，则切平面始终存在，称该参数化曲面是**光滑的 (Smooth)**。

---

## 2. 描述曲面的三种方式

1.  **显式函数 (Graphs):** $z = f(x,y)$ 
    * 参数化最简单：$\sigma(x,y) = (x, y, f(x,y))$
2.  **隐式方程 (Sets of solutions):** $F(x,y,z) = 0$
3.  **参数化方程 (Parametrized surfaces):** $\sigma(u,v)$
    * 这是进行曲面积分时**最简单、最通用**的方式。

**【经典参数化案例】**
* **球面 (Sphere):** 半径为 $R$
    $\sigma(\theta, \phi) = (R\cos\theta\sin\phi, R\sin\theta\sin\phi, R\cos\phi)$
* **圆锥面 (Cone):** $z = \sqrt{x^2+y^2} \le h$
    $\sigma(\rho, \theta) = (\rho\cos\theta, \rho\sin\theta, \rho), \quad (0 \le \theta \le 2\pi, \ 0 \le \rho \le h)$

---

## 3. 第一类曲面积分 (对标量函数的积分)

**定义式：**
$$\iint_\Sigma f(x,y,z) \,dS \equiv \iint_D f(\sigma(u,v)) |\sigma_u \times \sigma_v| \,du dv$$
* **面积微元 (Surface differential):** $dS = |\sigma_u \times \sigma_v| dudv$
* **几何意义：** 物理上可理解为求弯曲薄片的总质量（$f$ 为密度）。当 $f=1$ 时，得到曲面的**表面积**。
    $$\text{Area}(\Sigma) = \iint_D |\sigma_u \times \sigma_v| \,du dv$$

---

## 4. 三种常见曲面的面积微元 $dS$ (快捷公式推导)

### Case 1: 退化为水平面 $z = z_0$
* $\sigma(u,v) = (x(u,v), y(u,v), z_0)$
* $\sigma_u = (x_u, y_u, 0)$, $\sigma_v = (x_v, y_v, 0)$
* **推导：** $|\sigma_u \times \sigma_v| = |(0, 0, x_u y_v - x_v y_u)| = |x_u y_v - x_v y_u|$
* **结论：** 这恰好是二维坐标变换的**雅可比行列式 $|J|$**。三维降维完美自洽。

### Case 2: 显式曲面 $z = f(x,y)$ (最常用)
* $\sigma_x = (1, 0, f_x)$, $\sigma_y = (0, 1, f_y)$
* 法向量：$\sigma_x \times \sigma_y = (-f_x, -f_y, 1)$
* **结论 (拉伸系数)：** $dS = \sqrt{1 + f_x^2 + f_y^2} \,dxdy$
* **面积公式：** $\text{Area}(\Sigma) = \iint_D \sqrt{1 + f_x^2 + f_y^2} \,dxdy$

### Case 3: 隐式曲面 $F(x,y,z) = 0$
* 利用隐函数求导法则 (Implicit Function Theorem)：
    $f_x = -\frac{F_x}{F_z}$, $f_y = -\frac{F_y}{F_z}$
* 代入 Case 2 的叉乘模长公式：
    $|\sigma_x \times \sigma_y| = \left| \left(\frac{F_x}{F_z}, \frac{F_y}{F_z}, 1\right) \right| = \frac{1}{|F_z|} \sqrt{F_x^2 + F_y^2 + F_z^2} = \frac{|\nabla F|}{|F_z|}$
* **结论 (拉伸系数)：** $dS = \frac{|\nabla F|}{|F_z|} \,dxdy$

---

## 5. 综合计算大题 (The Cone Example)

**题目：**
计算积分 $\iint_\Sigma (x^2+y^2+z^2) \,dS$，其中曲面 $\Sigma$ 为圆锥面 $z = \sqrt{x^2+y^2}$，且位于 $xy$ 平面区域 $x^2+y^2 \le 2x$ 的正上方。

**Step 1: 确定参数化与投影区域 $D$**
* 曲面为显式函数 $z = \sqrt{x^2+y^2}$，直接使用 $(x,y)$ 作为参数。
* 投影区域 $D$: $x^2+y^2 \le 2x \implies (x-1)^2+y^2 \le 1$ (圆心在 $(1,0)$，半径为 $1$ 的圆)。

**Step 2: 计算拉伸系数 $dS$**
* 套用公式：$dS = \sqrt{1 + z_x^2 + z_y^2} \,dxdy$
* $z_x = \frac{x}{\sqrt{x^2+y^2}}, \quad z_y = \frac{y}{\sqrt{x^2+y^2}}$
* $z_x^2 + z_y^2 = \frac{x^2+y^2}{x^2+y^2} = 1$
* $dS = \sqrt{1 + 1} \,dxdy = \sqrt{2} \,dxdy$

**Step 3: 将被积函数降维并转换极坐标**
* 将 $z$ 替换掉：$f(x,y,z) = x^2+y^2 + (\sqrt{x^2+y^2})^2 = 2(x^2+y^2)$
* 组装二重积分：
    $I = \iint_D 2(x^2+y^2) \cdot \sqrt{2} \,dxdy = 2\sqrt{2} \iint_D (x^2+y^2) \,dxdy$
* 转极坐标 $(x=r\cos\theta, y=r\sin\theta, dxdy=rdrd\theta)$：
    边界 $x^2+y^2 \le 2x \implies r^2 \le 2r\cos\theta \implies 0 \le r \le 2\cos\theta$
    角度范围：$-\frac{\pi}{2} \le \theta \le \frac{\pi}{2}$

**Step 4: 积分计算过程**
$$I = 2\sqrt{2} \int_{-\pi/2}^{\pi/2} \int_0^{2\cos\theta} (r^2) \cdot r \,dr d\theta$$

先对 $r$ 积分：
$$\int_0^{2\cos\theta} r^3 \,dr = \left[ \frac{1}{4}r^4 \right]_0^{2\cos\theta} = \frac{1}{4}(16\cos^4\theta) = 4\cos^4\theta$$

代回外层对 $\theta$ 积分 (利用偶函数对# 向量微积分笔记：三维曲面与第一类曲面积分
*(Surfaces in $\mathbb{R}^3$ & Surface Integrals of Scalar Functions)*

---

## 1. 核心概念升维：从曲线到曲面

### 1.1 一维曲线 (Curves) 的回顾
* **本质：** 三维空间中的单参数子集 (1-parameter subsets)。
* **参数化：** $\gamma(t) = (x(t), y(t), z(t)), \quad t \in [a, b]$
* **切向量：** $\gamma'(t) = (x'(t), y'(t), z'(t))$

### 1.2 二维曲面 (Surfaces) 的定义
* **本质：** 三维空间中的双参数子集 (2-parameter subsets)。记为 $\Sigma$。
* **参数化：** $\sigma: D \subseteq \mathbb{R}^2 \to \mathbb{R}^3$
    $$\sigma(u,v) = (x(u,v), y(u,v), z(u,v))$$
* **两个切向量：** 沿着网格线求偏导
    1.  $\sigma_u = \frac{\partial \sigma}{\partial u} = (x_u, y_u, z_u)$
    2.  $\sigma_v = \frac{\partial \sigma}{\partial v} = (x_v, y_v, z_v)$

### 1.3 切平面与曲面的“光滑”判定 (Smoothness)
由两个切向量叉乘得到**法向量 (Normal Vector)** $\vec{N}$：
$$\vec{N} = \sigma_u \times \sigma_v$$
* **光滑判定：** 若在定义域 $D$ 内恒有 $\vec{N} \neq \vec{0}$，则切平面始终存在，称该参数化曲面是**光滑的 (Smooth)**。

---

## 2. 描述曲面的三种方式

1.  **显式函数 (Graphs):** $z = f(x,y)$ 
    * 参数化最简单：$\sigma(x,y) = (x, y, f(x,y))$
2.  **隐式方程 (Sets of solutions):** $F(x,y,z) = 0$
3.  **参数化方程 (Parametrized surfaces):** $\sigma(u,v)$
    * 这是进行曲面积分时**最简单、最通用**的方式。

**【经典参数化案例】**
* **球面 (Sphere):** 半径为 $R$
    $\sigma(\theta, \phi) = (R\cos\theta\sin\phi, R\sin\theta\sin\phi, R\cos\phi)$
* **圆锥面 (Cone):** $z = \sqrt{x^2+y^2} \le h$
    $\sigma(\rho, \theta) = (\rho\cos\theta, \rho\sin\theta, \rho), \quad (0 \le \theta \le 2\pi, \ 0 \le \rho \le h)$

---

## 3. 第一类曲面积分 (对标量函数的积分)

**定义式：**
$$\iint_\Sigma f(x,y,z) \,dS \equiv \iint_D f(\sigma(u,v)) |\sigma_u \times \sigma_v| \,du dv$$
* **面积微元 (Surface differential):** $dS = |\sigma_u \times \sigma_v| dudv$
* **几何意义：** 物理上可理解为求弯曲薄片的总质量（$f$ 为密度）。当 $f=1$ 时，得到曲面的**表面积**。
    $$\text{Area}(\Sigma) = \iint_D |\sigma_u \times \sigma_v| \,du dv$$

---

## 4. 三种常见曲面的面积微元 $dS$ (快捷公式推导)

### Case 1: 退化为水平面 $z = z_0$
* $\sigma(u,v) = (x(u,v), y(u,v), z_0)$
* $\sigma_u = (x_u, y_u, 0)$, $\sigma_v = (x_v, y_v, 0)$
* **推导：** $|\sigma_u \times \sigma_v| = |(0, 0, x_u y_v - x_v y_u)| = |x_u y_v - x_v y_u|$
* **结论：** 这恰好是二维坐标变换的**雅可比行列式 $|J|$**。三维降维完美自洽。

### Case 2: 显式曲面 $z = f(x,y)$ (最常用)
* $\sigma_x = (1, 0, f_x)$, $\sigma_y = (0, 1, f_y)$
* 法向量：$\sigma_x \times \sigma_y = (-f_x, -f_y, 1)$
* **结论 (拉伸系数)：** $dS = \sqrt{1 + f_x^2 + f_y^2} \,dxdy$
* **面积公式：** $\text{Area}(\Sigma) = \iint_D \sqrt{1 + f_x^2 + f_y^2} \,dxdy$

### Case 3: 隐式曲面 $F(x,y,z) = 0$
* 利用隐函数求导法则 (Implicit Function Theorem)：
    $f_x = -\frac{F_x}{F_z}$, $f_y = -\frac{F_y}{F_z}$
* 代入 Case 2 的叉乘模长公式：
    $|\sigma_x \times \sigma_y| = \left| \left(\frac{F_x}{F_z}, \frac{F_y}{F_z}, 1\right) \right| = \frac{1}{|F_z|} \sqrt{F_x^2 + F_y^2 + F_z^2} = \frac{|\nabla F|}{|F_z|}$
* **结论 (拉伸系数)：** $dS = \frac{|\nabla F|}{|F_z|} \,dxdy$

---

## 5. 综合计算大题 (The Cone Example)

**题目：**
计算积分 $\iint_\Sigma (x^2+y^2+z^2) \,dS$，其中曲面 $\Sigma$ 为圆锥面 $z = \sqrt{x^2+y^2}$，且位于 $xy$ 平面区域 $x^2+y^2 \le 2x$ 的正上方。

**Step 1: 确定参数化与投影区域 $D$**
* 曲面为显式函数 $z = \sqrt{x^2+y^2}$，直接使用 $(x,y)$ 作为参数。
* 投影区域 $D$: $x^2+y^2 \le 2x \implies (x-1)^2+y^2 \le 1$ (圆心在 $(1,0)$，半径为 $1$ 的圆)。

**Step 2: 计算拉伸系数 $dS$**
* 套用公式：$dS = \sqrt{1 + z_x^2 + z_y^2} \,dxdy$
* $z_x = \frac{x}{\sqrt{x^2+y^2}}, \quad z_y = \frac{y}{\sqrt{x^2+y^2}}$
* $z_x^2 + z_y^2 = \frac{x^2+y^2}{x^2+y^2} = 1$
* $dS = \sqrt{1 + 1} \,dxdy = \sqrt{2} \,dxdy$

**Step 3: 将被积函数降维并转换极坐标**
* 将 $z$ 替换掉：$f(x,y,z) = x^2+y^2 + (\sqrt{x^2+y^2})^2 = 2(x^2+y^2)$
* 组装二重积分：
    $I = \iint_D 2(x^2+y^2) \cdot \sqrt{2} \,dxdy = 2\sqrt{2} \iint_D (x^2+y^2) \,dxdy$
* 转极坐标 $(x=r\cos\theta, y=r\sin\theta, dxdy=rdrd\theta)$：
    边界 $x^2+y^2 \le 2x \implies r^2 \le 2r\cos\theta \implies 0 \le r \le 2\cos\theta$
    角度范围：$-\frac{\pi}{2} \le \theta \le \frac{\pi}{2}$

**Step 4: 积分计算过程**
$$I = 2\sqrt{2} \int_{-\pi/2}^{\pi/2} \int_0^{2\cos\theta} (r^2) \cdot r \,dr d\theta$$

先对 $r$ 积分：
$$\int_0^{2\cos\theta} r^3 \,dr = \left[ \frac{1}{4}r^4 \right]_0^{2\cos\theta} = \frac{1}{4}(16\cos^4\theta) = 4\cos^4\theta$$

代回外层对 $\theta$ 积分 (利用偶函数对称性)：
$$I = 2\sqrt{2} \int_{-\pi/2}^{\pi/2} 4\cos^4\theta \,d\theta = 8\sqrt{2} \times 2 \int_0^{\pi/2} \cos^4\theta \,d\theta$$
$$I = 16\sqrt{2} \int_0^{\pi/2} \cos^4\theta \,d\theta$$

利用华里士公式 (Wallis' Formula) $\int_0^{\pi/2} \cos^4\theta \,d\theta = \frac{3!!}{4!!}\frac{\pi}{2} = \frac{3}{4} \cdot \frac{1}{2} \cdot \frac{\pi}{2} = \frac{3\pi}{16}$：
$$I = 16\sqrt{2} \left( \frac{3\pi}{16} \right) = \mathbf{3\sqrt{2}\pi}$$# 向量微积分笔记：三维曲面与第一类曲面积分
*(Surfaces in $\mathbb{R}^3$ & Surface Integrals of Scalar Functions)*

---

## 1. 核心概念升维：从曲线到曲面

### 1.1 一维曲线 (Curves) 的回顾
* **本质：** 三维空间中的单参数子集 (1-parameter subsets)。
* **参数化：** $\gamma(t) = (x(t), y(t), z(t)), \quad t \in [a, b]$
* **切向量：** $\gamma'(t) = (x'(t), y'(t), z'(t))$

### 1.2 二维曲面 (Surfaces) 的定义
* **本质：** 三维空间中的双参数子集 (2-parameter subsets)。记为 $\Sigma$。
* **参数化：** $\sigma: D \subseteq \mathbb{R}^2 \to \mathbb{R}^3$
    $$\sigma(u,v) = (x(u,v), y(u,v), z(u,v))$$
* **两个切向量：** 沿着网格线求偏导
    1.  $\sigma_u = \frac{\partial \sigma}{\partial u} = (x_u, y_u, z_u)$
    2.  $\sigma_v = \frac{\partial \sigma}{\partial v} = (x_v, y_v, z_v)$

### 1.3 切平面与曲面的“光滑”判定 (Smoothness)
由两个切向量叉乘得到**法向量 (Normal Vector)** $\vec{N}$：
$$\vec{N} = \sigma_u \times \sigma_v$$
* **光滑判定：** 若在定义域 $D$ 内恒有 $\vec{N} \neq \vec{0}$，则切平面始终存在，称该参数化曲面是**光滑的 (Smooth)**。

---

## 2. 描述曲面的三种方式

1.  **显式函数 (Graphs):** $z = f(x,y)$ 
    * 参数化最简单：$\sigma(x,y) = (x, y, f(x,y))$
2.  **隐式方程 (Sets of solutions):** $F(x,y,z) = 0$
3.  **参数化方程 (Parametrized surfaces):** $\sigma(u,v)$
    * 这是进行曲面积分时**最简单、最通用**的方式。

**【经典参数化案例】**
* **球面 (Sphere):** 半径为 $R$
    $\sigma(\theta, \phi) = (R\cos\theta\sin\phi, R\sin\theta\sin\phi, R\cos\phi)$
* **圆锥面 (Cone):** $z = \sqrt{x^2+y^2} \le h$
    $\sigma(\rho, \theta) = (\rho\cos\theta, \rho\sin\theta, \rho), \quad (0 \le \theta \le 2\pi, \ 0 \le \rho \le h)$

---

## 3. 第一类曲面积分 (对标量函数的积分)

**定义式：**
$$\iint_\Sigma f(x,y,z) \,dS \equiv \iint_D f(\sigma(u,v)) |\sigma_u \times \sigma_v| \,du dv$$
* **面积微元 (Surface differential):** $dS = |\sigma_u \times \sigma_v| dudv$
* **几何意义：** 物理上可理解为求弯曲薄片的总质量（$f$ 为密度）。当 $f=1$ 时，得到曲面的**表面积**。
    $$\text{Area}(\Sigma) = \iint_D |\sigma_u \times \sigma_v| \,du dv$$

---

## 4. 三种常见曲面的面积微元 $dS$ (快捷公式推导)

### Case 1: 退化为水平面 $z = z_0$
* $\sigma(u,v) = (x(u,v), y(u,v), z_0)$
* $\sigma_u = (x_u, y_u, 0)$, $\sigma_v = (x_v, y_v, 0)$
* **推导：** $|\sigma_u \times \sigma_v| = |(0, 0, x_u y_v - x_v y_u)| = |x_u y_v - x_v y_u|$
* **结论：** 这恰好是二维坐标变换的**雅可比行列式 $|J|$**。三维降维完美自洽。

### Case 2: 显式曲面 $z = f(x,y)$ (最常用)
* $\sigma_x = (1, 0, f_x)$, $\sigma_y = (0, 1, f_y)$
* 法向量：$\sigma_x \times \sigma_y = (-f_x, -f_y, 1)$
* **结论 (拉伸系数)：** $dS = \sqrt{1 + f_x^2 + f_y^2} \,dxdy$
* **面积公式：** $\text{Area}(\Sigma) = \iint_D \sqrt{1 + f_x^2 + f_y^2} \,dxdy$

### Case 3: 隐式曲面 $F(x,y,z) = 0$
* 利用隐函数求导法则 (Implicit Function Theorem)：
    $f_x = -\frac{F_x}{F_z}$, $f_y = -\frac{F_y}{F_z}$
* 代入 Case 2 的叉乘模长公式：
    $|\sigma_x \times \sigma_y| = \left| \left(\frac{F_x}{F_z}, \frac{F_y}{F_z}, 1\right) \right| = \frac{1}{|F_z|} \sqrt{F_x^2 + F_y^2 + F_z^2} = \frac{|\nabla F|}{|F_z|}$
* **结论 (拉伸系数)：** $dS = \frac{|\nabla F|}{|F_z|} \,dxdy$

---

## 5. 综合计算大题 (The Cone Example)

**题目：**
计算积分 $\iint_\Sigma (x^2+y^2+z^2) \,dS$，其中曲面 $\Sigma$ 为圆锥面 $z = \sqrt{x^2+y^2}$，且位于 $xy$ 平面区域 $x^2+y^2 \le 2x$ 的正上方。

**Step 1: 确定参数化与投影区域 $D$**
* 曲面为显式函数 $z = \sqrt{x^2+y^2}$，直接使用 $(x,y)$ 作为参数。
* 投影区域 $D$: $x^2+y^2 \le 2x \implies (x-1)^2+y^2 \le 1$ (圆心在 $(1,0)$，半径为 $1$ 的圆)。

**Step 2: 计算拉伸系数 $dS$**
* 套用公式：$dS = \sqrt{1 + z_x^2 + z_y^2} \,dxdy$
* $z_x = \frac{x}{\sqrt{x^2+y^2}}, \quad z_y = \frac{y}{\sqrt{x^2+y^2}}$
* $z_x^2 + z_y^2 = \frac{x^2+y^2}{x^2+y^2} = 1$
* $dS = \sqrt{1 + 1} \,dxdy = \sqrt{2} \,dxdy$

**Step 3: 将被积函数降维并转换极坐标**
* 将 $z$ 替换掉：$f(x,y,z) = x^2+y^2 + (\sqrt{x^2+y^2})^2 = 2(x^2+y^2)$
* 组装二重积分：
    $I = \iint_D 2(x^2+y^2) \cdot \sqrt{2} \,dxdy = 2\sqrt{2} \iint_D (x^2+y^2) \,dxdy$
* 转极坐标 $(x=r\cos\theta, y=r\sin\theta, dxdy=rdrd\theta)$：
    边界 $x^2+y^2 \le 2x \implies r^2 \le 2r\cos\theta \implies 0 \le r \le 2\cos\theta$
    角度范围：$-\frac{\pi}{2} \le \theta \le \frac{\pi}{2}$

**Step 4: 积分计算过程**
$$I = 2\sqrt{2} \int_{-\pi/2}^{\pi/2} \int_0^{2\cos\theta} (r^2) \cdot r \,dr d\theta$$

先对 $r$ 积分：
$$\int_0^{2\cos\theta} r^3 \,dr = \left[ \frac{1}{4}r^4 \right]_0^{2\cos\theta} = \frac{1}{4}(16\cos^4\theta) = 4\cos^4\theta$$

代回外层对 $\theta$ 积分 (利用偶函数对称性)：
$$I = 2\sqrt{2} \int_{-\pi/2}^{\pi/2} 4\cos^4\theta \,d\theta = 8\sqrt{2} \times 2 \int_0^{\pi/2} \cos^4\theta \,d\theta$$
$$I = 16\sqrt{2} \int_0^{\pi/2} \cos^4\theta \,d\theta$$

利用华里士公式 (Wallis' Formula) $\int_0^{\pi/2} \cos^4\theta \,d\theta = \frac{3!!}{4!!}\frac{\pi}{2} = \frac{3}{4} \cdot \frac{1}{2} \cdot \frac{\pi}{2} = \frac{3\pi}{16}$：
$$I = 16\sqrt{2} \left( \frac{3\pi}{16} \right) = \mathbf{3\sqrt{2}\pi}$$称性)：
$$I = 2\sqrt{2} \int_{-\pi/2}^{\pi/2} 4\cos^4\theta \,d\theta = 8\sqrt{2} \times 2 \int_0^{\pi/2} \cos^4\theta \,d\theta$$
$$I = 16\sqrt{2} \int_0^{\pi/2} \cos^4\theta \,d\theta$$

利用华里士公式 (Wallis' Formula) $\int_0^{\pi/2} \cos^4\theta \,d\theta = \frac{3!!}{4!!}\frac{\pi}{2} = \frac{3}{4} \cdot \frac{1}{2} \cdot \frac{\pi}{2} = \frac{3\pi}{16}$：
$$I = 16\sqrt{2} \left( \frac{3\pi}{16} \right) = \mathbf{3\sqrt{2}\pi}$$