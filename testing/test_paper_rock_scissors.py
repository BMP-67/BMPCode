import unittest
from paper_rock_scissors import get_result

class TestRockPaperScissors(unittest.TestCase):
    def test_tie(self):
        self.assertEqual(get_result('rock', 'rock'), 'tie')
        self.assertEqual(get_result('paper', 'paper'), 'tie')
        self.assertEqual(get_result('scissors', 'scissors'), 'tie')

    def test_win(self):
        self.assertEqual(get_result('rock', 'scissors'), 'win')
        self.assertEqual(get_result('paper', 'rock'), 'win')
        self.assertEqual(get_result('scissors', 'paper'), 'win')

    def test_lose(self):
        self.assertEqual(get_result('rock', 'paper'), 'lose')
        self.assertEqual(get_result('paper', 'scissors'), 'lose')
        self.assertEqual(get_result('scissors', 'rock'), 'lose')

    def test_invalid_user_choice(self):
        self.assertEqual(get_result('lizard', 'rock'), 'lose')
        self.assertEqual(get_result('', 'rock'), 'lose')
        self.assertEqual(get_result(None, 'rock'), 'lose')

    def test_invalid_computer_choice(self):
        self.assertEqual(get_result('rock', 'lizard'), 'win')
        self.assertEqual(get_result('rock', ''), 'win')
        self.assertEqual(get_result('rock', None), 'win')

    def test_both_invalid(self):
        self.assertEqual(get_result('lizard', 'spock'), 'lose')

    def test_case_sensitivity(self):
        self.assertEqual(get_result('Rock', 'rock'), 'lose')
        self.assertEqual(get_result('PAPER', 'rock'), 'lose')
        self.assertEqual(get_result('scIsSoRs', 'paper'), 'lose')

    def test_non_string_input(self):
        self.assertEqual(get_result(1, 'rock'), 'lose')
        self.assertEqual(get_result('rock', 2), 'win')
        self.assertEqual(get_result(None, None), 'lose')

    def test_whitespace_input(self):
        self.assertEqual(get_result(' rock ', 'scissors'), 'lose')
        self.assertEqual(get_result('paper', ' rock '), 'win')

if __name__ == '__main__':
    unittest.main()