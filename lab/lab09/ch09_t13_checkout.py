from typing import List

global shopping_list
global stock
global prices

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}



def compute_bill(food: List[str]) -> float:
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    return total


shopping_list = ["banana", "orange"]
result = compute_bill(shopping_list)
print(result)

stock["banana"] += 1
stock["orange"] += 1
