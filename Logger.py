from datetime import datetime
from google.cloud.logging_v2.handlers import CloudLoggingHandler
import google.cloud.logging_v2
import logging

class MyLogger(logging.Logger):
    """This class extends `Logger` class from `logging` module and logs personalized messages for debugs, error and info etc.
    It can be also used to log to **Google cloud logger** so user can view and investigate the execution 
    process.
    """

    def __init__(self, python_file, log_file_name=None, level=logging.DEBUG):
        """Instantiates a `MyLogger` object and sets default filehandler and streamhandler. It 
        also sets the default format for log messages.

        :param str python_file: Name of python file.
        :param str log_file_name: Name of log file (creates if not exist).
        :param str level: Optional Default log level. 
        """
        super(MyLogger, self).__init__(python_file, level)
        self.__set_formatter()
        #self.__set_fileHandler(log_file_name)
        #self.__set_cloudHandler(log_file_name)
        self.__set_streamHandler()
       


    def __set_formatter(self):
        """
        Sets the default format for log messages.
        """
        #self.formatter = logging.Formatter('%(asctime)s' + ' [%(lineno)s] - [%(levelname)s]: %(message)s ----> ' %(name)s', "%Y-%m-%d %H:%M:%S")' 
                            
        self.formatter = logging.Formatter('[%(asctime)s] - [%(lineno)s] - [%(levelname)s]:  %(message)s ---->  %(name)s', "%Y-%m-%d %H:%M:%S") 
                              

    def __set_fileHandler(self, log_file_name):
        """
        Sets the default file handler for our class. 


        """
        if log_file_name is not None:
            self.file_handler = logging.FileHandler(log_file_name)
            self.file_handler.setLevel(logging.INFO)
            self.file_handler.setFormatter(self.formatter)
            self.addHandler(self.file_handler)

    def __set_streamHandler(self):
        """
        Sets the default stream handler for our class.
        """
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(self.formatter)
        self.addHandler(self.stream_handler)

    def __set_cloudHandler(self, log_file_name):
        """
        Sets **Google cloud handler** for class thus enables cloud logging.
        """
        client = google.cloud.logging_v2.Client()
        cloud_handler = CloudLoggingHandler(client, name=log_file_name)
        cloud_handler.setLevel(logging.INFO)
        cloud_handler.setFormatter(self.formatter)
        self.addHandler(cloud_handler)