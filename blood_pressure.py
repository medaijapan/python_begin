#140以上が高血圧 130以上140未満が高値血圧 100以上130未満が正常値 100未満が低血圧(WHO基準)
input_pressure = input("血圧をいれてください。")
pressure = int(input_pressure) #文字列として入力された血圧を数字に直している。

if pressure>=140:
  print('高血圧です。')
elif pressure>=130:
  print('高値血圧です。')
elif pressure>=100:
  print('正常値です。')
else:
  print('低血圧です。')
