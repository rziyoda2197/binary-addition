def binary_addition(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

# Test qilish
a = 5  # 101
b = 3  # 011
print("Sonlar: ", a, b)
print("Natija: ", binary_addition(a, b))
```

```python
def binary_addition(a, b):
    while b:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

# Test qilish
a = 5  # 101
b = 3  # 011
print("Sonlar: ", a, b)
print("Natija: ", binary_addition(a, b))
