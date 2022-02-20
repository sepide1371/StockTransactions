from rest_framework.response import Response


class MessageCodes:
    Successful_Operation = 0
    Internal_Error = 1
    Input_Error = 2
    Not_Found = 3

    messages_names = {
        Successful_Operation: 'Successful Operation',
        Internal_Error: 'Internal Error',
        Input_Error: 'Input Error',
        Not_Found: 'Not Found',

    }


class CustomResponse(Response):
    def __init__(self, data, msg_code=0, msg_status=0, **kwargs):
        response_data = {
            "Header": {
                "Status": msg_status,
                "Message": MessageCodes.messages_names[msg_code],
                "MessageCode": msg_code,
            },
            "ContentData": data
        }
        print("response_data-------")
        print(response_data)

        super().__init__(response_data, **kwargs)
