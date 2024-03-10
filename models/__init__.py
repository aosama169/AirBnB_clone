#!/usr/bin/python3

"""
Initializing Storage module as a global (singleton) Object
"""

from .engine.file_storage import FileStorage
"""
Retrieve storage instance
"""
storage = FileStorage()
storage.reload()
