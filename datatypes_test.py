# Define a function called data_type, to take one argument. Compare and return results, based on the argument supplied to the function. Complete the test to produce the perfect function that accounts for all expectations.

# For strings, return its length.
# For None return string 'no value'
# For booleans return the boolean
# For integers return a string showing how it compares to hundred e.g. For 67 return 'less than 100' for 4034 return 'more than 100' or equal to 100 as the case may be
# For lists return the 3rd item, or None if it doesn't exist


class DataTypeTestCase(TestCase):

  def test_none_type(self):
    self.assertEqual('no value', data_type(None))

  def test_array_type(self):
    self.assertEqual(3, data_type([1, 2, 3]))

  def test_small_array_type(self):
    self.assertEqual(None, data_type([1, 2]))

  def test_small_booleans_type(self):
    self.assertEqual(True, data_type(True))

  def test_small_integer_type(self):
    self.assertEqual('less than 100', data_type(3))

  def test_large_integer_type(self):
    self.assertEqual('more than 100', data_type(200))
  
  def test_str_type(self):
    self.assertEqual(6, data_type('andela'))