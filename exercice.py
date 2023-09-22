

import random

def get_first_part_of_name(name):
	# TODO: Extraire premier prenom
	parts = name.split("-")
	first_part = parts[0]
	first_part = first_part.capitalize()
	return f"Bonjour {first_part}"	


def get_random_sentence(animals, adjectives, fruits):
	animale = random.choice(animals)
	adjectif = random.choice(adjectives)
	fruit = random.choice(fruits)
	return f"Aujourd’hui, j’ai vu un {animale} s’emparer d’un panier {adjectif} plein de {fruit}"

def encrypt(text, shift):
	return ""

def decrypt(encrypted_text, shift):
	return ""


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
