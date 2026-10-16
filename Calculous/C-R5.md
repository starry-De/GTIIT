你好！期末复习进入到了最核心也是最容易拉开差距的部分。第五周（Lecture 9 & 10）的内容全面展开了**多元函数的可微性（Differentiability）、方向导数（Directional Derivative）、梯度（Gradient）以及多元复合函数求导的链式法则（Chain Rule）**。

这里有大量的理论证明，尤其是“可微”与“连续”、“偏导数存在”之间的逻辑关系，是期末考试证明题和判断题的重灾区。我已经为你整理了最纯净、无干扰的复习讲义，包含完整的定理证明。

---

# 微积分 2M 期末复习讲义 (Lecture 9 & 10)

## 一、 多元函数的可微性 (Differentiability)

我们之前发现，仅有偏导数存在，甚至不足以保证函数连续。因此我们需要一个比“偏导数存在”更强的概念——**可微（Differentiable）**，它代表函数在某点附近能被一个平面（切平面）完美地线性逼近。

### 1. 严格定义
函数 $f(x,y)$ 在点 $(x_0, y_0)$ 可微，当且仅当存在常数 $A, B \in \mathbb{R}$，使得：
$$f(x_0+h, y_0+k) - f(x_0, y_0) = A\cdot h + B\cdot k + \alpha(h,k)\sqrt{h^2+k^2}$$
并且满足当 $(h,k) \to -(0,0)$ 时，余项 $\alpha(h,k) \to 0$。

### 2. 三大核心定理与完整证明

> **定理 1：可微必定导致偏导数存在（且揭示 A, B 的真面目）**
> **内容**：如果 $f$ 在 $(x_0, y_0)$ 可微，那么它在该点的偏导数必然存在，且 $A = \frac{\partial f}{\partial x}(x_0, y_0)$， $B = \frac{\partial f}{\partial y}(x_0, y_0)$。
> **完整证明**：
> 1. 根据可微的定义，令 $k = 0$（即只在 $x$ 方向产生增量 $h$），代入定义式得：
>    $f(x_0+h, y_0) - f(x_0, y_0) = A\cdot h + \alpha(h,0)\sqrt{h^2+0^2} = A\cdot h + \alpha(h,0)|h|$
> 2. 两边同除以 $h$：
>    $\frac{f(x_0+h, y_0) - f(x_0, y_0)}{h} = A + \alpha(h,0)\frac{|h|}{h}$
> 3. 对两边取极限 $h \to 0$。因为 $\lim_{h\to 0}\alpha(h,0) = 0$，且 $\frac{|h|}{h} = \pm 1$ 是有界的，所以后面那一项的极限为 0。
> 4. 左边的极限正是对 $x$ 的偏导数定义。因此 $\frac{\partial f}{\partial x}(x_0, y_0) = A$。同理，令 $h=0$ 可证 $B = \frac{\partial f}{\partial y}$。得证。

> **定理 2：可微必定连续 (Differentiability $\implies$ Continuity)**
> **内容**：如果 $f$ 在 $(x_0, y_0)$ 可微，那么它在该点连续。
> **完整证明**：
> 1. 考察函数值的增量在 $(h,k) \to (0,0)$ 时的极限：
>    $\lim_{(h,k)\to(0,0)} [f(x_0+h, y_0+k) - f(x_0, y_0)]$
> 2. 将可微的定义式代入：
>    $= \lim_{(h,k)\to(0,0)} [A h + B k + \alpha(h,k)\sqrt{h^2+k^2}]$
> 3. 显然，当 $h \to 0, k \to 0$ 且 $\alpha \to 0$ 时，上式整体的极限为 $0 + 0 + 0 = 0$。
> 4. 即 $\lim_{(h,k)\to(0,0)} f(x_0+h, y_0+k) = f(x_0, y_0)$。这正是连续的定义。得证。

> **定理 3：偏导数连续必定可微 ($f \in C^1 \implies$ Differentiable)**
> **内容**：如果 $f$ 的偏导数在 $(x_0,y_0)$ 的某个邻域内不仅存在，而且是**连续**的（记作 $f \in C^1$），那么 $f$ 在该点必定可微。
> *(注：此定理证明较复杂，PPT中要求 Skipped，但结论必须牢记：连续偏导是可微的充分条件)*。

---

## 二、 方向导数与梯度 (Directional Derivative & Gradient)

### 1. 方向导数
方向导数衡量的是函数沿着某个**特定方向单位向量 $\hat{u} = (u_1, u_2)$**（注意：必须是单位向量，$u_1^2+u_2^2=1$）的变化率。
* **定义**：$\frac{\partial f}{\partial \hat{u}}(x_0,y_0) = \lim_{h\to 0} \frac{f(x_0+hu_1, y_0+hu_2) - f(x_0, y_0)}{h}$

