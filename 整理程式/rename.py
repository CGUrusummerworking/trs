import os
import shutil

def 檔案改名():
	現在目錄 = os.path.dirname(__file__)

	來源 = open(os.path.join(現在目錄, 'source.txt'), encoding='UTF-8')
	來源檔案 = 來源.readlines()  # 依行讀入至List
	來源.close()

	目標 = open(os.path.join(現在目錄, 'target.txt'), encoding='UTF-8')
	目標檔案 = 目標.readlines()  # 依行讀入至List
	目標.close()

	字典 = dict()  # 建立dictionary
	來源檔案.sort()
	目標檔案.sort()

	x = 0

	新來源 = []
	新目標 = []

	for 成員 in 來源檔案:
		新來源.append(成員.strip())
	for 成員 in 目標檔案:
		新目標.append(成員.strip())

	while x < len(來源檔案):
		字典[新來源[x]] = 新目標[x]
		x += 1

	完成數 = 0


	for dirPath, dirNames, fileNames in os.walk(os.path.join(現在目錄, '..', '文件檔案')):
		for 檔名 in fileNames:
			try:
# 				os.rename(dirPath + '/' + 檔名,dirPath+ '/' + 字典[檔名])
				a = 字典[檔名]
				完成數 += 1
			except:
				print(檔名, "可能因為已存在或是其他原因而沒改名")


	print(完成數, "個檔案更名完成")

if __name__ == '__main__':
		檔案改名()

