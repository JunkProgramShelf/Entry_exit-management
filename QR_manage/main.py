import pyzbar
from pyzbar.pyzbar import decode,ZBarSymbol
import cv2
import numpy as np
import csv
import datetime as dtm
import time
import os

os.add_dll_directory("C:\Python310\lib\site-packages\pyzbar\libzbar-64.dll")
#os.add_dll_directory("C:\Python310\lib\site-packages\pyzbar\libiconv-64.dll")
plc=2# room ID
def edit_contrast(image, gamma):
    """Contrast manage"""
    look_up_table = [np.uint8(255.0 / (1 + np.exp(-gamma * (i - 128.) / 255.)))
        for i in range(256)]
    result_image = np.array([look_up_table[value]
                             for value in image.flat], dtype=np.uint8)
    result_image = result_image.reshape(image.shape)
    return result_image


if __name__ == "__main__":
	capture = cv2.VideoCapture(0)#PC camera:0、Web Camera:1
	cv2.namedWindow('frame')
	if capture.isOpened() is False:#Camera error
		raise IOError("IO Error")
	ret, frame = capture.read()
	while True:
		if ret == False:
			continue
        # grayscale
		gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		image = edit_contrast(gray_scale, 5)
        # decode and getting QR code
		codes = decode(image)
		if len(codes)>0:
			
			input=codes[0][0].decode('utf-8','ignore')
			num0=input#[1:len(input)-1]
            
			print(num0)
			font = cv2.FONT_HERSHEY_SIMPLEX
			cv2.putText(frame,str("complited"),(10,300), font, 2,(255,255,255),2,cv2.LINE_AA)
            #Check
			flag=0
			file=dtm.datetime.now()
			name=file.strftime('%Y%m%d')#file name
			if os.path.exists("./"+name+".csv"):#check file
				with open('./'+name+'.csv','r')as fp:
					r=csv.reader(fp)
					for row in r:
            			#print(row[0])
						if num0==row[0]:
							flag+=1
            #csv output
            #print(flag)
			if flag % 2==0:
				flag=1
			else:
				flag=0
			with open('./'+name+'.csv','a',newline='')as f:#in or out
				writer=csv.writer(f)
				writer.writerow([num0,dtm.datetime.now(),flag]) 
			with open('./meibo.csv','r+',newline='')as f1:#management 
				reader=csv.reader(f1)
            	#header=next(reader) header skip
				row=[x for x in reader]
				with open('./meibo.csv','w',newline='')as f2:
					writemeibo=csv.writer(f2)
					for rr in row:
						if rr[0]==num0:
							rr[plc]=flag
						writemeibo.writerow(rr)
			time.sleep(0.5)
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) >= 0:#end process
			break
		ret, frame = capture.read() 
		#time.sleep(0.1)
capture.release()
cv2.destroyAllWindows()