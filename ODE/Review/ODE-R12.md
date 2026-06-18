# 常微分方程 (ODE) 第十二讲：重特征值与复数特征值

本讲继续研究常系数齐次线性方程组 $\overline{X}' = A\overline{X}$。
在第十一讲中，我们解决了矩阵 $A$ 拥有“两个相异实数特征值”的情况。这一讲，我们将攻克剩下的两种复杂情况：**特征值相等（重根）** 以及 **特征值为复数（共轭复根）**。

## 一、 情况 2：重实数特征值 (Repeated Eigenvalues)

当矩阵 $A$ (以 $2 \times 2$ 为例) 只有一个重特征值 $\lambda_1$，且只能算出一个线性无关的特征向量 $\overline{V}$ 时，由于解的数量不够，我们需要强行凑出第二个解。

**【核心公式】**：
基础解系由以下两个向量构成：

1. 第一个解（常规解）：
   $$
   \overline{X}^{(1)}(t) = e^{\lambda_1 t}\overline{V}
   $$

2. 第二个解（带 $t$ 的广义解）：
   $$
   \overline{X}^{(2)}(t) = t e^{\lambda_1 t}\overline{V} + e^{\lambda_1 t}\overline{W}
   $$
   
   *这里的* $\overline{W}$ *叫做**广义特征向量 (Generalized eigenvector)**，它必须满足代数方程：*
   $$
   (A - \lambda_1 I)\overline{W} = \overline{V}
   $$

**【相图形态】**：**不当节点 (Improper Node)**。

* 若 $\lambda_1 < 0$：轨迹盘旋指向原点，**渐近稳定 (Asymptotically stable)**。

* 若 $\lambda_1 > 0$：轨迹盘旋远离原点，**不稳定 (Unstable)**。

### 例题

**题目**：求 $\overline{X}' = \begin{pmatrix} 1 & -1 \\ 1 & 3 \end{pmatrix} \overline{X}$ 的基础解系。
**解析**：
**Step 1：求特征值**
$$
\det(A - rI) = \begin{vmatrix} 1 - r & -1 \\ 1 & 3 - r \end{vmatrix} = (1-r)(3-r) - (-1)(1) = (r^2 - 4r + 3) + 1 = 0
$$

即 $r^2 - 4r + 4 = 0 \implies (r-2)^2 = 0$。
得到唯一重实根特征值：$\lambda_1 = 2$。

**Step 2：求常规特征向量** $\overline{V}$
求解 $(A - 2I)\overline{V} = 0$：
$$
\begin{pmatrix} 1-2 & -1 \\ 1 & 3-2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} -1 & -1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

列出方程：$-x - y = 0 \implies y = -x$。
令 $x = 1$，得 $y = -1$。
**常规特征向量**：$\overline{V} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$。
由此得到第一个解：$\overline{X}^{(1)}(t) = e^{2t} \begin{pmatrix} 1 \\ -1 \end{pmatrix}$。

**Step 3：求广义特征向量** $\overline{W}$
求解 $(A - 2I)\overline{W} = \overline{V}$：
$$
\begin{pmatrix} -1 & -1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} w_1 \\ w_2 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}
$$

取第一行方程：$-w_1 - w_2 = 1 \implies w_1 + w_2 = -1$。
这个方程有无穷多解，我们**为了计算方便，随便取一组最简单的数**即可。例如令 $w_1 = 0$，则 $w_2 = -1$。
**广义特征向量**：$\overline{W} = \begin{pmatrix} 0 \\ -1 \end{pmatrix}$。
由此得到第二个解：$\overline{X}^{(2)}(t) = t e^{2t} \begin{pmatrix} 1 \\ -1 \end{pmatrix} + e^{2t} \begin{pmatrix} 0 \\ -1 \end{pmatrix}$。

**最终通解**：
$$
\overline{X}(t) = c_1 e^{2t} \begin{pmatrix} 1 \\ -1 \end{pmatrix} + c_2 e^{2t} \left[ t \begin{pmatrix} 1 \\ -1 \end{pmatrix} + \begin{pmatrix} 0 \\ -1 \end{pmatrix} \right]
$$

## 二、 情况 3：复数特征值 (Complex Eigenvalues)

当矩阵 $A$ 的特征方程无实数根时，会得到一对共轭复根 $r = \lambda \pm i\mu$。
根据定理 (Thm. 7.4.5)：如果我们求出了一个复数形式的解 $\overline{X}_c(t) = \overline{v}(t) + i\overline{u}(t)$，那么它的**实部** $\overline{v}(t)$ 和 **虚部** $\overline{u}(t)$ 分别构成了方程组的两个实数基础解。

**【解题核心操作】**：

1. 算出一个复数特征值 $r = \lambda + i\mu$。
2. 算出对应的复数特征向量 $\overline{V}$。
3. 写出复数解 $\overline{X}_c = e^{(\lambda + i\mu)t} \overline{V}$。
4. 利用欧拉公式 $e^{i\mu t} = \cos(\mu t) + i\sin(\mu t)$ 将其展开。
5. 将实部和虚部分离开来，得到最终的两个实解。

**【相图形态】**：

1. **螺旋点 (Spiral Point)**：实部 $\lambda \neq 0$ 时。
   * $\lambda < 0$：向内旋转，**渐近稳定 (Asymptotically stable)**。
   * $\lambda > 0$：向外旋转，**不稳定 (Unstable)**。
