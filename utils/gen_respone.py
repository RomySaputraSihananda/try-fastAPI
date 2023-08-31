def gen_respone(data):
    
    [data, message] = data;

    respone = {
        'success': True,
        'message': message,
        'datalength': len(data),
        'data': data
    };

    return respone;