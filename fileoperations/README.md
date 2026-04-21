# Reading Dictionaries in Python

## Do We Need `.items()` to Read a Dictionary?

No, not always. It depends on what you want to read.

## 3 Ways to Read a Dictionary

Consider the following dictionary:

```python
counts = {'a': 2, 'b': 1, 'c': 3}
```

### 1. Using `.items()` (Most Common)

```python
for k, v in counts.items():
    print(k, v)
```

Output:

```
a 2
b 1
c 3
```

This provides both key and value, which is ideal when you need both.

### 2. Using Keys Only

```python
for k in counts:
    print(k)
```

Output:

```
a
b
c
```

This iterates over keys by default.

### 3. Using Keys to Get Values

```python
for k in counts:
    print(k, counts[k])
```

Output:

```
a 2
b 1
c 3
```

This works without `.items()` but is slightly less clean.

## For the Question: "To read dictionary do we need items method?"

Answer: "No, but `.items()` is the best way when we need both key and value together."

## Why `.items()` is Preferred

Instead of:

```python
for k in counts:
    if counts[k] == 2:
        print(k)
```

Use:

```python
for k, v in counts.items():
    if v == 2:
        print(k)
```

This is cleaner and faster (no repeated indexing).

## Interview-Ready Answer

"`.items()` is used to iterate over both keys and values together. Without it, we only get keys and must manually access values."

If you want, I can also explain `.keys()` vs `.values()` vs `.items()` (a very common interview question).
