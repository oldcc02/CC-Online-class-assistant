# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import json
import sys
import time

import selenium.webdriver.support.ui as ui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QMainWindow
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# from db_method.db_method import find_usr_iswindow, find_user_last_chapter_course, find_last_user, \
#     update_last_user_is_ans
# from my_socket.tcp_client import send_data
# from online_class_method.cc_log import writelog
# from online_class_method.find_answer import get_ans


# from online_class_method.xxt import Runthread
# from online_class_method.xxt import start_chapter


# class Runthread(QtCore.QThread):
#     #  通过类成员对象定义信号对象
#     signal1 = pyqtSignal(int)
#     signal2 = pyqtSignal(str)
#     signal3 = pyqtSignal(str)
#     signal4 = pyqtSignal(object)
#
#     def __init__(self):
#         super(Runthread, self).__init__()
#         self.ui = Ui_main()
#         self.Chapter = self.ui.ChaptersCheck.currentText()
#         self.course = self.ui.CouresCheck.currentText()
#         self.is_ans =None
#
#     def __del__(self):
#         self.wait()
#
#     def run(self):
#         try:
#             flag = find_usr_iswindow()
#             Chapter, course, is_ans = find_user_last_chapter_course()
#             self.is_ans = is_ans
#             Chapter = Chapter.split(' ')
#             if Chapter[1] == '' or course == '':
#                 self.signal2.emit('请选择正确的课程和章节开始')
#             elif Chapter[2] == '已完成':
#                 self.signal2.emit('这章已经完成了')
#             else:
#                 self.signal2.emit('即将从 {}{} 自动观看'.format(Chapter[0], Chapter[1]))
#                 dr = self.start_chapter(course, show=flag)
#                 # *******************匹配对应的章节
#                 elements = dr.find_elements_by_class_name('articlename')
#                 for element in elements:
#                     title = element.get_attribute('title')
#                     if Chapter[1] == title:
#                         element.click()
#                         break
#                 # ***********************
#                 self.playvideo(dr)
#         except Exception as e:
#             writelog('视频播放线程出错')
#             writelog(str(e))
#             sys.exit(0)
#
#     def getPureDomainCookies(self,cookies):
#         domain2cookie = {}  # 做一个域到cookie的映射
#         for cookie in cookies:
#             domain = cookie['domain']
#             if domain in domain2cookie:
#                 domain2cookie[domain].append(cookie)
#             else:
#                 domain2cookie[domain] = []
#         maxCnt = 0
#         ansDomain = ''
#         for domain in domain2cookie.keys():
#             cnt = len(domain2cookie[domain])
#             if cnt > maxCnt:
#                 maxCnt = cnt
#                 ansDomain = domain
#         ansCookies = domain2cookie[ansDomain]
#         return ansCookies
#
#     def start_chapter(self, course, show=True):  # 重新创建一个driver，进入用户选择的课程
#         try:
#             global url, cookies
#             if not show:
#                 options = Options()
#                 options.add_argument("--mute-audio")  # 静音
#                 dr = webdriver.Chrome(chrome_options=options)
#                 dr.maximize_window()
#                 self.signal4.emit(dr)
#             else:
#                 options = Options()
#                 options.add_argument('--headless')
#                 options.add_argument("--mute-audio")  # 静音
#                 dr = webdriver.Chrome(chrome_options=options)
#
#             with open('./course.txt', 'r') as f:
#                 data = json.load(f)
#
#             for i in range(len(data)):
#                 if course == data[i][0]:
#                     cookies = data[i][2]
#                     url = data[i][1]
#                     break
#             cookies = self.getPureDomainCookies(cookies)
#
#             dr.get(url)
#             for cookie in cookies:
#                 dr.add_cookie(cookie)
#             time.sleep(1)
#             dr.get(url)
#             # 有的账号 会出现cookie验证通过 但是仍需要再次输入验证码，以此下方法再次登录来规避
#             try:
#                 dr.find_element_by_id('frame_content')
#                 dr.switch_to.frame('frame_content')
#                 user = find_last_user()
#                 dr.find_element_by_class_name('ipt-tel').send_keys(user[1])
#                 time.sleep(0.5)
#                 dr.find_element_by_class_name('ipt-pwd').send_keys(user[2])
#                 time.sleep(0.5)
#                 dr.find_element_by_id('loginBtn').click()
#                 time.sleep(1)
#                 dr.switch_to.default_content()
#             except NoSuchElementException:
#                 pass
#             finally:
#                 return dr
#         except Exception as e:
#             writelog('进入课程失败')
#             writelog(str(e))
#             sys.exit(0)
#
#     def playvideo(self, dr):  # 开始播放视频
#         try:
#             try:
#                 wait = ui.WebDriverWait(dr, 10)
#                 wait.until(lambda dr: dr.find_element_by_class_name('goback'))
#             except TimeoutException:
#                 writelog('连接超时 错误信息：未找到开始播放')
#                 dr.quit()
#                 sys.exit(0)
#             now_chapter = dr.find_element_by_xpath('//*[@id="mainid"]/h1').text
#             self.signal2.emit('正在看： ' + now_chapter)
#             # 进入frame第一层
#             dr.switch_to.frame('iframe')
#             # 进入frame第二层
#             dr.switch_to.frame(dr.find_elements_by_tag_name("iframe")[0])
#             # 下拉滚动条至播放器
#             time.sleep(0.1)
#             vedioplay = dr.find_element_by_id('video')
#             dr.execute_script('arguments[0].scrollIntoView();', vedioplay)
#             time.sleep(0.1)
#             # 播放视频了
#             # print('准备播放视频')
#             self.signal3.emit('准备播放视频')
#             time.sleep(0.2)
#             # print('开始播放')
#             self.signal3.emit('开始播放' + now_chapter)
#             dr.find_element_by_class_name('vjs-big-play-button').click()
#             # 暂停按钮定位
#             start = dr.find_element_by_xpath('//*[@id="video"]/div[5]/button[1]')
#             # 静音按钮定位
#             voice = dr.find_element_by_xpath('//*[@id="video"]/div[5]/div[6]/button')
#             # 调节速度按钮定位
#             speed = dr.find_element_by_xpath('//*[@id="video"]/div[5]/div[1]')
#             # 移动鼠标至视频 等待0.1秒
#             ActionChains(dr).context_click(vedioplay).perform()
#             time.sleep(0.1)
#             # 视频时长定位
#             alltime = dr.find_element_by_class_name('vjs-duration-display').text
#             # 点击静音按钮
#             voice.click()
#             # 调至二倍速
#             for i in range(3):
#                 speed.click()
#             start.click()
#             time.sleep(0.5)
#             start.click()
#             self.signal3.emit('已静音二倍速播放')
#             while 1:
#                 self.listener(dr, vedioplay, alltime)
#         except Exception as e:
#             writelog('播放视频出错')
#             writelog(str(e))
#             dr.quit()
#             sys.exit(0)
#
#     def listener(self, dr, vedioplay, alltime):  # 使用监听器的地方
#         try:
#             time.sleep(1)
#             # 移动鼠标至控制台 等待0.1秒
#             ActionChains(dr).context_click(vedioplay).perform()
#             res = self.listensubmit(dr)
#             # 播放时长定位
#             nowtime = dr.find_element_by_xpath('//*[@id="video"]/div[5]/div[2]/span[2]').text
#             if res:
#                 ans = dr.find_elements_by_name('ans-videoquiz-opt')
#                 for ans in ans:
#                     ans.click()
#                     dr.find_element_by_class_name('ans-videoquiz-submit').click()
#                     self.listenalert(dr)
#                     self.listenalert(dr)
#                     submit = self.listensubmit(dr)
#                     if submit is False:
#                         self.signal3.emit('答对了，继续看视频')
#                         break
#                         # // *[ @ id = "videoquiz-1038"] / ul / li[1] / label / input
#             if nowtime == alltime:
#                 self.signal1.emit(0)
#                 time.sleep(1)
#                 self.nextvedio(dr)
#             now = nowtime.split(':')
#             all = alltime.split(':')
#             now_s = int(now[0]) * 60 + int(now[1])
#             all_s = int(all[0]) * 60 + int(all[1])
#             if all_s:
#                 self.signal1.emit(int(now_s / all_s * 100))
#             # print(str(now_s) + '  ' + str(all_s))
#         except Exception as e:
#             writelog('监听弹窗出错')
#             writelog(str(e))
#             dr.quit()
#             sys.exit(0)
#
#     def listensubmit(self, dr):  # 答题事件监听
#         try:
#             dr.find_element_by_class_name('ans-videoquiz-submit')
#         except NoSuchElementException:
#             return False
#         else:
#             self.signal3.emit('有题')
#             return True
#
#     def listenalert(self, dr):  # 弹窗监听
#         try:
#             dr.switch_to.alert
#         except NoAlertPresentException:
#             return False
#         else:
#             dr.switch_to.alert.accept()
#             return True
#
#     def nextvedio(self, dr):  # 下一章
#         try:
#             # 回到上一级框架
#             dr.switch_to.default_content()
#             # # 回到上一级框架
#             # dr.switch_to.default_content()
#             # 下拉滚动条
#             js = 'var action=document.documentElement.scrollTop=10001'
#             dr.execute_script(js)
#             time.sleep(0.5)
#             # 定位下一页
#             element = dr.find_element_by_id('right2')
#             # 点击下一页
#             ActionChains(dr).move_to_element(element).click(element).perform()
#             if self.is_ans:
#                 try:
#                     wait = ui.WebDriverWait(dr, 10)
#                     wait.until(lambda dr: dr.find_element_by_id('iframe'))
#                 except TimeoutException:
#                     writelog('连接超时 错误信息：未找到测验题')
#                     dr.quit()
#                     sys.exit(0)
#                 self.signal3.emit('开始做章节测验题')
#                 self.find_TM(dr)
#                 self.signal3.emit('做完啦\n')
#             else:
#                 self.signal3.emit(' \n')
#             # 下拉滚动条
#             time.sleep(1.5)
#             dr.execute_script(js)
#             # 定位下一页
#             element = dr.find_element_by_id('right2')
#             # 定位下一页
#             ActionChains(dr).move_to_element(element).click(element).perform()
#             time.sleep(1.5)
#             self.playvideo(dr)
#         except Exception as e:
#             writelog('切换下一章出错')
#             writelog(str(e))
#             dr.quit()
#             sys.exit(0)
#
#     def find_TM(self, dr):
#         iframe1 = dr.find_elements_by_tag_name('iframe')
#         dr.switch_to.frame(iframe1[0])
#         # 进入frame第二层
#         iframe2 = dr.find_elements_by_tag_name('iframe')
#         dr.switch_to.frame(iframe2[0])
#         # 进入frame第三层
#         iframe3 = dr.find_elements_by_tag_name('iframe')
#         dr.switch_to.frame(iframe3[0])
#
#         try:
#             wait = ui.WebDriverWait(dr, 10)
#             wait.until(lambda dr: dr.find_element_by_class_name('ZyTop'))
#         except Exception as e:
#             writelog('连接超时 错误信息：题目验证出错')
#             writelog(str(e))
#             dr.quit()
#             sys.exit(0)
#         else:
#             # 检测是否已经做过
#             try:
#                 dr.find_element(By.XPATH, "//a[@class='Btn_blue_1 marleft10']/span")
#             except NoSuchElementException:
#                 dr.switch_to.default_content()
#             else:
#                 try:
#                     # 选择题elements
#                     xzt = dr.find_elements_by_xpath('//*[@class="Zy_ulTop w-top fl"]/../../div[1]/div')
#                     # 判断题elements
#                     pdt = dr.find_elements_by_xpath('//*[@class="Py_tk"]/../../div[1]/div')
#                     # 选择题答案elements
#                     xztda = dr.find_elements_by_xpath('//*[@class="TiMu"]/div[2]/ul/li/a')
#                     # 判断题答案elements
#                     pdtda = dr.find_elements_by_xpath('//*[@class="Py_tk"]/ul/li/label/input')
#                     choses = []
#                     for an in xztda:
#                         chose = an.text
#                         chose.replace(' ', '')
#                         choses.append(chose)
#
#                     # 回答选择题
#                     tm = {}
#                     if xzt:
#                         for i in range(int(len(choses) / 4)):
#                             time.sleep(1)
#                             cut_a = choses[4 * i:4 * (i + 1)]
#                             tm['question'] = xzt[i].text
#                             tm['ans'] = cut_a
#                             a, t = get_ans(tm['question'])
#                             a = a.replace('\n', '').replace(' ', '')
#                             if a == '暂未查询到答案！':
#                                 a, t = get_ans(tm['question'])
#                                 a = a.replace('\n', '').replace(' ', '')
#                             if '单选题' in tm['question']:
#                                 for an in tm['ans']:
#                                     if a in an:
#                                         dr.find_element_by_partial_link_text(a).click()
#                             else:  # 多选题
#                                 for an in tm['ans']:
#                                     if an in a:
#                                         dr.find_element_by_partial_link_text(an).click()
#                             tm = {}
#
#                     # 回答判断题
#                     if pdt:
#                         j = 0
#                         for i in range(int(len(pdt))):
#                             time.sleep(1)
#                             tm = {}
#                             tm['question'] = pdt[i].text
#                             a, t = get_ans(tm['question'])
#                             a = a.replace('\n', '').replace(' ', '')
#                             if a == '暂未查询到答案！':
#                                 a, t = get_ans(tm['question'])
#                                 a = a.replace('\n', '').replace(' ', '')
#                             if a == '正确' or a == '√':
#                                 pdtda[j + i].click()
#                             if a == '错误' or a == '×':
#                                 pdtda[j + i + 1].click()
#                             j = j + 1
#
#                     # 提交
#                     time.sleep(2)  # 临时解决答题结束闪退bug
#                     dr.find_element(By.XPATH, "//a[@class='Btn_blue_1 marleft10']/span").click()
#                     time.sleep(2)  # 临时解决答题结束闪退bug
#                     dr.find_element(By.LINK_TEXT, "确定").click()
#                     dr.switch_to.default_content()
#                 except Exception as e:
#                     writelog('答题出错')
#                     writelog(str(e))
#                     dr.quit()


