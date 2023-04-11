import sys

def error_message_detials(error, error_detail:sys):
    _,_,tb = error_detail.exc_info()
    file_name = tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in: {file_name} | Line no: {tb.tb_lineno} |\n {str(error)}"

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detials(error_message, error_detail)
    
    def __str__(self):
        return self.error_message