import numpy as np
from .similarity import distance, angle

def compute_class_means(images: np.ndarray, labels: np.ndarray) -> dict:
    """Compute mean image for each digit class."""
    mean_images = {}
    for n in np.unique(labels):
        mean_images[n] = np.mean(images[labels == n], axis=0)
    return mean_images

def compute_similarity_matrices(mean_images: dict):
    """Compute pairwise distance and angle matrices between class means."""
    classes = list(mean_images.keys())
    n = len(classes)
    MD = np.zeros((n, n))
    AG = np.zeros((n, n))
    for i in classes:
        for j in classes:
            MD[i, j] = distance(mean_images[i], mean_images[j])
            AG[i, j] = angle(mean_images[i].ravel(), mean_images[j].ravel())
    return MD, AG

