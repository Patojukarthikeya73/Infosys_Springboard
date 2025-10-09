# CodeGenie AI Explainer and Code Generator

## Overview

This project is a comprehensive pipeline designed to analyze, explain, and semantically represent Python code snippets using advanced NLP transformer models. The system integrates parsing, structural analysis, embedding generation, and visualization, aiming to enhance understanding and usability of source code by both humans and machines.

---

## Milestone 1: Code Explainer Pipeline

### Step 1: Collect Code Snippets
- Carefully select diverse Python code snippets to cover a wide range of programming features and complexity.
- Focus on including functions, classes, imports, control flows, and error handling to ensure robust testing for parsing and embedding stages.
- The diversity in collected snippets increases the generalization and real-world relevance of the pipeline.

### Step 2: Code Explanation Functionality
- Introduce a dedicated module that automatically generates human-readable explanations of Python code snippets.
- The functionality relies on analyzing code structure, extracting docstrings, and recognizing key programming constructs.
- This step strengthens the interpretability of the pipeline by providing transparent explanations supporting easier understanding and debugging for developers and non-developers alike.
- **Main focus:** clarity, contextual awareness, and summarization of code intent without requiring external large models.

### Step 3: Parse Snippets Using Abstract Syntax Tree (AST)
- Utilize Python’s AST library to extract precise structural elements such as functions, classes, import statements, and control flow elements.
- Parsing ensures systematic and language-aware code feature extraction, laying the foundation for semantic embedding.
- **Emphasis:** syntactic correctness and structural completeness for uniform downstream processing.

### Step 4: Tokenize Code Snippets
- Apply tokenization to transform code into discrete tokens representing keywords, identifiers, literals, and operators.
- Tokenization bridges raw code and embedding models by aligning input format to pretrained transformer expectations.
- **Challenge addressed:** preserving code semantics in the token sequence, facilitating effective embedding generation.

### Step 5: Generate Code Embeddings Using Multiple Pretrained Models
- Embed the tokenized code snippets using three different pretrained sentence-transformer models: MiniLM, DistilRoBERTa, and MPNet.
- Each model provides unique semantic representations, highlighting different facets of code meaning.
- Producing multiple embeddings helps compare model strengths and informs selection for specific code analysis applications.

### Step 6: Visualize and Compare Embeddings
- Reduce high-dimensional embeddings using Principal Component Analysis (PCA) for visualization.
- Visual plots illustrate relationships, clustering, and distances among code snippets per model.
- **Purpose:** interpret model behavior and effectiveness for code semantic grouping.

---

## Results & Key Observations

- The **code explanation step** plays a critical role in improving pipeline usability by offering concise, understandable code summaries that complement embedding data.
- **AST parsing** provides accurate and reliable extraction of linguistic and structural features critical for semantic representation.
- **Tokenization** produces compatible input for transformer models, preserving meaningful syntax boundaries.
- **Multi-model embeddings** expose varied semantic interpretations, facilitating robust code similarity evaluation.
- **Visualization** offers intuitive insight into embedding space, enabling qualitative assessment of model outputs.

---

## Approaches, Methodologies, and Tools Used

### **1. Code Collection Approach**
**Methodology:**
- Code snippets were selected to ensure diversity in syntax and semantics — including function definitions, loops, conditionals, imports, and exception handling.
- The dataset creation followed a **representative sampling** strategy to mimic real-world development patterns and enhance the model’s robustness.

**Tools Used:**
- **Manual curation** for high-quality code samples.
- **GitHub Repositories & Open Datasets** (for collecting example scripts).
- **Python I/O utilities** (`os`, `glob`) to batch-read snippets for analysis.

---

### **2. Code Explanation Module**
**Approach:**
- Uses **rule-based AST traversal** and **pattern matching** to interpret code structures.
- Extracts logical elements (function names, parameters, conditions) and converts them into human-readable text.
- No external LLMs are required — this ensures lightweight, interpretable performance.

**Methodology:**
- Implements a **bottom-up explanation strategy** — first understanding small units (functions, loops), then generating contextual summaries.
- Uses **syntactic templates** and **semantic interpretation rules** to produce explanations.

**Tools Used:**
- **Python `ast` module** – to parse and traverse syntax trees.
- **Custom logic engine** for converting nodes into readable explanations.
- **NLP utilities** (`re`, `textwrap`) for formatting and summarizing text output.

---

### **3. AST Parsing and Structural Analysis**
**Approach:**
- Employs the **Abstract Syntax Tree (AST)** framework to understand the syntactic structure of Python code.
- Extracts entities like **FunctionDef**, **ClassDef**, **If**, **For**, and **Import** nodes for semantic analysis.

**Methodology:**
- Recursive traversal and feature extraction from the AST hierarchy.
- Error handling mechanisms ensure malformed or incomplete snippets don’t break parsing.
- Produces structured representations usable by downstream models.

**Tools Used:**
- **`ast` (Abstract Syntax Tree)** – for syntax parsing and node inspection.
- **`json`** – for representing extracted structural metadata.
- **`inspect`** – for runtime introspection of functions/classes (when applicable).

---

### **4. Tokenization Process**
**Approach:**
- Uses **context-aware tokenization** that separates code into identifiers, operators, and literals while preserving semantic relationships.
- Focuses on aligning tokenization with transformer model expectations for optimal embedding generation.

**Methodology:**
- Employs **custom tokenizers** and **pretrained HuggingFace tokenizers** compatible with each model.
- Ensures **semantic retention** — avoiding splitting meaningful code identifiers incorrectly.

**Tools Used:**
- **`tokenizers` (HuggingFace)** – for efficient subword-based tokenization.
- **`re` (Regular Expressions)** – for rule-based custom tokenization.
- **`nltk`** – for preprocessing textual docstrings when necessary.

---

### **5. Embedding Generation**
**Approach:**
- Leverages **sentence-transformer architectures** to convert tokenized code into dense semantic embeddings.
- Models: `all-MiniLM-L6-v2`, `distilroberta-base`, `all-mpnet-base-v2`.
- Multiple embeddings are generated per snippet for cross-model comparison.

**Methodology:**
- Each model encodes the same snippet, and the resulting embeddings are compared using **cosine similarity**.
- Ensures model-agnostic benchmarking and insight into representational variance.

**Tools Used:**
- **`sentence-transformers`** – for generating embeddings using pretrained transformers.
- **`numpy` / `pandas`** – for managing embedding vectors and computing similarity metrics.
- **`scikit-learn`** – for PCA reduction and clustering analysis.

---

### **6. Visualization and Comparison**
**Approach:**
- Applies **dimensionality reduction** techniques to visualize high-dimensional embeddings in 2D.
- Uses **Principal Component Analysis (PCA)** for interpretability and simplicity.

**Methodology:**
- Embeddings are normalized and projected onto two principal axes.
- Visualizations highlight semantic closeness among code snippets.

**Tools Used:**
- **`matplotlib`** – for static 2D visualization of embedding distributions.
- **`scikit-learn.decomposition.PCA`** – for dimensionality reduction.
- **`plotly`** – for optional interactive embedding visualization.

---

## How to Run the Pipeline

1. Clone this repository and install all dependencies, especially ensuring compatibility with `numpy==1.26.4` for sentence-transformers.
2. Progress through the pipeline steps starting from raw code snippets, leveraging modular scripts or notebooks.
3. Use the explanation module to generate understandable summaries.
4. Generate and analyze embeddings to explore semantic similarities.
5. Visualize embedding relationships with the provided visualization tools.
