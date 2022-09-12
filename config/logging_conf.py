import logging


def config_logs() -> None:
    """
    Define the configuration for every log used by this program.

    **params:** None

    **returns:** None
    """
    logging.basicConfig(filename="predictions.log",
                        encoding='utf-8',
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