2. **中心 (Center)**：实部 $\lambda = 0$（纯虚根）时。
   * 轨迹是一个个封闭的椭圆环，永远绕圈。**稳定但不渐近稳定 (Stable, but not asymptotically)**。

### 例题 a (螺旋点)

**题目**：求 $\overline{X}' = \begin{pmatrix} -1/2 & 1 \\ -1 & -1/2 \end{pmatrix} \overline{X}$ 的实基础解系。
**解析**：
**Step 1：求特征值**
$$
\begin{vmatrix} -1/2 - r & 1 \\ -1 & -1/2 - r \end{vmatrix} = (-1/2 - r)^2 - (-1)(1) = (r + 1/2)^2 + 1 = 0
$$

即 $(r + 1/2)^2 = -1 \implies r + 1/2 = \pm i \implies r = -1/2 \pm i$。
[*(注：实部* $\lambda = -1/2 < 0$*，属于**稳定螺旋点**)*。]()

**Step 2：求对应复特征向量 (取** $r = -1/2 + i$**)**
$$
(A - rI)\overline{V} = \begin{pmatrix} -1/2 - (-1/2 + i) & 1 \\ -1 & -1/2 - (-1/2 + i) \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} -i & 1 \\ -1 & -i \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

取第一行方程：$-ix + y = 0 \implies y = ix$。
令 $x = 1$，则 $y = i$。特征向量 $\overline{V} = \begin{pmatrix} 1 \\ i \end{pmatrix}$。

**Step 3：欧拉公式展开并分离实虚部**
复数解为：
$$
\overline{X}_c(t) = e^{(-1/2 + i)t} \begin{pmatrix} 1 \\ i \end{pmatrix} = e^{-t/2} e^{it} \begin{pmatrix} 1 \\ i \end{pmatrix}
$$

代入 $e^{it} = \cos t + i\sin t$：
$$
\overline{X}_c(t) = e^{-t/2} (\cos t + i\sin t) \begin{pmatrix} 1 \\ i \end{pmatrix} = e^{-t/2} \begin{pmatrix} \cos t + i\sin t \\ i(\cos t + i\sin t) \end{pmatrix}
$$

化简第二行 (注意 $i^2 = -1$)：
$$
\overline{X}_c(t) = e^{-t/2} \begin{pmatrix} \cos t + i\sin t \\ -\sin t + i\cos t \end{pmatrix}
$$

把含有 $i$ 的项分离开来：
$$
\overline{X}_c(t) = e^{-t/2} \left[ \begin{pmatrix} \cos t \\ -\sin t \end{pmatrix} + i \begin{pmatrix} \sin t \\ \cos t \end{pmatrix} \right]
$$

**最终通解** (由实部向量和虚部向量组合)：
$$
\overline{X}(t) = c_1 e^{-t/2} \begin{pmatrix} \cos t \\ -\sin t \end{pmatrix} + c_2 e^{-t/2} \begin{pmatrix} \sin t \\ \cos t \end{pmatrix}
$$

### 例题 b (中心)

**题目**：求 $\overline{X}' = \begin{pmatrix} 1 & -4 \\ 1/2 & -1 \end{pmatrix} \overline{X}$ 的实基础解系。
**解析**：
**Step 1：求特征值**
$$
\begin{vmatrix} 1 - r & -4 \\ 1/2 & -1 - r \end{vmatrix} = (1-r)(-1-r) - (-4)(1/2) = (r^2 - 1) + 2 = r^2 + 1 = 0
$$

解得 $r = \pm i$。
[*(注：实部* $\lambda = 0$*，属于**稳定中心**)*。]()

**Step 2：求对应复特征向量 (取** $r = i$**)**
$$
(A - iI)\overline{V} = \begin{pmatrix} 1 - i & -4 \\ 1/2 & -1 - i \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

取第一行方程：$(1-i)x - 4y = 0 \implies 4y = (1-i)x$。
为了避开分数，我们令 $x = 2+2i$（这是凑出来的技巧，或者你可以直接令 $x=4, y=1-i$ 也可以）：
*如果令* $x = 2+2i$*，则* $4y = (1-i)(2+2i) = 2(1-i^2) = 2(1 - (-1)) = 4 \implies y = 1$*。*
特征向量 $\overline{V} = \begin{pmatrix} 2+2i \\ 1 \end{pmatrix}$。

**Step 3：欧拉公式展开并分离实虚部**
复数解为：
$$
\overline{X}_c(t) = e^{it} \begin{pmatrix} 2+2i \\ 1 \end{pmatrix} = (\cos t + i\sin t) \begin{pmatrix} 2+2i \\ 1 \end{pmatrix}
$$

分别把 $\cos t + i\sin t$ 乘进上下两行：
* 第一行：$(\cos t + i\sin t)(2+2i) = 2\cos t + 2i\cos t + 2i\sin t + 2i^2\sin t = (2\cos t - 2\sin t) + i(2\cos t + 2\sin t)$
* 第二行：$(\cos t + i\sin t)(1) = \cos t + i\sin t$

组合起来分离实虚部：
$$
\overline{X}_c(t) = \begin{pmatrix} 2\cos t - 2\sin t \\ \cos t \end{pmatrix} + i \begin{pmatrix} 2\cos t + 2\sin t \\ \sin t \end{pmatrix}
$$

**最终通解**：
$$
\overline{X}(t) = c_1 \begin{pmatrix} 2\cos t - 2\sin t \\ \cos t \end{pmatrix} + c_2 \begin{pmatrix} 2\cos t + 2\sin t \\ \sin t \end{pmatrix}
$$