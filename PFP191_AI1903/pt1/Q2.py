def find_pairs(basket, expected_total):
    pairs = []
    for i in range(len(basket)):
        for j in range(i+1, len(basket)):
            if basket[i] + basket[j] == expected_total:
                pairs.append((basket[i], basket[j]))
    return pairs

def main():
    basket = list(range(2, 20))
    expected_total = int(input("Enter the total sought: "))
    print("\nBALL LOTTERY\n=============")
    picks = 0
    found = False
    while picks + 1 < len(basket):
        pairs = find_pairs(basket, expected_total)
        if not pairs:
            print("No more pairs found with the expected total.")
            break
        found = True
        for pair in pairs:
            picks += 1
            print(f"Return of picks {picks} and {picks + 1} : {pair[0]} + {pair[1]}")
        basket.pop(0)
        basket.pop(0)
    if found:
        print(f"You got your total in {picks} picks!")
    else:
        print("No pairs found with the expected total.")

if __name__ == "__main__":
    main()
