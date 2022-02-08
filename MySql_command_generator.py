#!/usr/bin/env python
# coding: utf-8

# In[16]:


def GenRandom(indStmntDict):
    RetStmnt=[random.choice(indStmntDict[int(i)]) for i in stmnt2]
    return RetStmnt
def GenRollNo(Rollformat):
    rf=[]
    k=0
    for i in Rollformat:
        if i=='X';
         i=str(k)
         k+=1
    return rf    
    
first_names=[]
last_names=['Parvatikar','Patel','Sharma','Tyagi','Singh','Verma','Agarwal']
names="Vishnu Amanda2. Jay3. Anna4. Abdullah5. Tamara6. Abdul7. Maya8. Jai9. Tara10. Rohan11. Ana12. Ajay13. Aisha14. Ram15. Alisha16. Sanjay17. Anya18. Ravi19. Lila20. Arman21. Amara22. Amit23. Fatima24. Sandeep25. Anika26. Vijay27. Anita28. Rahul29. Trisha30. Ira31. Arya32. Ibrahim33. Anjali34. Ashwin35. Jasmin36. Kiran37. Priya38. Krish39. Asha40. Arjun41. Ida42. Rajesh43. Riya44. Dev45. Mira46. Deepak47. Shyla48. Arun49. Mara50. Anand"
name=''.join([i for i in names if not i.isdigit()])
name=''.join([i for i in name if not i=='.'])
first_names=name.split(' ')
age=[i for i in range(18,35)]
print(first_names)
print(last_names)


# In[ ]:


#INSERT INTO TABLENAME(FNAME,LNAME)VALUES


# In[22]:


import random


stmnt=input('Input the Statement : Ex:INSERT INTO TABLENAME(COLMN1, COLMN2, ...)VALUES')
print('Enter what all should be there along with statement : ')

indStmntDict={1:first_names , 2:last_names , 3:age , 4:'Roll_Number' , 5:'Date'}
stmnt2=input('1)first_name , 2)last_name , 3) age , 4)Roll_Number(With format) , 5)Date')

n=int(input('Enter number of Statements required :'))


FinalStmnt=""
FinalStmnt1=""

for i in range(n):
 FinalStmnt1=stmnt+'('
 for ele in GenRandom(indStmntDict):
        FinalStmnt1+=ele
        FinalStmnt1+=","
 FinalStmnt1=FinalStmnt1[:-1]
 FinalStmnt1+=');\n'
 FinalStmnt+=FinalStmnt1
print(FinalStmnt2)
print(FinalStmnt)


# In[23]:


import pyperclip as pp

pp.copy(FinalStmnt)


# In[ ]:




