import logging
from datetime import datetime 
import os


LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"

LOG_DIR = "logs"

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)


logging.basicConfig(
filename=LOG_FILE_PATH,
format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s %(message)s",
level = logging.INFO
)