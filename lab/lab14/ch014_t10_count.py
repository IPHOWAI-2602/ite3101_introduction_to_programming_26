def count(sequence, item):
  total = 0
  for element in sequence:
    if element == item:
      total += 1
  return total