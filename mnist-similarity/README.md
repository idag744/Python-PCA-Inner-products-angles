# MNIST Similarity Explorer

This project explores **distances** and **angles** between images in the MNIST handwritten digits dataset.  
It demonstrates how simple vector operations (dot products, norms, Euclidean distance) can measure **similarity between digits**.

---

## ✨ Features
- Compute **Euclidean distances** between digit images.
- Compute **angles between image vectors**.
- Find **most similar and most different digits** in the dataset.
- Visualize **mean images for each class** and compare them with distance/angle heatmaps.
- Interactive exploration notebook.

---

## 📂 Project Structure
mnist-similarity/
│
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── similarity.py      # distance & angle functions
│   ├── analysis.py        # analysis functions (mean images, similarity matrices)
│   ├── visualization.py   # plotting functions
│   └── data_loader.py     # MNIST loader
│
├── notebooks/
│   └── mnist_exploration.ipynb  # for demos & visualizations
│
└── examples/
    └── compare_digits.py  # example script showing usage

---

## 🚀 Quickstart

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/mnist-similarity.git
   cd mnist-similarity
2. Install dependencies:

pip install -r requirements.txt


3. Run example script:

python examples/compare_digits.py


4. Explore interactively:

jupyter notebook notebooks/mnist_exploration.ipynb
