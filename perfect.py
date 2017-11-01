"""perfect"""
def main():
    """perfrect"""
    num = int(input())
    count = 0
    for power in prime(num):
        if 2**(power-1)*(2**power-1) < num:
            count += 2**(power-1)*(2**power-1)
    print(count)
def prime(number):
    """find prime"""
    count = 0
    prime_list = [2]
    for i in range(3, (number+1)//3):
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                count += 1
        if count == 0:
            prime_list.append(i)
        count = 0
    return prime_list
main()
