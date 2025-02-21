# handstrength
A standard algorithm for turning poker hands into comparable 16-bit integers which correspond to their strength.

## Poker Hand Strength Evaluation Algorithm

### 1️⃣ Categorizing Poker Hands

Each poker hand falls into a standard ranking:

- **Royal Flush** (Strongest)
- **Straight Flush**
- **Four of a Kind**
- **Full House**
- **Flush**
- **Straight**
- **Three of a Kind**
- **Two Pair**
- **One Pair**
- **High Card** (Weakest)

Each category should be assigned a unique ranking value.

### 2️⃣ Encoding Hand Strength into a 16-bit Integer

A poker hand’s strength can be encoded into a 16-bit integer using the following bit allocation:

- **Bits 15-12** → Hand Rank (e.g., Royal Flush = `1111`, One Pair = `0010`, etc.)
- **Bits 11-0** → High Card & Tie-Breaker Values (e.g., kicker values for hands of the same rank)

This ensures that hands of higher categories will always have a greater numeric value than those of lower categories.

### 3️⃣ Evaluating a Hand

1. **Sort the Cards** → Order cards by rank.
2. **Check for Special Hands**:
   - Identify flushes (same suit).
   - Identify straights (consecutive values).
   - Identify duplicates (pairs, three/four of a kind).
3. **Assign a Hand Rank** → Based on the category above.
4. **Compute High Cards & Kickers** → Encode tiebreaker rules for same-rank hands.

### 4️⃣ Example Conversion

Example for ♠A ♠K ♠Q ♠J ♠10 (Royal Flush):
```
Hand Rank (1111) | High Card Encoding (000000000000)
Final 16-bit value: 0b1111000000000000 = 0xF000
```
