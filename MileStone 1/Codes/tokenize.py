import io
import tokenize

def tokenize_code(snippet):
    tokens = []
    readline = io.BytesIO(snippet.encode('utf-8')).readline
    for tok in tokenize.tokenize(readline):
        tokens.append((tokenize.tok_name.get(tok.type), tok.string))
    return tokens

for idx, snippet in enumerate(code_snippets):
    print(f"\n## Tokens for Snippet {idx+1}")
    print(tokenize_code(snippet))



