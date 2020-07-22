import pandas as pd
import numpy as np
import json 
from .util import unwrap_zb_error
try:
    import _pickle as pickle
except:
    import pickle 
from ast import literal_eval

def parse_object(s):
    return json.loads(s)

class PutPages():

    def __init__(self, client, keys, data):
        self.client = client 
        self.keys = keys 
        self.data = data 
        self.max_bytes_per_page = 2000000 
        self.cur_idx = 0 
    
    def put_all(self, table_id, overwrite=False, table_owner_id=None):
        """
        Puts data into specified table. 

        Parameters: 
            table_id: string 
            overwrite: boolean (default=False)
            table_owner_id: string (default=self.client.id())
        """
        key_pages, value_pages = self.pagify()

        for i in range(len(key_pages)):
            keys = key_pages[i]
            values = value_pages[i]
            
            error = self.client.put_multi(table_id, keys, values, overwrite, table_owner_id)
            
            if unwrap_zb_error(error) is not None:
                return unwrap_zb_error(error)

        return None


    def pagify(self):
        """
        Returns 2d array of strings, 2d array of bytes.
        """
        page_bytes = 0 
        cur_page = []
        cur_page_values = []
        pages = []
        page_values = []

        for i in range(len(self.keys)):
            d_len = len(self.data[i])
            if (page_bytes + d_len) > self.max_bytes_per_page:
                pages.append(cur_page)
                page_values.append(cur_page_values)
                cur_page = []
                cur_page_values = []
                page_bytes = 0 

            cur_page.append(self.keys[i])
            cur_page_values.append(self.data[i])
            page_bytes += d_len

        if len(cur_page) > 0:
            pages.append(cur_page)
            page_values.append(cur_page_values)

        return pages, page_values 

class PaginationHandler():

    def __init__(self, f):
        """
        Initializes instance of PaginationHandler class.

        Parameters:
            f: paginationRequester - func (int) -> (dict[string][byte], bool) 
        """
        self.requester = f #paginationRequester func (int) -> (dict[string][]byte, bool)
        self.cur_data = None #dict[string][]byte
        self.cur_page = -1 #int
        self.has_next_page = True #bool
        self.cur_i = 0
        self.cur_keys = []
        self.return_dict = False 

    def __iter__(self):
        return self 

    def __next__(self):
        if self.cur_keys == []:
            self.cur_keys = self.keys()

        if self.cur_i >= len(self.cur_keys):
            if self.has_next_page:
                self.next()
                self.cur_keys = self.keys()
                self.cur_i = 0
            else:
                raise StopIteration()

        if len(self.cur_keys) > self.cur_i:
            cur_key = self.cur_keys[self.cur_i]
            cur_item = self.cur_data[cur_key]
            self.cur_i += 1
        else:
            raise StopIteration()


        try:
            if self.return_dict:
                return json.loads(cur_item)

            elif cur_item is not None:
                return cur_item
                
            else:
                return cur_key
        except TypeError:
            #Comes to this if (return literal_eval(cur_item.decode())) fails because cur_item is None
            if cur_item is not None:
                return pickle.loads(cur_item)
            return cur_key
        

    def return_pretty(self):
        """
        Will make items return as Python dictionaries when PaginationHandler is iterated through. 
        """
        self.return_dict = True 

    def return_bytes(self):
        """
        Will make items return as bytes when PaginationHandler is iterated through. 
        """
        self.return_dict = False 
    
    def data(self):
        """
        Returns dict that maps strings to a list of bytes. 
        """
        return self.cur_data 

    def keys(self):
        """
        Returns a list of strings. 
        """
        keys = []
        for key in self.cur_data:
            keys.append(key)
        return keys 

    def data_all(self):
        """
        Returns a dict that maps strings to a list of bytes.
        """
        i = 1
        data = self.cur_data
        while(self.has_next_page):
            dat, nxt = self.requester(i)
            for key in dat:
                data[key] = dat[key]
            i += 1
            self.has_next_page = nxt 
            self.cur_page = i 
            if len(dat) == 0 or not nxt:
                break 
        
        self.has_next_page = False 
        self.cur_data = data  
        return self.cur_data

    def keys_all(self):
        """
        Returns a list of string.
        """
        ks = []
        for k in self.cur_data:
            ks.append(k)

        if not self.has_next_page:
            return ks 
        
        i = 1
        while(True):
            dat, nxt = self.requester(i)
            for k in dat:
                ks.append(k)
                self.cur_data[k] = None 
            i += 1 
            self.has_next_page = nxt 
            self.cur_page = i 
            if len(dat) == 0 or not nxt:
                break 
        
        self.has_next_page = False 
        return ks
    
    def next(self):
        """
        Changes the current data stored in the pagination handler to the next page if there is one. 
        """
        if not self.has_next_page:
            return 

        self.cur_page += 1 
        dat, nxt = self.requester(self.cur_page)
        
        self.cur_data = dat
        self.has_next_page = nxt  

    def to_dataframe(self):
        """
        Transforms all data in PaginationHandler into pandas.DataFrame.
        """
        indices = []
        df_data = {}

        all_data = self.data_all()
        for i in all_data:
            indices.append(i)

            #turn entry from bytes to python dictionary 
            #to_dict = all_data[i].decode()
            #entry = literal_eval(to_dict.replace('null', 'None'))
            entry = parse_object(all_data[i])
            for key in entry: 
                if key not in df_data:
                    df_data[key] = [entry[key]]
                else:
                    df_data[key].append(entry[key])

        return pd.DataFrame(df_data, index=indices)

    def to_numpy_arrays(self):
        """
        Transforms all data in PaginationHandler into a list of numpy arrays. 
        """
        tot = [pickle.loads(i) for i in self]
    
        return np.concatenate(tuple(tot), axis=0) 

