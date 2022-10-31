import sys
from functools import reduce
from operator import mul

PRICE_IDX = 9


def main():
    var_mean_prices: list[tuple[float, float, int]] = []  # var, mean, size
    for line in sys.stdin:
        chunk_var, chunk_mean, chunk_size = line.split(',')
        var_mean_prices.append((float(chunk_var), float(chunk_mean), int(chunk_size)))

    prices_len = sum(map(lambda pair: pair[2], var_mean_prices))
    prices_sum_mean = sum(map(lambda pair: pair[1] * pair[2], var_mean_prices))
    prices_mean = prices_sum_mean / prices_len

    prices_sum_var = sum(map(lambda pair: pair[0] * pair[2], var_mean_prices))
    prices_power_mean = sum(map(lambda pair: (pair[1] - prices_mean) ** 2 * pair[2], var_mean_prices))

    var = prices_sum_var / prices_len + prices_power_mean / prices_len
    sys.stdout.write(str(var) + '\n')


if __name__ == '__main__':
    main()
