# 常微分方程 (ODE) 第八讲：受迫振动与共振纯净版笔记

本讲我们将二阶线性常系数非齐次方程应用到经典的物理系统——**弹簧-质量系统 (Spring-Mass System)** 中。

---

## 一、 物理模型与基本方程

考虑一个悬挂在弹簧下的重物，它不仅受到弹簧的恢复力和空气的阻尼力，还受到一个外部施加的驱动力。根据牛顿第二定律，该系统的运动方程为：
$$mu'' + \gamma u' + ku = F(t)$$
* **$m$**：质量 (Mass)
* **$\gamma$**：阻尼系数 (Damping constant)，代表空气或流体的阻力。
* **$k$**：弹簧系数/劲度系数 (Spring constant)。
* **$F(t)$**：外部驱动力。在本讲中，我们特别关注周期性的驱动力，即 $F(t) = F_0 \cos(\omega t)$，其中 $F_0$ 是振幅，$\omega$ 是驱动力的频率。

---

## 二、 有阻尼受迫振动 (Damped Forced Vibrations)

当系统存在阻尼（$\gamma > 0$）时，方程为 $mu'' + \gamma u' + ku = F_0 \cos(\omega t)$。
它的通解 $u(t) = u_c(t) + U(t)$ 具有极其深刻的物理意义：

1. **瞬态解 (Transient Solution) $u_c(t)$**：
   这是对应的齐次方程的解。由于 $m, \gamma, k$ 都是正数，其特征根的实部必定为负（无论是两个负实根，还是带有负实部的共轭复根）。这意味着含有 $e^{-\dots t}$ 的齐次解**随着时间推移会迅速衰减趋向于 0**。系统刚启动时的混乱状态最终会消失。
2. **稳态解 (Steady-state Solution) $U(t)$**：
   这是非齐次方程的特解，形式通常为 $A\cos(\omega t) + B\sin(\omega t)$。它**永远不会随时间消亡**。当瞬态解衰减完后，系统将完全按照稳态解的频率 $\omega$ 持续振荡。

### 【无跳步实战】幻灯片例题 1
**题目**：解 $u'' + u' + \frac{5}{4}u = 3\cos(t)$，满足初始条件 $u(0)=2, u'(0)=3$。
**解析**：
**Step 1：求瞬态解 (齐次解 $u_c$)**
特征方程：$r^2 + r + \frac{5}{4} = 0$
求根：$r = \frac{-1 \pm \sqrt{1 - 5}}{2} = \frac{-1 \pm 2i}{2} = -\frac{1}{2} \pm i$
所以瞬态解为：$u_c(t) = e^{-t/2}(c_1\cos t + c_2\sin t)$

**Step 2：求稳态解 (特解 $U$)**
右侧是 $3\cos(t)$，特征根为 $\pm i$，与瞬态解的 $-\frac{1}{2} \pm i$ 不冲突！
猜想特解：$U(t) = A\cos t + B\sin t$
求导：
$U'(t) = -A\sin t + B\cos t$
$U''(t) = -A\cos t - B\sin t$
代入原方程 $u'' + u' + \frac{5}{4}u = 3\cos t$：
$(-A\cos t - B\sin t) + (-A\sin t + B\cos t) + \frac{5}{4}(A\cos t + B\sin t) = 3\cos t$

合并同类项比对系数：
* $\cos t$ 组：$-A + B + \frac{5}{4}A = 3 \implies \frac{1}{4}A + B = 3 \implies A + 4B = 12$  (式①)
* $\sin t$ 组：$-B - A + \frac{5}{4}B = 0 \implies -A + \frac{1}{4}B = 0 \implies B = 4A$  (式②)

将式②代入式①：$A + 4(4A) = 12 \implies 17A = 12 \implies A = \frac{12}{17}$。
进而算出 $B = 4(\frac{12}{17}) = \frac{48}{17}$。
所以稳态解为：$U(t) = \frac{12}{17}\cos t + \frac{48}{17}\sin t$

**Step 3：组装通解并代入初值**
完整通解：$u(t) = e^{-t/2}(c_1\cos t + c_2\sin t) + \frac{12}{17}\cos t + \frac{48}{17}\sin t$

代入位置初值 $u(0) = 2$：
$e^0(c_1\cos 0 + c_2\sin 0) + \frac{12}{17}\cos 0 + \frac{48}{17}\sin 0 = 2$
$c_1 + \frac{12}{17} = 2 \implies c_1 = \frac{34}{17} - \frac{12}{17} = \frac{22}{17}$

