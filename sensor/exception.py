import sys


class SensorException(Exception):

    def __init__(self,error_message,error_detail:sys):
        super().__init__()
        self.error_message = SensorException.prepare_error_message(error_message, error_detail)


    @staticmethod
    def prepare_error_message(error_message,error_detail:sys)->str:
        _,_,exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_no = exc_tb.tb_lineno
        error_message = f"Error occured script name [{file_name}] and line no [{line_no}] error message: [{error_message}]"
        return error_message

    def __repr__(self):
        return self.error_message

    def __str__(self):
        return self.error_message

