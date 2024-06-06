"""
ddt library helps with data-driven testing
"""
from ddt import ddt, data, unpack, file_data

@ddt  # decorating class with ddt to imply we are using data-driven testing and to use its functionalities
class TestClass:
    
    @data(("sample data1", "sample data2", "sample data3..."))
    @unpack
    def test_func(self):
        pass
    
    
    # alternate way
    @file_data("path/to/testdata")
    def test_func2(self):
        pass
    
    # reading from excel
    @data(("list from util file that reads excel","sheetname"))
    @unpack
    def test_func3(self):
        pass