def main():
    n, t = map(int, input().split(" "))
    max_list = [0] * t
    count = 0
    while count < n:
        amount, minute = map(int, input().split(" "))
        while minute >= 0:
            if max_list[minute] < amount:
                temp_amount = max_list[minute]
                max_list[minute] = amount
                if temp_amount == 0:
                    break
                amount = temp_amount
                minute -= 1
            else:
                minute -= 1
        count += 1
    print(sum(max_list))


if __name__ == "__main__":
    main()