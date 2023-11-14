import logging

# 配置全局日志记录
logging.basicConfig(
    level=logging.DEBUG,  # 设置日志级别
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# 创建全局 logger
logger = logging.getLogger('local_logger')

if __name__ == "__main__":
    logger.debug('这是一个调试消息')
    logger.info('这是一个信息消息')
    logger.warning('这是一个警告消息')
    logger.error('这是一个错误消息')
    logger.critical('这是一个严重错误消息')