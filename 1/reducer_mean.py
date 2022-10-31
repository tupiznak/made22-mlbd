import sys

PRICE_IDX = 9


def main():
    mean_prices: list[tuple[float, int]] = []
    for line in sys.stdin:
        chunk_mean, chunk_size = line.split(',')
        mean_prices.append((float(chunk_mean), int(chunk_size)))
    prices_mean_sum = sum(map(lambda pair: pair[0] * pair[1], mean_prices))
    prices_len = sum(map(lambda pair: pair[1], mean_prices))
    mean = prices_mean_sum / prices_len
    sys.stdout.write(str(mean) + '\n')


if __name__ == '__main__':
    main()
