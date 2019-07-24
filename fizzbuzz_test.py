# Create a function fizz_buzz to return 'Fizz', 'Buzz', 'FizzBuzz', or the argument it receives, all depending on the argument of the function, a number that is divisible by, 3, 5, or both 3 and 5, respectively.

# When the number is not divisible by 3 or 5, the number itself should be returned.

class FizzBuzzClassTest(TestCase):
    """docstring for FizzBuzz"""

    def test_fizz_1(self):
        self.assertEqual(fizz_buzz(3), 'Fizz', msg='should return `Fizz` for number divisible by 3')
    
    def test_fizz_2(self):
        self.assertEqual(fizz_buzz(33), 'Fizz', msg='should return `Fizz` for number divisible by 3')
    
    def test_buzz_1(self):
        self.assertEqual(fizz_buzz(5), 'Buzz', msg='should return `Buzz` for number divisible by 5')
    
    def test_buzz_2(self):
        self.assertEqual(fizz_buzz(25), 'Buzz', msg='should return `Buzz` for number divisible by 5')

    def test_fizz_buzz_1(self):
        self.assertEqual(fizz_buzz(15), 'FizzBuzz', msg='should return `FizzBuzz` for number divisible by 3 and 5')
    
    def test_fizz_buzz_2(self):
        self.assertEqual(fizz_buzz(105), 'FizzBuzz', msg='should return `FizzBuzz` for number divisible by 3 and 5')
        
    def test_indivisible_1(self):
        self.assertEqual(fizz_buzz(101), 101, msg='should return the number if its in divisible by neither 3 or 5')
        
    def test_indivisible_2(self):
        self.assertEqual(fizz_buzz(8), 8, msg='should return the number if its in divisible by neither 3 or 5')