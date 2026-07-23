The 2-site Hubbard model reads
$$
\hat{H} = -t\sum_\sigma(c_{1\sigma}^\dagger c_{2\sigma} + c_{2\sigma}^\dagger c_{1\sigma}) + U \sum_{i=1}^2 n_{i\uparrow} n_{i\downarrow}
$$

Let's use the following ordering convention,
- first up-spins, then down-spins
- site number increasing from left to right.

We consider 2 electrons, the basis is:

$$
\begin{split}
0:\quad & c_{1\uparrow}^\dagger c_{2\uparrow}^\dagger|\rangle = |\uparrow, \uparrow\rangle= |1 1\rangle |0 0 \rangle\\
1:\quad & c_{1\uparrow}^\dagger c_{1\downarrow}^\dagger|\rangle =|D, 0\rangle= |1 0\rangle |1 0 \rangle\\
2:\quad & c_{1\uparrow}^\dagger c_{2\downarrow}^\dagger|\rangle =|\uparrow, \downarrow\rangle= |1 0\rangle |0 1 \rangle\\
3:\quad & c_{2\uparrow}^\dagger c_{1\downarrow}^\dagger|\rangle =|\downarrow, \uparrow\rangle= |0 1\rangle |1 0 \rangle\\
4:\quad & c_{2\uparrow}^\dagger c_{2\downarrow}^\dagger|\rangle =|0, D\rangle= |0 1\rangle |0 1 \rangle\\
5:\quad & c_{1\downarrow}^\dagger c_{2\downarrow}^\dagger|\rangle =|\downarrow,\downarrow\rangle= |0 0\rangle |1 1 \rangle\\
\end{split}
$$

$$
\begin{split}
\hat{T}|0\rangle &= 0 \\
\hat{T}|1\rangle &= -t(c_{2\downarrow}^\dagger c_{1\downarrow} + c_{2\uparrow}^\dagger c_{1\uparrow})c_{1\uparrow}^\dagger c_{1\downarrow}^\dagger|\rangle \\
&= -tc_{2\downarrow}^\dagger c_{1\downarrow}c_{1\uparrow}^\dagger c_{1\downarrow}^\dagger|\rangle -t c_{2\uparrow}^\dagger c_{1\uparrow}c_{1\uparrow}^\dagger c_{1\downarrow}^\dagger|\rangle \\
&= tc_{2\downarrow}^\dagger c_{1\uparrow}^\dagger c_{1\downarrow} c_{1\downarrow}^\dagger|\rangle -t c_{2\uparrow}^\dagger c_{1\downarrow}^\dagger|\rangle + t c_{2\uparrow}^\dagger c_{1\uparrow}^\dagger c_{1\uparrow} c_{1\downarrow}^\dagger|\rangle \\
&= -t c_{1\uparrow}^\dagger c_{2\downarrow}^\dagger |\rangle -t|3\rangle = -t|2\rangle -t|3\rangle \\
\hat{T}|2\rangle &=  -t (c_{1\downarrow}^\dagger c_{2\downarrow} + c_{2\uparrow}^\dagger c_{1\uparrow})c_{1\uparrow}^\dagger c_{2\downarrow}^\dagger|\rangle \\
&=  -t |1\rangle -t |4\rangle \\
\hat{T}|3\rangle &= -t c_{1\uparrow}^\dagger c_{2\uparrow}c_{2\uparrow}^\dagger c_{1\downarrow}^\dagger |\rangle -t  c_{2\downarrow}^\dagger c_{1\downarrow} c_{2\uparrow}^\dagger c_{1\downarrow}^\dagger|\rangle\\
&= -t |1\rangle - t  |4\rangle\\
\hat{T}|4\rangle &= -t c_{1\uparrow}^\dagger c_{2\uparrow}c_{2\uparrow}^\dagger c_{2\downarrow}^\dagger|\rangle -tc_{1\downarrow}^\dagger c_{2\downarrow} c_{2\uparrow}^\dagger c_{2\downarrow}^\dagger|\rangle \\
&= -t c_{1\uparrow}^\dagger c_{2\downarrow}^\dagger|\rangle + tc_{1\downarrow}^\dagger c_{2\uparrow}^\dagger |\rangle \\
&= -t |2\rangle - t|3\rangle \\
\hat{T}|5\rangle &= 0 \\
\end{split}
$$

