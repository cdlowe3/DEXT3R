import pandas as pd

class Bourbon:
    def __init__(self, name, distillery, age, proof, price, notes):
        self.name = name
        self.distillery = distillery
        self.age = age
        self.proof = proof
        self.price = price
        self.notes = notes

class Bourbon:
    # ... (same as above)

    def create_bourbon_collection():
        bourbons = []
    # Replace with your bourbon data
    bourbons.append(Bourbon("Pappy Van Winkle", "Buffalo Trace", 23, 114.2, 3000, "Complex caramel, vanilla, oak"))
    # ... add more bourbons

    return bourbons

def save_to_excel(bourbons, filename="bourbon_collection.xlsx"):
    data = [[b.name, b.distillery, b.age, b.proof, b.price, b.notes] for b in bourbons]
    df = pd.DataFrame(data, columns=["Name", "Distillery", "Age", "Proof", "Price", "Notes"])
    df.to_excel(filename, index=False)

if __name__ == "__main__":
    bourbon_collection = create_bourbon_collection()
    save_to_excel(bourbon_collection)
