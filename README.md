# PY110: Advanced Python Concepts

Welcome to PY110 – Advanced Python, the next step in my journey from diesel to debugging. This repo contains all my notes, exercises, and practice problems as I dive deeper into Python's advanced features and best practices. Adding this line here to update my README

---

## 🧠 Topics Covered

This phase focuses on leveling up beyond the basics, including:

- **Function Internals**
  - `*args`, `**kwargs`, unpacking patterns
  - Default arguments and their traps
- **First-Class Functions & Functional Programming**
  - Higher-order functions (`map`, `filter`, `reduce`, `lambda`)
  - Closures, scopes, and the LEGB rule
- **Decorators & Generator Functions**
  - Creating and applying decorators
  - Lazy evaluation, `yield`, and generator pipelines
- **Object-Oriented Deep Dive**
  - Dunder methods, custom classes, and inheritance
  - Encapsulation, polymorphism, and composition
- **Data Structures & Algorithms**
  - Lists, dictionaries, sets, and tuples
  - Searching, sorting, and recursion
- **Error Handling & Testing**
  - Try/except blocks, custom exceptions
  - Writing unit tests with `unittest` and `pytest`
- **File I/O & Context Managers**
  - Reading from and writing to files
  - Using `with` statements for resource management

---

## 📁 Directory Structure

```plaintext
PY_110/
├── exercises/
│   ├── Easy_1/
│   │   ├── string_to_integer.py
│   │   ├── integer_to_string.py
│   │   ├── signed_integer_to_string.py
│   │   ├── string_to_signed_integer.py
│   │   ├── word_sizes.py
│   │   ├── swap.py
│   │   ├── running_total.py
│   │   └── search.py
│   └── ...
├── lesson_1/
│   ├── notes.md
│   └── examples.py
├── .gitignore
└── README.md
```

---

## 📝 Recent Additions

Here are some of the latest exercises and utilities added:

- **String and Integer Conversions**
  - `string_to_integer.py`: Converts a numeric string to an integer without using `int()`.
  - `integer_to_string.py`: Converts an integer to a string without using `str()`.
  - `signed_integer_to_string.py`: Handles signed integers for conversion to strings.
  - `string_to_signed_integer.py`: Parses signed numeric strings into integers.

- **String Manipulation**
  - `word_sizes.py`: Calculates the frequency of word lengths in a given string.
  - `swap.py`: Swaps the first and last characters of each word in a string.

- **List Operations**
  - `running_total.py`: Computes the running total of a list of numbers.
  - `search.py`: Checks if a number exists within a list.

---

## 🚀 Getting Started

To run any of the exercises:

1. Clone the repository:
   ```bash
   git clone https://github.com/jdarov/PY_110.git
   ```
2. Navigate to the desired directory:
   ```bash
   cd PY_110/exercises/Easy_1
   ```
3. Run the Python script:
   ```bash
   python3 script_name.py
   ```

---

## 📚 Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Real Python Tutorials](https://realpython.com/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.