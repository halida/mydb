#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: mydb
"""
import os.path

class DB():
    def __init__(self, filename, create_file=True):
        if not os.path.isfile(filename):
            if not create_file:
                raise Exception('filename : %s not exists!' % filename)
        self.tables = {}
        self.columns = {}

    def create_table(self, table_name, columns):
        self.tables[table_name] = []
        self.columns[table_name] = columns

    def __getattr__(self, name):
        if name not in self.tables:
            raise Exception('cannot find table: %s' % name)
        return Table(self, name)

class Table():
    def __init__(self, db, name):
        self.name = name
        self.db = db

    def insert(self, *args):
        column = args
        self.db.tables[self.name].append(column)

    def select(self, **kw):
        data = self.db.tables[self.name]
        if kw == {}:
            return data

        result = []
        for row in data:
            for k in kw:
                i = self.db.columns[self.name].index(k)
                if row[i] != kw[k]:
                    break
            else:
                result += row
        return result
            
            


            
        
        
