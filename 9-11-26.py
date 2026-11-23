import numpy as np

# Optional: Set a seed for reproducible results while testing
np.random.seed(42)

# ==========================================
# Task 1 – Random Decimal Matrix
# ==========================================
print("--- Task 1: Random Decimal Matrix ---")
matrix_4x4 = np.random.random((4, 4))
print(matrix_4x4)
print()

# ==========================================
# Task 2 – Filter rand() Output
# ==========================================
print("--- Task 2: Filter rand() Output ---")
matrix_3x3 = np.random.rand(3, 3)
greater_than_half = matrix_3x3[matrix_3x3 > 0.5]
print("3x3 Matrix:\n", matrix_3x3)
print("Elements > 0.5:\n", greater_than_half)
print()

# ==========================================
# Task 3 – Normal Distribution Sample
# ==========================================
print("--- Task 3: Normal Distribution Sample ---")
normal_samples = np.random.randn(20)
pos_count = np.sum(normal_samples > 0)
neg_count = np.sum(normal_samples < 0)

# Replace negative values with 0 (in-place via boolean mask)
cleaned_samples = normal_samples.copy()
cleaned_samples[cleaned_samples < 0] = 0

print("Original 20 values:\n", normal_samples)
print(f"Positive count: {pos_count}, Negative count: {neg_count}")
print("After replacing negative values with 0:\n", cleaned_samples)
print()

# ==========================================
# Task 4 – Random Integers Statistics
# ==========================================
print("--- Task 4: Random Integers Statistics ---")
rand_ints = np.random.randint(1, 101, size=25)  # high is exclusive, so 101 includes 100
even_numbers = rand_ints[rand_ints % 2 == 0]

print("25 Random Integers (1–100):\n", rand_ints)
print("Max:", np.max(rand_ints))
print("Min:", np.min(rand_ints))
print("Mean:", np.mean(rand_ints))
print("Even numbers:", even_numbers)
print()

# ==========================================
# Task 5 – Random Selection of Marks
# ==========================================
print("--- Task 5: Random Selection of Marks ---")
marks = np.array([35, 45, 55, 65, 75, 85, 95])
selected_marks = np.random.choice(marks, size=4, replace=False)  # replace=False ensures distinct values
print("Original marks:", marks)
print("4 Distinct selected marks:", selected_marks)
print()

# ==========================================
# Task 6 – Shuffle Sequence
# ==========================================
print("--- Task 6: Shuffle Sequence ---")
seq_1_to_20 = np.arange(1, 21)
print("Before shuffle:", seq_1_to_20)
np.random.shuffle(seq_1_to_20)  # Mutates array in-place and returns None
print("After in-place shuffle:", seq_1_to_20)
print()

# ==========================================
# Task 7 – Permutation Check
# ==========================================
print("--- Task 7: Permutation Check ---")
tens_array = np.arange(10, 101, 10)  # [10, 20, ..., 100]
permuted_array = np.random.permutation(tens_array)
is_unchanged = np.array_equal(tens_array, np.arange(10, 101, 10))

print("Original array:", tens_array)
print("Permuted array:", permuted_array)
print("Original array unchanged?", is_unchanged)
print()

# ==========================================
# Task 8 – Boolean Masking of Student Marks
# ==========================================
print("--- Task 8: Boolean Masking of Student Marks ---")
student_marks = np.random.randint(0, 101, size=20)
failed = student_marks[student_marks < 40]
passed = student_marks[student_marks >= 40]
distinction = student_marks[student_marks >= 75]

print("All 20 student marks:", student_marks)
print("Failed (< 40):", failed)
print("Passed (>= 40):", passed)
print("Distinction (>= 75):", distinction)
print()

# ==========================================
# Task 9 – Salary Analysis with Masks
# ==========================================
print("--- Task 9: Salary Analysis with Masks ---")
salaries = np.random.randint(20000, 100001, size=15)
above_50k = salaries[salaries > 50000]
mid_range = salaries[(salaries >= 30000) & (salaries <= 70000)]

adjusted_salaries = salaries.copy()
adjusted_salaries[adjusted_salaries < 25000] = 25000

print("Original salaries (₹):", salaries)
print("Salaries > ₹50,000:", above_50k)
print("Salaries between ₹30,000 and ₹70,000 (inclusive):", mid_range)
print("Adjusted salaries (floor ₹25,000):", adjusted_salaries)
print()

# ==========================================
# Task 10 – Online Shopping Price Pipeline
# ==========================================
print("--- Task 10: Online Shopping Price Pipeline ---")
prices = np.random.randint(100, 10001, size=20)

# 1. Choose 5 random prices
five_random_prices = np.random.choice(prices, size=5, replace=False)

# 2. Shuffle the full price list (working on a copy to keep original clear if needed)
shuffled_prices = prices.copy()
np.random.shuffle(shuffled_prices)

# 3 & 4. Identify products priced above 5000 and apply a 10% discount
high_priced_mask = shuffled_prices > 5000
high_priced_items = shuffled_prices[high_priced_mask]

discounted_prices = shuffled_prices.astype(float).copy()
discounted_prices[high_priced_mask] *= 0.90  # 10% off -> pay 90%

# 5. Compute total cost after discounts
total_after_discount = np.sum(discounted_prices)

print("Initial 20 prices (₹):", prices)
print("1. 5 random prices:", five_random_prices)
print("2. Shuffled prices:", shuffled_prices)
print("3. Prices > ₹5,000:", high_priced_items)
print("4. Prices after 10% discount on > ₹5,000:", np.round(discounted_prices, 2))
print(f"5. Total cost after discounts: ₹{total_after_discount:.2f}")