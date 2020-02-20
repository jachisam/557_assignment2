#!/usr/bin/env python
# coding: utf-8

# In[56]:


with open('gps.csv') as csvfile, open("/Users/jordanchisam/Desktop/101.csv", "wb") as csvfile2:
    reader = csv.reader(csvfile)
    next(reader, None)  # skip the headers
    writer = csv.writer(csvfile2, delimiter=',')
    for row in reader:
        id_ = int(float(row[1]))
        if(id_ == 101):
            writer.writerow(row)
       


# In[ ]:





# In[ ]:




