import sys

def receive():
    import time
    import logging
    from logging import config
    listener = config.listen()
    listener.start()

    try:
        while True:
            logging.debug('debug')
            logging.info('info')
            some_logger = logging.getLogger('some')
            some_logger.warning('warning')
            some_logger.error('error')
            other_logger = some_logger.getChild('other')
            other_logger.critical('critical')

            time.sleep(5)
    except KeyboardInterrupt:
        config.stopListening()
        listener.join()


def send():
    import os
    import struct
    import socket
    from logging import config

    ini_filename = os.path.splitext(__file__)[0] + '.ini'
    with open(ini_filename, 'rb') as fh:
        data = fh.read()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', config.DEFAULT_LOGGING_CONFIG_PORT))
    sock.send(struct.pack('>L', len(data)))
    sock.send(data)
    sock.close()


if __name__ == '__main__':
    if sys.argv[-1] == 'send':
        send()
    elif sys.argv[-1] == 'rec':
        receive()
    else:
        print(f'Usage {sys.argv[0]} [send/rec]')
