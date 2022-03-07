from pydoc import plain
import load_client
import record_information


def query_data_record(client_name,  record_ids=[], record_type_in=[]):
  """
  client_name String
  record_type list
  record_type list
  """
  client = load_client.load_client(client_name)
  sentThis = ['65739e53-9b1d-4cd0-a084-7ee86300f29a', '15646350-249f-469c-adbc-90d1435c506e']

  record_return = client.query( data=True, record=record_ids , writer='all')
  return record_return
  

def query_data_record_round(client_name, record_name):
  """
  client_name String
  record_type list
  """
  client = load_client.load_client(client_name)
  record_type_name = []
  record_type_name.append(record_name)

  record_return = client.query( data=True, record_type=record_type_name, writer=[load_client.return_client_id(client_name)])
  size = len(record_return)

  if size != 0:
    last_game = record_return._QueryResult__records[size-1]._Record__meta._Meta__plain['round']
    return last_game
  
  return 0



def query_data_record_round_winner(client_name,  round_number):
  """
  client_name String
  """
  client = load_client.load_client(client_name)

  if round_number < 1:
    return 'No games'

  record_return = client.query( data=True, record_type=['judgement'], writer='all')
  size = len(record_return)

  if size != 0 and round_number-1 < size:
    last_game = record_return._QueryResult__records[round_number-1].data['winner']
    print (last_game)
    return last_game
  
  return 'No games'



def query_data_record_last_judged(client_name):
  """
  client_name String
  """
  client = load_client.load_client(client_name)


  record_return = client.query( data=True, record_type=['judgement'], writer='all')
  size = len(record_return)

  if size != 0:
    last_game = record_return._QueryResult__records[-1]._Record__meta.plain['round']
    return int(last_game)
  
  return 0


def query_delete_record_all(client_name):
  """
  client_name String
  record_type list
  record_type list
  """
  client = load_client.load_client(client_name)
  client_id = load_client.return_client_id(client_name)
  record_return = client.query(data=True, writer=[client_id])

  for record in record_return:
    # record_id = (record.meta.record_id)
    #print(record.meta.user_id)
    record_information.delete_record_all(client_name, record.meta.version, record.meta.record_id)

  return record_return



# query_delete_record_all('Judge_Clarence')
# query_delete_record_all('Bruce')
# query_delete_record_all('Alicia')




# query_data_record_last_judged('Judge_Clarence')
#query_data_record_round_winner('Bruce', 1)

#query_data_record_round('Bruce', 'game')
#records = query_record_name('Judge_Clarence', 'game')
#records = query_data_record('bruce', None, None)
#records = query_data_record_winner('Judge_Clarence', None, None)
#records = query_data_record_winner('Alicia', None, None)
#records = query_data_record_winner('Bruce', None, None)
#records = query_judgements_and_delete('Judge_Clarence')



    

  # if(record_name == 'game'):
  #   for x in record_return:
  #     print (f'{x.data["name"]} = {x.data["move"]}')

  # elif(record_name == 'judgement'):
  #   for x in record_return:
  #     print (f'{x.data["winner"]}')

