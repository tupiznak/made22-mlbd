import sys

PRICE_IDX = 9


def main(sys=sys):
    prices = []
    for line in sys.stdin:
        prices.append(int(line.split(',')[PRICE_IDX]))
    mean = sum(prices) / len(prices)
    sys.stdout.write(str(mean) + '\n')


if __name__ == '__main__':
    main()
