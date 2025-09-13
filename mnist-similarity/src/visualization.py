import matplotlib.pyplot as plt
import numpy as np

def plot_similarity_matrix(matrix, title: str, labels: list):
    """Plot similarity (distance or angle) matrix as heatmap."""
    fig, ax = plt.subplots(figsize=(6, 5))
    grid = ax.imshow(matrix, interpolation='nearest', cmap="viridis")
    ax.set(title=title, xticks=range(len(labels)), yticks=range(len(labels)))
    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)
    fig.colorbar(grid)
    plt.show()

