import csv
import sys

PRICE_IDX = 9


def main():
    prices: list[int] = []
    reader = csv.reader(sys.stdin, delimiter=',')
    for line in reader:
        prices.append(int(line[PRICE_IDX]))
    mean = sum(prices) / len(prices)
    var = sum(map(lambda el: (el - mean) ** 2, prices)) / len(prices)
    sys.stdout.write(f'{var},{mean},{len(prices)}\n')


if __name__ == '__main__':
    main()
