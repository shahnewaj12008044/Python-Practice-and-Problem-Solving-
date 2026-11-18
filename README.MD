# Python Practice and Problem Solving

Python from basics to advanced — theory notes and problem solving,
written while learning. Everything here runs with plain Python 3, no
extra libraries needed.

## How it is organised

### `theory/`
Short files, one topic each. Read them in order.

| File | Topic |
| --- | --- |
| `01-variables-data-types.py` | Variables, int, float, string, bool, type conversion |
| `02-operators.py` | Arithmetic, comparison, logical, assignment, membership |
| `03-conditionals.py` | if / elif / else, nested if, ternary |
| `04-loops.py` | for, while, break, continue, nested loops |
| `05-functions.py` | def, return, default args, *args, scope, recursion |
| `06-lists.py` | List operations, slicing, methods, comprehension |
| `07-tuples-dicts-sets.py` | Tuples, dictionaries, sets |
| `08-strings.py` | String methods, slicing, f-strings |
| `09-file-handling.py` | Reading and writing files |
| `10-error-handling.py` | try / except / else / finally, raising errors |
| `11-oop-basics.py` | Classes, objects, inheritance |
| `12-lambda-map-filter.py` | lambda, map, filter, sorted with key |

### `problem-solving/`
Problems with solutions. Each file has the problem at the top —
try it yourself first, then check the solution.

- `easy/` — even/odd, largest of three, factorial, palindrome, fibonacci
- `medium/` — prime numbers, vowel counting, second largest, anagrams, word frequency
- `hard/` — binary search, merge sort, longest substring, 0/1 knapsack

## How to run

```bash
python3 theory/01-variables-data-types.py
python3 problem-solving/easy/01-even-or-odd.py
```

Change the test values at the top of a file and run it again to see
how the output changes.
