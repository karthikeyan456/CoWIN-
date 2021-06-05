import requests
import json
import csv
import sys
from columnar import columnar
import pyshorteners
from win10toast import ToastNotifier
district='Chennai'
f=open(r"C:\Users\SENTHILKUMAR\Desktop\CoWIN Automation\distlist.csv",'r')
distid=0
csvr=csv.reader(f)
for row in csvr:
    if csvr.line_num==1:
        continue
    if row[1]==district:
        distid=int(row[0])
#district id for chennai
#print(distid)
date='03-06-2021'
age='47'
pincode='0'
vaccinepref="COVAXIN"
dose=2
pay="PAID"
if int(age)<18:
    print("Vaccine not available for the given age group")
    sys.exit()
if int(age)<=44:
    age=18
if int(age)>=45:
    age=45


def generatemapurl(name,add):
    str1=''
    str1=name+add
    str1=str1.replace(' ','+')
    str1=str1.replace(',','%2C')

    urla='https://www.google.com/maps/search/?api=1&query=%s'%(str1)
    s = pyshorteners.Shortener()
    l=urla
    try:
        return s.tinyurl.short(l)
    except:
        return urla
        

   





url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=%s&date=%s"%(distid,date)

f=open(r"C:\Users\SENTHILKUMAR\Desktop\CoWIN Automation\cowindata.csv","w",newline='')
result=requests.get(url)
#print(result.text)
json=result.json()
#print(json)
data=json['sessions']
csvw=csv.writer(f)
c=0
for j in data:
    if c==0:
        header=j.keys()
        csvw.writerow(header)
        c+=1
    csvw.writerow(j.values())
