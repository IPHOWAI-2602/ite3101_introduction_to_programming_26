from typing import List

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

# The following 3 lines of codes are for UnitTest and you don't need them for your real applications!
global shopping_list
global stock
global prices

# # Write your code below!


def compute_bill(food: list[str]) -> float:
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    return total


# === 請將購買和列印的程式碼移到檔案的最下方 ===
# 1. 覆蓋為 Task13 要求的清單：香蕉和橘子
shopping_list = ["banana", "orange"]

# 2. 計算並印出結果
result = compute_bill(shopping_list)
print(result)
