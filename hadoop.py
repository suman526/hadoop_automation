#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
import subprocess
while True:
        os.system("clear")
        os.system('tput setaf 7')
        print("\t\t\tWELCOME TO THE WORLD OF HADOOP !!")
        print("\t\t\t=================================")
        while True:
            os.system('tput setaf 2')
            print("""
                        PRESS 1: TO INSTALL HADOOP & JAVA
                        PRESS 2: TO CONFIGURE DATA NODE & NAME NODE
                        PRESS 3: TO FORMAT NAME NODE
                        PRESS 4: TO START HADOOP SERVICES
                        PRESS 5: TO STOP HADOOP SERVICES
                        PRESS 6: TO GET HADOOP REPORTS
                        PRESS 7: TO RETURN TO THE MAIN MENU
                    """)
            choice = input("Enter your choice: ")
            if choice == "1":
                os.system("rpm -ihv  jdk-8u171-linux-x64.rpm")
                os.system("rpm -ihv hadoop-1.2.1-1.x86_64.rpm --force")
            elif choice == "2":
                os.system("vim /etc/hadoop/hdfs-site.xml")
                os.system("vim /etc/hadoop/core-site.xml")
            elif choice == '3':
                os.system("hadoop namenode -format")
                input("Enter to continue.....")
            elif choice == "4":
                node = input("""
                                    PRESS 1: FOR NAMENODE
                                    PRESS 2: FOR DATANODE
                                        """)
                if node == "1":
                    os.system("hadoop-daemon.sh start namenode")
                    input("Enter to continue.....")
                elif node == "2":
                    os.system("hadoop-daemon.sh start datanode")
                    input("Enter to continue.....")
                else:
                    print("wrong choice!!! :( ")
                    break
            elif choice == 5:
                stopnode = input("""
                                    PRESS 1: FOR NAMENODE
                                    PRESS 2: FOR DATANODE
                                        """)
                if stopnode == "1":
                    os.system("hadoop-daemon.sh stop namenode")
                    input("Enter to continue.....")
                elif stopnode == "2":
                    os.system("hadoop-daemon.sh stop datanode")
                    input("Enter to continue.....")
                else:
                    print("WRONG CHOICE ! :( ")
                    break
            elif choice == "6":
                os.system("hadoop dfsasdmin -report")
                input("Enter to continue.....")
            else:
                input("Enter to continue.....")
                break


# In[ ]: