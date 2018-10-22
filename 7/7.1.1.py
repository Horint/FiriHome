##import time
##
##def clock(f):
##    def wrap(*args):
##        start_time = time.clock()
##        ret = f(*args)
##        print(time.clock() -start_time)
##        return ret
##    return wrap
##
##@clock
##def a():
##    print('Hello fskflsdmfsdflmkdslflsdkmf')

import time

def clock(enable = True):  
    def decor(f):
        def wrap(*args, **kwargs):
            if enable is True:
                start_time = time.clock()
                sam = f(*args, **kwargs)
                print (time.clock() -start_time)
                return sam
            else:
                return print ('Enable = False')
        return wrap
    return decor

@clock(enable = True)
def a():
    print( ' В двенадцать часов по ночам \n Из гроба встает барабанщик;\n ходит он взад и вперед,\n И бьет он проворно тревогу.\n И в темных гробах барабан \n Могучую будит пехоту; \n Встают молодцы егеря,\n Встают старики гренадеры, \n Встают из-под русских снегов, \n С роскошных полей италийских,\n Встают с африканских степей, \n С горючих песков Палестины ')
    
@clock(enable = False)
def b():
        print( ' В двенадцать часов по ночам \n Из гроба встает барабанщик;\n ходит он взад и вперед,\n И бьет он проворно тревогу.\n И в темных гробах барабан \n Могучую будит пехоту; \n Встают молодцы егеря,\n Встают старики гренадеры, \n Встают из-под русских снегов, \n С роскошных полей италийских,\n Встают с африканских степей, \n С горючих песков Палестины ')

