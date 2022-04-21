from datetime import datetime


def give_log_path(some_path):
    path = some_path

    def log_decor(some_function):
        def new_function(*args, **kwargs):
            date_time = datetime.now().__str__()
            function_name = some_function.__name__
            pos_agrs = args
            name_args = kwargs
            result = some_function(*args, **kwargs)
            log = f'дата и время: {date_time}, функция: {function_name}, ' + \
                  f'позиционные аргументы: {pos_agrs}, именованные аргументы: {name_args}, результат: {result}'
            with open(path + 'logs.txt', 'a') as f:
                f.write(log + '\n')
            return result
        return new_function
    return log_decor
