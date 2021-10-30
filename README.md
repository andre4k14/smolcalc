# Smolcalc,

is a small calculator library. to use it simply install smolcalc.

```bash
pip3 install "git+http://192.168.4.222:9080/andre4k14/calculator.git"
```

## How to use it. 

```python
from smolcalc.calculator import evaluate

print(evaluate("1+2*6/67")) #=> 1.1791044776119404
print(evaluate("1+2*6/67",decimal_separator=",")) #=> 1,1791044776119404

```


if you find any errors, inefficient pieces of code or any other problem pls tell me, so I can learn and fix it
