import os
import shutil

def 檔案複製():
	列表 = open('file_list.txt',encoding='UTF-8')
	檔案成員 = 列表.readlines()
	列表.close()
	
	
	字典 = dict()
	檔案成員.sort()
	
	for 成員 in 檔案成員:
		處理過的成員 = 成員.strip()
		檔名 = os.path.basename(處理過的成員)
		所屬資料夾 = 處理過的成員.strip(檔名)
		字典[os.path.basename(處理過的成員)] = 所屬資料夾

	
	
	位置 = "C:/Users/jeng/git/trs/"
	開啟的位置 = os.listdir(位置)
	
	
	for 成員 in 開啟的位置:
		#print(字典[成員])
		try:
			目標位置= 位置  + 字典[成員]
			if (not(os.path.exists(目標位置))):
				os.makedirs(目標位置)
			shutil.copy(位置 + '/' + 成員,目標位置  + 成員)
		except:
			print(字典[成員])


	
	
if __name__ == '__main__':
		檔案複製()
		