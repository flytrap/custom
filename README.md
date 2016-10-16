# custom
Custom self carry

## example:
```python
c = CustomCarry('000000)
li = []
for i in xrange(10000):
    li.append(c.next())
li[0] == '000001'  # True
```