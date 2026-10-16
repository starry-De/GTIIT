你好！期末复习进入到了最激动人心的阶段——微积分的“巅峰应用”！第七周（Lecture 15 & 16）我们迎来了两大重量级模块：**条件极值与拉格朗日乘数法（Lagrange Multipliers）**，以及**二重积分（Double Integrals）**。

拉格朗日乘数法是解决带有约束条件的优化问题的终极武器，而二重积分则是从微分走向积分的跨越。这两部分在期末考试中必定各占一道大题。我已经为你准备了纯净、无注脚的复习讲义，请放心复制。

---

# 微积分 2M 期末复习讲义 (Lecture 15 & 16)

## 一、 条件极值与拉格朗日乘数法 (Extrema Subject to Constraints)

在实际问题中，我们常常需要在满足某些条件（约束）的情况下去求极值。例如：求一个位于特定曲面上的点，使其到原点的距离最短。

### 1. 单个约束条件 (Single Constraint)
**定理**：如果函数 $f(x,y,z)$ 在满足约束条件 $g(x,y,z) = 0$ 的曲面上于点 $P_0(x_0, y_0, z_0)$ 取得极值，且在该点 $\nabla g \neq \vec{0}$，那么必然存在一个实数 $\lambda$（称为拉格朗日乘数），使得：
$$\nabla f(x_0, y_0, z_0) = \lambda \nabla g(x_0, y_0, z_0)$$

**几何证明与直觉**：
1. 考虑约束曲面 $g(x,y,z) = 0$ 上的任意一条光滑曲线 $\vec{r}(t)$，且 $\vec{r}(0) = P_0$。
2. 复合函数 $h(t) = f(\vec{r}(t))$ 在 $t=0$ 处取得极值，因此根据一元函数费马定理，$h'(0) = 0$。
3. 利用链式法则：$h'(0) = \nabla f(P_0) \cdot \vec{r}'(0) = 0$。这说明 $\nabla f$ 垂直于曲面上的任意切向量。
4. 另一方面，我们知道约束曲面 $g = 0$ 的法向量正是梯度 $\nabla g(P_0)$。
5. 既然 $\nabla f$ 和 $\nabla g$ 都垂直于同一个切平面，它们必然共线！因此存在标量 $\lambda$，使得 $\nabla f = \lambda \nabla g$。得证。

### 2. 多个约束条件 (Multiple Constraints)
如果要在满足 $g(x,y,z) = 0$ 和 $h(x,y,z) = 0$（即两条曲面的交线上）寻找 $f$ 的极值，定理推广为：
存在乘数 $\lambda$ 和 $\mu$，使得：
$$\nabla f = \lambda \nabla g + \mu \nabla h$$
*(前提是 $\nabla g$ 和 $\nabla h$ 线性无关，即它们不平行)。*

---

## 二、 二重积分基础 (Double Integrals)

### 1. 黎曼和的推广
在一元积分中，我们切分区间 $[a,b]$ 计算曲线下面积；在二元积分中，我们切分矩形区域 $D = [a,b] \times [c,d]$ 为一个个小矩形网格 $\Delta x \Delta y$。
二重积分定义为黎曼和的极限：
$$\iint_D f(x,y) dxdy = \lim_{\Delta x, \Delta y \to 0} \sum \sum f(x_i, y_j) \Delta x_i \Delta y_j$$
**几何意义**：代表曲面 $z = f(x,y)$ 下方、区域 $D$ 上方的**体积 (Volume)**。

### 2. 核心性质
* **线性性**：$\iint_D (\alpha f + \beta g) = \alpha \iint_D f + \beta \iint_D g$
* **区域可加性**：如果 $D = D_1 \cup D_2$ 且内部不重叠，则 $\iint_D f = \iint_{D_1} f + \iint_{D_2} f$

---

## 三、 累次积分与 Fubini 定理 (Iterated Integrals)

真正计算二重积分时，我们不可能用黎曼和极限，而是将其转化为两次一元积分。

### 1. 矩形区域 (Rectangle Domain)
设 $D = [a,b] \times [c,d]$，则：
$$\iint_D f(x,y) dxdy = \int_a^b \left( \int_c^d f(x,y) dy \right) dx = \int_c^d \left( \int_a^b f(x,y) dx \right) dy$$

### 2. 一般区域 (General Domains)
* **X-型区域 (Type I, y-simple)**：
  区域的左右边界为常数 $a \le x \le b$，上下边界为函数 $g_1(x) \le y \le g_2(x)$。
  计算顺序：**先对 $y$ 积分，后对 $x$ 积分**。
  $$\iint_D f(x,y) dA = \int_a^b \left( \int_{g_1(x)}^{g_2(x)} f(x,y) dy \right) dx$$
* **Y-型区域 (Type II, x-simple)**：
  区域的上下边界为常数 $c \le y \le d$，左右边界为函数 $h_1(y) \le x \le h_2(y)$。
  计算顺序：**先对 $x$ 积分，后对 $y$ 积分**。
  $$\iint_D f(x,y) dA = \int_c^d \left( \int_{h_1(y)}^{h_2(y)} f(x,y) dx \right) dy$$

