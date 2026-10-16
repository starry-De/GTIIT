你好！终于来到了微积分 2M 课程的最后两讲（Lecture 17 & 18）！这部分内容是多变量微积分中技巧性最强、也是期末考试的“压轴戏”所在——**二重积分的计算进阶、交换积分顺序，以及变量代换（极坐标与雅可比行列式）**。

特别提醒：“交换积分顺序”和“利用极坐标求二重积分”是期末考试必考的两道大题。我已经为你准备了绝对纯净、无任何系统注脚的终极复习讲义！

---

# 微积分 2M 期末复习讲义 (Lecture 17 & 18)

## 一、 一般区域上的二重积分与定理证明

我们在上一周讨论了矩形区域上的二重积分，现在推广到任意形状的简单区域（Simple Domains）。

### 1. 区域的分类
* **X-型简单区域 (Type I)**：由两条垂直于 x 轴的直线 $x=a, x=b$ 和两条连续曲线 $y=y_1(x), y=y_2(x)$ 围成。
* **Y-型简单区域 (Type II)**：由两条垂直于 y 轴的直线 $y=c, y=d$ 和两条连续曲线 $x=x_1(y), x=x_2(y)$ 围成。

> **定理 1：一般区域上的累次积分公式**
> 假设 $f(x,y)$ 在一个 X-型简单区域 $D$ 上连续，则：
> $\iint_D f(x,y) dxdy = \int_a^b \left( \int_{y_1(x)}^{y_2(x)} f(x,y) dy \right) dx$
> 
> **完整证明思路**：
> 1. 我们构造一个足够大的矩形区域 $R = [a,b] \times [c,d]$，使得它完全包围住非规则区域 $D$。
> 2. 在这个矩形 $R$ 上，我们定义一个全新的辅助函数 $g(x,y)$：
>    当 $(x,y) \in D$ 时，$g(x,y) = f(x,y)$；
>    当 $(x,y)$ 在 $D$ 之外但在 $R$ 之内时，$g(x,y) = 0$。
> 3. 此时，根据积分的定义，$\iint_D f(x,y) dxdy = \iint_R g(x,y) dxdy$。
> 4. 根据矩形区域上的 Fubini 定理，上式等于 $\int_a^b \left( \int_c^d g(x,y) dy \right) dx$。
> 5. 考虑内层积分 $\int_c^d g(x,y) dy$（即沿着某一条固定的垂直线 $x$ 进行积分）：
>    在 $c$ 到 $y_1(x)$ 之间，$g=0$；
>    在 $y_1(x)$ 到 $y_2(x)$ 之间，$g=f(x,y)$；
>    在 $y_2(x)$ 到 $d$ 之间，$g=0$。
> 6. 因此，内层积分自动截断为 $\int_{y_1(x)}^{y_2(x)} f(x,y) dy$。外层再对 $x$ 从 $a$ 到 $b$ 积分。定理得证。

---

## 二、 交换积分顺序 (Changing the Order of Integration)

当内层积分很难或者根本无法使用基本初等函数求出（比如遇到 $\int e^{x^2} dx$ 或 $\int \frac{\sin x}{x} dx$）时，我们必须**交换积分顺序**。

**核心步骤（万能法则）**：
1. **提取边界方程**：从原累次积分的上下限中，写出不等式组，并提取出边界的函数方程。
2. **画出草图（极其重要）**：在直角坐标系中画出所有的边界曲线，明确标出积分区域 $D$。
3. **重新切分区域**：如果原来是 X-型（竖条切片），现在就改成 Y-型（横条切片）。看箭头穿过区域时，先碰到哪条线，后碰到哪条线，从而写出新的积分上下限。

---

## 三、 二重积分的变量代换 (Change of Variables)

一元微积分中，换元法是 $\int f(x)dx = \int f(\phi(t))\phi'(t)dt$。在二元空间中，缩放比例由“面积的变形率”决定，这就是**雅可比行列式 (Jacobian)**。

