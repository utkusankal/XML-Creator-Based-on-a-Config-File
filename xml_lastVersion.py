#!/usr/bin/env python
# coding: utf-8

# In[224]:



import xml_config_finalVersion as conf
import pprint

from io import BytesIO
from xml.dom import minidom 
import os
import xml.etree.ElementTree as et
from xml.etree.ElementTree import Element, SubElement, Comment
from xml.etree import ElementTree
#import pretty
from io import StringIO


# In[225]:


#print(conf.configuration["SNMP"])


# In[226]:


def pretty_xml(xml_str, indent="  "):
    """
    A very simple, hopefully not simplistic, XML pretty printer.
    Concept courtesy Mark Williams.
    """
    if not hasattr(xml_str, "read"): # ElementTree uses file-like objects
        fn = StringIO(xml_str)  # cStringIO doesn't support UTF-8
    else:
        fn = xml_str
    cursor = 0
    out_list = []
    for event, elem in et.iterparse(fn, events=('start', 'end')):
        if event == 'start':
            attrs = ' '.join([k+'="'+v+'"' for k, v in elem.items()])
            cur_tag = ('<{tag} {attrs}>'.format(tag=elem.tag, attrs=attrs)
                       if attrs else '<{tag}>'.format(tag=elem.tag))
            if elem.text is None:
                had_txt = False
                txt = '\n'
            else:
                had_txt = True
                txt = elem.text
            out_list.extend([indent*cursor, cur_tag, txt])
            cursor += 1
        else:
            cursor -= 1
            cur_ind = cursor*indent if not had_txt else ''
            out_list.extend([cur_ind, '</{0}>'.format(elem.tag), '\n'])
            had_txt = False
    return ''.join(out_list)


# In[227]:


dictn=conf.configuration["SNMP"]

#print(dictn)

#for key in dictn.values():
    #print(key)
def xml(root,dictn):
    iterator=0
    if(type(dictn)==list):
        dictn=dictn[iterator]
        iterator+=1
    SNMPid=0
    
    for key,val in dictn.items():
        SNMPid+=1
        k=key
        #print(k)
        
        key=et.SubElement(root,key)
        
       
        
        
        if type(val)==dict:
            k2id=0
            
            for key2,val2 in val.items():
                k2=key2
                
                k22=key2
                
                #print("k2",k2)
                
                
                if(k2.startswith("Node")):
                    k2id+=1
                   # node="Node"
                    #node=et.Element(node)
                    
                    
                
                key2=et.SubElement(key,key2)
                
                if(type(val2)==dict):
                    dictn=val
                   
                    #Modifikasyon
                    
                    
                    count=1
                    
                    for k in val2:
                        a=k
                        
                        k=et.SubElement(key2,k)
                        
                    
                        if type(val2[a])==list:
                            
                            dictn=val2[a]
                            
                            k.set("type",val2[a][0])
                            k.text=str(val2[a][1])
                            key.set("id",str(SNMPid))
                           
                            
                            
                            
                    count+=1
                    
                    
                    
                        
                    
                    
                    
                        
                            
                            
                            
                    
                
                else:
                    
                    for key3 in val2[0]:
                        
                        k3=key3
                        
                       
                        
                        
                        
                        key3=et.SubElement(key2,key3)
                        counter=0
                        if type(val2[0][k3])==list:
                            counter=counter+1
                            for k in val2:#[0][k3]
                                
                                key3.set("type",val2[0][k3][0])
                                key3.text=(val2[0][k3][1])
                                key2.set("id",str(k2id))
                                #node.set("id",str(counter+1))
                                counter+=1
                                
                                
                        
                                
                                
                        
                        #buraya kadar sadece oid eksik
                        if type(val2[0][k3])==dict:
                            for key4,val4 in val2[0][k3].items():
                                
                                k4=key4
                                
                                k5=key4
                                key4=et.SubElement(key3,k4)
                                counter1=1
                                for val in val2[0][k3].values():
                                    if type(val)==list:
                                        key4.set("id",str(counter1))
                                        key4.set("type",val[0])
                                        
                                        key4.text=val[1][0]
                                        index=0
                                        for i in val[1]:
                                            counter1+=1
                                            oid=et.SubElement(key3,"oid")
                                            oid.set("id",str(counter1))
                                            oid.set("type",val[0])
                                            oid.text=i
                                        
                        
                            
                            
                    
                                            
                            
                        #key3.text=val2[0][k3][1]
                               
                        
                        
                            
                        
                        
                        
                        
                
                
                
                
        
                
                
        
        
        
            
            """if(type(dic1[key2])==dict):
                for k3 in dic1[key2]:
                    k3=et.SubElement(root,k3)
                    root2=k3
                    newroot.append(root2)
            else:
                pass
               
            
       
            
          
        
                    
                 
                    
            
        
                
                
                #a=k
                #print("k is :",k)
                #a=et.SubElement(root,a)
                #k.set("type",new[a][0])
            
            """
   
                                
    return root


root=et.Element("SNMP")
newroot=xml(root,dictn)
output1=et.tostring(newroot)


# In[228]:


xmlstr=(pretty_xml(str(output1,'utf-8')))
                         


# In[229]:


xmlstr


# In[230]:


with open("XML1.xml", "w") as f:
    f.write(xmlstr)


# In[ ]:




