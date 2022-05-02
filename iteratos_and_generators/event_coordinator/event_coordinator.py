guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  while True:
    guest = yield
    line_data = text_file.readline().strip().split(",")
    if guest is not None:
      line_data = guest.split(',')
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    yield name

guest_chart = read_guestlist('guest_list.txt')
for x in range(10):
  print(next(guest_chart))
next(guest_chart)
print(guest_chart.send("Jane,35"))

for x in range(10):
  print(next(guest_chart))

guest_age = ((name, guests[name]) for name in guests if guests[name] > 21)
for age in guest_age:
  print(age)

def table_one():
  for i in range(1,2):
    for j in range(1,6):
      yield "Chicken",f"Table {i}",f"Seat {j}"

def table_two():
  for i in range(2,3):
    for j in range(6,11):
      yield "Beef",f"Table {i}",f"Seat {j}"

def table_three():
  for i in range(3,4):
    for j in range(11,16):
      yield "Fish",f"Table {i}",f"Seat {j}"

def combined_tables():
  yield from table_one()
  yield from table_two()
  yield from table_three()

tables = combined_tables()
for table in tables:
  print(table)

def guest_assigning(guest_dict, table_generator):
  for name in guest_dict.keys():
    yield name, next(table_generator)


guest_assignment = guest_assigning(guests, combined_tables())
for assignment in guest_assignment:
  print(assignment)
