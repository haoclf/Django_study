#!/usr/bin/env python
#  -*- coding:utf8  -*-

import logging
from  logging import handlers


class mlog():
    def log_info(self,message):
        LOG_FILE = '/tmp/dbde.log'
        handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler
        fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s  - %(name)s - %(message)s'

        formatter = logging.Formatter(fmt)   # 实例化formatter
        handler.setFormatter(formatter)      # 为handler添加formatter

        logger = logging.getLogger('report')    # 获取名为tst的logger
        logger.addHandler(handler)           # 为logger添加handler
        logger.setLevel(logging.DEBUG)
        
        logger.info('%s' % message)
        logger.removeHandler(handler)

    def log_error(self,message):
        LOG_FILE = '/tmp/dbde.log'
        handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler
        fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

        formatter = logging.Formatter(fmt)   # 实例化formatter
        handler.setFormatter(formatter)      # 为handler添加formatter

        logger = logging.getLogger('report')    # 获取名为tst的logger
        logger.addHandler(handler)           # 为logger添加handler
        logger.setLevel(logging.DEBUG)

        logger.error('%s' % message)
        logger.removeHandler(handler)
        #logger.info('first info message')
	#logger.debug('first debug message')
    
 
if __name__ == '__main__':
    cmd = mlog()
    cmd.log_func()
