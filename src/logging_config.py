import logging
import os

# Определение пути к папке logs
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(project_root, 'logs')

# создаем папку logs, если не существует
os.makedirs(LOG_DIR, exist_ok=True)

# Создаем форматтер
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Настройка логгера для masks
logger_masks = logging.getLogger('masks')
logger_masks.setLevel(logging.DEBUG)
file_handler_masks = logging.FileHandler(os.path.join(LOG_DIR, 'masks.log'), mode='w', encoding='utf-8')
file_handler_masks.setLevel(logging.DEBUG)
file_handler_masks.setFormatter(formatter)
logger_masks.addHandler(file_handler_masks)

# Настройка логера для utils
logger_utils = logging.getLogger('utils')
logger_utils.setLevel(logging.DEBUG)
file_handler_utils = logging.FileHandler(os.path.join(LOG_DIR, 'utils.log'), mode='w', encoding='utf-8')
file_handler_utils.setLevel(logging.DEBUG)
file_handler_utils.setFormatter(formatter)
logger_utils.addHandler(file_handler_utils)
