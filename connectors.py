import gdown
import os
import time


def get_data():

    file_id = os.getenv('SEVEN_WONDERS_DS_URL')
    url = f"https://drive.google.com/uc?id={file_id}"
    output = "data.xlsx"

    if not os.path.exists(output):
        gdown.download(url, output, quiet=False)

    # 等待文件下载完成
    while not os.path.exists(output):
        time.sleep(1)  # 等待1秒
    
    # 确保文件下载完成
    file_size = 0
    while True:
        current_size = os.path.getsize(output)
        if current_size == file_size:
            break  # 文件大小不再变化，说明下载完成
        file_size = current_size
        time.sleep(1)  # 再等待1秒
    
    return True
