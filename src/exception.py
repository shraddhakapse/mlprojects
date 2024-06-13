import sys
sys.path.append("..")
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()                                 # to get the detail info 
    file_name = exc_tb.tb_frame.f_code.co_filename                       # file name in which exception is present

    error_message = "Eror occured in python script name [{0}] line number [{1}] error message [{2}]", file_name, exc_tb.tb_lineno, str(error)

class CustomException(Exception):
    def __init__(self,error_message, error_detail:sys):    # error message and error details
        super().__init__(error_message)                      # we want to call parent exception class
        self.error_messsage = error_message_detail(error_message,error_detail)
        


    def __str__(self):
        return self.error_message

'''if __name__ == '__main__':
    try:
        a=1/0
    except Exception as e:
        logging.info("Divison by Zero")
        raise CustomException(e,sys)                               # e is message while exception is comming

'''