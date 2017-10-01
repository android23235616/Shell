# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 23:49:43 2017

@author: Tanmay
"""

import pymysql
from flask import session
class SQL:
    def __init__(self):
        session['subject']='android'
        self.conn = pymysql.connect(
                host='localhost',
                user='root',
                password='wart414ways465',
                db='attendance'#,
                #charset='utf8mb4',
                #cursorclass=pymysql.cursors.DictCursor
                )
        print ("Opened database successfully")

        self.cursor = self.conn.cursor()



    def giveCursor(self):
        return self.cursor

    def ex(self,query,a):
        self.cursor.execute(query,a)
        return self.cursor.fetchall()

    def check_login(self,name,password):
        query=  "SELECT * FROM coordinator_details WHERE name = %s AND mac = %s"
        self.cursor.execute(query,(name,password))
        if(self.cursor.fetchone()!=None):
            session['subject']='android'
            return True
        else:
            return False

    def __exit__(self):
        self.conn.close()
