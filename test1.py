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
    >>> db.save()

    >>> db = SqlDB('xxx.db')
    >>> db.execute('select * from people where name="halida"')
    ['halida', 25, 'M']

    >>> import os
    >>> result = os.system('rm xxx.db')
    """
    import doctest
    doctest.testmod()
    
if __name__=="__main__":
    main()