> **定理 4：可微函数的方向导数计算公式**
> **内容**：如果 $f$ 在 $(x_0,y_0)$ 处 $C^1$（或可微），则沿方向 $\hat{u} = (u_1, u_2)$ 的方向导数为：
> $\frac{\partial f}{\partial \hat{u}} = \frac{\partial f}{\partial x}u_1 + \frac{\partial f}{\partial y}u_2$
> **完整证明**：
> 1. 因为 $f$ 可微，利用可微的定义，将增量 $\Delta x = hu_1, \Delta y = hu_2$ 代入：
>    $f(x_0+hu_1, y_0+hu_2) - f(x_0, y_0) = f_x \cdot (hu_1) + f_y \cdot (hu_2) + \alpha \sqrt{(hu_1)^2+(hu_2)^2}$
> 2. 提取 $h$，且因为 $u_1^2+u_2^2=1$，根号项变为 $|h|$：
>    $= h(f_x u_1 + f_y u_2) + \alpha |h|$
> 3. 两边同除以 $h$ 并取极限 $h \to 0$：
>    $\lim_{h\to 0} \frac{\Delta f}{h} = \lim_{h\to 0} [f_x u_1 + f_y u_2 + \alpha \frac{|h|}{h}]$
> 4. 因为 $\alpha \to 0$ 且 $\frac{|h|}{h}$ 有界，所以最后一项为 0。最终得到 $f_x u_1 + f_y u_2$。得证。

### 2. 梯度向量 (Gradient)
* **定义**：梯度是一个向量场，由所有的偏导数组成：$\nabla f = (\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y})$。
* **方向导数与梯度的内积形式**：根据定理4，$\frac{\partial f}{\partial \hat{u}} = \nabla f \cdot \hat{u} = |\nabla f| |\hat{u}| \cos\theta = |\nabla f| \cos\theta$。
* **核心几何意义**：
    * **最陡上升方向 (Steepest ascent)**：当 $\theta = 0$ 时，方向导数最大。即**梯度 $\nabla f$ 总是指向函数值增加最快的方向**。
    * **等值线正交**：当 $\theta = 90^\circ$ 时，方向导数为 0（函数值不变）。说明**梯度垂直于等值线（或等值面）**。

---

## 三、 多元复合函数的链式法则 (The Chain Rule)

类似于一元函数的剥洋葱，多元函数如果包含中间变量，全导数或偏导数需要沿着路径累加。

### 情境 1：一个独立变量 $t$
已知 $f(x,y)$，且 $x=x(t), y=y(t)$。令 $F(t) = f(x(t), y(t))$。
**公式**：$\frac{dF}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}$
*（就像两根树杈，求导时要分别走过 $x$ 树杈和 $y$ 树杈，最后相加）*

### 情境 2：两个独立变量 $u, v$
已知 $f(x,y)$，且 $x=x(u,v), y=y(u,v)$。令 $F(u,v) = f(x(u,v), y(u,v))$。
**公式**：
* 对 $u$ 求导：$\frac{\partial F}{\partial u} = \frac{\partial f}{\partial x}\frac{\partial x}{\partial u} + \frac{\partial f}{\partial y}\frac{\partial y}{\partial u}$
* 对 $v$ 求导：$\frac{\partial F}{\partial v} = \frac{\partial f}{\partial x}\frac{\partial x}{\partial v} + \frac{\partial f}{\partial y}\frac{\partial y}{\partial v}$

---

## 四、 重点例题详细解析

**【例题 1：利用定义证明函数可微】 (来源 Lecture 9)**
**题目**：已知 $f(x,y) = \frac{x^2y}{\sqrt{x^2+y^2}}$ (原点外)，$f(0,0)=0$。证明 $f$ 在 $(0,0)$ 处可微。
**解析**：
1. **求偏导数 $A, B$**：
   $A = f_x(0,0) = \lim_{h\to 0} \frac{f(h,0)-0}{h} = \lim_{h\to 0} \frac{0}{h} = 0$。
   $B = f_y(0,0) = \lim_{k\to 0} \frac{f(0,k)-0}{k} = \lim_{k\to 0} \frac{0}{k} = 0$。
2. **利用定义校验余项 $\alpha(h,k)$**：
   $\alpha(h,k) = \frac{f(h,k) - f(0,0) - Ah - Bk}{\sqrt{h^2+k^2}} = \frac{\frac{h^2k}{\sqrt{h^2+k^2}} - 0 - 0 - 0}{\sqrt{h^2+k^2}} = \frac{h^2k}{h^2+k^2}$。
