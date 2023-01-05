import numpy as np
from scipy.linalg import svd

Mat1=np.array([[1,3,5,7],[9,11,13,15],[17,19,21,23],[25,27,29,31]])
X,B,T=svd(Mat1)
print("\nDecomposed Matrix is (X)")
print(X)
print("\n")
print("Inverse of Matrix is (B)")
print(B)
print("\n")
print("Transpose of the Matrix is (T)")
print(T)

print("\n################")
print("X + T")
print(np.add(X,T))

print("\n")
print("X - T")
print(np.subtract(X,T))

print("\n")
print("2X^3")
Mat2=np.multiply(X,X)
Mat3=np.multiply(X,Mat2)
Mat4=np.multiply(2,Mat3)
print(Mat4)
