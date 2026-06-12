# Calculus 2M 习题课 #11 —— 线积分与格林公式完整演练

---

## 一、 标量函数的线积分与质量计算

### 1. 核心知识点与技巧
设 $f: \mathbb{R}^3 \rightarrow \mathbb{R}$ 为标量函数，$\vec{r}(t) = (x(t), y(t), z(t))$ 是一条平滑曲线，参数 $t \in [a, b]$。线积分的定义及计算公式为：
$$\int_{\vec{r}} f \, dr = \int_a^b f(\vec{r}(t)) |\vec{r}'(t)| \, dt$$

💡 **Tips (解题思路)**：
* **弧长微元**：公式中的 $dr$ 对应的就是 $|\vec{r}'(t)| \, dt$。
* **三步法**：参数化曲线定边界 $\rightarrow$ 求导数算模长 $\rightarrow$ 替换变量做定积分。

---

### 【例题 1】求二维细圆环的总质量
**题目**：考虑一个二维的细圆环形薄片，方程为 $x^2 + y^2 = R^2$。设沿该圆环的质量密度函数为 $\rho(x,y) = |y|$。求该薄片的总质量。

#### 解析：
**Step 1：参数化曲线**
* **目的**：将二维方程转化为单变量参数形式，以便于积分。
* **过程**：令 $\vec{r}(t) = (R\cos t, R\sin t)$，圆环一圈对应的参数范围为 $t \in [0, 2\pi]$。即 $x(t) = R\cos t$，$y(t) = R\sin t$。

**Step 2：计算切向量与模长 (弧长微元)**
* **目的**：求出微小弧长片段对应的表达式 $|\vec{r}'(t)|dt$。
* **过程**：
  对 $\vec{r}(t)$ 求导：$\vec{r}'(t) = (-R\sin t, R\cos t)$
  求向量模长：$|\vec{r}'(t)| = \sqrt{(-R\sin t)^2 + (R\cos t)^2} = \sqrt{R^2(\sin^2 t + \cos^2 t)} = R$

**Step 3：代入公式并积分**
* **目的**：结合密度函数与弧长微元，计算最终结果。
* **过程**：
  $$\text{Mass} = \int_{\vec{r}} \rho(\vec{r}(t)) |\vec{r}'(t)| \, dt = \int_0^{2\pi} |R\sin t| \cdot R \, dt = R^2 \int_0^{2\pi} |\sin t| \, dt$$
  💡 **Tip (利用图像对称性化简)**：被积函数 $|\sin t|$ 在 $[0, 2\pi]$ 区间上的图像为两个面积相等的全正波峰。可以将其转化为半周期 $[0, \pi]$ 上积分的 2 倍：
  $$= 2R^2 \int_0^\pi \sin t \, dt$$
  $$= 2R^2 [-\cos t]_0^\pi = 2R^2(1 - (-1)) = 4R^2$$

**答案**：$4R^2$

---

## 二、 曲线弧长的计算

### 1. 核心知识点与技巧
当标量线积分的被积函数恒为 1，即 $f(\vec{r}(t)) \equiv 1$ 时，该积分在几何上直接表示参数曲线的**总弧长**：
$$L = \int_a^b |\vec{r}'(t)| \, dt$$

💡 **Tips**：
* 积分遇到 $\sqrt{1 - \cos t}$ 形式时，核心破局点是**半角公式**：$1 - \cos t = 2\sin^2(\frac{t}{2})$，用以脱去根号。

---

### 【例题 2】求摆线的弧长
**题目**：求半径为 $R$ 的轮子滚动一整圈后，其边缘上一点所形成的摆线（cycloid）的弧长。

#### 解析：
**Step 1：写出摆线参数方程及求导**
* **目的**：确立积分对象和边界条件。
* **过程**：摆线滚动一圈的标准参数方程为 $\vec{r}(t) = (R(t - \sin t), R(1 - \cos t))$，范围 $t \in [0, 2\pi]$。
  求导：$\vec{r}'(t) = (R(1 - \cos t), R\sin t)$

