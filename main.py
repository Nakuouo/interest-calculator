def main():
    try:
        deposit = float(input("请输入存款数额："))
        year = int(input("请输入年限："))
    except ValueError or NameError:
        print("请输入合法的数字\n")
        deposit = 0
        year = 0
        main()

    interestList = []
    deposit1 = deposit
    n = 1
    while n <= year:
        rate = float(input(f"请输入第{n}年的利率（%）："))
        interest = deposit1 * rate * 0.01
        deposit1 = deposit1 + interest
        interestList.append(interest)
        n = n + 1
    interestTotal = sum(interestList)
    print("您目前存入的{:.1f}元将在{}年后获得{:.1f}元利息。".format(deposit, year, interestTotal))


main()
