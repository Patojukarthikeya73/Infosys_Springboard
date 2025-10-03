# 🧞‍♂️ CodeGenie: AI Code Explainer & Generator

## ✨ Overview

**CodeGenie** is an intelligent tool that demystifies Python code using abstract syntax trees (AST) and advanced transformer-based models. It explains structure and semantics while also offering insights into how different language models interpret code.

---

## 📚 Features

- 🔍 **AST Parsing** — Extracts functions, classes, imports, loops, conditionals, and exception blocks
- 🤖 **Transformer Embeddings** — Uses MiniLM, DistilRoBERTa, and MPNet for vector representations
- 📊 **Model Comparisons** — Compares semantic embeddings and similarities
- 📈 **Visualizations** — Interactive plots using TSNE/PCA
- 📎 **Colab Ready** — Fully executable in Google Colaboratory

---

## 🧠 Methodology

1. Parse each code snippet with Python’s built-in `ast` module.
2. Tokenize and encode the code using pretrained transformer models.
3. Calculate embedding similarities across models.
4. Visualize and analyze the models' understanding of code.

---

## 📦 Requirements

```bash
pip install sentence-transformers transformers scikit-learn matplotlib seaborn
