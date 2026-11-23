# NumPy Random & Boolean Masking Assignment

A collection of 10 Python exercises demonstrating NumPy's random number generation, array shuffling/permutation, statistical operations, and boolean indexing/masking techniques.

## 📋 Overview of Tasks

The script [`9-11-26.py`](9-11-26.py) covers the following tasks (using `np.random.seed(42)` for reproducible output):

1. **Random Decimal Matrix:** Generates a $4 \times 4$ matrix of random floats in `[0.0, 1.0)` using `np.random.random()`.
2. **Filter `rand()` Output:** Creates a $3 \times 3$ matrix via `np.random.rand()` and filters values greater than `0.5`.
3. **Normal Distribution Sample:** Samples 20 values from a standard normal distribution (`np.random.randn()`), counts positive/negative values, and replaces negative values with `0`.
4. **Random Integers Statistics:** Generates 25 random integers between `1` and `100` (`np.random.randint()`), computes `max`, `min`, and `mean`, and extracts even numbers.
5. **Random Selection of Marks:** Selects 4 distinct values without replacement from a predefined array of marks using `np.random.choice(..., replace=False)`.
6. **Shuffle Sequence:** Shuffles a 1D array of numbers from `1` to `20` in-place using `np.random.shuffle()`.
7. **Permutation Check:** Creates a shuffled copy of `[10, 20, ..., 100]` using `np.random.permutation()` and verifies that the original array remains unaltered.
8. **Boolean Masking of Student Marks:** Generates 20 random student marks (`0–100`) and categorizes them into **Failed** (`< 40`), **Passed** (`>= 40`), and **Distinction** (`>= 75`).
9. **Salary Analysis with Masks:** Analyzes 15 random salaries (`₹20,000–₹1,00,000`) by filtering salaries `> ₹50,000`, filtering salaries between `₹30,000` and `₹70,000`, and applying a minimum salary floor of `₹25,000`.
10. **Online Shopping Price Pipeline:** Simulates an e-commerce pricing workflow on 20 random prices (`₹100–₹10,000`):
    - Samples 5 random prices without replacement.
    - Shuffles the price list.
    - Applies a **10% discount** to all items priced above `₹5,000`.
    - Computes the final total cart cost after discounts.

## 🛠️ Prerequisites

- **Python 3.x**
- **NumPy**

Install NumPy if you haven't already:

```bash
pip install numpy
