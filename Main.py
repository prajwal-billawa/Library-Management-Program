


#------Module Imports------------


import random
import pickle
import datetime
import os
import shutil


#------Class Blueprint-----------

class Library:
    cc=[] #Holds unique values of Id
    def __init__(self,d,m): #init function to declare variables
        self.Book_no=0
        self.Book_name=''
        self.Rec_name=''
        self.Rec_no=0
        self.rec_date=''
        self.initial_date=datetime.date.today()
        self.final_date=datetime.date.today()+datetime.timedelta(days=5)
        self.Fine=0
        self.dict={}
        self.temp_list=[]
        self.x=0
        self.tdate=d
        self.tmonth=m
        self.fined=datetime.date(datetime.date.today().year,m,d) #Set future date
        

        
        
    def Create_Membership(self):  #Function to create Memebership
        self.Rec_name=input('Please enter your name: '.center(columns)).capitalize()
        
        self.Rec_no=int(input('Please enter your ID Number: '.center(columns)))
        while True:
            if self.Rec_no in Library.cc:
                print('Id taken\nTry Again'.center(columns))
                self.Rec_no=int(input('Please enter your ID Number: '.center(columns)))
                pass
            else:
                Library.cc.append(self.Rec_no)
                break
            
        self.rec_date=datetime.date.today()     #Set date of record
        self.fined=datetime.date(datetime.date.today().year,self.tmonth,self.tdate)
        
        #Library.cc.append(self.Rec_no)
        
        
        

    def Issue_book(self): #Function to append issued books

        self.Book_name=str(input('Enter the name of book: '.center(columns)))
        self.x=random.randint(1,99999)
        self.dict[self.x]=self.Book_name
        self.initial_date=datetime.date.today()
        self.final_date=self.initial_date+datetime.timedelta(days=5)

        
    def Current_Status(self): #Display function
        self.fined=datetime.date(datetime.date.today().year,self.tmonth,self.tdate)
        self.final_date=self.initial_date+datetime.timedelta(days=5) #Date incremention by 5 to initial date
        if self.dict!={}:
        
            if self.fined>self.final_date:
                self.Fine=2*((self.fined-self.final_date).days)
            else:
                self.Fine=0
        else:
            self.Fine=0
        print('Recipient Name is: ',self.Rec_name)
        print('Recipient Number is: ',self.Rec_no)
        print('Issue date is: ',self.initial_date)
        print('Last date for book is: ',self.final_date)
        print('Fine is: $',self.Fine)
        print('Books are: ',self.dict)

        

    def Return_book(self,ID=0,nm=''):
        
        if ID!=0 and nm=='': #Delete by id
            if self.dict!={}:
                try:
                    self.dict.pop(ID)
                except:
                    print('Id is not present'.center(columns))
        elif ID==0 and nm!='': #Delete by name
            try:
                self.temp_list=list(self.dict.items())
                for self.i in self.temp_list:
                    for self.j in self.i:
                        if self.j==nm:
                            self.temp_list.remove(self.i)
                        else:
                            continue
                self.dict=dict(self.temp_list)
            except:
                    print('Name is not present'.center(columns))
        else:print('Error!!!'.center(columns))

        
        if self.dict!={}:
            self.fined=datetime.date(datetime.date.today().year,self.tmonth,self.tdate)
            if self.fined>self.final_date:
                self.Fine=2*((self.fined-self.final_date).days)
            else:
                self.Fine=0
        else:
            self.Fine=0
        
        
        print()
    
    def Renew_book(self): #Renew function to modify issued date
        self.Rec_name=self.Rec_name
        self.Rec_no=self.Rec_no
        self.Fine=self.Fine
        self.dict=self.dict
        self.initial_date=datetime.date(datetime.date.today().year,self.tmonth,self.tdate)
        self.final_date=self.initial_date+datetime.timedelta(days=5)
        self.fined=datetime.date(datetime.date.today().year,self.tmonth,self.tdate)
        Library.Current_Status(self)
        print()
      
#--------------------------------MAIN-----------------------------------

columns = shutil.get_terminal_size().columns #Set screen size
        

while True:  #Try catch to check validity of date
    try: 
        d=int(input('Enter the Date today (1-31)'.center(columns)))
        m=int(input('Enter the Month today (1-12)'.center(columns)))
        if (d>31 or d<0) or (m>12 or m<0):
            raise ValueError('Invalid Date Given!!!'.center(columns))
        else:
            break
    except ValueError as ve:
        print(ve)
        continue

print('Date is: ',datetime.date(datetime.date.today().year,m,d))
       
