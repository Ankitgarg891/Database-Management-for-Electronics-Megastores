# Importing some modules

import os
import pickle
import time




#####################          CLASSES OF ADMINISTRATOR      #####################


#.......EMPLOYEE.......
class employee:
          ecode=None
          name=None
          price=None
          def __init__(self):
                    self.ecode=0
                    self.name='A'
                    self.salary=0
          def input(self):
                    
                    self.name=raw_input('Enter name of Employee-')
                    self.salary=input('Enter salary of Employee-')
                    self.ecode=input("Enter Employee code-")
          def show(self):
                    print self.ecode,
                    print '     ',
                    print self.name,
                    l=len(self.name)
                    a=30-l
                    s=''
                    for i in range (a):
                              s+=' '
                    print s,
                    print self.salary,
                    

#........CUSTOMERS........
class customers:
          
          name='a'
          
          address='n'
          pn=0
          def __init__(self):
                          self.t=time.strftime("%X")
                          self.d=time.strftime("%x")
          def addcustomer(self):
                    
                    self.name=raw_input('Enter your name-')
                    self.adress=raw_input('Enter Your Address-')
                    
                    self.pn=input("Enter your phone number")
          def showcustomer(self):
                    print self.name,
                    l=len(self.name)
                    a=20-l
                    s=''
                    for i in range (a):
                              s+=' '
                    print '     ',
                    print self.address,
                    l=len(self.address)
                    a=40-l
                    s=''
                    for i in range (a):
                              s+=' '
                    print s,
                    print self.pn,
                    print '     ',
                    print self.d,
                    print '            ',
                    print self.t


#############################  FUNCTIIONS OF ADMINISTRATOR  #############################

def seeallproducts():
          file=open("price list.txt","r+")
          pro=file.read()
          print pro
          file.close()
         

def Addproducts():
          pcode=895
          p=str(pcode)
          na=raw_input('Enter Product name')
          n='	'
          pr=raw_input ('Enter Product price')
          l=40-len(na)
          sp=''
          for i in range(l):
                    sp=sp+' '
                    
          file=open("price list.txt","ab+")
          strn=p+n+na+sp+pr
          file.writelines(strn)
          
        



def EditEmployeeImformation():
          
          def addemployees():
                    ak=employee()
                    ak.input()
                    files=open('employee.txt','ab+')  
                    pickle.dump(ak,files)
                    files.close()


          def editsalary():
                    print 'List Of Employees-'
                    display()
                    print
                    mod=raw_input("Enter name of Employee to modify salary-")
                    sal=input('Enter new salary-')
                    file2=open('sample1.txt','ab')
                    files=open('employee.txt','rb')
                    
                    try:
                              r=pickle.load(files)
                              if r.name != mod:
                                        
                                        pickle.dump(r,file2)
                                                  
                              else:
                                        r.salary=sal 
                                        pickle.dump(r,file2)
                                        
                    except EOFError:
                              pass
                    files.close()          
                    file2.close()
                    os.remove('employee.txt')
                    files.close()          
                    file2.close()
                    os.rename('sample1.txt','employee.txt')
                    print
                    print 'Data Sucessfully edited...'
                    

          def display():
              
                    files=open('employee.txt','rb')  
                    try :
                              d=pickle.load(files)
                              while d:
                                        
                                        d.show()
                                        
                                        d=pickle.load(files)
                                        print
                                        
                              
                    except EOFError:
                              pass
                    files.close()
                                        
          a=1
          while a==1:
                    print                    
                    j=''' What do you want to do...
1.)Display List of Employees
2.)Edit Salary
3.)Add Employees'''
                    for i in range (0,len(j)):
                              time.sleep(.01)
                              print j[i],
                              time.sleep(.01)
                    
                    print
                    c=input ('Enter ur choice here-')
                    if c==1:
                              display()
                              
                    elif c==2:
                              editsalary()
                    elif c==3:
                              addemployees()
                    
                    else:
                              'Print wrong choice'

def seeEmployeeslist():
          print 'Code      Name                            Salary'
          files=open('employee.txt','rb')  
          try :
                                
                    d=pickle.load(files)
                    while d:
                                        
                              d.show()
                                        
                              d=pickle.load(files)
                              print
                                        
                              
          except EOFError:
                    pass
          files.close()


          
