#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: test1
"""
from mydb import *

def main():
    """
    >>> db = DB('xxx.db')
    >>> db.create_table('people', ['name', 'age', 'gender'])
    >>> db.people.insert('halida', 25, 'M')
    >>> db.people.select(name='halida')
    ['halida', 25, 'M']

    db.people.insert(column=['name', 'age'], value=['sophia', 15])
    """
    import doctest
    doctest.testmod()
    
if __name__=="__main__":
    main()