print('Welcome'.center(columns))    
print('What would you like to do?'.center(columns))
choice='Y'
while choice=='Y' or choice=='y' or choice=='yes' or choice=='Yes' or choice=='YES': #Menu page
    print('1.Create a membership id'.center(columns))
    print('2.Issue book'.center(columns))
    print('3.Get current status'.center(columns))
    print('4.Return book'.center(columns))
    print('5.Delete membership'.center(columns))
    print('6.Renew book'.center(columns))
    c=str(input('Which choice would you like to continue with? '.center(columns)))
    Object=Library(d,m) #Object

    #Memership Creation
    if c=='1':
        fw=open('book.dat','wb')
        
        while True:
            Object.Create_Membership()
            pickle.dump(Object,fw)
            ch=input('Continue (Yes/No)'.center(columns))
            if ch=='Yes' or ch=='yes' or ch=='YES' or ch=='y' or ch=='Y':
                continue
            else:
                break
        fw.close()
            

    #Issue book
    elif c=='2':

        fr=open('book.dat','rb')
        i=int(input('Enter Account Number: '.center(columns)))
        try:
            while True:
                Object=pickle.load(fr)
                if Object.Rec_no==i:
                    fw=open('book.dat','wb')
                    while True:
                        Object.Issue_book()
                        
                        ch=input('Enter another book??? (Y/N)'.center(columns))
                        if ch=='Yes' or ch=='yes' or ch=='YES' or ch=='y' or ch=='Y':
                            continue
                        else:
                            break
                    pickle.dump(Object,fw)
                    fw.close()
                else:continue
        
        except:
            pass
        fr.close()
        

    #Display function    
    elif c=='3':
        
        i=int(input('Enter Account Number: '.center(columns)))
        try:
            file=open('book.dat','rb')
        except FileNotFoundError:
            print('File Does Not Exist!!!')
        else:pass
        try:
            while True:
                Object=pickle.load(file)
                if Object.Rec_no == i:
                    Object.Current_Status()
                    print('User is present'.center(columns))
                    break
                else:
                    pass
                        
        except EOFError:
            print('User is not present'.center(columns))
        
        file.close()



    #Return Book
    elif c=='4':

        file=open('book.dat','rb')
        i=int(input('Enter Account Number: '.center(columns)))
        try:
            
            while True:
                
                Object=pickle.load(file)
                
                
                if Object.Rec_no==i:
                    fw=open('book.dat','wb')
                    c='yes'
                    while c=='Yes' or c=='yes' or c=='YES' or c=='y' or c=='Y':
            
                        print('1)Enter ID number'.center(columns))
                        print('2)Enter book name'.center(columns))
                        try:
                            c=int(input('Enter your choice: '.center(columns)))
                            if c==1:
                                ID=int(input('Enter the ID of book: '.center(columns)))
                                Object.Return_book(ID,'')
                            elif c==2:
                                nm=str(input('Enter the Name of book: '.center(columns)))
                                Object.Return_book(0,nm)
                            else:
                                print('Invalid Choice Given!!!'.center(columns))
                        except:
                            print('Invalid Choice entered!!!')
                        print('Do you want to continue? '.center(columns))
                        c=str(input('Enter your choice(yes/no)'.center(columns)))
                    pickle.dump(Object,fw)
                    fw.close()
                else:continue

        except EOFError:pass
        except KeyError:pass
        file.close()
                                
        

    #Delete memebership           
    elif c=='5':
        while True: 
            try:
                i=int(input('Enter Recipient Number: '.center(columns)))
                if isinstance(i,int)!=True:
                    raise ValueError('invalid Value Given'.center(columns))
                else:
                    break
            except ValueError as ve:
                print(ve)
                continue
        file=open('book.dat','rb')
        fw=open('Temp.dat','wb')
        try:
            while True:
                Object=pickle.load(file)
                if Object.Rec_no==i:
                    pass
                else:
                    pickle.dump(Object,fw)
                    
        except EOFError:
            print('End of File!!!'.center(columns))
            
        file.close()
        fw.close()
        os.remove('book.dat')
        os.rename('Temp.dat','book.dat')


    #Renew book
    elif c=='6':
        while True: 
            try:
                i=int(input('Enter Recipient Number: '.center(columns)))
                if isinstance(i,int)!=True:
                    raise ValueError('invalid Value Given'.center(columns))
                else:
                    break
            except ValueError as ve:
                print(ve)
                continue
        
        file=open('book.dat','rb')
        fw=open('Temp.dat','wb')
        try:
            while True:
                Object=pickle.load(file)
                if Object.Rec_no==i:
                    Object.Renew_book()
                    pickle.dump(Object,fw)
                else:
                    pickle.dump(Object,fw)
                    
        except EOFError:
            print('Done'.center(columns))
            
        file.close()
        fw.close()
        os.remove('book.dat')
        os.rename('Temp.dat','book.dat')
       
    else:
        print('Invalid choice entered!!!'.center(columns))
        
    
    choice=input('Go to Menu? Y/N'.center(columns))


#---------------------------------END-----------------------------





        

