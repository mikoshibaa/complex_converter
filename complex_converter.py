# -*- coding: utf-8 -*-
"""complex_converter.ipynb

Automatically generated by Colaboratory.


複素ベクトル$\boldsymbol{z} \in \mathbb{C}^{M}$を次元2倍の実ベクトル$\in \mathbb{R}^{2M}$として扱いたいときの変換器

\begin{align}
\rm{C \ to\  R}:
\boldsymbol{z} \mapsto 
\begin{bmatrix} 
\Re(\boldsymbol{z}) \\
\Im(\boldsymbol{z})
\end{bmatrix}
\end{align}
逆変換$\rm{R \to C}$も実装済み． \\
複素行列$A \in \mathbb{C}^{N \times M}$は$\mathbb{C}^{2N \times 2M}$に写る

\begin{align}
\rm{C \ to\  R}:
A \mapsto 
\begin{bmatrix} 
\Re(A) & -\Im(A) \\
\Im(A) & \Re(A) \\
\end{bmatrix}
\end{align}

本モジュールは$\boldsymbol{z}, A$のshapeが$( \rm{batch size}, M, 1\ \rm{or} \ N)$のときのみ対応している.
"""

import numpy as np

class ComplexConverter:
  def __init__(self):
    return
  
  def CtoR(self, z):
    z_dim = z.ndim
    
    if z_dim == 3:
      batch_size, M, N = z.shape
      if N == 1:
        real_vec = np.array([
            np.concatenate([
            z[:, :, 0].real,
            z[:, :, 0].imag
          ], axis = 1)
        ]).transpose((1, 2, 0))
        return real_vec
      
      else:
        real_matrix_row_1 = np.concatenate([z.real, -z.imag], axis = 2)
        real_matrix_row_2 = np.concatenate([z.imag, z.real], axis = 2)
        real_matrix = np.concatenate([
            real_matrix_row_1,
            real_matrix_row_2
        ], axis = 1)
        return real_matrix

    
    else:
      raise ValueError("imput ndim must be 3")

  def RtoC(self, H):
    H_dim = H.ndim

    if H_dim == 3:
      batch_size, M, N = H.shape
      if N == 1:
        v_real, v_comp = H[:, 0:M//2, :], H[:, M//2:M, :]
        v_comp = v_real + 1j * v_comp
        return v_comp
      
      else:
        mat_real, mat_imag = H[:, 0:M//2, 0:M//2], H[:, M//2:M, 0:M//2]
        mat_comp = mat_real + 1j * mat_imag
        return mat_comp
    
    else:
      raise ValueError("imput ndim must be 3")