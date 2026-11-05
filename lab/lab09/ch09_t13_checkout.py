from typing import List

# 關鍵修正：將 global 宣告移到最頂端，在所有變數賦值之前！
global shopping_list
global stock
global prices

# 初始化資料
stock = {
    "banana": 6,
    "apple": 8,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# 函式定義


def compute_bill(food: list[str]) -> float:
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    return total


# Task13 要求的購買清單與列印結果（放最底部）
shopping_list = ["banana", "orange"]
result = compute_bill(shopping_list)
print(result)
