# Write your code below:
import surfshop
import unittest
import datetime

class Test_surfshop(unittest.TestCase):

  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test_add_one_surfboard(self):
    message = self.cart.add_surfboards(1)
    self.assertEqual(message, 'Successfully added 1 surfboard to cart!', 'atleast add one surfboard to the cart')

  # def test_add_two_surfboards(self):
  #   message = self.cart.add_surfboards(2)
  #   self.assertEqual(message, 'Successfully added 2 surfboards to cart!', 'din\'t add two surfboards to the cart')

  def test_multiple_surfboards(self):
    for i in range(2,5):
      with self.subTest():
        message = self.cart.add_surfboards(i)
        self.assertEqual(message, f'Successfully added {i} surfboards to cart!')
        self.cart = surfshop.ShoppingCart()

  @unittest.skip
  def test_add_five_surfboards(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

  #@unittest.expectedFailure
  def test_locals_discount(self):
    self.assertTrue(self.cart.apply_locals_discount())

  def test_set_checkout_date(self):
    time_stamp_1 = datetime.datetime(2019, 2, 12, 16, 24, 5)
    time_stamp_2 = datetime.datetime(2022, 3, 21, 9, 20, 8)
    time_stamp_3 = datetime.datetime(2020, 4, 22, 12, 30, 4)
    time_stamps = [time_stamp_1, time_stamp_2, time_stamp_3]
    for stamp in time_stamps:
      with self.subTest(stamp):
        time_now = datetime.datetime.now()
        if stamp <= time_now:
          self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, stamp)
        else:
          self.assertEqual(stamp, self.cart.set_checkout_date(stamp), "No value is being returned")
          self.cart = surfshop.ShoppingCart()

unittest.main()
