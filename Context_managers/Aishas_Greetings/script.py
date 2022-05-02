# Write your code below:
from contextlib import contextmanager

@contextmanager
def generic(card_type, sender, recipient):
  generic_card = open(card_type, 'r')
  order_card = open(f'{sender}_generic.txt', 'w')
  try:
    order_card.write(f"Dear {recipient},\n \n")
    order_card.write(generic_card.read())
    order_card.write(f"\nSincerely,\n{sender}\n")
    yield order_card

  finally:
    generic_card.close()
    order_card.close()

with generic('thankyou_card.txt', 'Mwenda', 'Amanda') as thankyou:
  print('Card Generated!')

with open('Mwenda_generic.txt', 'r') as thankyou_read:
  print(thankyou_read.read())

class personalized:
  def __init__(self, sender, receiver):
    self.sender = sender
    self.receiver = receiver
    self.file = open(f"{self.sender}_personalized.txt", "w")

  def __enter__(self):
    self.file.write(f"Dear {self.receiver}, \n \n")
    return self.file

  def __exit__(self, exc_type, exc_value, Traceback):
    self.file.write(f"\n \nSincerely, \n{self.sender}\n")
    self.file.close()

with personalized("John", "Michael") as personal_card:
  personal_card.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")

with open('John_personalized.txt', 'r') as personal_card_read:
  print(personal_card_read.read())

with generic("happy_bday.txt","Josiah", "Remy") as bday_card, personalized("Josiah", "Esther") as personal_card_2:
  personal_card_2.write("Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!")

with open('Josiah_generic.txt', 'r') as bdaycard_read:
  print(bdaycard_read.read())

with open('Josiah_personalized.txt', 'r') as personal_card_read_2:
  print(personal_card_read_2.read())

  
