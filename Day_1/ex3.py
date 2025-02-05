def chia_het_cho_3(min, max):
    for i in range(min, max):
        if i % 3 == 0:
            print(i, end=" ")
            
print("Các số chia hết cho 3: ")
chia_het_cho_3(1, 100)