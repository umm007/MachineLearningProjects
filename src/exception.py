import sys

def error_message_detail(error, error_details: sys):
    """
    Generates a detailed error message with the script name and line number where the error occurred.
    """
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script: [{0}], Line: [{1}], Error: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Corrected `super()` syntax
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message