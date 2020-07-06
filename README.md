# python-zb-client
Python3 ZB client

## Installation 
Run the following to install: 
```python
pip install zbpy 
```

## External dependencies and easiest ways to satisfy them 
### Note: a C compiler is not required when running zbpy on Windows. However, all requests made with ecdsa on Windows will be slightly slower when compared to other operating systems.
1. - OSX -> Run 'brew install gcc'
2. - Linux -> Run 'apt-get install libgmp3-dev'
3. - Centos -> Run 'yum install gmp gmp-devel gmp-status' 


## Usage 

## Creating an account
If you don't already have an account there are two ways to make one using this module. If you are using Jupyter notebooks simply run the following:  
Note: due to the depreciation of certain functions in IPython, creating an account using in a Jupyter notebook won't work with Python 3.8. 
```python
from zbpy import client 

%createaccount
```
Otherwise in the python interactive shell run the function new_account_interactive() like so: 
```python
from zbpy import util

util.new_account_interactive()
```
Answer the prompts that will appear and if the account is created successfully three files will be created in your current directory. One will contain your private key, another will contain your public key, and the third will contain both keys along with your user id. Your user id will be used to login (shown below).

## Test your installation 
To test that everything has installed correctly run the test_zbpy method from zbpy.util like so in either Jupyter notebooks or the Python interactive shell: 
```python
form zbpy import util 

util.test_zbpy()
```


## Creating a Zetabase client 
```python
from zbpy import client 

client = client.ZetabaseClient('YOUR USER ID')
```
## Connecting your client to Zetabase
```python
client.connect()
```
## If you would like to use jwt security for all requests run the following code
```python
client.set_id_password('YOUR USERNAME', 'YOUR PASSWORD')
client.auth_login_jwt()
```

## If you would rather use ecdsa security for all requests import your private and public key from the file generated when you created an account
```python
priv_key = client.import_key('FILEPATH TO PRIVATE KEY', public=False)
pub_key = client.import_key('FILEPATH TO PUBLIC KEY', public=True)

client.set_id_key(priv_key, pub_key)
```

## Creating Tables
#### There are two methods to create tables using zbpy. There are two optional parameters with both of the methods: 
1. perms: used to specify the permissions of the table (can also be added to an existing table using the add_perm() method)
2.  allow_jwt: if true, allows data to be put into the table using jwt security.  

If you are creating a table to hold a pandas dataframe the easiest way is to use the following function. This will create a table with indexed fields that match the names and types of the columns of your dataframe and then insert your dataframe into the table.
```python
client.put_dataframe_new_table('TABLE ID', YOUR DATAFRAME, 'YOUR DF KEY')
```
If you would like a subset of the DataFrame's columns to be turned into indexed fields in the table use the 'specify_fields' parameter. 
```python
client.put_dataframe_new_table('Table ID', YOUR DATAFRAME, 'YOUR DF KEY', specify_fields=['age', 'height'])
```
#### The other way of creating tables involves specifying the table type and indexed fields yourself. 
```python 
from zbpy.indexedfieldentity import IndexedField
from zbpy import zb_protocol_pb2 as zb

index_age = IndexedField('age', zb.QueryOrdering.INTEGRAL_NUMBERS)
index_height = IndexedField('heigh', zb.QueryOrdering.REAL_NUMBERS)

client.create_table('TABLE ID', zb.TableDataFormat.JSON, [index_age, index_height], [OPTIONAL PERMS], allow_jwt=True)
```

## Creating permissions and adding them to existing tables
```python
from zbpy.permissionentity import PermEntry
from zbpy import zb_protocol_pb2 as zb

perm = PermEntry(zb.PermissionLevel.READ, zb.PermissionAudienceType.PUBLIC, '')

client.add_permission('TABLE ID', perm)
```

## Retrieving data and Pagination
When using the functions list_keys(), get(), and query(), the data is returning as a PaginationHandler. A Pagination handler can be iteration over or turned into pandas DataFrames using the to_dataframe() method (both demonstrated below).

## Retrieving keys from table
```python
list_keys = client.list_keys('TABLE ID')
keys = [key for key in list_keys]
```

## Retrieving data by key 
```python
result = client.get('TABLE ID', ['KEY 1', 'KEY 2', 'KEY 3', 'etc.'])

dataframe = result.to_dataframe()
```

### If you would like your json to return as python dictionaries when iterated over use the return_pretty() method like so:
```python
result = client.get('TABLE ID', ['KEY 1', 'KEY 2', 'KEY 3', 'etc.'])
result.return_pretty()

for i in result:
    print(i)
```

## Retrieving data by query 
To query data from Zetabase utilize, Field objects as well as indexed fields in tables. The example below assumes that a table exists with indexed fields 'age' and 'name'. Queries use '&' and '|' for 'and' and 'or' operators. 
### **IMPORTANT**: when creating queries the field must always come before the value, as shown below. 
```python
from zbpy import cleanqueries

age = Field('age')
name = Field('name')

query = ((age == 19) | ((age > 25) & (age <= 27))) & (name == 'Austin')
result = client.query('TABLE ID', query)

for i in result:
    print(i)
```

## Inserting data 
To insert a pandas dataframe into an existing table use the put_dataframe() method. To differentiate between different dataframes within a single table use the df_key parameter. Because uuids are used as subkeys for rows of a dataframe when entered into Zetabase, dataframes can be appended to one another by simply using the same df_key within a table. 
```python
client.put_dataframe('TABLE ID', YOUR DATAFRAME, 'YOUR DF KEY')
```
To insert individual pieces of data use the put_data() method and to insert multiple pieces of data at a time use the put_multi() method. 
#### **IMPORTANT**: For optimal speed use jwt instead of ecdsa when using multiput. 

```python
client.put_data('TABLE ID', 'DATA KEY', DATA AS BYTES)
client.put_multi('TABLE ID', ['KEY 1', 'KEY 2', 'KEY 3', 'etc.'], [DATA1 AS BYTES, DATA2 AS BYTES, etc.])
```
