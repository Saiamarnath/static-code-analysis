import json
import logging
from datetime import datetime

stock_data = {}

# FIX 2: Changed the dangerous default value 'logs=[]' to 'logs=None'.
# This prevents different calls from sharing the same list.
def addItem(item="default", qty=0, logs=None):
    if logs is None:
        # A new list is created for each call!
        logs = []

    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    
    # Using a modern f-string for cleaner formatting, as suggested! [cite: 78]
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def removeItem(item, qty):
    # FIX 3: Replaced the broad 'except:' with a specific 'except KeyError'.
    # This makes our code safer and easier to debug.
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        # Now it only catches the error we expect.
        print(f"Warning: Tried to remove {item}, but it wasn't in stock.")

def getQty(item):
    # Using .get() is a safer way to access dictionary keys.
    return stock_data.get(item, 0)

def loadData(file="inventory.json"):
    global stock_data
    # FIX 4: Using 'with open(...)' ensures the file is always closed safely.
    try:
        with open(file, "r") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        print(f"Warning: {file} not found. Starting with an empty inventory.")
        stock_data = {}


def saveData(file="inventory.json"):
    # FIX 4: Also using 'with open(...)' here for safe file writing.
    with open(file, "w") as f:
        # Using json.dump with an indent makes the saved file much more readable!
        json.dump(stock_data, f, indent=4)

def printData():
    print("--- Items Report ---")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")
    print("--------------------")

def checkLowItems(threshold=5):
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    # Corrected the call that would cause a crash to show working code.
    addItem("apple", 10)
    addItem("banana", 8)
    addItem("oranges", 4)
    
    removeItem("apple", 3)
    removeItem("orange", 1) # This item doesn't exist, will now show a warning.
    
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    
    saveData()
    loadData()
    printData()
    
    # FIX 1: The dangerous 'eval' call has been completely removed.
    print("Script finished safely.")

main()