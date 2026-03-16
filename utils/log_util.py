import os,time,logging

from autoTest_ecshop.utils.getPath import get_log_path

# 获取日志存放路径
log_path = get_log_path()
# 如果log文件夹不存在，则新创建一个
if not os.path.exists(log_path):
    os.mkdir(log_path)

class Logger:
    def __init__(self):
        # 定义日志位置和文件名
        self.logname = os.path.join(log_path, "{}.log".format(time.strftime("%Y-%m-%d")))
        # 定义一个日志容器
        self.logger = logging.getLogger("logger")
        # 设置日志打印的级别
        self.logger.setLevel(logging.DEBUG)
        # 创建日志输入的格式
        self.formater = logging.Formatter(
            '【%(asctime)s】【%(filename)s  %(lineno)d】【%(levelname)s】: %(message)s')
        # 创建日志处理器，用来存放日志文件
        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        # 文件存放日志级别
        self.filelogger.setLevel(logging.DEBUG)
        # 文件存放日志格式
        self.filelogger.setFormatter(self.formater)
        # 创建日志处理器，在控制台打印
        self.console = logging.StreamHandler()
        # 设置控制台打印日志界别
        self.console.setLevel(logging.DEBUG)
        # 控制台打印日志格式
        self.console.setFormatter(self.formater)
        # 将日志输出渠道添加到日志收集器中
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)

# 实例化日志容器
logger = Logger().logger

if __name__ == '__main__':
    logger.debug("我打印DEBUG日志")
    logger.info("我打印INFO日志")
    logger.warning("我打印WARNING日志")
    logger.error("我打印ERROR日志")
