import sqlite3
import os

def openDB():
    return sqlite3.connect(os.path.join(os.path.dirname(__file__), "../universe.db"))