#!/usr/bin/env python
# encoding:utf-8

"""
import os
from time import localtime, strftime
# noinspection PyUnresolvedReferences
import logging
from selenium import webdriver
from pathlib import Path


def Screenshot(driver):
    # shezhijietuwenjinbaocun lujin
    path = 'D:\\123\\loginfo'
    path = os.path.join(path, "ScreenShot")
    if not os.path.exists(path):
        os.mkdir(path)
        # shezhi jietu de wenjianming
        file_name = strftime('%Y_%M_%D_%H_%M_%S', localtime()) + '.png'
        path = os.path.join(path, file_name)
        log = logging.getLogger('ScreenShot')
        try:
            driver.get_screenshot_as_file(path)
            log.info('jietuchenggong')
        except OSError:
            log.info('jietushibai')
            
if __name__ == "__main__":
    driver0 = webdriver.Firefox()
    Screenshot(driver0)
   # driver0.quit()


i = 1
scrpath = 'D:\\123\\loginfo'  #指定的保存目录
capturename = '\\'+str(i) + '.png'  #自定义命名截图
wholepath = scrpath+capturename
if Path(scrpath).is_dir():  #判断文件夹路径是否已经存在
    pass
else:
    Path(scrpath).mkdir()   #如果不存在，创建文件夹
while Path(wholepath).exists():   #判断文件是否已经存在，也可使用is_file()判断
    i+=1
    capturename = '\\'+str(i) + '.png'
    wholepath = scrpath+capturename
    driver.get_screenshot_as_file(wholepath) #不能接受Path类的值，只能是字符串，否则无法截图
"""

import unittest
from selenium import webdriver
from pathlib import Path
#import os

srcpath = ""
class MyTestCase(unittest.TestCase):
     def setUp(self):
         #self.driver = webdriver.Chrome(executable_path = '/python/driver/chromedriver')
         #self.driver = webdriver.Firefox()
         self.driver = webdriver.Firefox()


     def testCapturescreen(self):
         global srcpath
         url = "http://www.sogou.com"
         # 访问首页
         self.driver.get(url)
         i = 1
         scrpath = 'D:\SeleniumTest\loginfo\ScreenShot'
         # 指定的保存目录
         capturename = '\\' + str(i) + '.png'
         wholepath = scrpath + capturename
         # p_classpath = Path(scrpath)
         # if Path(scrpath).is_dir():
         # pathlib.Path(scrpath).mkdir(parents=True, exist_ok=True )
         Path(scrpath).mkdir(parents=True, exist_ok=True)
         if Path(scrpath).is_dir():
          # 判断文件夹路径是否已经存在
           pass
         else:
          #Path(scrpath).mkdir() 0o777
          p_classpath.mkdir(parents = True, exist_ok = True)
         while Path(wholepath).exists():
          # 判断文件是否已经存在，也可使用is_file()判断
          i += 1
          capturename = '\\' + str(i) + '.png'
          wholepath = scrpath + capturename
          driver.get_screenshot_as_file(wholepath)
         try:
          # 调用get_screenshot_as_file（filename)方法，对浏览器当前打开页面进行截图保存，并保为D:\photo目录下，
          result = self.driver.get_screenshot_as_file(r'D:\SeleniumTest\loginfo\ScreenShot\photo1.png')
          print(result)
          i = 1
          srcpath = 'D:\SeleniumTest\loginfo\ScreenShot'
          capturename = '\\'+str(i)+ '.png '
          #//
          wholepath = "{0}{1}".format(srcpath, capturename)
          if Path(srcpath).is_dir():
           pass
           #Path( srcpath ).mkdir( )
           Path(srcpath).mkdir(parents = True, exist_ok = True)
          while Path(wholepath).exists():
           i += 1
           capturename = '\\'+str(i)+ '.png'
           wholepath = srcpath+capturename
           driver.get_screenshot_as_file(wholepath)
         except IOError as e: print('exception')

if __name__ == "__main__":
  unittest.main()
