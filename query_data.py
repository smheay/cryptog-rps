import load_client

"""
        Parameters
        ----------
        data: bool
            Whether to include the record's data when returned in the query.
            Optional.

        writer: list
            List of writer ids to filter on.
            Optional.

        record: list
            List of record ids to filter on.
            Optional.

        record_type: list
            List of record types to filter on.
            Optional.

        plain: dict
            JSON-style Plaintext meta data query object to use for matching
            against record plaintext meta data fields.
            Optional.

        page_size : int
            How many records to return per query. Can be used in conjunction
            with last_index to read records in 'batches'.

        last_index : int
            Retrieve records from this index onwards. Starts at 0 to return all.
            Useful for retrieving records in 'batches'. Exposed to user through
            the QueryResult.after_index method.

        Returns
        -------
        e3db.QueryResult
            Iterable object that returns decrypted e3db.Record objects.
        """

# data	false	Bool	Flag to include data in records returned
# writer	false	String or Array	Records written by a single writer or list of writers
# record	false	String or Array	Select single record or list of records
# type	false	String or Array	Select records of a type or types
# metadata	false	Array	Associative array of plaintext meta to use as filter
# pageSize	false	Number	Page size returned by response

def query_data_record(client_name,  record_ids=[], record_type_in=[]):
  """
  client_name String
  record_type list
  record_type list
  """

  client = load_client.load_client(client_name)
  sentThis = ['65739e53-9b1d-4cd0-a084-7ee86300f29a', '15646350-249f-469c-adbc-90d1435c506e']

  record_type_name = ['game']
  #sentThis = '65739e53-9b1d-4cd0-a084-7ee86300f29a'


  #record_return = client.query(data=True, record_type=record_type_name, writer='all')
  record_return = client.query( data=True, record=sentThis, writer='all')

  # for x in record_return:
  #   print (f'{x.data["name"]} = {x.data["move"]}')

  return record_return
  

def query_record_name(client_name, record_name):
  """
  client_name String
  record_type list
  record_type list
  """

  client = load_client.load_client(client_name)
  record_type_name = []
  record_type_name.append(record_name)
  record_return = client.query(data=True, record_type=record_type_name, writer='all')

  if(record_name == 'game'):
    for x in record_return:
      print (f'{x.data["name"]} = {x.data["move"]}')

  elif(record_name == 'judgement'):
    for x in record_return:
      print (f'{x.data["winner"]}')


  return record_return


def query_data_record_winner(client_name,  record_ids=[], record_type_in=[]):
  """
  client_name String
  record_type list
  record_type list
  """
  client = load_client.load_client(client_name)

  record_type_name = ['judgement']
  #sentThis = '65739e53-9b1d-4cd0-a084-7ee86300f29a'

  
  record_return = client.query(record_type=record_type_name, writer='all')
  #record_return = client.query( plain=u'{ "round":"1"}', writer='all')
  print(record_return.__len__())
    
  print(record_return.meta['round'])

  for x in record_return:
    print (f'The winner is:: {x.data["winner"]} ')

  return record_return



def query_judgements_and_delete(client_name):
  """
  client_name String
  record_type list
  record_type list
  """
  client = load_client.load_client(client_name)

  record_type_name = ['judgement']
  
  record_return = client.query(record_type=record_type_name, writer='all')
  print(record_return.__len__())

  for x in record_return:
    print (f'The winner is:: {x.data["winner"]} ')
    print (f'The winner is:: {x.meta["round"]} ')

  return record_return





#records = query_record_name('Judge_Clarence', 'judgement')
#records = query_data_record('bruce', None, None)
#records = query_data_record_winner('Judge_Clarence', None, None)
#records = query_data_record_winner('Alicia', None, None)
#records = query_data_record_winner('Bruce', None, None)
#records = query_judgements_and_delete('Judge_Clarence')




