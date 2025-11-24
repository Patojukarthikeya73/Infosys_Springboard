# 📘 Infosys CodeGenie: AI Explainer and Code Generator
## 🧩 Milestone 2 — Code Generation, Evaluation & Interactive UIs

### 🎯 Objectives
This milestone focuses on implementing and evaluating multiple pretrained **code generation models** using Hugging Face.  
The main goals include:

- Implementing **code generation** using five pretrained transformer models.  
- Evaluating outputs with **complexity**, **maintainability**, and **Lines of Code (LOC)** metrics.  
- Designing **two interactive Google Colab UIs** for model benchmarking and inspection.  
- Testing with **10 domain-specific prompts**.  
- Visualizing **model performance** through comparative plots.

---

## 🧠 Detailed Approach & Methodology

### 1. Model Integration and Setup
- **Environment Setup:**  
  - Use **Google Colab GPU runtime** for efficient inference.  
  - Install required libraries:
    ```bash
    pip install transformers torch radon matplotlib ipywidgets
    ```

- **Authentication with Hugging Face:**  
  - Create an account on [Hugging Face](https://huggingface.co/).
  - Generate a Read Access Token (Settings → Access Tokens).  
  - Store it securely in Colab as:
    ```python
    from google.colab import userdata
    HF_TOKEN = userdata.get('HF_TOKEN')
    ```

- **Model Loading:**  
  Load all models using `transformers` library with `torch.bfloat16` precision and `device_map="auto"` for optimized resource allocation.
  ```python
  from transformers import AutoTokenizer, AutoModelForCausalLM

  models = {
      "DeepSeek": "deepseek-ai/deepseek-coder-1.3b-instruct",
      "Phi-2": "microsoft/phi-2",
      "Gemma": "google/gemma-2b-it",
      "Stable-Code": "stabilityai/stable-code-3b",
      "Replit-Code": "replit/replit-code-v1-3b"
  }

  tokenizers, model_objs = {}, {}
  for name, model_id in models.items():
      tokenizers[name] = AutoTokenizer.from_pretrained(model_id, token=HF_TOKEN)
      model_objs[name] = AutoModelForCausalLM.from_pretrained(
          model_id, token=HF_TOKEN, torch_dtype=torch.bfloat16, device_map="auto"
      )
  ```

---

### 2. Code Generation Process
Each model is prompted with a natural language description, and it generates corresponding code using controlled sampling parameters.

```python
def generate_code(prompt, model_name):
    tokenizer = tokenizers[model_name]
    model = model_objs[model_name]
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    output = model.generate(**inputs, max_length=256, temperature=0.7, top_p=0.9)
    return tokenizer.decode(output[0], skip_special_tokens=True)
```

**Approach Highlights:**
- Used same prompts for all models for fair benchmarking.  
- Applied consistent generation settings to ensure reproducibility.  
- Stored all generated code snippets for later metric evaluation.

---

### 3. Evaluation Methodology
We used the **Radon** library to compute three important software quality metrics:

| Metric | Description | Tool Used |
|---------|-------------|------------|
| **Cyclomatic Complexity** | Measures logical complexity of the generated code. | `radon.complexity.cc_visit()` |
| **Maintainability Index** | Quantifies code maintainability and readability. | `radon.metrics.mi_visit()` |
| **Lines of Code (LOC)** | Total executable lines, excluding comments and blank lines. | `radon.raw.analyze()` |

```python
from radon.complexity import cc_visit
from radon.metrics import mi_visit
from radon.raw import analyze

def evaluate_code(code):
    complexity = sum([f.complexity for f in cc_visit(code)])
    maintainability = mi_visit(code, True)
    loc = analyze(code).loc
    return {"Complexity": complexity, "Maintainability": maintainability, "LOC": loc}
```

**Methodology Summary:**
1. Generate code using all 5 models for each of the 10 test prompts.  
2. Run metrics evaluation on each code output.  
3. Store results in structured pandas DataFrame for easy comparison.  
4. Visualize differences using bar plots.

---

### 4. Interactive UIs (Using ipywidgets)

#### **UI 1: Benchmark All Models**
- User inputs a single prompt.  
- The system generates code from **all five models**.  
- Displays each model’s code, along with its metrics (Complexity, Maintainability, LOC).  
- Produces a **comparison bar chart** for metric visualization.

#### **UI 2: Inspect Selected Models**
- User selects models via **checkboxes**.  
- Generates and evaluates code only for selected models.  
- Shows per-model metrics and formatted code output.

```python
import ipywidgets as widgets
from IPython.display import display, Markdown

prompt_input = widgets.Textarea(description="Prompt:")
model_checkboxes = [widgets.Checkbox(value=True, description=m) for m in models.keys()]
generate_button = widgets.Button(description="Generate Code")

def on_click(_):
    selected_models = [cb.description for cb in model_checkboxes if cb.value]
    for model in selected_models:
        code = generate_code(prompt_input.value, model)
        metrics = evaluate_code(code)
        display(Markdown(f"### {model}\n```python\n{code}\n```\n**Metrics:** {metrics}"))

generate_button.on_click(on_click)
display(prompt_input, *model_checkboxes, generate_button)
```

---

### 5. Visualization and Performance Analysis
The evaluation results are visualized using `matplotlib`.  
Plots display comparative performance of all models across metrics.

```python
import matplotlib.pyplot as plt
import pandas as pd

# Assume metrics_df contains results for all models
metrics_df.plot(kind='bar', figsize=(10,6))
plt.title("Model Performance Comparison")
plt.ylabel("Metric Value")
plt.show()
```

**Plots Created:**
- **Bar Plot:** Average Complexity, Maintainability, LOC.  
- **Radar Plot (optional):** Overall model performance visualization.

---

### 6. Testing with 10 Prompts
The system was tested with **10 prompts** from diverse coding domains:
1. Sorting algorithms  
2. String manipulation  
3. Database connection  
4. REST API example  
5. Data Science preprocessing  
6. Mathematical formula generation  
7. File I/O operations  
8. OOP example  
9. Recursive function  
10. Error handling in Python  

For each prompt, the generated outputs were recorded, evaluated, and visualized.

---

### 7. Tools & Libraries Used

| Category | Tools / Libraries | Purpose |
|-----------|------------------|----------|
| **Core Models** | DeepSeek-Coder, Phi-2, Gemma-2B-IT, Stable-Code-3B, Replit-Code-3B | Code generation |
| **Frameworks** | Transformers, PyTorch | Model inference |
| **Evaluation** | Radon | Code quality metrics |
| **UI Components** | Ipywidgets, IPython | Interactive UI design |
| **Visualization** | Matplotlib, Seaborn (optional) | Metric plots |
| **Data Handling** | Pandas, NumPy | Storing and comparing results |
| **Runtime** | Google Colab GPU | Execution environment |

---

### 🚀 Future Enhancements
- Integrate fine-tuned, domain-specific models for better accuracy.  
- Expand evaluation metrics to include execution time and error analysis.  
- Add export functionality for CSV/JSON reports.  
- Deploy on **Gradio** or **Streamlit** as a web app for broader accessibility.

---

### ✅ Summary
Milestone 2 successfully implemented **code generation**, **automated evaluation**, and **interactive analysis** across multiple pretrained models.  
The combination of Hugging Face Transformers, Radon metrics, and ipywidgets UIs provides an end-to-end evaluation pipeline for assessing code generation model quality.
