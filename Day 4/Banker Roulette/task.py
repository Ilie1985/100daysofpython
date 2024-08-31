import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

friend_that_has_to_pay = random.randint(0, len(friends)-1)
print(f"The friend that has to pay is {friends[friend_that_has_to_pay]}")

