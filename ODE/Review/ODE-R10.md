# 常微分方程 (ODE) 第十讲：拉普拉斯变换

本讲引入了一种极其强大的数学工具——**拉普拉斯变换 (Laplace Transform)**。它能把关于时间 $t$ 的微分方程，转换成关于变量 $s$ 的普通代数方程，解出代数方程后再“逆变换”回来，从而巧妙地避开复杂的积分和特解猜测。

---

## 一、 广义积分与拉普拉斯变换的定义

### 1. 广义积分回顾
在无穷区间上的积分被定义为极限：
$$\int_a^\infty f(t)dt = \lim_{b \to \infty} \int_a^b f(t)dt$$

**【例 1】**：计算 $\int_0^\infty e^{\lambda t} dt$
**详细解析**：
$$\int_0^\infty e^{\lambda t} dt = \lim_{b \to \infty} \left[ \frac{1}{\lambda} e^{\lambda t} \right]_0^b = \lim_{b \to \infty} \left( \frac{e^{\lambda b}}{\lambda} - \frac{1}{\lambda} \right)$$
* 当 $\lambda > 0$ 时，$e^{\lambda b} \to \infty$，积分**发散**。
* 当 $\lambda < 0$ 时，$e^{\lambda b} \to 0$，积分**收敛**，结果为 $-\frac{1}{\lambda}$。

### 2. 拉普拉斯变换定义
对于定义在 $t \ge 0$ 上的函数 $f(t)$，其拉普拉斯变换 $F(s)$ 或 $\mathcal{L}\{f\}$ 定义为：
$$\mathcal{L}\{f\} = F(s) = \int_0^\infty e^{-st} f(t) dt$$

**【例 2】**：求 $\mathcal{L}\{1\}$ 和 $\mathcal{L}\{e^{at}\}$
**详细解析**：
* $\mathcal{L}\{1\} = \int_0^\infty e^{-st} (1) dt = \lim_{b \to \infty} \left[ -\frac{1}{s} e^{-st} \right]_0^b = 0 - \left(-\frac{1}{s}\right) = \frac{1}{s} \quad (要求 \ s > 0)$
* $\mathcal{L}\{e^{at}\} = \int_0^\infty e^{-st} e^{at} dt = \int_0^\infty e^{-(s-a)t} dt$
  (利用例1的结论，令 $\lambda = -(s-a)$，必须要求 $-(s-a) < 0$ 即 $s > a$ 才能收敛)
  $= \left[ -\frac{1}{s-a} e^{-(s-a)t} \right]_0^\infty = \frac{1}{s-a} \quad (要求 \ s > a)$

---

## 二、 拉普拉斯变换的核心性质与解 ODE