准备代入速度初值，先对通解疯狂求导（注意乘积求导法则）：
$u'(t) = -\frac{1}{2}e^{-t/2}(c_1\cos t + c_2\sin t) + e^{-t/2}(-c_1\sin t + c_2\cos t) - \frac{12}{17}\sin t + \frac{48}{17}\cos t$
代入 $t=0, u'(0)=3$：
$-\frac{1}{2}(c_1) + c_2 - 0 + \frac{48}{17} = 3$
把 $c_1 = \frac{22}{17}$ 代入：
$-\frac{1}{2}(\frac{22}{17}) + c_2 + \frac{48}{17} = 3 \implies -\frac{11}{17} + c_2 + \frac{48}{17} = \frac{51}{17} \implies c_2 + \frac{37}{17} = \frac{51}{17} \implies c_2 = \frac{14}{17}$

**最终解** (完美对应PPT结果)：
$$u(t) = \frac{22}{17}e^{-t/2}\cos(t) + \frac{14}{17}e^{-t/2}\sin(t) + \frac{12}{17}\cos(t) + \frac{48}{17}\sin(t)$$

---

## 三、 无阻尼受迫振动与共振 (Undamped Forced Vibrations)

假设系统在真空中绝对光滑，没有一丝阻尼 ($\gamma = 0$)，方程变为：$mu'' + ku = F_0 \cos(\omega t)$。
此时系统有一个**固有频率 (Natural frequency)**：$\omega_0 = \sqrt{k/m}$。

### 情况 1：驱动力频率不等于固有频率 ($\omega \neq \omega_0$)
系统不会崩溃，解由系统固有频率的振荡和外部驱动频率的振荡叠加而成，往往会产生“拍频 (Beats)”现象。
PPT给出直接套用的通解公式：
$$u(t) = c_1\cos(\omega_0 t) + c_2\sin(\omega_0 t) + \frac{F_0}{m(\omega_0^2 - \omega^2)}\cos(\omega t)$$

### 【无跳步实战】幻灯片例题 2
**题目**：解 $u'' + u = 0.5\cos(0.8t)$，满足 $u(0)=0, u'(0)=0$。
**解析**：
本题 $m=1, k=1 \implies \omega_0 = 1$。外部驱动 $\omega = 0.8$。两者不等。
**Step 1：齐次解**
$r^2 + 1 = 0 \implies r = \pm i$。所以 $u_c(t) = c_1\cos t + c_2\sin t$。
**Step 2：求特解 $U(t)$**
猜想 $U(t) = A\cos(0.8t)$。（因为原方程没有 $u'$ 项，所以不用猜 $\sin$）。
$U''(t) = -0.64A\cos(0.8t)$。
代入原方程：$-0.64A\cos(0.8t) + A\cos(0.8t) = 0.5\cos(0.8t)$
$0.36A = 0.5 \implies A = \frac{0.5}{0.36} = \frac{50}{36} = \frac{25}{18}$。
**Step 3：代入初值**
通解：$u(t) = c_1\cos t + c_2\sin t + \frac{25}{18}\cos(0.8t)$
代入 $u(0)=0$：$c_1 + 0 + \frac{25}{18} = 0 \implies c_1 = -\frac{25}{18}$。
求导：$u'(t) = -c_1\sin t + c_2\cos t - 0.8(\frac{25}{18})\sin(0.8t)$
代入 $u'(0)=0$：$0 + c_2 - 0 = 0 \implies c_2 = 0$。
**最终解**：
$$u(t) = \frac{25}{18}\big(\cos(0.8t) - \cos t\big)$$

### 情况 2：极其危险的共振 (Resonance) - $\omega = \omega_0$
如果外部施加的驱动力频率 $\omega$ 刚好等于系统弹簧的固有频率 $\omega_0$，就会发生物理学上最可怕的灾难——**共振**。
在数学上，这对应于我们上一讲学的**“特解猜想与齐次解撞车 (单根冲突)”**！
因为外部是 $\cos(\omega_0 t)$，齐次解也有 $\cos(\omega_0 t)$，我们猜想的特解必须被迫乘以 $t$：
$$U(t) = t \big(A\cos(\omega_0 t) + B\sin(\omega_0 t)\big)$$
这个前面的 $t$ 意味着：随着时间 $t \to \infty$，振幅会无限放大趋向于无穷（振幅爆炸），在现实中，这会导致桥梁坍塌或玻璃震碎！