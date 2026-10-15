animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = ("duck")  # Use index() to find "duck"

duck_index = animals.index("duck")
animals.insert(duck_index, "cobra")


print(animals)  # Observe what prints after the insert operation
