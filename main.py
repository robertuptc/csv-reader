import csv

def available_pets():
    animals = input("What type of animal are you looking for?: ")
    try:

        with open(f"/Users/robert/Exercises/csv-reader/data/{animals}s.csv") as f:
            catsreader = csv.DictReader(f, skipinitialspace=True)
            print(f"We have the following {animals}s: ")
            for row in catsreader:
                print(f"{row['name']} is a {row['age']} year old {row['breed']}.")
    except:
        print(f"Sorry, we don't have any {animals} here")

available_pets()
