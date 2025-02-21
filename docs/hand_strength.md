# Poker Hand Strength Evaluation Algorithm

## 1️⃣ Categorizing Poker Hands

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

## 2️⃣ Encoding Hand Strength into a 16-bit Integer

A poker hand’s strength can be encoded into a 16-bit integer using the following bit allocation:

- **Bits 15-12** → Hand Rank (e.g., Royal Flush = `1111`, One Pair = `0010`, etc.)
- **Bits 11-0** → High Card & Tie-Breaker Values (e.g., kicker values for hands of the same rank)

This ensures that hands of higher categories will always have a greater numeric value than those of lower categories.

## 3️⃣ Evaluating a Hand

1. **Sort the Cards** → Order cards by rank.
2. **Check for Special Hands**:
   - Identify flushes (same suit).
   - Identify straights (consecutive values).
   - Identify duplicates (pairs, three/four of a kind).
3. **Assign a Hand Rank** → Based on the category above.
4. **Compute High Cards & Kickers** → Encode tiebreaker rules for same-rank hands.

## 4️⃣ Example Conversion

Example for ♠A ♠K ♠Q ♠J ♠10 (Royal Flush):
```
Hand Rank (1111) | High Card Encoding (000000000000)
Final 16-bit value: 0b1111000000000000 = 0xF000
```

Example for ♠9 ♠8 ♠7 ♠6 ♠5 (Straight Flush):
```
Hand Rank (1110) | High Card Encoding (000000000000)
Final 16-bit value: 0b1110000000000000 = 0xE000
```

Example for ♠A ♠A ♠A ♠A ♠K (Four of a Kind):
```
Hand Rank (1101) | High Card Encoding (000000000000)
Final 16-bit value: 0b1101000000000000 = 0xD000
```

Example for ♠A ♠A ♠A ♠K ♠K (Full House):
```
Hand Rank (1100) | High Card Encoding (000000000000)
Final 16-bit value: 0b1100000000000000 = 0xC000
```

Example for ♠A ♠K ♠Q ♠J ♠9 (Flush):
```
Hand Rank (1011) | High Card Encoding (000000000000)
Final 16-bit value: 0b1011000000000000 = 0xB000
```

Example for ♠A ♠K ♠Q ♠J ♠10 (Straight):
```
Hand Rank (1010) | High Card Encoding (000000000000)
Final 16-bit value: 0b1010000000000000 = 0xA000
```

Example for ♠A ♠A ♠A ♠K ♠Q (Three of a Kind):
```
Hand Rank (1001) | High Card Encoding (000000000000)
Final 16-bit value: 0b1001000000000000 = 0x9000
```

Example for ♠A ♠A ♠K ♠K ♠Q (Two Pair):
```
Hand Rank (1000) | High Card Encoding (000000000000)
Final 16-bit value: 0b1000000000000000 = 0x8000
```

Example for ♠A ♠A ♠K ♠Q ♠J (One Pair):
```
Hand Rank (0111) | High Card Encoding (000000000000)
Final 16-bit value: 0b0111000000000000 = 0x7000
```

Example for ♠A ♠K ♠Q ♠J ♠9 (High Card):
```
Hand Rank (0110) | High Card Encoding (000000000000)
Final 16-bit value: 0b0110000000000000 = 0x6000
```
