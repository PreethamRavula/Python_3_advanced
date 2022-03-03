import datetime

class TooManyBoardsError(Exception):
    def __str__(self):
      return 'Cart cannot have more that 4 surfboards in it!'


class CheckoutDateError(Exception):
    def __str__(self):
      return 'Checkout date cannot be before the presnt date and time'

class ShoppingCart:
    def __init__(self):
        self.num_surfboards = 0
        self.checkout_date = None
        self.locals_discount = False

    def add_surfboards(self, quantity=1):
        if self.num_surfboards + quantity > 4:
            raise TooManyBoardsError
        else:
            self.num_surfboards += quantity
            suffix = '' if quantity == 1 else 's'
            return f'Successfully added {quantity} surfboard{suffix} to cart!'

    def set_checkout_date(self, date):
        if date <= datetime.datetime.now():
            raise CheckoutDateError
        else:
            self.checkout_date = date
            return self.checkout_date

    def apply_locals_discount(self):
        self.local_discount = True
        return self.local_discount