3. **考察 $\lim_{(h,k)\to(0,0)} \alpha(h,k)$**：
   使用极坐标 $h = r\cos\theta, k = r\sin\theta$。
   $\alpha(r,\theta) = \frac{r^2\cos^2\theta \cdot r\sin\theta}{r^2} = r\cos^2\theta\sin\theta$。
   当 $r \to 0$ 时，显然 $\alpha \to 0$。
4. **结论**：因为余项极限为 0，所以函数在 $(0,0)$ 处可微。

**【例题 2：偏导存在，方向导数公式却失效的反例】 (来源 Lecture 10)**
**题目**：考虑 $f(x,y) = \sqrt[3]{xy^2}$。它在 $(0,0)$ 的偏导数是多少？它的方向导数能否用 $\nabla f \cdot \hat{u}$ 计算？它可微吗？
**解析**：
1. **求偏导数**：$f_x(0,0) = \lim_{h\to 0} \frac{0-0}{h}=0$，$f_y(0,0) = \lim_{k\to 0} \frac{0-0}{k}=0$。所以 $\nabla f(0,0) = (0,0)$。
2. **用定义求方向导数 $\hat{u} = (u_1, u_2)$**：
   $\frac{\partial f}{\partial \hat{u}}(0,0) = \lim_{h\to 0} \frac{f(hu_1, hu_2) - 0}{h} = \lim_{h\to 0} \frac{\sqrt[3]{h^3 u_1 u_2^2}}{h} = \sqrt[3]{u_1 u_2^2}$。
3. **验证公式**：$\nabla f \cdot \hat{u} = (0,0) \cdot (u_1, u_2) = 0$。
   但是我们用定义算出来的方向导数是 $\sqrt[3]{u_1 u_2^2} \neq 0$！
4. **结论**：公式 $\frac{\partial f}{\partial \hat{u}} = \nabla f \cdot \hat{u}$ 失败了！为什么？因为这个公式的前提是函数必须**可微**。这反证了该函数在 $(0,0)$ 处**不可微**。

**【例题 3：链式法则应用】 (来源 Lecture 10)**
**题目**：设 $f(x,y) = e^{x^2y}$，其中 $x(u,v) = \sqrt{uv}$， $y(u,v) = \frac{1}{v}$。求 $\frac{\partial F}{\partial u}$。
**解析**：
* 方法一（链式法则）：
  $\frac{\partial F}{\partial u} = \frac{\partial f}{\partial x}\frac{\partial x}{\partial u} + \frac{\partial f}{\partial y}\frac{\partial y}{\partial u}$
  $= (2xy e^{x^2y}) \cdot (\frac{1}{2}\sqrt{\frac{v}{u}}) + (x^2 e^{x^2y}) \cdot 0$
  $= 2(\sqrt{uv})(\frac{1}{v})e^{(\sqrt{uv})^2(1/v)} \cdot \frac{\sqrt{v}}{2\sqrt{u}} = 2\frac{\sqrt{u}}{\sqrt{v}}e^u \cdot \frac{\sqrt{v}}{2\sqrt{u}} = e^u$。
* 方法二（直接代入，适合用来检查）：
  $F(u,v) = e^{(\sqrt{uv})^2 \cdot (1/v)} = e^{uv \cdot \frac{1}{v}} = e^u$。
  对其求 $u$ 的偏导，直接得到 $e^u$。结果一致！

---

## 五、 考前查漏补缺自测题

建议手写以下几题，检验对梯度的几何意义和链式法则的掌握：

**题目 1：方向导数与梯度**
已知函数 $f(x,y) = 3x^2 - 2y^2$。
(1) 求出该函数在点 $(1, 1)$ 处的梯度 $\nabla f(1,1)$。
(2) 求出在该点处，函数值增加最快的方向（用单位向量表示）及其最大变化率。
(3) 计算该函数在点 $(1, 1)$ 沿从原点指向点 $(3, 4)$ 方向的方向导数。

**题目 2：链式法则全导数**
设 $z = x^2 y + xy^2$，其中 $x = \cos t$, $y = \sin t$。
利用链式法则求出全导数 $\frac{dz}{dt}$，并将结果化简。（不需要化成只含 $t$ 的完全三角函数式，但必须合并同类项）。

**题目 3：可微性的真假辨析（非常典型）**
判断对错并简述理由：如果 $f(x,y)$ 在 $(a,b)$ 的两个偏导数 $\frac{\partial f}{\partial x}$ 和 $\frac{\partial f}{\partial y}$ 都存在，那么 $f$ 在 $(a,b)$ 处一定可微。
*(提示：回忆 Lecture 9 和 10 里的那些奇怪的反例)*。

如果上述自测题有疑问，随时可以让我为你详细解答！