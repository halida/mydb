#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: test1
"""
from mydb import *

def main():
    """
    >>> db = connect('xxx.db')
    >>> db.create_table('people', ['name', 'age', 'gender'])
    >>> db.people.insert('halida', 25, 'M')
    >>> db.people.insert(column=['name', 'age'], value=['sophia', 15])
    >>> db.people.get(name='sophia')
    ['sophia', 15, None]
    """
    import docmod
    docmod.test()
    
if __name__=="__main__":
    main()
