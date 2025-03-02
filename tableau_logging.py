import logging

format = logging.Formatter(fmt = '[%(asctime)s] [%(levelname)s]: %(message)s')
tableau_logger = logging.getLogger()
tableau_logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(format)
tableau_logger.addHandler(handler)