f.close()
f=open(r"C:\Users\SENTHILKUMAR\Desktop\CoWIN Automation\cowindata.csv","r")
csvr=csv.reader(f)
opdata=[]
for row in csvr:
    if csvr.line_num==1:
        continue
    if int(row[18])==age:
        if pincode!='0' and row[6]==pincode:
            if vaccinepref!="ANY" and vaccinepref=="COVAXIN" and row[19]=='COVAXIN':
                if pay!="ANY" and pay=="PAID" and int(row[17])!=0:
                    if dose==1 and int(row[14])>0:
                        opdata.append([row[0],row[1],row[2],row[14],row[19],row[17],generatemapurl(row[1],row[2])])
                    if dose==2 and int(row[15])>0:
                        opdata.append([row[0],row[1],row[2],row[15],row[19],row[17],generatemapurl(row[1],row[2])])
                if pay!="ANY" and pay=="FREE" and int(row[17])==0:
                    if dose==1 and int(row[14])>0:
                        opdata.append([row[0],row[1],row[2],row[14],row[19],row[17],generatemapurl(row[1],row[2])])
                    if dose==2 and int(row[15])>0:
                        opdata.append([row[0],row[1],row[2],row[15],row[19],row[17],generatemapurl(row[1],row[2])])
                if pay=="ANY":
                    if dose==1 and int(row[14])>0:
                        opdata.append([row[0],row[1],row[2],row[14],row[19],row[17],generatemapurl(row[1],row[2])])
                    if dose==2 and int(row[15])>0:
                        opdata.append([row[0],row[1],row[2],row[15],row[19],row[17],generatemapurl(row[1],row[2])])
            if vaccinepref!="ANY" and vaccinepref=="COVISHIELD" and row[19]=='COVISHIELD':
                if pay!="ANY" and pay=="PAID" and int(row[17])!=0:
                    if dose==1 and int(row[14])>0:
                        opdata.append([row[0],row[1],row[2],row[14],row[19],row[17],generatemapurl(row[1],row[2])])
                    if dose==2 and int(row[15])>0:
                        opdata.append([row[0],row[1],row[2],row[15],row[19],row[17],generatemapurl(row[1],row[2])])
                if pay!="ANY" and pay=="FREE" and int(row[17])==0:
                    if dose==1 and int(row[14])>0:
                        opdata.append([row[0],row[1],row[2],row[14],row[19],row[17],generatemapurl(row[1],row[2])])
                    if dose==2 and int(row[15])>0:
                        opdata.append([row[0],row[1],row[2],row[15],row[19],row[17],generatemapurl(row[1],row[2])])
                if pay=="ANY":
                    if dose==1 and int(row[14])>0:
                        opdata.append([row[0],row[1],row[2],row[14],row[19],row[17],generatemapurl(row[1],row[2])])
                    if dose==2 and int(row[15])>0:
                        opdata.append([row[0],row[1],row[2],row[15],row[19],row[17],generatemapurl(row[1],row[2])])
            if vaccinepref=="ANY":
                if pay!="ANY" and pay=="PAID" and int(row[17])!=0:
                    if dose==1 and int(row[14])>0:
                        opdata.append([row[0],row[1],row[2],row[14],row[19],row[17],generatemapurl(row[1],row[2])])
                    if dose==2 and int(row[15])>0:
                        opdata.append([row[0],row[1],row[2],row[15],row[19],row[17],generatemapurl(row[1],row[2])])
                if pay!="ANY" and pay=="FREE" and int(row[17]==0):
                    if dose==1 and int(row[14])>0:
                        opdata.append([row[0],row[1],row[2],row[14],row[19],row[17],generatemapurl(row[1],row[2])])
                    if dose==2 and int(row[15])>0:
                        opdata.append([row[0],row[1],row[2],row[15],row[19],row[17],generatemapurl(row[1],row[2])])
                if pay=="ANY":
                    if dose==1 and int(row[14])>0:
                        opdata.append([row[0],row[1],row[2],row[14],row[19],row[17],generatemapurl(row[1],row[2])])
                    if dose==2 and int(row[15])>0:
                        opdata.append([row[0],row[1],row[2],row[15],row[19],row[17],generatemapurl(row[1],row[2])])
        if pincode=='0':
            if vaccinepref!="ANY" and vaccinepref=="COVAXIN" and row[19]=='COVAXIN':
                if pay!="ANY" and pay=="PAID" and int(row[17])!=0:
                    if dose==1 and int(row[14])>0:
                        opdata.append([row[0],row[1],row[2],row[14],row[19],row[17],generatemapurl(row[1],row[2])])
                    if dose==2 and int(row[15])>0:
                        opdata.append([row[0],row[1],row[2],row[15],row[19],row[17],generatemapurl(row[1],row[2])])
                if pay!="ANY" and pay=="FREE" and int(row[17])==0:
                    if dose==1 and int(row[14])>0:
                        opdata.append([row[0],row[1],row[2],row[14],row[19],row[17],generatemapurl(row[1],row[2])])
                    if dose==2 and int(row[15])>0:
                        opdata.append([row[0],row[1],row[2],row[15],row[19],row[17],generatemapurl(row[1],row[2])])
                if pay=="ANY":
                    if dose==1 and int(row[14])>0:
                        opdata.append([row[0],row[1],row[2],row[14],row[19],row[17],generatemapurl(row[1],row[2])])
                    if dose==2 and int(row[15])>0:
                        opdata.append([row[0],row[1],row[2],row[15],row[19],row[17],generatemapurl(row[1],row[2])])
            if vaccinepref!="ANY" and vaccinepref=="COVISHIELD" and row[19]=='COVISHIELD':
                if pay!="ANY" and pay=="PAID" and int(row[17])!=0:
                    if dose==1 and int(row[14])>0:
                        opdata.append([row[0],row[1],row[2],row[14],row[19],row[17],generatemapurl(row[1],row[2])])
                    if dose==2 and int(row[15])>0:
                        opdata.append([row[0],row[1],row[2],row[15],row[19],row[17],generatemapurl(row[1],row[2])])
                if pay!="ANY" and pay=="FREE" and int(row[17])==0:
                    if dose==1 and int(row[14])>0:
                        opdata.append([row[0],row[1],row[2],row[14],row[19],row[17],generatemapurl(row[1],row[2])])
                    if dose==2 and int(row[15])>0:
                        opdata.append([row[0],row[1],row[2],row[15],row[19],row[17],generatemapurl(row[1],row[2])])
                if pay=="ANY":
                    if dose==1 and int(row[14])>0:
                        opdata.append([row[0],row[1],row[2],row[14],row[19],row[17],generatemapurl(row[1],row[2])])
                    if dose==2 and int(row[15])>0:
                        opdata.append([row[0],row[1],row[2],row[15],row[19],row[17],generatemapurl(row[1],row[2])])
            if vaccinepref=="ANY":
                if pay!="ANY" and pay=="PAID" and int(row[17])!=0:
                    if dose==1 and int(row[14])>0:
                        opdata.append([row[0],row[1],row[2],row[14],row[19],row[17],generatemapurl(row[1],row[2])])
                    if dose==2 and int(row[15])>0:
                        opdata.append([row[0],row[1],row[2],row[15],row[19],row[17],generatemapurl(row[1],row[2])])
                if pay!="ANY" and pay=="FREE" and int(row[17]==0):
                    if dose==1 and int(row[14])>0:
                        opdata.append([row[0],row[1],row[2],row[14],row[19],row[17],generatemapurl(row[1],row[2])])
                    if dose==2 and int(row[15])>0:
                        opdata.append([row[0],row[1],row[2],row[15],row[19],row[17],generatemapurl(row[1],row[2])])
                if pay=="ANY":
                    if dose==1 and int(row[14])>0:
                        opdata.append([row[0],row[1],row[2],row[14],row[19],row[17],generatemapurl(row[1],row[2])])
                    if dose==2 and int(row[15])>0:
                        opdata.append([row[0],row[1],row[2],row[15],row[19],row[17],generatemapurl(row[1],row[2])])
            
if len(opdata)==0:
    print("NO DATA AVAILABLE")

else:
    txt=['CENTER ID','NAME','ADDRESS','AVAILABLE DOSES','VACCINE','FEE','GOOGLE MAPS URL']
    table=columnar(opdata,headers=txt,max_column_width=160)
    #print(table)
    f=open("vdata.txt",'w')
    f.write(table)
    f.close()
    n = ToastNotifier()
    n.show_toast("CoWIN","Vaccine Available.For more details visit vdata file in CoWIN Automation Folder in Desktop.For booking visit https://www.cowin.gov.in", duration = 10,icon_path =r"C:\Users\SENTHILKUMAR\Desktop\CoWIN Automation\cowinicon.ico")
 
    

            


            


                




    
