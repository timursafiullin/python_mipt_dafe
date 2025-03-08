import numpy as np

class ShapeMismatchError(Exception):
    pass

def can_satisfy_demand(
    costs: np.ndarray,
    resource_amounts: np.ndarray,
    demand_expected: np.ndarray,
) -> bool:

    if (costs.shape[0] != resource_amounts.size) and (costs.shape[1] != demand_expected.size) and (resource_amounts.size != demand_expected):
        raise ShapeMismatchError()

    total_resources = costs @ demand_expected

    return np.all(total_resources <= resource_amounts)

def get_projections_components(
    matrix: np.ndarray,
    vector: np.ndarray,
) -> tuple[np.ndarray | None, np.ndarray | None]:

    if matrix.shape[0] != matrix.shape[1]:
        raise ShapeMismatchError("Matrice should be square")
    elif matrix.shape[1] != vector.shape[0]:
        raise ShapeMismatchError("Matrice columns should be equal to vector size")

    if np.linalg.det(matrix) == 0:
        return None, None

    norms_basys = np.linalg.norm(matrix, axis=1)

    orthogonal_projection = ((np.dot(matrix, vector) / (norms_basys)**2) * matrix.T).T
    orthogonal_component = vector - orthogonal_projection

    return orthogonal_projection, orthogonal_component

def adaptive_filter(
        Vs: np.ndarray,
        Vj: np.ndarray,
        diag_A: np.ndarray
) -> np.ndarray:
    M, K = Vj.shape

    if Vj.ndim != 2 or Vs.ndim != 2 or diag_A.ndim != 1:
        raise ShapeMismatchError()

    if diag_A.shape[0] != K or Vs.shape[0] != M:
        raise ShapeMismatchError()

    I = np.eye(K, dtype=Vj.dtype)
    A = np.diag(diag_A)

    coeff = (I + Vj.conj().T @ Vj @ A)
    b = Vj.conj().T @ Vs
    x = np.linalg.solve(coeff, b)

    y = Vs - Vj @ x
    return y


with open('./source/diag_A_data.npy', 'rb') as f:
    diag_A = np.load(f)

with open('./source/Vj_data.npy', 'rb') as f:
    Vj = np.load(f)

with open('./source/Vs_data.npy', 'rb') as f:
    Vs = np.load(f)

with open('./source/y_data.npy', 'rb') as f:
    y_check = np.load(f)

y = adaptive_filter(Vs, Vj, diag_A)
assert np.allclose(y, y_check)