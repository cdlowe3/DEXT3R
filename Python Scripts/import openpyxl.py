import os
import datetime

def get_bourbon_data():
  """Prompts user for bourbon data and returns a dictionary."""
  bourbon = {}
  bourbon['name'] = input("Enter bourbon name: ")
  bourbon['distillery'] = input("Enter distillery: ")
  bourbon['age'] = int(input("Enter age (in years): "))
  bourbon['proof'] = float(input("Enter proof: "))
  bourbon['price'] = float(input("Enter price: "))
  bourbon['rating'] = float(input("Enter rating (0-5): "))
  bourbon['notes'] = input("Enter notes: ")
  bourbon['date_added'] = datetime.datetime.now()
  return bourbon

def create_bourbon_collection():
  """Creates a list of bourbons by prompting user input."""
  bourbons = []
  while True:
    bourbon = get_bourbon_data()
    bourbons.append(bourbon)
    if input("Add another bourbon? (y/n): ").lower() != 'y':
      break
  return bourbons

def save_to_excel(bourbons, filename='bourbon_collection.xlsx'):
  """Saves the bourbon collection to an Excel file."""
  # ... (same as previous code)

if __name__ == '__main__':
  bourbon_collection = create_bourbon_collection()
  save_to_excel(bourbon_collection)