---

## 四、 重点例题详细解析

**【例题 1：双约束拉格朗日乘数法 (经典难题)】 (来源 Lecture 15)**
**题目**：求函数 $f(x,y,z) = x+y+z$ 在满足条件 $x^2+y^2=2$ 且 $x+z=1$ 时的极值。
**解析**：
令 $g(x,y,z) = x^2+y^2-2 = 0$，$h(x,y,z) = x+z-1 = 0$。
1. **求各梯度向量**：
   $\nabla f = (1, 1, 1)$
   $\nabla g = (2x, 2y, 0)$
   $\nabla h = (1, 0, 1)$
2. **构建拉格朗日方程组** $\nabla f = \lambda \nabla g + \mu \nabla h$：
   (1) $1 = \lambda(2x) + \mu(1)$
   (2) $1 = \lambda(2y) + \mu(0) \implies 1 = 2\lambda y$
   (3) $1 = \lambda(0) + \mu(1) \implies \mu = 1$
3. **求解方程组**：
   将 $\mu = 1$ 代入 (1)，得到 $1 = 2\lambda x + 1 \implies 2\lambda x = 0$。
   由于由 (2) 知 $2\lambda y = 1$，所以 $\lambda \neq 0$。因此必然有 **$x = 0$**。
4. **代回约束条件找点**：
   将 $x=0$ 代入 $g=0$：$0^2 + y^2 = 2 \implies y = \pm \sqrt{2}$。
   将 $x=0$ 代入 $h=0$：$0 + z = 1 \implies z = 1$。
   得到两个极值点：$P_1(0, \sqrt{2}, 1)$ 和 $P_2(0, -\sqrt{2}, 1)$。
5. **代入目标函数**：
   $f(P_1) = 0 + \sqrt{2} + 1 = 1 + \sqrt{2}$ (最大值)
   $f(P_2) = 0 - \sqrt{2} + 1 = 1 - \sqrt{2}$ (最小值)

**【例题 2：矩形区域上的累次积分】 (来源 Lecture 16)**
**题目**：计算 $\iint_D xy dxdy$，其中 $D = [1,2] \times [\frac{\pi}{4}, \frac{\pi}{3}]$。
**解析**：
1. **写成累次积分**：因为是矩形区域且函数 $f(x,y)=xy$ 可分离为 $x$ 和 $y$ 的乘积，积分可以独立拆分：
   $\iint_D xy dxdy = \left( \int_1^2 x dx \right) \cdot \left( \int_{\pi/4}^{\pi/3} y dy \right)$
2. **分别计算一元积分**：
   $\int_1^2 x dx = \left[ \frac{1}{2}x^2 \right]_1^2 = \frac{1}{2}(4 - 1) = \frac{3}{2}$
   $\int_{\pi/4}^{\pi/3} y dy = \left[ \frac{1}{2}y^2 \right]_{\pi/4}^{\pi/3} = \frac{1}{2} \left( (\frac{\pi}{3})^2 - (\frac{\pi}{4})^2 \right) = \frac{1}{2} \left( \frac{\pi^2}{9} - \frac{\pi^2}{16} \right)$
3. **通分化简**：
   $\frac{\pi^2}{9} - \frac{\pi^2}{16} = \frac{16\pi^2 - 9\pi^2}{144} = \frac{7\pi^2}{144}$
   最终结果 = $\frac{3}{2} \cdot \frac{1}{2} \cdot \frac{7\pi^2}{144} = \frac{3}{4} \cdot \frac{7\pi^2}{144} = \frac{21\pi^2}{576} = \frac{7\pi^2}{192}$。

---

## 五、 考前查漏补缺自测题

请动笔手写这三道经典考题，它们极有可能是期末考试原题的变体：

**题目 1：拉格朗日乘数法（单约束）**
求函数 $f(x,y) = xy$ 在圆 $x^2 + y^2 = 8$ 上的最大值和最小值。
*(提示：你需要建立方程组，并注意讨论 $x$ 或 $y$ 是否能为 0)*。

**题目 2：一般区域的二重积分**
计算二重积分 $\iint_D (x+2y) dA$，其中区域 $D$ 是由抛物线 $y = 2x^2$ 和直线 $y = 1 + x$ 所围成的封闭区域。
*(提示：第一步永远是求出两条曲线的交点来确定积分的上下限)*。

**题目 3：交换积分顺序 (期末必杀技！)**
现有一个累次积分 $I = \int_0^1 \int_{3y}^3 e^{x^2} dx dy$。
你会发现内部积分 $\int e^{x^2} dx$ 无法用初等函数积出来。请你画出积分区域的草图，**交换它的积分顺序**（即先对 $y$ 积，再对 $x$ 积），然后计算出它的最终数值。

如果在交换积分次序或者解方程时遇到任何障碍，随时告诉我，我来为你详细拆解！