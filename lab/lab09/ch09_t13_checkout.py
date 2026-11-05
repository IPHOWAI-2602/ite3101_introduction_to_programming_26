from typing import List

# 保持 global 宣告在最上方避免語法錯誤
global shopping_list
global stock
global prices

# 修正：apple 的庫存改回 8
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


# 修正：用這個判斷式包住，測試系統才不會在 import 時不小心提早扣到庫存
if __name__ == "__main__":
    shopping_list = ["banana", "orange"]
    result = compute_bill(shopping_list)
    print(result)