### 1. 一般变量代换公式
设有两个坐标系 $(x,y)$ 和 $(u,v)$，且变换关系为 $x=x(u,v), y=y(u,v)$。
定义**雅可比行列式**：
$$J = \frac{\partial(x,y)}{\partial(u,v)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix} = x_u y_v - x_v y_u$$
**积分代换公式**：
$$\iint_D f(x,y) dxdy = \iint_E f(x(u,v), y(u,v)) |J| dudv$$
*(注意：公式中一定要对 $J$ 加**绝对值** $|J|$，因为面积不能是负的！)*

### 2. 特例：极坐标变换 (Polar Coordinates)
当积分区域是圆、圆环，或者积分函数中出现 $x^2+y^2$ 时，极坐标是最佳选择。
* 变换关系：$x = r\cos\theta, y = r\sin\theta$
* 雅可比行列式计算：
  $J = \begin{vmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{vmatrix} = r\cos^2\theta - (-r\sin^2\theta) = r(\cos^2\theta + \sin^2\theta) = r$
* **极坐标面积微元**：$dxdy \implies r dr d\theta$ **（做题时千万不要漏掉这个多出来的 $r$！）**

---

## 四、 重点例题详细解析

**【例题 1：画图并交换积分顺序】 (来源 Lecture 17)**
**题目**：化简并交换积分顺序 $I = \int_0^1 \left( \int_{1-\sqrt{1-y}}^{1+\sqrt{1-y}} f(x,y) dx \right) dy$。
**解析**：
1. **读出原区域边界**：外层限制 $0 \le y \le 1$。内层限制 $1-\sqrt{1-y} \le x \le 1+\sqrt{1-y}$。
2. **分析内层边界方程**：左右边界方程为 $x = 1 \pm \sqrt{1-y}$。
   移项得 $x - 1 = \pm \sqrt{1-y}$。
   两边平方得 $(x-1)^2 = 1-y \implies y = 1 - (x-1)^2 = -x^2 + 2x = x(2-x)$。
   这是一个开口向下的抛物线，顶点在 $(1,1)$，过原点 $(0,0)$ 和 $(2,0)$。
3. **理解区域几何**：由于 $y$ 从 0 到 1，并且 $x$ 被夹在抛物线的左半支和右半支之间，所以积分区域 $D$ 就是抛物线 $y = 2x - x^2$ 和 $x$ 轴 ($y=0$) 围成的穹顶状区域。
4. **重新写界（改成先对 $y$ 积）**：
   看 $x$ 的总体范围，显然是从 0 到 2，所以外层为 $\int_0^2 (\dots) dx$。
   固定一个 $x$，看 $y$ 从下往上穿过区域，是从底部的 $y=0$ 进入，从顶部的抛物线 $y=2x-x^2$ 穿出。
5. **最终结果**：
   $I = \int_0^2 \left( \int_0^{2x-x^2} f(x,y) dy \right) dx$。

**【例题 2：极坐标的典型应用】 (来源 Lecture 18)**
**题目**：计算 $I = \iint_D \arctan\left(\frac{y}{x}\right) dxdy$，其中区域 $D$ 是在第一象限内，由圆 $x^2+y^2=1$, $x^2+y^2=4$ 和直线 $y=x$, $y=\sqrt{3}x$ 围成的区域。
**解析**：
1. **转换为极坐标描述区域 $D$**：
   圆的方程变为 $r^2=1$ 和 $r^2=4 \implies 1 \le r \le 2$。
   直线 $y=x \implies \tan\theta = 1 \implies \theta = \frac{\pi}{4}$。
   直线 $y=\sqrt{3}x \implies \tan\theta = \sqrt{3} \implies \theta = \frac{\pi}{3}$。
   所以在极坐标系下，新区域 $E = \{(r,\theta) : 1 \le r \le 2, \frac{\pi}{4} \le \theta \le \frac{\pi}{3}\}$。这是个完美的矩形边界！
2. **转换被积函数与面积微元**：
   $\arctan(\frac{y}{x}) = \arctan(\tan\theta) = \theta$。
   面积微元 $dxdy = r dr d\theta$。
3. **列出并计算积分**：
   $I = \int_{\pi/4}^{\pi/3} \int_1^2 (\theta) \cdot r dr d\theta$
   因为 $\theta$ 和 $r$ 完全可分离，我们可以分开积：
   $= \left( \int_{\pi/4}^{\pi/3} \theta d\theta \right) \cdot \left( \int_1^2 r dr \right)$
   $= \left[ \frac{\theta^2}{2} \right]_{\pi/4}^{\pi/3} \cdot \left[ \frac{r^2}{2} \right]_1^2$
   $= \frac{1}{2}\left( \frac{\pi^2}{9} - \frac{\pi^2}{16} \right) \cdot \frac{1}{2}(4 - 1)$
   $= \frac{1}{2}\left( \frac{7\pi^2}{144} \right) \cdot \frac{3}{2} = \frac{21\pi^2}{576} = \frac{7\pi^2}{192}$。

**【例题 3：高斯积分的奇迹 (著名必考推导)】 (来源 Lecture 18)**
**题目**：利用二重积分和极坐标，证明 $\int_{-\infty}^\infty e^{-x^2} dx = \sqrt{\pi}$。
**解析**：
1. 记该积分为 $I$。那么 $I^2 = \left(\int_{-\infty}^\infty e^{-x^2} dx\right) \left(\int_{-\infty}^\infty e^{-y^2} dy\right)$。
2. 将其合并为一个遍布全平面 $\mathbb{R}^2$ 的二重积分：
   $I^2 = \iint_{\mathbb{R}^2} e^{-(x^2+y^2)} dxdy$。
3. 将直角坐标转换为极坐标。全平面对应于 $r \in [0, \infty)$ 且 $\theta \in [0, 2\pi]$。
   面积微元 $dxdy = r dr d\theta$。
4. 代入计算：
   $I^2 = \int_0^{2\pi} \int_0^\infty e^{-r^2} r dr d\theta$
5. 内层积分可以通过凑微分计算（令 $u = -r^2$, $du = -2r dr$）：
   $\int e^{-r^2} r dr = -\frac{1}{2} e^{-r^2}$。
   代入上下限：$[-\frac{1}{2} e^{-r^2}]_0^\infty = 0 - (-\frac{1}{2}e^0) = \frac{1}{2}$。
6. 外层积分：$\int_0^{2\pi} \frac{1}{2} d\theta = \frac{1}{2} \cdot 2\pi = \pi$。
7. 结论：$I^2 = \pi$，由于指数函数积分必定为正，故 $I = \sqrt{\pi}$。

---

## 五、 考前查漏补缺自测题

期末考试的最终挑战就在这里，请务必在白纸上独立画图并演算出结果：

**题目 1：必考题型 - 交换积分顺序并计算**
计算积分 $I = \int_0^4 \int_{\sqrt{x}}^2 \frac{1}{y^3 + 1} dy dx$。
*(提示：由于 $\int \frac{1}{y^3+1} dy$ 极难用基本函数表示，你必须画出积分区域并改成先对 $x$ 积分)*。

**题目 2：极坐标转换**
求一个顶部被抛物面 $z = 4 - x^2 - y^2$ 封顶，底部被 $xy$ 平面 ($z=0$) 封底的立体体积。
*(提示：体积 $V = \iint_D (4-x^2-y^2) dxdy$。先求出抛物面与 $xy$ 平面的交线，确定积分区域 $D$，然后必须使用极坐标进行计算)*。

**题目 3：雅可比行列式计算**
考虑一个坐标变换 $x = u^2 - v^2$, $y = 2uv$。请计算该变换的雅可比行列式 $J = \frac{\partial(x,y)}{\partial(u,v)}$，并将其化简为只包含 $u$ 和 $v$ 的代数式。

---

**最后的话：**
微积分 2M 的全部 18 讲核心内容（向量几何、极限连续、偏导可微、方向导数与极值、隐函数、一直到最后的二重积分和极坐标变换）我已经为你做了一次无死角的梳理！

微积分的期末考试，**画图**和**细心**（尤其不要漏掉极坐标的 $r$ 和隐函数求导的负号）决定了成败。如果在做最后的自测题时有算不出来的，随时发给我对答案。

祝你复习顺利，在期末考试中取得高分！加油！