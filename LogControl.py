import logging
class LogControl:
    def debug(self,message):
        self.message = message
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            filename='/temp/myapp.log')
        logging.debug('BIG_IP %s', self.message)
 
    def info(self,message):
        self.message = message
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            filename='/temp/myapp.log')
        logging.info('BIG_IP %s', self.message)
    def warning(self,message):
        self.message = message
        nn = 30
        logging.basicConfig(level=logging.WARNING,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            filename='/temp/myapp.log')
        logging.warning('BIG_IP %s', self.message)
    def error(self,message):
        self.message = message
        nn = 30
        logging.basicConfig(level=logging.ERROR,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            filename='/temp/myapp.log')
        logging.error('BIG_IP %s', self.message)
    def critical(self,message):
        self.message = message
        nn = 30
        logging.basicConfig(level=logging.CRITICAL,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            filename='/temp/myapp.log')
        logging.critical('BIG_IP %s', self.message)
