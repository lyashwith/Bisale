# Bisale

**Bisale** is a simple, beginner-friendly programming language and interpreter written in Python.

Bisale is currently in an **early development stage**. The interpreter is being built manually to understand how programming languages work, starting with a custom **lexer** and **parser**.

## Current Syntax

### Integer Variables

Use `int()` to declare integer variables:

```bisale
int(a)
```

A variable without an assigned value starts with `0`.

Multiple variables can be declared in one statement:

```bisale
int(a,b,c)
```

Values can also be assigned during declaration:

```bisale
int(a=1)
int(b=2)
```

Assigned and unassigned variables can be mixed:

```bisale
int(a=1,b,c=3)
```

This creates:

```text
a = 1
b = 0
c = 3
```

## Example

A current Bisale program:

```bisale
int(i=1,j=1)
int(k)
int(l=2,w)
```

The parser currently produces:

```text
{'i': 1, 'j': 1, 'k': 0, 'l': 2, 'w': 0}
```

## Source Files

Bisale source files use the `.bisale` extension.

For example:

```text
example.bisale
```

The interpreter asks for the Bisale filename:

```text
Enter Bisale name to cook:example
```

It then reads:

```text
example.bisale
```

## Interpreter Architecture

Bisale currently follows this basic processing pipeline:

```text
.bisale source
      ↓
    Lexer
      ↓
    Tokens
      ↓
    Parser
      ↓
 Variable dictionary
```

### Lexer

The lexer reads the source code **character by character** and converts the source into tokens.

For example:

```bisale
int(a=1)
```

is converted into tokens similar to:

```text
INT
LEFT_PARENT
IDENTIFIER
EQUAL
INTEGER
RIGHT_PARENT
```

### Token Types

The lexer currently recognizes the following token types:

| Token          | Meaning                    |
| -------------- | -------------------------- |
| `INT`          | `int` variable declaration |
| `OUTPUT`       | `thojpav` output keyword   |
| `LEFT_PARENT`  | `(`                        |
| `RIGHT_PARENT` | `)`                        |
| `EQUAL`        | `=`                        |
| `COMMA`        | `,`                        |
| `SEMICOLON`    | `;`                        |
| `IDENTIFIER`   | Variable name              |
| `INTEGER`      | Integer value              |

### Parser

The parser reads the tokens produced by the lexer and processes variable declarations.

For example:

```bisale
int(a=10,b,c=5)
```

produces a Python dictionary:

```python
{
    "a": 10,
    "b": 0,
    "c": 5
}
```

The dictionary is currently used to store the declared variables and their values.

## Current Features

* [x] `.bisale` source files
* [x] Character-by-character lexical analysis
* [x] Token generation
* [x] Integer variable declaration
* [x] Multiple variable declarations
* [x] Integer value assignment during declaration
* [x] Default value `0`
* [x] Mixed assigned and unassigned variables
* [x] `thojpav` recognition by the lexer
* [ ] `thojpav()` output execution

## Output

Bisale uses **`thojpav()`** as its output keyword.

The lexer currently recognizes `thojpav` and generates an `OUTPUT` token.

Example syntax:

```bisale
thojpav(a);
```

However, **output execution is not yet implemented in the parser**.

The output system will be developed separately as the interpreter grows.

## Future Development

As Bisale develops, additional language functionality may be added.

Possible future areas include:

* Completing `thojpav()` output execution.
* Supporting multiple variables in output statements.
* Supporting direct values in output statements.
* Adding additional data types.
* Adding arithmetic operations.
* Adding input functionality.
* Improving syntax validation.
* Adding better Bisale-specific error messages.
* Expanding the lexer and parser.

These are areas for future development and are **not currently implemented**.

## Limitations

The current implementation is a basic lexer and parser and has several limitations:

* Only integer variables are currently supported.
* Negative integers such as `-1` are not currently recognized as `INTEGER` tokens.
* Decimal numbers are not supported.
* Input statements are not supported.
* Arithmetic operations such as `+`, `-`, `*`, and `/` are not supported.
* `thojpav()` is recognized by the lexer, but its execution is not yet implemented.
* Invalid or incomplete syntax can cause Python `IndexError` exceptions because the parser currently assumes that some token positions exist.
* Invalid integer assignments can cause parsing problems.
* Unsupported statements may be ignored instead of producing Bisale-specific errors.
* Variable redeclaration currently overwrites the previous value in the Python dictionary.
* Whitespace is currently ignored by the lexer, so some malformed input may result in unexpected identifiers.
* The entire `.bisale` source file is currently read into memory before lexical analysis.

## Project Structure

```text
Bisale/
│
├── Atil.py
├── example.bisale
└── README.md
```
### `Atil.py`

Contains the Python implementation of the **Atil interpreter**, including the lexer and parser.

### `example.bisale`

Contains an example Bisale source program.

### `README.md`

Contains documentation for the Bisale language and interpreter.

## About

Bisale is a personal programming-language project created to explore how programming languages and interpreters work.

The interpreter is being developed **incrementally from scratch in Python**, with the lexer and parser implemented manually as part of the learning process.

## Author

Developed by **Yashwith L**

<a href="https://github.com/lyashwith">
  <img src="https://avatars.githubusercontent.com/u/313887780?s=100" alt="GitHub Logo" width="50">
</a>

---

## Support

If you find **Bisale** useful or interesting, consider giving the repository a ⭐ on GitHub.