def SeeListofRegisteredCustomers():
                print
                print 'Name         Address                                   Phone No.    Day of Joining        Time of Joining'
                files=open('customerlist.txt','rb')  
                try :
                                
                    d=pickle.load(files)
                    while d:
                                        
                              d.showcustomer()
                                        
                              d=pickle.load(files)
                              print
                                        
                              
                except EOFError:
                    pass
                files.close()

                          
          
    


def Administrator():
          wel='U will get 3 chances to Login'
          print
          for i in range (0,len(wel)):
                                        time.sleep(.01)
                                        print wel[i],
                                        time.sleep(.01)
          a=0
          while a<4:
                    print
                    user=raw_input('User Id:')
                    pas=raw_input('Password:')
                    
          
                    if user=='Ankit':
                              if pas=='ak891':
                                        for i in range(0,5):
                                                  time.sleep(0.1)
                                                  print '.',
                                        print 'Login successful'
                                        a=4
                              else:
                                        print 'Wrong password'
                                        a+=1

                    else:
                              print 'Wrong user id'
                              a+=1


          if a==4:
                    while True:                           
                              
                              time.sleep(.5)
                              wel='''
What do u want to do today-
1.)See all products
2.)Add products
3.)see Employees list
4.)Edit Employee Imformation
5.)See List of Registered Customers '''
          
                              for i in range (0,len(wel)):
                                        time.sleep(.01)
                                        print wel[i],
                                        time.sleep(.01)
          
                              time.sleep(.5)
                              print
                              print
                              ch='Enter YOur cHoiCe hErE-'
                              for i in range (0,len(ch)):
                                        time.sleep(.01)
                                        print ch[i],
                                        time.sleep(.01)
                              ch=input('')
                              if ch==1:
                                        seeallproducts()
                                        
                              elif ch==2:
                                        Addproducts()
                              elif ch==3:
                                        seeEmployeeslist()
                              elif ch==4:
                                        EditEmployeeImformation()
                              elif ch==5:
                                        SeeListofRegisteredCustomers()
                              
                              else:
                                        print 'Wrong Choice'

                                        

################### FUNCTIONS OF CUSTOMERS #############################
def seeinfo():
          print
          name=raw_input("Enter Your Name")
          print 'Name         Address                                   Phone No.    Day of Joining        Time of Joining'
          a=customers()
          
          files=open('customerlist.txt','rb')
          try :
                    while True:
                              d=pickle.load(files)
                              if not d:
                                        break
                              elif d.name ==name:
                                        d.showcustomer()                                                                      
                                        print
          except EOFError:
                    pass
          files.close()



def seeallproducts():
          file=open("price list.txt","r+")
          pro=file.read()
          print pro
          file.close()

def editname(name):
          mod=name
          sal=raw_input('Enter Correct Name here-')
          file2=open('sample1.txt','ab')
          files=open('customerlist.txt','rb')
          try:
                    while True:
                              r=pickle.load(files)
                              if r.name != mod:
                                        pickle.dump(r,file2)
                              else:
                                        r.name=sal 
                                        pickle.dump(r,file2)
                                                  
          except EOFError:
                    pass
          files.close()          
          file2.close()
          os.remove('customerlist.txt')
          files.close()          
          file2.close()
          os.rename('sample1.txt','customerlist.txt')
def editaddress(name):
          mod=name
          sal=raw_input('Enter Correct Address here-')
          file2=open('sample1.txt','ab')
          files=open('customerlist.txt','rb')
          try:
                    while True:
                              r=pickle.load(files)
                              if r.name != mod:
                                        pickle.dump(r,file2)
                              else:
                                        r.address=sal 
                                        pickle.dump(r,file2)
                                                  
          except EOFError:
                    pass
          files.close()          
          file2.close()
          os.remove('customerlist.txt')
          files.close()          
          file2.close()
          os.rename('sample1.txt','customerlist.txt')
