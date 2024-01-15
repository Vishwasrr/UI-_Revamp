import logging

# create logger
logger = logging.getLogger("demolog")
logger.setLevel(logging.DEBUG)


# create console handler or file handler
class LoggerDemo:
    @staticmethod
    def cust_logger():
        ch = logging.StreamHandler(__name__)  # to display if the message if coming from the script or model
        ch = logging.StreamHandler(LoggerDemo.__name__)  # to display class name along with the log levels
        fh = logging.FileHandler("demologfile.log")

        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(name)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        formatter1 = logging.Formatter('%(asctime)s - %(levelname)s : %(name)s')

        fh.setFormatter(formatter1)

        ch.setFormatter(formatter)

        logger.addHandler(ch)
        logger.addHandler(fh)

        logger.debug("debug log statement")
        logger.info("info log statement")
        logger.warning("warning log statement")
        logger.error("error log statement")
        logger.critical("critical log statement")


ld = LoggerDemo()
ld.cust_logger()
