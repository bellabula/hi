tempF = input('請輸入華氏溫度:')
tempF = float(tempF)
tempC = (tempF - 32) * 5 / 9
tempC = round(tempC, 2)
print('攝氏溫度為 ', tempC)