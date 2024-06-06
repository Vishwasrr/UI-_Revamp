"""https://docs.python.org/3/library/logging.html#logrecord-attributes"""
import logging

# create logger


# create console handler or file handler
class LoggerDemo:
    @staticmethod
    def cust_logger():
        # ch = logging.StreamHandler()  # creating console handler or file handler and set the log level
        logger = logging.getLogger(LoggerDemo.__name__)
        logger.setLevel(logging.DEBUG)
        # to display if the message if coming from the script or module
        ch = logging.StreamHandler(__name__)
        # to display class name along with the log levels
        ch = logging.StreamHandler(LoggerDemo.__name__)
        fh = logging.FileHandler("demologfile.log")

        # creating the formatter object. This is to specify what kinda formatting pattern to use.
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s : %(name)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        formatter1 = logging.Formatter(
            '%(asctime)s - %(levelname)s : %(name)s')
        # here name is the filename. Log details are displayed along with filenames making debugging easy. Because we know from where the errors are being logged

        # setting the type of formatter required by passing it to the original console/file handler object
        fh.setFormatter(formatter1)

        ch.setFormatter(formatter)

        # adding it to logger object
        logger.addHandler(ch)
        logger.addHandler(fh)

        # logger.debug("debug log statement")
        logger.info("info log statement")
        # logger.warning("warning log statement")
        # logger.error("error log statement")
        # logger.critical("critical log statement")


"""
Explanations:

"""


ld = LoggerDemo()
ld.cust_logger()
