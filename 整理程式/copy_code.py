import os

def 檔案複製():
	列表 = open('test.txt',encoding='UTF-8')
	檔案成員 = 列表.readlines()
	列表.close()
	
	
	字典 = dict()
	
	
	for 成員 in 檔案成員:
		處理過的成員 = 成員.strip()
		字典[os.path.basename(處理過的成員)] = 處理過的成員
		
	print (字典)
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
if __name__ == '__main__':
		檔案複製()