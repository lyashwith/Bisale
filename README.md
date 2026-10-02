# Bisale

**Bisale** is a simple, beginner-friendly programming language/interpreter written in Python.

Bisale currently supports integer variables and printing their values.

> **Bisale is currently in an early development stage.**

## Example

A simple Bisale program:

```bisale
int(a=1)
int(b=2)

tojpav(a);
tojpav(b);
tojpav(a,b);
```

Output:

```text
1
2
1 2
```

## Syntax

### Integer Variables

Use `int()` to create an integer variable:

```bisale
int(a=1)
int(b=2)
```

The value is stored as an integer.

### Printing Variables

Use `tojpav()` to print the value of a variable:

```bisale
tojpav(a);
```

Output:

```text
1
```

Multiple variables can be printed together:

```bisale
tojpav(a,b);
```

Output:

```text
1 2
```

## Running a Bisale Program

Bisale source files use the `.bisale` extension.

For example:

```text
example.bisale
```

Run the Python interpreter:

```text
python interpreter.py
```

The interpreter asks for the Bisale filename:

```text
Enter Bisale file: example
```

It then reads:

```text
example.bisale
```

and interprets the supported Bisale statements.

## Interpreter

The current Bisale interpreter is written in **Python**.

It reads the `.bisale` file line by line and interprets the supported statements.

### Supported Statements

| Statement      | Purpose                    |
| -------------- | -------------------------- |
| `int(a=1)`     | Create an integer variable |
| `tojpav(a);`   | Print a variable           |
| `tojpav(a,b);` | Print multiple variables   |

## Project Structure

```text
bisale/
│
├── interpreter.py
├── example.bisale
└── README.md
```

### `interpreter.py`

Contains the Python interpreter that reads and executes Bisale programs.

### `example.bisale`

Contains an example Bisale program demonstrating integer variables and output.

### `README.md`

Contains documentation for the Bisale language and interpreter.

## Current Features

* [x] Integer variable declaration
* [x] Integer value assignment
* [x] Print a single variable
* [x] Print multiple variables
* [x] `.bisale` source files

## Limitations

The current interpreter is a basic implementation and has several limitations:

* Only integer values are currently supported.
* Variable names and values must follow the syntax expected by the interpreter.
* Invalid integer values can cause a Python `ValueError`.
* Using a variable that has not been declared can cause a Python `KeyError`.
* Invalid or incomplete `int()` statements can cause parsing errors.
* Multiple `=` characters in an `int()` statement are not handled correctly.
* Leading spaces before `int()` or `tojpav()` can prevent the interpreter from recognizing the statement.
* Empty or invalid `tojpav()` calls are not handled safely.
* Unsupported statements are currently ignored rather than producing a Bisale-specific error message.
* The interpreter does not yet provide custom syntax or runtime error messages.
* Variable names are stored exactly as entered, so accidental spaces can result in unexpected variable names.
* Declaring the same variable more than once overwrites its previous value.
* `tojpav()` with multiple variables does not explicitly add a newline after printing them, which can affect the formatting of subsequent output.
* The interpreter reads the entire `.bisale` file into memory before processing it.
* The interpreter currently relies on simple string processing rather than a dedicated lexer and parser.

## About

Bisale is a personal programming-language project created to explore how programming languages and interpreters work.

The current interpreter is implemented in Python.
## 👤 Author

Developed by **Yashwith L**

<a href="https://github.com/lyashwith">
  <img src="https://avatars.githubusercontent.com/u/313887780?s=100" alt="GitHub Logo" width="50">
</a>

---

## ⭐ Support

If you find **Bisale** useful or interesting, consider giving the repository a ⭐ on GitHub.


