def soNguyenTo(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

n = int(input("Nhập 1 số: "))

if soNguyenTo(n):
    print(f"{n} là 1 số nguyên tố")
else:
    print(f"{n} không phải là 1 số nguyên tố")