**Step 2：计算弧长微元 (展开与化简)**
* **目的**：求出切向量模长，将其化简为可积分的形式。
* **过程**：
  $$|\vec{r}'(t)| = \sqrt{R^2(1 - \cos t)^2 + (R\sin t)^2}$$
  $$= \sqrt{R^2(1 - 2\cos t + \cos^2 t) + R^2\sin^2 t}$$
  提出 $R^2$ 并应用 $\sin^2 t + \cos^2 t = 1$：
  $$= \sqrt{R^2(2 - 2\cos t)} = \sqrt{2}R\sqrt{1 - \cos t}$$

**Step 3：应用半角公式并定积分**
* **目的**：脱去根号，求出绝对值并在给定区间内积分。
* **过程**：
  $$\text{Length} = \int_0^{2\pi} \sqrt{2}R\sqrt{1 - \cos t} \, dt$$
  代入半角公式 $1 - \cos t = 2\sin^2(\frac{t}{2})$：
  $$= \int_0^{2\pi} \sqrt{2}R \sqrt{2\sin^2\left(\frac{t}{2}\right)} \, dt = 2R \int_0^{2\pi} \left|\sin\left(\frac{t}{2}\right)\right| \, dt$$
  由于 $t \in [0, 2\pi]$，则 $\frac{t}{2} \in [0, \pi]$，正弦值在此区间非负，直接去掉绝对值：
  $$= 2R \int_0^{2\pi} \sin\left(\frac{t}{2}\right) \, dt = 2R \left[ -2\cos\left(\frac{t}{2}\right) \right]_0^{2\pi} = -4R(\cos\pi - \cos 0) = -4R(-1 - 1) = 8R$$

**答案**：$8R$

---

## 三、 向量函数的线积分与路径代入技巧

### 1. 核心知识点与技巧
设向量场 $\vec{F} = (P, Q, R)$ 沿平滑曲线 $\vec{r}(t)$ 运动。线积分可用点乘表示，或展开为坐标微分形式：
$$\int_{\vec{r}} \vec{F} \cdot d\vec{r} = \int_{\vec{r}} Pdx + Qdy + Rdz$$

💡 **Tips**：
* 物理意义：相当于力 $\vec{F}$ 沿轨迹做的**功**。方向很重要。
* 计算技巧：当曲线路径平行于坐标轴（如水平或垂直线段）时，其对应的微分项（$dx, dy$ 或 $dz$）为 $0$。将其与常数坐标一同代入原式，可极大简化计算。

---

### 【例题 3】计算包含反正切原函数的线积分
**题目**：计算线积分 $\int_{\vec{r}} \frac{y}{x^2+y^2}dx + \frac{x}{x^2+y^2}dy$，假设路径为垂直直线 $x=1$，运动范围从 $y=1$ 到 $y=\sqrt{3}$。

#### 解析：
**方法一：常规换元积分法**
* **目的**：按部就班计算参数化后的定积分。
* **过程**：积分最终化简为 $\int_1^{\sqrt{3}} \frac{1}{1+t^2} \, dt$ 的形式。利用基础积分表求得原函数为反正切：
  $$[\arctan(t)]_1^{\sqrt{3}} = \arctan(\sqrt{3}) - \arctan(1) = \frac{\pi}{3} - \frac{\pi}{4} = \frac{\pi}{12}$$

**方法二：微分代入法 (Another way - 极简操作)**
* **目的**：利用特定路径的几何性质消去冗余项。
* **过程**：因为路径 $\vec{r}$ 是直线 $x=1$，其在 $x$ 轴方向没有位移变化，故微分 $dx = 0$。
  将 $x=1$ 和 $dx=0$ 强制代入原始微分式中：
  $$= \int_1^{\sqrt{3}} \frac{y}{1^2+y^2}(0) + \frac{1}{1^2+y^2}dy = \int_1^{\sqrt{3}} \frac{1}{1+y^2} \, dy$$
  一步到位化简为基本积分，结果同上为 $\frac{\pi}{12}$。

---

## 四、 格林公式 (Green's Theorem) 与路径转换

### 1. 核心知识点与技巧
设 $D$ 为平面区域，边界 $\partial D$ 为**正向闭合**（逆时针，区域始终在左侧）的光滑曲线。线积分转化为二重积分的公式为：
$$\int_{\partial D} Pdx + Qdy = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx dy$$