class mainw(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(500, 700)
        main.setMinimumSize(QtCore.QSize(500, 700))
        main.setMaximumSize(QtCore.QSize(600, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/cc.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(14, 10, 471, 621))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CouresCheck = QtWidgets.QComboBox(self.layoutWidget)
        self.CouresCheck.setMinimumSize(QtCore.QSize(0, 0))
        self.CouresCheck.setMaximumSize(QtCore.QSize(321, 20))
        self.CouresCheck.setObjectName("CouresCheck")
        self.CouresCheck.addItem("")
        self.CouresCheck.addItem("")
        self.horizontalLayout.addWidget(self.CouresCheck)
        self.ChaptersCheck = QtWidgets.QComboBox(self.layoutWidget)
        self.ChaptersCheck.setMinimumSize(QtCore.QSize(0, 0))
        self.ChaptersCheck.setMaximumSize(QtCore.QSize(321, 20))
        self.ChaptersCheck.setObjectName("ChaptersCheck")
        self.ChaptersCheck.addItem("")
        self.ChaptersCheck.addItem("")
        self.horizontalLayout.addWidget(self.ChaptersCheck)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.StartBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartBtn.sizePolicy().hasHeightForWidth())
        self.StartBtn.setSizePolicy(sizePolicy)
        self.StartBtn.setMinimumSize(QtCore.QSize(71, 31))
        self.StartBtn.setMaximumSize(QtCore.QSize(71, 31))
        self.StartBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartBtn.setObjectName("StartBtn")
        self.horizontalLayout_2.addWidget(self.StartBtn)
        self.AutoAnswer = QtWidgets.QCheckBox(self.layoutWidget)
        # self.AutoAnswer.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AutoAnswer.sizePolicy().hasHeightForWidth())
        self.AutoAnswer.setSizePolicy(sizePolicy)
        self.AutoAnswer.setObjectName("AutoAnswer")
        self.horizontalLayout_2.addWidget(self.AutoAnswer)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.chapternow = QtWidgets.QLabel(self.layoutWidget)
        self.chapternow.setObjectName("chapternow")
        self.verticalLayout.addWidget(self.chapternow)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.ChapterProgress = QtWidgets.QProgressBar(self.layoutWidget)
        self.ChapterProgress.setProperty("value", 0)
        self.ChapterProgress.setObjectName("ChapterProgress")
        self.verticalLayout.addWidget(self.ChapterProgress)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "cc网课助手"))
        self.label_2.setText(_translate("main", "课程"))
        self.label.setText(_translate("main", "章节"))
        self.StartBtn.setText(_translate("main", "开始观看"))
        self.AutoAnswer.setText(_translate("main", "开启课后答题"))
        self.AutoAnswer.setChecked(True)
        self.chapternow.setText(_translate("main", "第一章节"))
        self.label_4.setText(_translate("main", "当前章节进度"))

    def setWindowIcon(self, icon):
        self.setWindowIcon(icon)


