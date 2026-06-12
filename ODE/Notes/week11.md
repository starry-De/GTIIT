# 常系数齐次线性微分方程组的推导与求解

## 1. 从一阶方程到方程组的演进

### 一元一阶常微分方程
对于单一变量 $x(t)$，最基础的线性变化模型为变化率与自身成正比：
$$x'(t) = a x(t)$$
其解为经典的指数函数：
$$x(t) = C e^{at}$$

### 线性常微分方程组
当系统包含多个相互耦合、互相影响的变量时（以二维系统为例），各自的变化率由所有变量共同决定：
$$
\begin{cases}
x_1'(t) = a_{11}x_1(t) + a_{12}x_2(t) \\
x_2'(t) = a_{21}x_1(t) + a_{22}x_2(t)
\end{cases}
$$

引入状态向量 $\vec{X}(t) = \begin{pmatrix} x_1(t) \\ x_2(t) \end{pmatrix}$ 和系数矩阵 $A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}$，可将方程组写为矩阵形式：
$$\vec{X}' = A\vec{X}$$

---

## 2. 求解过程与理论通解的推导

### 核心假设
延续单变量的指数解特性，假设高维方程组的解具有如下形式：
$$\vec{X}(t) = \vec{v} e^{\lambda t} \quad (\vec{v} \neq \vec{0})$$
其中，常数 $\lambda$ 决定变化速率，常数向量 $\vec{v}$ 决定空间方向。

### 代入化简
将假设解代入方程 $\vec{X}' = A\vec{X}$ 的左右两边：
* **左边（求导）**：$$\vec{X}' = \frac{d}{dt}(\vec{v} e^{\lambda t}) = \lambda \vec{v} e^{\lambda t}$$
* **右边（相乘）**：$$A\vec{X} = A(\vec{v} e^{\lambda t}) = A\vec{v} e^{\lambda t}$$

令两边相等并约去不为零的 $e^{\lambda t}$，化简得：
$$A\vec{v} = \lambda \vec{v}$$
这表明：**求微分方程组的解，等价于求矩阵 $A$ 的特征值 $\lambda$ 和特征向量 $\vec{v}$。**

### 求解代数条件
将上式移项变形为：
$$(A - \lambda I)\vec{v} = \vec{0}$$
若想存在非零解 $\vec{v}$，系数矩阵 $(A - \lambda I)$ 必须不可逆，即其行列式必须为零：
$$\det(A - \lambda I) = 0$$

### 理论通解的构造
1. 通过求解特征方程 $\det(A - \lambda I) = 0$，可得到两个特征值 $\lambda_1$ 和 $\lambda_2$。
2. 将 $\lambda_1, \lambda_2$ 分别代回方程 $(A - \lambda I)\vec{v} = \vec{0}$，解出对应的两个独立特征向量 $\vec{v}_1$ 和 $\vec{v}_2$。
3. 此时得到两个基础特解：$\vec{X}_1(t) = \vec{v}_1 e^{\lambda_1 t}$ 和 $\vec{X}_2(t) = \vec{v}_2 e^{\lambda_2 t}$。
4. 根据线性系统的**叠加原理**，方程组的**理论通解**即为这两个特解的线性组合：
$$\vec{X}(t) = c_1 \vec{v}_1 e^{\lambda_1 t} + c_2 \vec{v}_2 e^{\lambda_2 t}$$

---

## 3. 经典例题详细求解流程

**题目**：求解微分方程组 $\vec{X}' = \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix} \vec{X}$

### 第一步：求特征值 $\lambda$
列出特征方程 $\det(A - \lambda I) = 0$：
$$\det \begin{pmatrix} 1 - \lambda & 2 \\ 3 & 2 - \lambda \end{pmatrix} = 0 \implies (1 - \lambda)(2 - \lambda) - 6 = 0$$
$$\lambda^2 - 3\lambda - 4 = 0 \implies (\lambda - 4)(\lambda + 1) = 0$$
解得特征值：
$$\lambda_1 = 4, \quad \lambda_2 = -1$$

### 第二步：求对应的特征向量 $\vec{v}$

* **当 $\lambda_1 = 4$ 时**：
  代入 $(A - 4I)\vec{v}_1 = \vec{0}$：
  $$\begin{pmatrix} -3 & 2 \\ 3 & -2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies -3x + 2y = 0$$
  取最简整数解，得到第一个特征向量：
  $$\vec{v}_1 = \begin{pmatrix} 2 \\ 3 \end{pmatrix}$$

