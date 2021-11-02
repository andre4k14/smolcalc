# Smolcalc,

is a small calculator library. to use it simply install smolcalc.

```bash
pip3 install "git+http://192.168.4.222:9080/andre4k14/calculator.git"
```

## How to use it. 

```python
from smolcalc.calculator import evaluate, evaluate_all

print(evaluate("1+2*6/67")) #=> 1.1791044776119404
print(evaluate("1+2*6/67",decimal_separator=",")) #=> 1,1791044776119404
print(evaluate("1+2*6/67",decimal_separator=".")) #=> 1.1791044776119404

print(evaluate_all(["1+2*6/67","1,5+3,5","lg(10)","2*(2,7 -1 )","1_000_000"],decimal_separator=",")) #=> ["1,1791044776119404","5","1","3,4000000000000004","1000000"]
print(evaluate_all(["1+2*6/67","1.5+3.5","lg(10)","2*(2.7 -1 )","1_000_000"])) #=> ["1.1791044776119404","5","1","3.4000000000000004","1000000"]
print(evaluate_all(["1+2*6/67","1,5+3,5","lg(10)","2*(2,7 -1 )","1_000_000"],decimal_separator=[".",",",",",",","."])) #=> ["1.1791044776119404","5","1","3,4000000000000004","1000000"]



```

all possible operators are + - * / () lg() ln() ^ pi sqrt() and !


if you find any errors, inefficient pieces of code or any other problem pls tell me, so I can learn and fix it
