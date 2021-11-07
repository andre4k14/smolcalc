# Smolcalc,

is a small calculator library. to use it simply install smolcalc.

```bash
pip3 install "git+https://github.com/andre4k14/smolcalc.git"
```

## How to use it. 

```python
from smolcalc import evaluate, evaluate_all

print(evaluate("1+2*6/67")) #=> 1.1791044776119404
print(evaluate("1+2*6/67",decimal_separator=",")) #=> 1,1791044776119404
print(evaluate("1+2*6/67",decimal_separator=".")) #=> 1.1791044776119404

#uses the gamma function for factorial 
print(evaluate("0,1!", special=True, decimal_separator=",")) #=> 0,951350769866873

print(evaluate_all(["1+2*6/67","1,5+3,5","lg(10)","2*(2,7 -1 )","1_000_000"],decimal_separator=",")) #=> ["1,1791044776119404","5","1","3,4000000000000004","1000000"]
print(evaluate_all(["1+2*6/67","1.5+3.5","lg(10)","2*(2.7 -1 )","1_000_000"])) #=> ["1.1791044776119404","5","1","3.4000000000000004","1000000"]
print(evaluate_all(["1+2*6/67","1,5+3,5","lg(10)","2*(2,7 -1 )","1_000_000"],decimal_separator=[".",",",",",",","."])) #=> ["1.1791044776119404","5","1","3,4000000000000004","1000000"]



```

All possible operators are +, -, *, /, (), lg(), ln(), ^, pi, e, sqrt() and ! (uses gamma function).

You can use . and , as the decimal_separator.

If special is True your can use the gamma function with decimal number else an error gets returned.

If you find any errors, inefficient pieces of code or any other problem pls tell me, so I can learn and fix it.

The library uses the standard math lib from python for lg(), ln(), ^, sqrt() and !.

The library is based on this GitHub project and video series:
https://github.com/davidcallanan/py-simple-math-interpreter
