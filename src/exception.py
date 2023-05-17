import sys
from src.logger import logging

def error_message_str(error, error_detail: sys):
    """ function to return error message for the package
        arg: error -> string for a specific exception
    """
    __, __, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_num = exc_tb.tb_lineno
    error_message = f'Error in python script name: [{file_name}], line: [{line_num}], error message: [{str(error)}]'

    return error_message

class CustomException(Exception):

    """
    Custom exception class (to call whenever exceptions are called)
    """
    
    def __init__(self, error_message, error_detail: sys):
        super().__init(error_message)
        self.error_message = error_message_str(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message