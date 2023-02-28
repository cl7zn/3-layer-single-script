#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pytest
import sqlite3
import db_viewer


# In[7]:


@pytest.fixture
def test_table():
    connection = sqlite3.connect("aquarium.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM fish")
    assert cursor.fetchall() == [('Sammy', 'shark', 1), ('Jamie', 'cuttlefish', 7)]


# In[ ]:




