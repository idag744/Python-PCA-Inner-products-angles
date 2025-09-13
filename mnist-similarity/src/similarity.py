import numpy as np

def distance(x0: np.ndarray, x1: np.ndarray) -> float:
    """
    Compute Euclidean distance between two vectors.

    Args:
        x0 (np.ndarray): First vector.
        x1 (np.ndarray): Second vector.

    Returns:
        float: Euclidean distance.
    """
    diff = x0 - x1
    return np.sqrt(diff @ diff)


def angle(x0: np.ndarray, x1: np.ndarray) -> float:
    """
    Compute the angle (in radians) between two vectors using the dot product.

    Args:
        x0 (np.ndarray): First vector.
        x1 (np.ndarray): Second vector.

    Returns:
        float: Angle in radians between vectors.
    """
    dot_product = np.dot(x0, x1)
    norm_x0 = np.linalg.norm(x0)
    norm_x1 = np.linalg.norm(x1)
    cos_theta = np.clip(dot_product / (norm_x0 * norm_x1), -1.0, 1.0)
    return np.arccos(cos_theta)

