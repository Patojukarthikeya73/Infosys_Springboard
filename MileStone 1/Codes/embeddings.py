import numpy
from sentence_transformers import SentenceTransformer

print(numpy.__version__)

models = {
    "MiniLM": SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2"),
    "DistilRoBERTa": SentenceTransformer("sentence-transformers/all-distilroberta-v1"),
    "MPNet": SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
}

embeddings = {}
for model_name, model in models.items():
    embeddings[model_name] = model.encode(code_snippets, batch_size=4, show_progress_bar=True)
    print(f"{model_name} embeddings shape:", embeddings[model_name].shape)




