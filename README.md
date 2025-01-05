# Python Bug: ZeroDivisionError in Average Calculation

This repository demonstrates a common error in Python: `ZeroDivisionError` when calculating the average of an empty list.

The file `bug.py` contains the buggy code. The file `bugSolution.py` shows the corrected version.

The bug occurs because the code attempts to divide by the length of an empty list, resulting in division by zero.

The solution adds a check to handle the empty list case gracefully, returning 0 as the average in such scenarios.

This is a simple yet common mistake that highlights the importance of edge case handling in programming.