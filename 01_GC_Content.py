```python

# 01 - GC Content Calculation
# Self-learned Python for Computational Biology

seq = input("Enter DNA sequence: ").upper()

length = len(seq)
gc_count = seq.count('G') + seq.count('C')

gc_percent = (gc_count / length) * 100 if length > 0 else 0

print(f"Length is {length}")
print(f"GC% is {gc_percent}")

# Sample Output: ATGCCCGG -> LENGTH IS 8, GC% 75.0
:
