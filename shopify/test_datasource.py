import pytest

class TestDatasource(object):

    def test_collect_with_a_single_map(self):
        d = Datasource([1,2,3]).map(lambda x: x*2)

        assert d.collect() == [2,4,6]

    def test_collect_with_two_maps(self):
        initial = Datasource([1,2,3])

        first = initial.map(lambda x: x*2)

        second = first.map(lambda x: x*3)

        assert initial.collect() == [1,2,3]
        assert first.collect() == [2,4,6]
        assert second.collect() == [6,12,18]

    def test_collect_with_chained_maps_and_filters(self):
        d = Datasource([1,2,3]) \
            .map(lambda x: x*2) \
            .filter(lambda x: x == 4) \
            .map(lambda x: x*3)

        assert d.collect() == [12]

class Datasource(object):
    
    def __init__(self, input_lst):
        
        self.input_lst = input_lst
        
        self.func_queue = []
        
    
    def _map(self, func):
        """Maps the provided function to the dataframe.
        
        @TODO: Instead of catching of exception, write a valitior to check for the arguments.
        
        Args:
            fucn: pyhton function
        Returns:
            A new dataframe
        """
        try:
            mapped = map(func, self.input_lst) 
        except TypeError as e:
            raise(e)
        
        self.input_lst = list(mapped)

        return self.input_lst
    
    
    def _filter(self, func):
        """Fitlers the datafram)e based on the function provided.
        
        @TODO: Instead of catching of exception, write a valitior to check for the arguments.
        
        Args:
            fucn: pyhton function
        Returns:
            A new dataframe
        """
        
        try:
            filtered = filter(func, self.input_lst)
        except TypeError as e:
            raise(e)
            
        self.input_lst = list(filtered)

        return self.input_lst
    
    
    def map(self, func):
        
        self.func_queue.append((self._map, func))
        
        return self
    
    def filter(self, func):
        
        self.func_queue.append((self._filter, func))
        
        return self
    
    
    def collect(self):
        """Prints out the contents of the dataframe.
        """
        result = []
        for func, arg in self.func_queue:
            result = func(arg)
            
            
        return result
    
    
pytest.main() 






