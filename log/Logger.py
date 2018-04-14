
# coding: utf-8

# In[1]:


#@author- Tejasvi Sharma
#@Logger
import logging
import time
logger = logging.getLogger()
fhandler = logging.FileHandler(filename='mylog'+str(time.strftime("%Y%m%d"))+str(time.strftime("%H%M%S"))+'.log', mode='a')
formatter = logging.Formatter('[%(asctime)s] %(name)s p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s','%m-%d %H:%M:%S')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.DEBUG)

