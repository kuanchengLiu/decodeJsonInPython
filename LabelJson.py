from os import listdir
from os.path import isfile, isdir, join
import os
import json

# serch key word


def keywordInJson(JFULL):
    if keywordLoseJson(JFULL):
        pass


def keywordLoseJson(JFULL):

    judge = JFULL.find('原告之訴駁回')
    if judge != -1:
        judge = JFULL.find('聲請人之聲請駁回')
        if judge != -1:
            return True
        else:
            return False
    else:
        return False


def keywordWinJson(JFULL):

    judge = JFULL.find('被告應給付原告')
    if judge != -1:
        return True
    else:
        return False


def keywordChangePlaceJson(JFULL):

    judge = JFULL.find('本件移送')
    if judge != -1:
        return True
    else:
        return False


def keywordPoolJudgeJson(JFULL):

    judge = JFULL.find('繳納裁判費')
    if judge != -1:
        return True
    else:
        return False


    # 获取当前文件路径
current_path = os.path.abspath(__file__)
# 指定要列出所有檔案的目錄
path = os.path.abspath(os.path.dirname(current_path) +
                       os.path.sep + "OriginClassiofication")

# 取得所有檔案與子目錄名稱
files = listdir(path)
JTITLE = []
# 以迴圈處理
for fName in files:
    # 產生檔案的絕對路徑
    fullpath = join(path, fName)
    # 判斷 fullpath 是檔案還是資料夾
    if isfile(fullpath):
        print("is file：", fName)
    elif isdir(fullpath):
        print("is Folder：", fName)
        # 獲取判決書路徑
        verdictPath = os.path.abspath(os.path.dirname(current_path) +
                                      os.path.sep + "OriginClassiofication" + os.path.sep + fName)
        verdictFiles = listdir(verdictPath)
        for verdict in verdictFiles:
            # 產生獲取判決書路徑
            if isfile(join(verdictPath, verdict)):
                print("verdict : ", verdict)
                # 拆解 .json file
                with open(join(verdictPath, verdict), encoding='utf-8') as fh:
                    data = json.load(fh)
                if data['JTITLE'] not in JTITLE:
                    JTITLE.append(data['JTITLE'])
                    ReClassificationPath = os.path.abspath(os.path.dirname(current_path) +
                                                           os.path.sep + "ReClassification")
                    print(ReClassificationPath)
                    ReClassificationFiles = listdir(ReClassificationPath)
                    for ReClassificationFileName in ReClassificationFiles:

                        ReClassificationFullPath = join(
                            ReClassificationFullPath, ReClassificationFileName)
                        print(ReClassificationFullPath)

                        if not in isdir(ReClassificationFileName):
                            os.mkdir(data['JTITLE'])
                            print('test')
                        else:

                print(JTITLE)
