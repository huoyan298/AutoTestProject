# coding: utf-8
import os, time
from loginfo.log_print import get_log
from selenium import webdriver


def screenshot(driver):
    # 设置截图文件保存的路径
    path = 'D:\\123\\loginfo'
    path = os.path.join(path, 'ScreenShot')
    if not os.path.exists(path):
        os.mkdir(path)
    # 设置要截图的文件名
    file_name = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime()) + '.png'
    path = os.path.join(path, file_name)
    log = get_log('ScreenShot')
    try:
        driver.get_screenshot_as_file(path)
        log.info('截图成功')
    except OSError:
        log.info('截图失败')


if __name__ == '__main__':
    driver0 = webdriver.Chrome()
    screenshot(driver0)
    #driver0.quit()