* **当 $\lambda_2 = -1$ 时**：
  代入 $(A - (-1)I)\vec{v}_2 = \vec{0}$：
  $$\begin{pmatrix} 2 & 2 \\ 3 & 3 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies x + y = 0$$
  取最简整数解，得到第二个特征向量：
  $$\vec{v}_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$$

### 第三步：组装最终通解并分析几何流向
将求得的特征值 and 特征向量代入理论通解公式，得到最终通解：
$$\vec{X}(t) = c_1 \begin{pmatrix} 2 \\ 3 \end{pmatrix} e^{4t} + c_2 \begin{pmatrix} 1 \\ -1 \end{pmatrix} e^{-t}$$

**几何特征与相图流向**：
* 沿着直线 $\vec{v}_1 = \begin{pmatrix} 2 \\ 3 \end{pmatrix}$ 方向（斜率 $y = 1.5x$），由于 $\lambda_1 = 4 > 0$，流向**背离原点向外**。
* 沿着直线 $\vec{v}_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$ 方向（斜率 $y = -x$），由于 $\lambda_2 = -1 < 0$，流向**指向原点向内**。
* 一正一负的特征值导致平面上的其他轨迹呈现双曲线形态：先向原点靠拢，随后被排斥轨道甩出。这种几何结构在数学上被称为**鞍点 (Saddle Point)**


# 常系数齐次线性微分方程组：相图分类与几何流向全解

在理解了 $\vec{X}' = A\vec{X}$ 的基本求解逻辑后，系统的几何流向（相图 Phase Portrait）取决于矩阵 $A$ 的**特征值性质**。以下结合全新白板课程内容，对相图的经典分类、几何轨迹判定以及基解矩阵进行由浅入深的系统梳理。

---

## 1. 相图的核心判别准则

系统的命运由通解公式中的指数项 $e^{\lambda t}$ 决定。若特征值 $\lambda$ 为实数：
* $\lambda > 0$：该特征向量方向为**排斥轴**（流向向外发散）。
* $\lambda < 0$：该特征向量方向为**吸引轴**（流向向内收敛）。

根据两个特征值的正负组合，相图主要分为以下三大经典几何流向类型。

---

## 2. 相图三大经典类型详解（结合白板案例）

### 类型一：鞍点 (Saddle Point) —— 一正一负
* **代数条件**：$\lambda_1, \lambda_2 \in \mathbb{R}$ 且 $\lambda_1 \cdot \lambda_2 < 0$（异号）。

#### 【白板案例重现】
系统通解为：
$$\vec{X}(t) = c_1 \begin{pmatrix} 1 \\ 2 \end{pmatrix} e^{-t} + c_2 \begin{pmatrix} 4 \\ -2 \end{pmatrix} e^{3t}$$

#### 几何流向拆解：
1. **稳定主轴（吸引）**：沿着 $\vec{v}_1 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$ 方向，由于 $\lambda_1 = -1 < 0$，流向在 $t \to \infty$ 时被死死**吸向原点**。
2. **不稳定主轴（排斥）**：沿着 $\vec{v}_2 = \begin{pmatrix} 4 \\ -2 \end{pmatrix}$ 方向，由于 $\lambda_2 = 3 > 0$，流向在 $t \to \infty$ 时飞速**逃离原点**。
3. **全景流向**：空间中任意其他初始点均受两股力量拉扯，轨迹呈现双曲线形态。由于原点同时具备吸引和排斥属性，该平衡点被称为**鞍点**。

---

### 类型二：不稳定节点 (Unstable Node) —— 同为正数
* **代数条件**：$\lambda_1, \lambda_2 \in \mathbb{R}$ 且 $\lambda_1, \lambda_2 > 0$（同正）。

