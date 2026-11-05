# 1. 之前的字典定義（確保資料存在）
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

# 2. 之前寫好的計算函式
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    return total

# 3. Task13 的指定要求：購買 banana 與 orange 並印出結果
shopping_list = ["banana", "orange"]
result = compute_bill(shopping_list)
print(result)
