import time

def action_decorator(func):
    print('1')
    def inner(*args, **kwargs):
        print('Someone is going to', func.__name__)
        start_time = time.time()
        result = func(*args, **kwargs)
        stop_time = time.time()
        print('Execution time {}'.format(stop_time - start_time))
        return result
    return inner

@action_decorator  # try to uncomment me
def shout(text):
    print(text.upper(), '!!!!')

