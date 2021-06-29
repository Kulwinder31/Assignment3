#Kulwinder Singh C0792797

import timeit
import logging
from Tests import TestStringMethods
logging.basicConfig(filename="file.log",level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(message)s')   # log file

logger = logging.getLogger()

start_time=timeit.default_timer()  #start time

logger.warning(f'START time : {str(start_time)}')
#Log events
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def div(x,y):
    return x/y
n1= 3;
n2 = 6;

result_add =add(n1,n2)
logging.info("Addition of two numbers")
logging.debug('ADD: {} {} {}'.format(n1,n2,result_add))

result_sub =sub(n1,n2)
logging.info("Subtraction of two numbers")
logging.debug('SUB: {} {} {}'.format(n1,n2,result_sub))

result_mul =multi(n1,n2)
logging.info("Multiplication of two numbers")
logging.debug('MUL: {} {} {}'.format(n1,n2,result_mul))

result_div =div(n1,n2)
logging.info("Division of two numbers")
logging.debug('DIV: {} {} {}'.format(n1,n2,result_div))

a=2;
b=0;
try:
    sum = a/b
except Exception as e:
    logging.critical("Exception occured: ",exc_info=True)


unitTest = TestStringMethods()
unitTest.test_equal()
logger.critical(f'All the Unit Test cases executed')
end_time= timeit.default_timer()
logger.warning(f'END time : {str(end_time)}')  # end time

