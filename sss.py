"""perfect2"""
def main():
    """perfect2"""
    num = int(input())
    all_sum = 0
    for number in [6, 28, 496, 8128]:
        if number <= num:
            all_sum += number
    print(all_sum)
main()
