import sys

PRICE_IDX = 9


def main():
    sum_price: int = 0
    prices_count = 0
    for line in sys.stdin:
        sum_price += int(line.split(',')[PRICE_IDX])
        prices_count += 1
    mean = sum_price / prices_count
    sys.stdout.write(f'{mean},{prices_count}\n')


if __name__ == '__main__':
    main()
