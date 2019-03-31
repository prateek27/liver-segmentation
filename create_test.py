

import os
import sys


# In[23]:


TEST_PATH = "liverseg-2017-nipsws/LiTS_database/"
FOLDER_PATH = sys.argv[1]
TEST_PATH +=FOLDER_PATH
#print(TEST_PATH)


# In[24]:


X_files = []

for p in os.listdir(TEST_PATH):
    path = os.path.join(FOLDER_PATH,p)
    for f in os.listdir(os.path.join(TEST_PATH,p)):
        X_files.append(os.path.join(FOLDER_PATH,p,f))


# In[25]:


#print(len(X_files))


if(len(X_files)%3==1):
    X_files.append(X_files[-1])
    X_files.append(X_files[-1])
    

if(len(X_files)%3==2):
    X_files.append(X_files[-1])



#print(len(X_files))
      
total_files = int(len(X_files)/3)*3
print("Processing "+str(total_files)+" files")
    


def writeToFile(X,filename):
    with open(filename,'w') as f:
        t = (len(X)//3)*3
        s = "dummy.png"
        for i in range(0,t,3):
            line = " ".join([X[i],s,s,X[i+1],s,s,X[i+2],s,s,'\n'])
            f.writelines(line)  


# In[29]:


writeToFile(X_files,"liverseg-2017-nipsws/seg_DatasetList/test.txt")
print("Done")
