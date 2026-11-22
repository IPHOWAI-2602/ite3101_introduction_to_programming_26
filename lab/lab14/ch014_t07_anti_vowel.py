def anti_vowel(text):
  vowels = "aeiouAEIOU"
  result = ""
  for ch in text:
    if ch not in vowels:
      result += ch
  return result