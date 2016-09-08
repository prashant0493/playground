'''FileFit tool--- 1.Fixes files to right directory
               --- 2.Provides wild card search feature
               --- 3.Removes duplicate files for you
               --- 4.Music playlist feature


######__"All bug fixes are welcomed!"__######               
'''
import os
  
def filefinder():
    name=input('File name: ')
    items=os.listdir(os.getcwd())
    if name in items:
        print(name + '--Found!')
    else:
        print('Search results:-->')
        for filename in items:
            x=name.find('*')
            if filename.startswith(name[:x]) and filename.endswith(name[x+1:]):
                print(filename,end=' ')     
            else:
                pass
def completefilefinder():   ### THIS IS INCOMLETE FUNCTION
    name=input('@CFF tool on: File name : ')
    items=os.listdir(os.getcwd())
    hashlist=[]
    QDict=dict()
    result=[]
    if name in items:  
        print(name+' --Found @CFF')
    else:                                           # filter * results
        for filename in items:   
            x=name.find('*')
        if filename.startswith(name[:x]) and filename.endswith(name[x+1:]):
            hashlist.append(filename)           # hashlist: contains filtered results for '*'
    
        for hashlist_i in hashlist:
            QDict[hashlist_i]=hashlist_i.split('?')                  # QDict: contains filtered result for '?'

        for hashlist_i in hashlist:
            for QDict_i in QDict:
                for entry in QDict[QDict_i]:
                    if entry in hashlist_i:
                        cflag=True
                    else:
                        cflag=False
                if cflag is true:   
                    result.append(hashlist_i)
                    
                        
                

        for i in Qlist:
            if i not in name:
                pass
                
#PLEASE IGNORE COMPLETEFILEFINDER FUNCTION



   
def main():
    while(1):
        print('\nMenu-->> 1.FileFinder\t2.Quit')
        try:
            input1=int(input())
            if input1==1:
                filefinder()
            elif input1==2:
                print('You said...so, Quiting...!')
                break
            else:
                print('Either 1 or 2. Anyway, next time! [Quitting...]')    
                break

        except ValueError as e1:
            print('Error: Numeric input required--> ',e1)

if __name__=="__main__":
    main()



