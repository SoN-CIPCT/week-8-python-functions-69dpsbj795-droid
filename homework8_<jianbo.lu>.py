def make_sandwich(*ingredients):
     print("\nSandwich Order Summary:")
     for ingredient in ingredients:
        print(f"{ingredient}")
make_sandwich("Turkey", "Lettuce", "Tomato")
make_sandwich("Ham", "Cheese", "Onion", "Pickles", "Mustard")