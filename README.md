# Smolcalc,

![Tests](https://github.com/andre4k14/smolcalc/actions/workflows/tests.yml/badge.svg)

This is a small calculator library.

## Installation

You need python 3.9 or higher.

### Requirements

None

To install it simply copy the command below.

```bash
pip3 install "git+https://github.com/andre4k14/smolcalc.git"
```

## How to use it.

```python
from smolcalc import evaluate, evaluate_all

print(evaluate("1+2*6/67"))  # => 1.1791044776119404
print(evaluate("1+2*6/67", decimal_separator=","))  # => 1,1791044776119404
print(evaluate("1+2*6/67", decimal_separator="."))  # => 1.1791044776119404

# uses the gamma function for factorial 
print(evaluate("0,1!", special=True, decimal_separator=","))  # => 9,513507698668732

print(evaluate_all(["1+2*6/67", "1,5+3,5", "lg(10)", "2*(2,7 -1 )", "1_000_000"], decimal_separator=","))
# output => ["1,1791044776119404","5","1","3,4000000000000004","1000000"]
print(evaluate_all(["1+2*6/67", "1.5+3.5", "lg(10)", "2*(2.7 -1 )", "1_000_000"]))
# output => ["1.1791044776119404","5","1","3.4000000000000004","1000000"]
print(evaluate_all(["1+2*6/67", "1,5+3,5", "lg(10)", "2*(2,7 -1 )", "1_000_000"],
                   decimal_separator=[".", ",", ",", ",", "."]))
# output => ["1.1791044776119404","5","1","3,4000000000000004","1000000"]
```

All possible operators are listed in the table below.

| operators         | symbole |    syntax    | 
|:------------------|:-------:|:------------:|
| plus              |    +    |  a+b or +a   |
| minus             |    -    |  a-b or -a   |
| multiple          |    *    |     a*b      |
| divide            |    /    |     a/b      |
| parentheses       |   ()    | (expression) |
| common logarithm  |  lg()   |    lg(a)     |
| natural logarithm |  ln()   |    ln(a)     |
| power             |    ^    |     a^b      |
| square root       | sqrt()  |   sqrt(a)    |
| factorial         |    !    |      a!      |

All possible constants are listed in the table below.

| constants      | symbole |
|:---------------|:-------:|
| Pi             |   pi    |
| euler's number |    e    |

Factorial uses gamma function if special==True

Order of Operators

1. parentheses
2. factorial
3. exponents
4. multiplication and division
5. addition and subtraction

You can use . and , as the decimal_separator.

If special is True your can use the gamma function with decimal number else an error gets returned.

If you find any errors, inefficient pieces of code or any other problem pls tell me, so I can learn and fix it.

The library uses the standard math lib from python for lg(), ln(), ^, sqrt() and !.

The library is based on this GitHub project and video series:
https://github.com/davidcallanan/py-simple-math-interpreter

## Installation for development

### Requirements

```bash
pip install -r requirements_dev.txt
```

Install the package locally

```bash
pip install -e . 
```

### tests

```bash
pytest
```

### linter

```bash
flake8 src
```

### static type checker

```bash
mypy src
```

### Running all tests for multiple python version

```bash
tox
```


