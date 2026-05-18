# Module 04 Concepts: Operators & Expressions

> This is a stub. Full content will be added in a future revision.
> The key topics are listed below with brief summaries to get you started.

---

## Arithmetic operators

| Operator | Name             | Example    | Result |
|----------|------------------|------------|--------|
| `+`      | Addition         | `5 + 3`    | `8`    |
| `-`      | Subtraction      | `5 - 3`    | `2`    |
| `*`      | Multiplication   | `5 * 3`    | `15`   |
| `/`      | Division         | `7 / 2`    | `3.5`  |
| `//`     | Floor division   | `7 // 2`   | `3`    |
| `%`      | Modulo (remainder)| `7 % 2`   | `1`    |
| `**`     | Exponentiation   | `2 ** 8`   | `256`  |

`/` always returns a float. `//` returns an int (when both operands are int).
`%` is great for checking if a number is even: `n % 2 == 0`.

---

## Comparison operators

Return `True` or `False`.

`==`  equal to  
`!=`  not equal to  
`<`   less than  
`>`   greater than  
`<=`  less than or equal to  
`>=`  greater than or equal to  

---

## Logical operators

`and` — True only if BOTH sides are True  
`or`  — True if AT LEAST ONE side is True  
`not` — inverts True to False, False to True  

---

## Operator precedence (high to low)

1. `()` — parentheses
2. `**` — exponentiation
3. `*`, `/`, `//`, `%` — multiplication/division
4. `+`, `-` — addition/subtraction
5. `==`, `!=`, `<`, `>`, `<=`, `>=` — comparison
6. `not`
7. `and`
8. `or`

When in doubt, use parentheses to make your intent explicit.

---

## Augmented assignment

```python
x = 10
x += 5    # same as x = x + 5  → 15
x -= 3    # same as x = x - 3  → 12
x *= 2    # same as x = x * 2  → 24
x //= 5   # same as x = x // 5 → 4
```

---

## Next steps

Run the exercise to practise everything in this module.
Then move to Module 05: Control Flow.