class Ui_main(QMainWindow, mainw):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.client = None
        self.flag = True
        self.dr = None
        self.thread = None
        self.is_ans = None
        self.app = QtWidgets.QApplication(sys.argv)

    def start(self):
        self.is_ans = 1 if self.AutoAnswer.isChecked() else 0
        # update_last_user_is_ans(self.is_ans)
        self.CouresCheck.setEnabled(False)
        self.ChaptersCheck.setEnabled(False)
        self.StartBtn.setEnabled(False)
        self.AutoAnswer.setEnabled(False)
        # 创建线程
        # self.thread = Runthread()
        # 连接信号
        self.thread.signal1.connect(self.Progress)  # 进程连接回传到GUI的事件
        self.thread.signal2.connect(self.showstate)  # 进程连接回传到GUI的事件
        self.thread.signal3.connect(self.showlog)  # 进程连接回传到GUI的事件
        self.thread.signal4.connect(self.driver_handle)  # 进程连接回传到GUI的事件
        # self.
        # 开始主线程
        self.thread.start()

    def driver_handle(self, object):
        self.dr = object

    def showlog(self, log):
        self.textEdit.insertPlainText(log + '\n')
        self.textEdit.moveCursor(QTextCursor.End)

    def showstate(self, msg):
        self.chapternow.setStyleSheet("color:red")
        self.chapternow.setText(str(msg))

    def Progress(self, msg):
        self.ChapterProgress.setValue(int(msg))  # 将线程的参数传入进度条

    # def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
    #     super().closeEvent(a0)
    #     try:
    #         if self.dr:
    #             self.dr.quit()
    #         if self.client is not None:
    #             try:
    #                 code = send_data(self.client, data='exit')
    #             except Exception as e:
    #                 writelog('向服务器发送断开信息失败')
    #                 writelog(str(e))
    #         writelog('退出程序')
    #         sys.exit(0)
    #     except Exception as e:
    #         writelog('关闭出错')
    #         writelog(str(e.__traceback__))
    #         sys.exit(0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_main()
    ui.StartBtn.clicked.connect(lambda: ui.start())
    ui.show()
    sys.exit(app.exec_())