### 1. 核心性质
* **线性性质**：$\mathcal{L}\{c_1 f_1(t) + c_2 f_2(t)\} = c_1\mathcal{L}\{f_1\} + c_2\mathcal{L}\{f_2\}$
* **【极其重要】导数的变换**：
  $$\mathcal{L}\{f'(t)\} = s\mathcal{L}\{f\} - f(0)$$
  $$\mathcal{L}\{f''(t)\} = s^2\mathcal{L}\{f\} - s f(0) - f'(0)$$
  *（注意：这就是拉氏变换能消灭微分的根本原因！）*

### 2. 利用拉氏变换解初值问题 (三步曲)
**【例 3】**：解 $y'' - y' - 2y = 0$, $y(0)=1, y'(0)=0$
**绝不跳步解析**：
**Step 1：两边同时取拉普拉斯变换**
设 $\mathcal{L}\{y(t)\} = Y(s)$。
方程变为：$\mathcal{L}\{y''\} - \mathcal{L}\{y'\} - 2\mathcal{L}\{y\} = 0$
套用导数公式并代入初值 $y(0)=1, y'(0)=0$：
$$[s^2 Y(s) - s(1) - 0] - [s Y(s) - 1] - 2Y(s) = 0$$

**Step 2：解代数方程求 $Y(s)$**
展开并合并含有 $Y(s)$ 的项：
$$s^2 Y(s) - s - s Y(s) + 1 - 2Y(s) = 0$$
$$(s^2 - s - 2) Y(s) - s + 1 = 0$$
$$Y(s) = \frac{s - 1}{s^2 - s - 2} = \frac{s - 1}{(s - 2)(s + 1)}$$

**Step 3：部分分式展开与逆变换**
我们需要把 $Y(s)$ 拆开，假设：
$$\frac{s - 1}{(s - 2)(s + 1)} = \frac{A}{s - 2} + \frac{B}{s + 1}$$
通分得：$A(s + 1) + B(s - 2) = s - 1$
* 令 $s = 2$：$A(3) + 0 = 1 \implies A = 1/3$
* 令 $s = -1$：$0 + B(-3) = -2 \implies B = 2/3$

所以 $Y(s) = \frac{1/3}{s - 2} + \frac{2/3}{s + 1}$。
查表逆变换（利用 $\mathcal{L}^{-1}\{\frac{1}{s-a}\} = e^{at}$）：
$$y(t) = \frac{1}{3} e^{2t} + \frac{2}{3} e^{-t}$$

---

## 三、 阶跃函数 (Heaviside Function) 与 平移定理

**1. 单位阶跃函数 $u_c(t)$**
定义为：在 $t < c$ 时为 0，在 $t \ge c$ 时突然变为 1（就像在 $t=c$ 时按下了开关）。
$$u_c(t) = \begin{cases} 0, & t < c \\ 1, & t \ge c \end{cases}$$
其拉氏变换为：$\mathcal{L}\{u_c(t)\} = \int_c^\infty e^{-st}(1) dt = \frac{e^{-cs}}{s}$。

**2. 平移定理 (Theorem 6.3.1)**
* **正向变换**：$\mathcal{L}\{u_c(t) f(t-c)\} = e^{-cs} F(s)$
* **逆向变换**：$\mathcal{L}^{-1}\{e^{-cs} F(s)\} = u_c(t) f(t-c)$
>*(物理意义：在频域 $s$ 中乘以 $e^{-cs}$，等于在时域 $t$ 中让函数“延迟 $c$ 秒”并在 $t=c$ 时才开启)*。

**【幻灯片 例题】**：设 $f(t) = \sin(t)$ 当 $0 \le t < \pi/4$，而在 $t \ge \pi/4$ 时 $f(t) = \sin(t) + \cos(t - \pi/4)$。求 $\mathcal{L}\{f\}$。
**详细解析**：
首先用阶跃函数改写 $f(t)$。由于多出来的那部分 $\cos(t - \pi/4)$ 恰好是在 $t = \pi/4$ 时“开启”的，所以：
$$f(t) = \sin(t) + u_{\pi/4}(t) \cos(t - \pi/4)$$
两边取拉氏变换：
$$\mathcal{L}\{f\} = \mathcal{L}\{\sin t\} + \mathcal{L}\{u_{\pi/4}(t) \cos(t - \pi/4)\}$$
查表可知 $\mathcal{L}\{\sin t\} = \frac{1}{s^2+1}$，且 $\mathcal{L}\{\cos t\} = \frac{s}{s^2+1}$。
套用平移定理：
$$\mathcal{L}\{f\} = \frac{1}{s^2+1} + e^{-\frac{\pi}{4}s} \frac{s}{s^2+1}$$

**【幻灯片 例题】**：已知 $F(s) = \frac{1 - e^{-2s}}{s^3}$，求逆变换 $f(t)$。
**详细解析**：
把 $F(s)$ 拆开：$F(s) = \frac{1}{s^3} - e^{-2s} \frac{1}{s^3}$
1. 首先处理不带 $e$ 的基础函数 $\frac{1}{s^3}$。查表得知 $\mathcal{L}\{t^2\} = \frac{2!}{s^3} = \frac{2}{s^3}$，所以 $\mathcal{L}^{-1}\{\frac{1}{s^3}\} = \frac{1}{2}t^2$。
2. 对于第二项 $e^{-2s} \frac{1}{s^3}$，存在 $e^{-2s}$ 意味着发生了延迟（$c=2$）。
   根据平移定理逆变换公式，我们要把基础解 $\frac{1}{2}t^2$ 延迟2秒，即把所有的 $t$ 替换为 $(t-2)$，并且前面挂上阶跃开关 $u_2(t)$。
   $\mathcal{L}^{-1}\left\{ e^{-2s} \frac{1}{s^3} \right\} = u_2(t) \cdot \frac{1}{2}(t-2)^2$
3. 组装最终答案：
   $$f(t) = \frac{1}{2}t^2 - \frac{1}{2} u_2(t) (t-2)^2$$

---

## 四、 脉冲函数 (狄拉克 δ 函数)

在物理中，我们常遇到瞬间巨大的冲击力（如锤击）。
**狄拉克 Delta 函数 $\delta(t-t_0)$** 被定义为：
* 在 $t \neq t_0$ 时，$\delta = 0$
* 但它在 $t=t_0$ 处的积分（总面积/冲量）等于 1。即 $\int_{-\infty}^\infty \delta(t) dt = 1$。
**它的拉氏变换极其简单完美**：
$$\mathcal{L}\{\delta(t-t_0)\} = e^{-s t_0}$$

**【幻灯片 终极例题】**：解 $2y'' + y' + 2y = \delta(t-5)$，初始条件 $y(0)=0, y'(0)=0$。
**绝不跳步解析**：
**Step 1：两边取拉氏变换**
$$2[s^2 Y(s) - 0 - 0] + [s Y(s) - 0] + 2Y(s) = e^{-5s}$$
$$(2s^2 + s + 2) Y(s) = e^{-5s}$$
$$Y(s) = e^{-5s} \frac{1}{2s^2 + s + 2}$$

**Step 2：对分式进行配方 (Completing the Square)**
我们先处理基础部分 $H(s) = \frac{1}{2s^2 + s + 2}$。
提取分母的 2：
$$H(s) = \frac{1}{2(s^2 + \frac{1}{2}s + 1)} = \frac{1/2}{s^2 + \frac{1}{2}s + 1}$$
对分母进行完全平方配方：
$$s^2 + \frac{1}{2}s + 1 = \left( s + \frac{1}{4} \right)^2 - \left(\frac{1}{4}\right)^2 + 1 = \left( s + \frac{1}{4} \right)^2 - \frac{1}{16} + \frac{16}{16} = \left( s + \frac{1}{4} \right)^2 + \frac{15}{16}$$
所以：
$$H(s) = \frac{1/2}{(s + 1/4)^2 + 15/16}$$

**Step 3：凑出标准衰减正弦形式并逆变换**
衰减正弦的拉氏变换标准公式是 $\mathcal{L}\{e^{at}\sin(\omega t)\} = \frac{\omega}{(s-a)^2 + \omega^2}$。
对比我们的式子：$a = -1/4$，且 $\omega^2 = 15/16 \implies \omega = \frac{\sqrt{15}}{4}$。
分子上需要出现 $\omega$ 即 $\frac{\sqrt{15}}{4}$，我们强行凑出来：
$$H(s) = \frac{1/2}{\frac{\sqrt{15}}{4}} \cdot \frac{\frac{\sqrt{15}}{4}}{(s + 1/4)^2 + 15/16} = \frac{2}{\sqrt{15}} \cdot \frac{\frac{\sqrt{15}}{4}}{(s + 1/4)^2 + 15/16}$$
现在可以完美查表逆变换了：
$$h(t) = \mathcal{L}^{-1}\{H(s)\} = \frac{2}{\sqrt{15}} e^{-t/4} \sin\left(\frac{\sqrt{15}}{4} t\right)$$

**Step 4：利用平移定理处理 $e^{-5s}$**
我们要求的是 $Y(s) = e^{-5s} H(s)$ 的逆变换。
根据平移定理，只需在 $h(t)$ 前面挂上 $u_5(t)$，并把里面所有的 $t$ 换成 $(t-5)$：
$$y(t) = u_5(t) h(t-5)$$
**最终无懈可击的答案**：
$$y(t) = u_5(t) \frac{2}{\sqrt{15}} e^{-(t-5)/4} \sin\left(\frac{\sqrt{15}}{4} (t-5)\right)$$

---

## 五. 全套常用拉普拉斯变换对照表

### 表 1：基础函数对照表 (时域 $\leftrightarrow$ 频域)

| 时域原函数 $f(t)$ ($t \ge 0$) | 频域象函数 $F(s)$ | 特征记忆 |
| :--- | :--- | :--- |
| $1$ | $\frac{1}{s}$ | 最基础的积木 |
| $t$ | $\frac{1}{s^2}$ | 幂次比时域多 1 阶 |
| $t^n$ ($n \in \mathbb{N}^+$) | $\frac{n!}{s^{n+1}}$ | 分子阶乘，分母幂次加 1 |
| $e^{at}$ | $\frac{1}{s-a}$ | 带有极点 $s=a$ |
| $\sin(\omega t)$ | $\frac{\omega}{s^2 + \omega^2}$ | 分母平方**和**，分子常数 $\omega$ |
| $\cos(\omega t)$ | $\frac{s}{s^2 + \omega^2}$ | 分母平方**和**，分子变量 $s$ |
| $\sinh(\omega t)$ | $\frac{\omega}{s^2 - \omega^2}$ | 分母平方**差**，分子常数 $\omega$ |
| $\cosh(\omega t)$ | $\frac{s}{s^2 - \omega^2}$ | 分母平方**差**，分子变量 $s$ |
| $\delta(t)$ (脉冲冲激) | $1$ | 变换后是个常数 |
| $u_c(t)$ (单位阶跃) | $\frac{e^{-sc}}{s}$ | 时间延迟开关 |

### 表 2：核心运算性质表 (语法变形规则)

| 性质名称 | 时域操作 $f(t)$ | 频域操作 $F(s)$ | 应用场景 |
| :--- | :--- | :--- | :--- |
| **线性性质** | $a f_1(t) + b f_2(t)$ | $a F_1(s) + b F_2(s)$ | 多项式拆分 |
| **第一平移 (s域平移)** | $e^{at} f(t)$ | $F(s-a)$ | 乘以指数衰减，s全体替换为(s-a) |
| **第二平移 (t域平移)** | $u_c(t) f(t-c)$ | $e^{-cs} F(s)$ | 延迟开启，频域乘 $e^{-cs}$ |
| **一阶微分** | $f'(t)$ | $sF(s) - f(0)$ | 降维核心魔法 |
| **时域积分** | $\int_{0}^{t} f(\tau) \, d\tau$ | $\frac{F(s)}{s}$ | 时域积分 = 频域除以 $s$ |
| **时域乘 $t$** | $t f(t)$ | $-F'(s)$ | 频域求导并添负号 |