class GetPages():

    def __init__(self, client, keys, max_item_size):
        self.data_keys = keys
        self.max_item_size = max_item_size
        self.max_page_size = 2000000
        self.client = client 
        self.pag_handlers = []
        self.pag_index = 0 

    def __iter__(self):
        return self 

    def __next__(self):
        cur_pag_handler = self.pag_handlers[self.pag_index]

        try:
            return cur_pag_handler.__next__()
        except StopIteration:
            if self.pag_index < len(self.pag_handlers) - 1:
                self.pag_index += 1
                cur_pag_handler = self.pag_handlers[self.pag_index]
                return cur_pag_handler.__next__()
            
            raise StopIteration()


    def break_keys(self):
        key_groups = []
        items_per_page = self.max_page_size // self.max_item_size

        len_keys = len(self.data_keys)
        for i in range(0, len_keys+items_per_page, items_per_page):
            kg = self.data_keys[i-items_per_page:i]
            key_groups.append(kg)
        
        return key_groups[1:]

    def get_all(self, table_id, table_owner_id=None):
        key_groups = self.break_keys()

        for kg in key_groups:
            pag = self.client.get(table_id, kg, table_owner_id)
            self.pag_handlers.append(pag)

    def data_all(self):
        data = {}
        for pag in self.pag_handlers:
            pag_data = pag.data_all()
            data.update(pag_data)

        return data

    def keys_all(self):
        keys = []
        for pag in self.pag_handlers:
            pag_keys = pag.keys_all()
            keys += pag_keys

        return keys

    def return_pretty(self):
        for pag in self.pag_handlers:
            pag.return_pretty()

    def return_bytes(self):
        for pag in self.pag_handlers:
            pag.return_bytes()

    def data(self):
        cur_pag_handler = self.pag_handlers[self.pag_index]
        return cur_pag_handler.data()

    def keys(self):
        keys = []
        cur_pag_handler = self.pag_handlers[self.pag_index]
        for key in cur_pag_handler.data():
            keys.append(key)
        
        return keys
    
    def next(self):
        cur_pag_handler = self.pag_handlers[self.pag_index]

        if cur_pag_handler.has_next_page:
            cur_pag_handler.next()
        elif self.pag_index < len(self.pag_handlers) - 1:
                self.pag_index += 1 

    def to_dataframe(self):
        dfs = []

        for pag in self.pag_handlers:
            dfs.append(pag.to_dataframe())

        return pd.concat(dfs)

    def to_numpy_arrays(self):
        arrays = []

        for pag in self.pag_handlers:
            arrays.append(pag.to_numpy_arrays())

        return np.concatenate(tuple(arrays), axis=0)


def standard_pagination_handler(f):
    """
    Returns an object of class PaginationHandler.
    
    Parameters: 
        f: paginationRequester - func (int) -> (dict[string][byte], bool) 
    """
    ph = PaginationHandler(f)
    ph.next()
    return ph