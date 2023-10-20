import numpy as np

P = np.array([[0, 0.5, 0.5, 0], [0.5, 0, 0, 0.5], [0.5, 0, 0, 0.5], [0, 0.5, 0.5, 0]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(P.T)

# Find the eigenvector corresponding to eigenvalue 1
N = eigenvectors[:, np.where(np.isclose(eigenvalues, 1))].reshape(
    4,
)

# Print the value of N
print(N)
