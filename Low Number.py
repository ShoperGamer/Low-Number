def minNumber(x,y,z): #ฟังก์ชั่นสำหรับหาค่าน้อยที่สุด
  P = x # P เอาไว้เปรียบเทียบ x y z ว่าอันไหนมากอันไหนน้อย
  if y < P:
    P = y
  if z < P:
    P = z
  return P #แสดงผลอันไหนน้อยสุด

x = int(input("x : "))
y = int(input("y : "))
z = int(input("z : "))

low = minNumber(x,y,z) #low เอาไว้เรียกแสดงผลฟังก์ชั่น
print("ค่าที่น้อยที่สุด :",low)
