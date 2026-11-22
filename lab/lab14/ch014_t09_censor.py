def censor(text, word):
  words = text.split()
  stars = "*" * len(word)
  result = []
  for w in words:
    if w == word:
      result.append(stars)
    else:
      result.append(w)
  return " ".join(result)