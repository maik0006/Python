#Contar cuántos números son mayores a 50 en una lista
nums = [10, 60, 75, 33, 99]
i = 0
contador = 0
while i < len(nums):
    if nums[i] > 50:
        contador += 1
    i += 1
print("Mayores a 50:", contador)