💡 **Tips**：
* **破局特征**：当被积函数 $P, Q$ 中存在极难积分的嵌套函数（如 $e^x\sin y$），但求偏导后 $Q_x - P_y$ 能相互抵消或变成常数时，必须用格林公式。若原路径不闭合，需手动补充辅助线封口。

---

### 【例题 4】化繁为简的非闭合路径线积分
**题目**：计算线积分 $I = \int_{\vec{r}} \underbrace{(e^x \sin y - y)}_{P}dx + \underbrace{(e^x \cos y - 1)}_{Q}dy$。
路径 $\vec{r}$ 由方程 $x^2 + y^2 = ax \ (y > 0, a > 0)$ 给定，方向为从 $(a, 0)$ 运动到 $(0, 0)$。

#### 解析：

<div style="color: #888888;">
<b>【错误探索：直接参数化】</b><br>
曲线配方为 $(x - \frac{a}{2})^2 + y^2 = (\frac{a}{2})^2$，是上半圆。设 $\vec{r}(t) = (\frac{a}{2} - \frac{a}{2}\cos t, \frac{a}{2}\sin t)$。若强行代入 $Pdx + Qdy$，会出现 $e^{\cos t}\sin(\sin t)$ 这类无法求原函数的复杂项。该方法走不通（Difficult!!）。
</div>

<br>

**【正确途径：利用格林公式转换路径】**

**Step 1：构建正向闭合曲线**
* **目的**：满足格林公式的“闭合”前提条件。
* **过程**：记原上半圆路径为 $r_1$。在 $x$ 轴上补充一条直线段 $r_2$，从 $(0,0)$ 指向 $(a,0)$。
  两段首尾相连形成闭合边界 $\partial D = r_1 \cup r_2$。验证方向：沿 $r_1$ 再沿 $r_2$ 行走，半圆区域 $D$ 始终在左手边，符合正向要求。

**Step 2：建立格林公式等式并移项**
* **目的**：分离出我们要求解的目标 $r_1$ 积分。
* **过程**：
  $$\int_{r_1 \cup r_2} Pdx + Qdy = \iint_D (Q_x - P_y) dx dy$$
  根据可加性展开并移项：
  $$\underbrace{\int_{r_1} Pdx + Qdy}_{\text{目标 (We need this)}} = \iint_D (Q_x - P_y) dx dy - \underbrace{\int_{r_2} Pdx + Qdy}_{\text{辅助线 (We don't need)}}$$

**Step 3：计算偏导数与二重积分**
* **目的**：利用偏导差消去恶心的超越函数。
* **过程**：
  $Q_x = \frac{\partial}{\partial x}(e^x \cos y - 1) = e^x \cos y$
  $P_y = \frac{\partial}{\partial y}(e^x \sin y - y) = e^x \cos y - 1$
  作差：$Q_x - P_y = e^x \cos y - (e^x \cos y - 1) = 1$。
  复杂的函数神奇消失！二重积分转化为求半圆面积：
  $$\iint_D 1 \, dx dy = \text{Area}(D) = \frac{1}{2} \cdot \pi \left(\frac{a}{2}\right)^2 = \frac{\pi a^2}{8}$$

**Step 4：计算辅助直线 $r_2$ 的线积分**
* **目的**：求出辅助部分的积分值，准备相减。
* **过程**：在直线 $r_2$ 上，$y$ 恒为 $0$，故微元 $dy = 0$，$x$ 从 $0 \rightarrow a$。代入原函数：
  $$\int_{r_2} Pdx + Qdy = \int_0^a (e^x \sin(0) - 0) dx + 0 = \int_0^a 0 \, dx = 0$$

**Step 5：求最终结果**
* **目的**：整合计算结果，得出答案。
* **过程**：将 Step 3 与 Step 4 的结果代回 Step 2 的等式：
  $$I = \int_{r_1} = \frac{\pi a^2}{8} - 0 = \frac{\pi a^2}{8}$$

**答案**：$\frac{\pi a^2}{8}$