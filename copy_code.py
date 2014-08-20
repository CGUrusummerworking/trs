import os
import shutil

def 檔案複製():
	
	已成功複製的數量 = 0
	列表 = open('整理程式/file_list.txt',encoding='UTF-8')
	檔案成員 = 列表.readlines()
	列表.close()
	
	字典 = dict()
	檔案成員.sort()
	
	for 成員 in 檔案成員:
		處理過的成員 = 成員.strip()
		檔名 = os.path.basename(處理過的成員)
		所屬資料夾 = 處理過的成員.strip(檔名)
		字典[檔名] = 所屬資料夾
		#print(檔名,":",字典[檔名])
	
	#要複製檔案的絕對路徑(本程式所在的當前目錄)
	位置 = os.getcwd()
	開啟位置的所有檔案 = os.listdir(位置)
	
	
	for 成員 in 開啟位置的所有檔案:
		
		#print(目標位置)
		
		try:
			目標位置 = 位置 + 字典[成員]
			if (not(os.path.exists(目標位置))):
				os.makedirs(目標位置)
				
			shutil.copy(位置 + '/' + 成員,目標位置  + 成員)
			print(成員,"複製完成")
			已成功複製的數量+=1
			
		except:
			print(成員,"複製失敗")
			複製失敗資料夾 = 位置  + '/複製失敗的檔案'
			if (not(os.path.exists(複製失敗資料夾))):
				os.makedirs(複製失敗資料夾)
			shutil.copy(位置 + '/' + 成員,複製失敗資料夾 + '/' + 成員 )


	print(已成功複製的數量,"個檔案複製結束")
	
if __name__ == '__main__':
		檔案複製()
		