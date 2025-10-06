# Step 1: Define a list of at least 10 code snippets
code_snippets = [
    "def factorial(n):\n    return 1 if n==0 else n*factorial(n-1)",
    "class MyClass:\n    def __init__(self, x):\n        self.x = x",
    "import math\n\ndef circle_area(r):\n    return math.pi * r ** 2",
    "def bubble_sort(arr):\n    for i in range(len(arr)):\n        for j in range(len(arr)-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]",
    "def fibonacci(n):\n    a, b = 0, 1\n    for _ in range(n):\n        a, b = b, a+b\n    return a",
    "class Vehicle:\n    pass",
    "from datetime import datetime\n\ndef get_current_time():\n    return datetime.now()",
    "def is_even(num):\n    return num % 2 == 0",
    "def greet(name):\n    print(f'Hello, {name}!')",
    "try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')"
]

