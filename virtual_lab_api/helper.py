def error_response(errors=[],message='',status_code=400,):
    response = {
        'success': 'False',
        'status_code': status_code,
        'message': message,
        'errors': errors
    }
    return response


def success_response(data=[],message='',status_code=200,):
    response = {
        'success': 'False',
        'status_code': status_code,
        'message': message,
        'data': data
    }
    return response


def is_member(user,group):
    return user.groups.filter(name=group).exists()


def is_in_multiple_groups(user,groups):
    return user.groups.filter(name__in=groups).exists()