#### 【白板案例重现】
方程组为 $\vec{X}' = \begin{pmatrix} 2 & -1 \\ -2 & 3 \end{pmatrix} \vec{X}$，其特征方程为 $\lambda^2 - 5\lambda + 4 = 0$，解得：
$$\lambda_1 = 1 \implies \vec{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \quad \lambda_2 = 4 \implies \vec{v}_2 = \begin{pmatrix} 1 \\ -2 \end{pmatrix}$$
系统通解为：
$$\vec{X}(t) = c_1 \begin{pmatrix} 1 \\ 1 \end{pmatrix} e^{t} + c_2 \begin{pmatrix} 1 \\ -2 \end{pmatrix} e^{4t}$$

#### 几何流向拆解：
1. **全向发散**：由于两个特征值均大于 0，随着 $t \to \infty$，所有轨迹最终都会**彻底逃离原点**（原点为源头 Source）。
2. **轨迹弯曲规律（快慢轴协作）**：
   * $\lambda_2 = 4$ 为**快轴**，增长极快；$\lambda_1 = 1$ 为**慢轴**，增长较慢。
   * 当 $t \to -\infty$（反向追溯历史）时，快轴衰减得远比慢轴快，因此所有轨迹在靠近原点时，都会**切于慢轴 $\vec{v}_1$**。
   * 当 $t \to \infty$（展望未来）时，快轴主导一切，因此远离原点时，轨迹会**平行于快轴 $\vec{v}_2$**。
   * 白板中推导的 $e^{4t} = (e^t)^4$（即 $y = x^4$ 关系），完美解释了非线性弯曲的几何成因。

> **补充说明**：同理，若 $\lambda_1, \lambda_2 < 0$（同负），流向完全反向，所有轨迹最终汇聚于原点，称为**稳定节点 (Stable Node / Sink)**。

---

### 类型三：稳定星形节点 (Stable "Star" Node) —— 重根简并
* **代数条件**：$\lambda_1 = \lambda_2 = \lambda < 0$（重根），且矩阵 $A$ 拥有两个线性独立的特征向量。

#### 【白板案例重现】
方程组为 $\vec{X}' = \begin{pmatrix} -3 & 0 \\ 0 & -3 \end{pmatrix} \vec{X}$。此时矩阵 $A = -3I$。
特征值为 $\lambda = -3$（重根）。

#### 几何流向拆解：
1. **全向量皆为特征向量**：由于 $A = -3I$，对于平面上任意非零向量 $\vec{v}$，均满足 $A\vec{v} = -3\vec{v}$。这意味着空间中**任意方向都是主干道**。
2. **完美直线汇聚**：系统通解可以直接写为：
   $$\vec{X}(t) = c_1 \begin{pmatrix} 1 \\ 0 \end{pmatrix} e^{-3t} + c_2 \begin{pmatrix} 0 \\ 1 \end{pmatrix} e^{-3t} = e^{-3t} \vec{X}_0$$
   由于没有快慢轴的拉扯，轨迹完全不发生任何弯曲。平面上所有的点都沿着各自方向的绝对直线，以相同的速率收敛于原点。在相图上呈现对称的**星形 (Star)**，称为**稳定星形节点**。

---

## 3. 理论进阶：基解矩阵 (Fundamental Matrix) 与初值求解

白板左下角引入了现代控制理论和高级微分方程中极其重要的概念——**基解矩阵 $\Psi(t)$**。

### 1. 概念定义
将相互独立的特解作为列向量横向拼成一个矩阵，这个矩阵就叫**基解矩阵**：
$$\Psi(t) = \begin{pmatrix} \vec{X}^{(1)}(t) & \Big| & \vec{X}^{(2)}(t) \end{pmatrix} = \begin{pmatrix} e^{-t} & & e^{3t} \\ 2e^{-t} & & -2e^{3t} \end{pmatrix}$$
利用基解矩阵，系统的通解公式可以从复杂的叠加形式精简为简洁的**矩阵乘法**：
$$\vec{X}(t) = \Psi(t) \vec{C} \quad \text{其中} \ \vec{C} = \begin{pmatrix} c_1 \\ c_2 \end{pmatrix}$$

### 2. 初始条件求解 (IVP)
如果系统给定了 $t = t_0$ 时刻的初始状态 $\vec{X}(t_0) = \vec{X}_0$，我们可以通过矩阵求逆直接秒杀常数向量 $\vec{C}$：
$$\vec{X}_0 = \Psi(t_0) \vec{C} \implies \vec{C} = \Psi^{-1}(t_0) \vec{X}_0$$

---

## 4. 常系数齐次线性方程组相图大总结

| 特征值性质 ($\lambda_1, \lambda_2$) | 平衡点几何名称 (Phase Portrait) | 原点稳定性 (Stability) | 轨迹几何形态描述 |
| :--- | :--- | :--- | :--- |
| **一正一负** ($\lambda_1 \cdot \lambda_2 < 0$) | **鞍点 (Saddle Point)** | 不稳定 | 沿一条轴吸入，沿另一条轴喷出，双曲线轨迹 |
| **同为正数** ($\lambda_1, \lambda_2 > 0$) | **不稳定节点 (Unstable Node)** | 不稳定 (Source) | 全向发散，靠近原点时切于慢轴，远离时平行于快轴 |
| **同为负数** ($\lambda_1, \lambda_2 < 0$) | **稳定节点 (Stable Node)** | 渐进稳定 (Sink) | 全向收敛，轨迹弯曲规律与不稳定节点相同，但方向朝内 |
| **相等且同负** ($A = \lambda I$) | **星形节点 (Star Node)** | 渐进稳定 (Sink) | 绝不弯曲，全空间所有点沿直线笔直刺向原点 |