def editphonenumber(name):
          mod=name
          sal=raw_input('Enter Correct Phone Number here-')
          file2=open('sample1.txt','ab')
          files=open('customerlist.txt','rb')
          try:
                    while True:
                              r=pickle.load(files)
                              if r.name != mod:
                                        pickle.dump(r,file2)
                              else:
                                        r.pn=sal 
                                        pickle.dump(r,file2)
                                                  
          except EOFError:
                    pass
          files.close()          
          file2.close()
          os.remove('customerlist.txt')
          files.close()          
          file2.close()
          os.rename('sample1.txt','customerlist.txt')




def editinfo():
          print
          name=raw_input("Enter Your Name:")
          print 'Name         Address                                   Phone No.    Day of Joining        Time of Joining'
          files=open('customerlist.txt','rb')  
          try :
                    d=pickle.load(files)
                    if d.name ==name:
                              d.showcustomer()                                                            
                              d=pickle.load(files)
                              print
          except EOFError:
                              pass
          files.close()
          wel=''' 
What Do You Want To Edit..??
1.)Name
2.)Address
3.)Phone Number'''

          for i in range (0,len(wel)):
                    time.sleep(.01)
                    print wel[i],
                    time.sleep(.01)
          while True:
                    time.sleep(.5)
                    print
                    print
                    ch='Enter Your choiCe here-'
                    for i in range (0,len(ch)):
                              time.sleep(.01)
                              print ch[i],
                              time.sleep(.01)
                    ch=input('')
                    if ch==1:
                              editname(name)
                              
                    elif ch==2:
                              editaddress(name)
                    elif ch==3:
                              editphonenumber(name)
                    else:
                              print 'Wrong Choice'
                              break





def oCustomer():
          wel='''
What do u want to do -
1.)See Your Details
2.)Edit Your Detals
3.)See List of all products'''
          
          for i in range (0,len(wel)):
                    time.sleep(.01)
                    print wel[i],
                    time.sleep(.01)
          while True:
                    time.sleep(.5)
                    print
                    print
                    ch='Enter YOur choiCe here-'
                    for i in range (0,len(ch)):
                              time.sleep(.01)
                              print ch[i],
                              time.sleep(.01)
                    ch=input('')
                    if ch==1:
                              seeinfo()
                    elif ch==2:
                              editinfo()
                    elif ch==3:
                              seeallproducts()       
                              
                    else:
                              print 'Wrong Choice'
          
          

############################# Function Of New Customer ###########################
          
def nCustomer():
          a=customers()
          a.addcustomer()
          files=open('customerlist.txt','ab+')
          pickle.dump(a,files)
          files.close()
          print 'You are Sucessfully Registered'
          print 'Thank You For Joining us...'






#####################################################################
#Main Menu
#####################################################################
          
now = time.strftime("%c")
for i in range(0,5):
          time.sleep(0.3)
          print '.',          
print
time.sleep(1)
wel='''
                    WELCOME TO

_________COMPUTER SCIENCE PROJECT ON PYTHON_________



Programme on Computer Shop Records Management System

        

                MADE BY-ANKIT '''

for i in range (0,len(wel)):
          time.sleep(.01)
          print wel[i],
          time.sleep(.01)


for i in range(0,5):
          time.sleep(0.3)
          print '.',
print        

## Date representation
print "Today's date "  + time.strftime("%x")




for i in range(0,5):
          time.sleep(0.3)
          print '.',
print
## Time representation
print "Current time " + time.strftime("%X")



#CompVision Records Management System




for i in range(0,5):
          time.sleep(0.2)
          print '.',
print  
import random                                                                                                                                                                                                                                                                                                                                                                #line 1
wel=''' 
How Do You Want To Login..

1.)Administrator
2.)Old Customer
3.)New Customer'''

for i in range (0,len(wel)):
          time.sleep(.01)
          print wel[i],
          time.sleep(.01)
while True:
          time.sleep(.5)
          print
          print
          ch='Enter YOur cHoiCe hErE-'
          for i in range (0,len(ch)):
                    time.sleep(.02)
                    print ch[i],
                    time.sleep(.02)
          ch=input('')
          if ch==1:
                    Administrator()
                    
          elif ch==2:
                    oCustomer()
          elif ch==3:
                    nCustomer()
          else:
                    print 'Wrong Choice'








