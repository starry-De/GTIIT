# 📔 ODE 知识笔记：幂级数解法 (Power Series Method)

## 1. 核心思想 (Core Concept)
对于变系数线性 ODE，假设解在常点（通常为 $x=0$）附近可展开为级数：
$$y(x) = \sum_{n=0}^{\infty} a_n x^n$$
通过将级数代入原方程，利用**多项式恒等定理**（所有系数必为 0）求出未知系数 $a_n$。

---

## 2. 方法论：四步 SOP 流程

### Step 1: 设与导 (Assumption)
写出标准三件套（注意求和起点）：
- $y = \sum_{n=0}^{\infty} a_n x^n$
- $y' = \sum_{n=1}^{\infty} n a_n x^{n-1}$
- $y'' = \sum_{n=2}^{\infty} n(n-1) a_n x^{n-2}$

### Step 2: 齐与换 (Shift Indices)
- **乘入：** 将方程项前的系数（如 $x, x^2$）乘进求和号内部。
- **换元：** 统一所有项的 $x$ 指数为 $x^m$。
  > *技巧：* 若原来是 $x^{n-k}$，令 $m = n-k \Rightarrow n = m+k$，同时更新 $a_n$ 为 $a_{m+k}$。

### Step 3: 提与合 (Peeling & Aligning)
- **提：** 找到各求和号起点的最大值（如 $m=2$），将起点较小的级数中 $m=0, 1$ 的项单独提出来。
- **合：** 将剩下的求和号合并为一个 $\sum_{m=k}^{\infty} [\dots] x^m$。

### Step 4: 推 (Recurrence Relation)
1. **外部项 = 0：** 解出 $a_2, a_3$ 等具体数值。
2. **内部系数 = 0：** 得到 $a_{m+k}$ 与 $a_m$ 的**递推公式**。

---

## 3. 上课实战：Airy 方程 $y'' - xy = 0$

### (1) 代入与换元
- **第一项** ($y''$): $\sum_{n=2}^{\infty} n(n-1) a_n x^{n-2} \xrightarrow{m=n-2} \sum_{m=0}^{\infty} (m+2)(m+1) a_{m+2} x^m$
- **第二项** ($-xy$): $-\sum_{n=0}^{\infty} a_n x^{n+1} \xrightarrow{m=n+1} \sum_{m=1}^{\infty} a_{m-1} x^m$

### (2) 提取与合并
由于第二项从 $m=1$ 开始，提取第一项的 $m=0$：
$$2a_2 + \sum_{m=1}^{\infty} \left[ (m+2)(m+1) a_{m+2} - a_{m-1} \right] x^m = 0$$

### (3) 递推逻辑

- **外部：** $2a_2 = 0 \Rightarrow a_2 = 0$
- **内部：** $a_{m+2} = \frac{a_{m-1}}{(m+2)(m+1)}$

**系数链条：**
- $a_0 \rightarrow a_3 \rightarrow a_6 \dots$ (第一基本解)
- $a_1 \rightarrow a_4 \rightarrow a_7 \dots$ (第二基本解)
- $a_2 \rightarrow a_5 \rightarrow a_8 = 0$ (全部为 0)

---

## 4. 复习要点 (Checklist)
- [ ] **初值检查：** 若给定了 $y(0)$ 和 $y'(0)$，则 $a_0 = y(0)$, $a_1 = y'(0)$。
- [ ] **收敛半径：** 注意 $(1+x^2)$ 这种前序系数在复平面上的零点会限制级数的收敛范围。
- [ ] **拆项技巧：** 面对 $(1+x)y''$，必须拆成 $y'' + xy''$ 分别处理。