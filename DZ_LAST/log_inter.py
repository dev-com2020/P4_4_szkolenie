import logging

# logger = logging.getLogger(__name__)
#
#
# class MyClass():
#     def __init__(self, count):
#         self.logger = logger.getChild(self.__class__.__name__)
#
#
#
#
# logger = logging.getLogger('main_module.sub_module')
# logger.addHandler(logging.FileHandler('sub_module.log'))
# logging.basicConfig(format='%(some_var)s: %(message)s')
logger = logging.getLogger()
# exception = 'Oops...'
# logger.error('Jakiś potworny błąd: %r', exception)
# logger.error('Prosty błąd', extra=dict(some_var='jakiś_value'))

try:
    raise RuntimeError('jakiś runtime error')
except Exception as exception:
    logger.exception('A ja mam wyjątek: %s', exception)

logger.error('Jakiś błąd!')
