CodeGenie AI Explainer and Code Generator

Overview
This project is a comprehensive pipeline designed to analyze, explain, and semantically represent Python code snippets using advanced NLP transformer models. The system integrates parsing, structural analysis, embedding generation, and visualization, aiming to enhance understanding and usability of source code by both humans and machines.

Milestone 1: Code Explainer Pipeline
Step 1: Collect Code Snippets
Carefully select diverse Python code snippets to cover a wide range of programming features and complexity.

Focus on including functions, classes, imports, control flows, and error handling to ensure robust testing for parsing and embedding stages.

The diversity in collected snippets increases the generalization and real-world relevance of the pipeline.

Step 2: Code Explanation Functionality
Introduce a dedicated module that automatically generates human-readable explanations of Python code snippets.

The functionality relies on analyzing code structure, extracting docstrings, and recognizing key programming constructs.

This step strengthens the interpretability of the pipeline by providing transparent explanations supporting easier understanding and debugging for developers and non-developers alike.

Main focus: clarity, contextual awareness, and summarization of code intent without requiring external large models.

Step 3: Parse Snippets Using Abstract Syntax Tree (AST)
Utilize Python’s AST library to extract precise structural elements such as functions, classes, import statements, and control flow elements.

Parsing ensures systematic and language-aware code feature extraction, laying the foundation for semantic embedding.

This step emphasizes syntactic correctness and structural completeness for uniform downstream processing.

Step 4: Tokenize Code Snippets
Apply tokenization to transform code into discrete tokens representing keywords, identifiers, literals, and operators.

Tokenization bridges raw code and embedding models by aligning input format to pretrained transformer expectations.

The main challenge addressed here is preserving code semantics in the token sequence, facilitating effective embedding generation.

Step 5: Generate Code Embeddings Using Multiple Pretrained Models
Embed the tokenized code snippets using three different pretrained sentence-transformer models: MiniLM, DistilRoBERTa, and MPNet.

Each model provides unique semantic representations, highlighting different facets of code meaning.

Producing multiple embeddings helps compare model strengths and informs selection for specific code analysis applications.

Step 6: Visualize and Compare Embeddings
Reduce high-dimensional embeddings using Principal Component Analysis (PCA) for visualization.

Visual plots illustrate relationships, clustering, and distances among code snippets per model.

This visualization step aids in interpreting model behavior and effectiveness for code semantic grouping.

Results & Key Observations
The code explanation step plays a critical role in improving pipeline usability by offering concise, understandable code summaries that complement embedding data.

AST parsing provides accurate and reliable extraction of linguistic and structural features critical for semantic representation.

Tokenization produces compatible input for transformer models, preserving meaningful syntax boundaries.

Multi-model embeddings expose varied semantic interpretations, facilitating robust code similarity evaluation.

Visualization offers intuitive insight into embedding space, enabling qualitative assessment of model outputs.

How to Run the Pipeline
Clone this repository and install all dependencies, especially ensuring compatibility with numpy==1.26.4 for sentence-transformers.

Progress through the pipeline steps starting from raw code snippets, leveraging modular scripts or notebooks.

Use the explanation module to generate understandable summaries.

Generate and analyze embeddings to explore semantic similarities.

Visualize embedding relationships with the provided visualization tools.



---

## 📦 Requirements

```bash
pip install sentence-transformers transformers scikit-learn matplotlib seaborn
