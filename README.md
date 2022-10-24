複素ベクトル$\boldsymbol{z} \in \mathbb{C}^{M}$を次元2倍の実ベクトル$\in \mathbb{R}^{2M}$として扱いたいときの変換器

$$
\rm{C \ to\  R}:
\boldsymbol{z} \mapsto 
\begin{bmatrix} 
\Re(\boldsymbol{z}) \\
\Im(\boldsymbol{z})
\end{bmatrix}
$$
逆変換$\rm{R \to C}$も実装済み． <br>
複素行列$A \in \mathbb{C}^{N \times M}$は$\mathbb{C}^{2N \times 2M}$に写る

$$
\rm{C \ to\  R}:
A \mapsto 
\begin{bmatrix} 
\Re(A) & -\Im(A) \\
\Im(A) & \Re(A) \\
\end{bmatrix}
$$