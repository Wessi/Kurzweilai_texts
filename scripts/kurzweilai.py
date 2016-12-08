#! /usr/bin/python


import eatiht.v2 as v2
import glob
# import pathlib as path
import os
from BeautifulSoup import BeautifulSoup
import re
import shutil
from shutil import copyfile

def getFileSize(file):
	file.seek(0,2)
	return file.tell()



def fileter_content(file):
	f = open(file,"r")

	output = ""
	soup = BeautifulSoup(f)
	divTag = soup.findAll("div", {"class":"content"})
	
	for tag in divTag:
		pTags = tag.findAll("p")
		#print(pTags)
		for tag in pTags:
			#print(tag.text)
			output += tag.text + "\n\n"
    return re.sub("&nbsp;", " ", output)


def extrac_html(path):
	file = open(path,"r")
	
	return v2.extract(file)
	

	

def create_txt_file(path):

	file = open(path,"w");
	return file



def copydirectorykut(src, dst):
    #dst = /home/icog-labs/test (2)/Output_Test/k11
    #src = /home/icog-labs/AGI-SITES/k1
    os.chdir(dst)
    list=os.listdir(src)
    nom= src+'.txt' # /home/icog-labs/AGI-SITES/k1.txt
    fitx= open(nom, 'w')
    
    copy_list = []
    for item in list:
        copy_me = src +"/"+ item # absolute path for each file
        copy_list.append(copy_me)
        fitx.write("%s\n" % item)
    fitx.close()

    f = open(nom,'r')
    for line in f.readlines():
        
        if "." in line:
                pass
                
        else:
            if not os.path.exists(dst+'/'+line[:-1]):
                os.makedirs(dst+'/'+line[:-1])
                copydirectorykut(src+'/'+line[:-1],dst+'/'+line[:-1])
            copydirectorykut(src+'/'+line[:-1],dst+'/'+line[:-1])
            
    f.close()
    os.remove(nom)
    os.chdir('..')



def copyfile2(src, dst):

    os.chdir(dst)
    list=os.listdir(src)
    # for i in list:
    #     print (src+"/"+ i)
    nom= src+'.txt'
    fitx= open(nom, 'w')
    

    for item in list:
        fitx.write("%s\n" % item)
    fitx.close()

    f = open(nom,'r')
    for line in f.readlines():

        copy_me = src + "/" + line
        copy_me =copy_me[:len(copy_me)-1]
        print (copy_me)
        if "html" in line:

            
            
                
               
		# print(src+'/'+line[:-1])
		
            oout = fileter_content(src+'/'+line[:-1]).encode('utf-8')

            if len(oout) == 0:
                copyfile(copy_me,"/home/icog-labs/test_copy/" + line)
                # file = create_txt_file(dst+'/empty/'+line[:-5] + "txt")
                # file.write(oout)

                # os.system('cp'+ oout+ '/empty/')
                # shutil.copyfile('/home/icog-labs/AGI-SITES/k1","/home/icog-labs/test (2)/Output_Test/k11/empty/')


            else:
                file = create_txt_file(dst+'/'+line[:-5] + "txt")
                file.write(oout)
			
       
    f.close()
    os.remove(nom)
    os.chdir('..')





# call these function in linux
copydirectorykut("/home/icog-labs/AGI-SITES/kruzweil_html","/home/icog-labs/test (2)/Output_Test/k11")
copyfile2("/home/icog-labs/AGI-SITES/kruzweil_html","/home/icog-labs/test (2)/Output_Test/k11")


#ex_html("/root/Desktop/project final/eatiht-0.1.11/Test_folder/root.html")





