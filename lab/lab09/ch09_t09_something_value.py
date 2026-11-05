# 確保上方沒有其他重複的 for 迴圈或印出程式碼

total = 0

for key in prices:
    print(key)
    print("price: %s" % prices[key])
    print("stock: %s" % stock[key])
    
    value = prices[key] * stock[key]
    total += value

print(total)
