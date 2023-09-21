## Make Change Coding Interview Practice

This repository contains practice problems for the [Make Change coding interview question](https://leetcode.com/problems/make-change/).

### Problem

You are given an integer array `coins` representing the denominations of coins you have, and an integer `amount` representing the amount of money you need to make change for. Return the minimum number of coins you need to make change for `amount`.

### Examples

```
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: You can use 1 coin worth 5, 1 coin worth 2, and 1 coin worth 1 to make change for 11.
```

```
Input: coins = [10], amount = 15
Output: 2
Explanation: You can use 2 coins worth 10 to make change for 15.
```

### Solution

The following is a solution in **Python**.

```python
def make_change(coins, amount):
  """
  Returns the minimum number of coins needed to make change for `amount`.

  Parameters:
    coins: An integer array representing the denominations of coins you have.
    amount: An integer representing the amount of money you need to make change for.

  Returns:
    An integer representing the minimum number of coins needed to make change for `amount`.
  """

  # Initialize the cache.
  cache = {}

  def _make_change(coins, amount):
    """
    Recursive helper function that computes the minimum number of coins needed to make change for `amount`.

    Parameters:
      coins: An integer array representing the denominations of coins you have.
      amount: An integer representing the amount of money you need to make change for.

    Returns:
      An integer representing the minimum number of coins needed to make change for `amount`.
    """

    # Base case: if the amount is 0, then we need 0 coins.
    if amount == 0:
      return 0

    # Check if we have already computed the answer for this amount.
    if amount in cache:
      return cache[amount]

    # Recursively compute the minimum number of coins needed to make change for `amount - 1`.
    best_num_coins = float("inf")
    for coin in coins:
      if amount - coin >= 0:
        best_num_coins = min(best_num_coins, _make_change(coins, amount - coin) + 1)

    # Cache the answer for this amount.
    cache[amount] = best_num_coins

    return best_num_coins

  return _make_change(coins, amount)
```

### References

* [Make Change on LeetCode](https://leetcode.com/problems/make-change/)