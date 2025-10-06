import ast

for idx, snippet in enumerate(code_snippets):
    print(f"\n## Snippet {idx+1}")
    tree = ast.parse(snippet)
    functions = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
    classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
    imports = [n.names[0].name for n in ast.walk(tree) if isinstance(n, ast.Import)]
    patterns = [type(n).__name__ for n in ast.walk(tree) if isinstance(n, (ast.For, ast.If, ast.While, ast.Try))]
    print("Functions:", functions)
    print("Classes:", classes)
    print("Imports:", imports)
    print("Patterns:", patterns)

