import logging

import pandas as pd


def main():
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    logger = logging.getLogger('default compute')

    logger.info('Load dataset...')
    df = pd.read_csv('./data/AB_NYC_2019.csv')
    prices = df.price
    logger.info('Compute metrics')
    mean, var = prices.mean(), prices.var()
    logger.info(f'Metrics: {mean=} {var=}')
    return mean, var


if __name__ == '__main__':
    main()
