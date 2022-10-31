import logging


def main():
    logger = logging.getLogger('download dataset')

    logger.info('Try kaggle auth...')
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
        api = KaggleApi()
        api.authenticate()
    except OSError:
        logger.error('KAGGLE_KEY and KAGGLE_USERNAME not found in environment. Exit.')
        return

    logger.info('Downloading dataset...')
    api.dataset_download_files('dgomonov/new-york-city-airbnb-open-data',
                               path='./data/',
                               unzip=True)
    logger.info('Dataset downloaded')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
