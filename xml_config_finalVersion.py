#!/usr/bin/env python



#global_variables={"SNMP":"","SNMPPoller":["id"],"Kafka":"","General":"","Node":["id"]}
#timeOut=3000

cpu_usage=["3.1.1.2","12.2.23.34.34","2.3.4.3.43.4"]
mem_usage=["3.1.1.5","13.2.23.34.34","22.3.4.3.43.4"]
host="10.0.1.23"

nodes1=[{"host":["CHAR",host],"protocol":["CHAR","udp"],"snmpVersion":["CHAR","VERSION_3"],"authprotocol":["CHAR","md5"],"password":["CHAR","testuser"],"privacypassphrase":["CHAR","testuser"],
                      "privacyprotocol":["CHAR","DES"],"username":["CHAR","testuser"],"community":["CHAR","null"],"timeOut":["INTEGER","3000"],"snmpPort":["INTEGER","161"],
                      "retry":["INTEGER","2"],'oids':{'oid':["CHAR",cpu_usage + mem_usage]}}]
nodes2=[{"host":["CHAR",host],"protocol":["CHAR","utku"],"snmpVersion":["CHAR","utku"],"authprotocol":["CHAR","md5"],"password":["CHAR","testuser"],"privacypassphrase":["CHAR","testuser"],
                      "privacyprotocol":["CHAR","DES"],"username":["CHAR","testuser"],"community":["CHAR","null"],"timeOut":["INTEGER","3000"],"snmpPort":["INTEGER","161"],
                      "retry":["INTEGER","2"],'oids':{'oid':["CHAR",cpu_usage + mem_usage]}}]
nodes3=[{"host":["CHAR",host],"protocol":["CHAR","aaa"],"snmpVersion":["CHAR","fvff"],"authprotocol":["CHAR","md5"],"password":["CHAR","tefdr"],"privacypassphrase":["CHAR","testuser"],
                      "privacyprotocol":["CHAR","DES"],"username":["CHAR","testuser"],"community":["CHAR","null"],"timeOut":["INTEGER","3000"],"snmpPort":["INTEGER","161"],
                      "retry":["INTEGER","2"],'oids':{'oid':["CHAR",cpu_usage + mem_usage]}}]

#kafka_variables={"BootstrapServer":"CHAR","TopicOutput":"CHAR","GroupId":"CHAR"}

#general_variables={"PollingTimer ": ["INTEGER",2000]}

#node_variables={"timeout":"3000","protocol":"udp","snmpVersion":"version_3","password":"testuser",
                #"privacypassphrase":"testuser","privacyprotocol":"DES","username":"testuser","community":"null","retry":"2","snmPort":"161"}

kafka_configuration={
    'BootstrapServer':["CHAR",'10.211.55.4:9092'],
    'TopicOutput':["CHAR",'VesselClassificationA'],
    'GroupId':["CHAR",'group01']
    }

general_configuration={"PollingTimer ": ["INTEGER",2000]}
snmppoller2={
    'Kafka': kafka_configuration,
    'General':general_configuration,
    'Node':nodes1,
    'Node  ':nodes2,
    
    }

snmppoller1={
    'Kafka': kafka_configuration,
    'General':general_configuration,
    'Node':nodes1,
    'Node  ':nodes2,
    'Node   ':nodes3,
   
    
    
    }


configuration={"SNMP":[{'SNMPPoller':snmppoller1,'SNMPPoller ':snmppoller2}]
    }



