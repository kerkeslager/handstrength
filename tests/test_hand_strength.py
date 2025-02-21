import unittest

class TestPokerHandStrength(unittest.TestCase):

    def test_royal_flush(self):
        hand = ['AS', 'KS', 'QS', 'JS', '10S']
        expected_value = 0xF000
        self.assertEqual(evaluate_hand(hand), expected_value)

    def test_straight_flush(self):
        hand = ['9S', '8S', '7S', '6S', '5S']
        expected_value = 0xE000
        self.assertEqual(evaluate_hand(hand), expected_value)

    def test_four_of_a_kind(self):
        hand = ['AS', 'AD', 'AC', 'AH', 'KS']
        expected_value = 0xD000
        self.assertEqual(evaluate_hand(hand), expected_value)

    def test_full_house(self):
        hand = ['AS', 'AD', 'AC', 'KS', 'KD']
        expected_value = 0xC000
        self.assertEqual(evaluate_hand(hand), expected_value)

    def test_flush(self):
        hand = ['AS', 'KS', 'QS', 'JS', '9S']
        expected_value = 0xB000
        self.assertEqual(evaluate_hand(hand), expected_value)

    def test_straight(self):
        hand = ['AS', 'KS', 'QS', 'JS', '10D']
        expected_value = 0xA000
        self.assertEqual(evaluate_hand(hand), expected_value)

    def test_three_of_a_kind(self):
        hand = ['AS', 'AD', 'AC', 'KS', 'QS']
        expected_value = 0x9000
        self.assertEqual(evaluate_hand(hand), expected_value)

    def test_two_pair(self):
        hand = ['AS', 'AD', 'KS', 'KD', 'QS']
        expected_value = 0x8000
        self.assertEqual(evaluate_hand(hand), expected_value)

    def test_one_pair(self):
        hand = ['AS', 'AD', 'KS', 'QS', 'JS']
        expected_value = 0x7000
        self.assertEqual(evaluate_hand(hand), expected_value)

    def test_high_card(self):
        hand = ['AS', 'KS', 'QS', 'JS', '9D']
        expected_value = 0x6000
        self.assertEqual(evaluate_hand(hand), expected_value)

if __name__ == '__main__':
    unittest.main()
