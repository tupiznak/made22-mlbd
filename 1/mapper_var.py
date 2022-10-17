import sys

PRICE_IDX = 9


def main():
    prices = []
    for line in sys.stdin:
        prices.append(int(line.split(',')[PRICE_IDX]))
    mean = sum(prices) / len(prices)
    var = sum(map(lambda el: (el - mean) ** 2, prices)) / len(prices)
    sys.stdout.write(str(var) + '\n')


if __name__ == '__main__':
    main()
