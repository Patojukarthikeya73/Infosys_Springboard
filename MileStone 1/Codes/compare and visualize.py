import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

pca = PCA(n_components=2)
plt.figure(figsize=(8,6))

for model_name in embeddings:
    reduced = pca.fit_transform(embeddings[model_name])
    plt.scatter(reduced[:,0], reduced[:,1], label=model_name)

plt.title("PCA of Code Snippet Embeddings by Model")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.grid(True)
plt.show()




