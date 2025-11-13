# Fine-Tune coding model project

**Base model used**: StartCoder 3B

## How to test ?

### Install dependency

```bash
pip install -r requirements.txt
```

### Generate solution

```python
    python uet_coder.py --problem `<problem_path>` --output `<solution_path>`
```

Example:

```python
    python uet_coder.py --problem Problem1.md --output Solution1.py
```

### Evaluate solution

```python
    python uet_marker.py --source_code_file `<solution_path>` --test_cases `<test_case_path>`
```

Example:

```python
    python uet_marker.py --source_code_file Solution1.py --test_cases TestCases1.txt
```
