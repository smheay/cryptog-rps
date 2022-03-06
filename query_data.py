from pydoc import plain
import load_client


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
  

def query_record_name(client_name, record_name):
  """
  client_name String
  record_type list
  record_type list
  """
  client = load_client.load_client(client_name)

  plain_name = [("round","1")]

  record_type_name = []
  record_type_name.append(record_name)
  record_return = client.query(data=True, record_type=record_type_name, plain=  {'item_id': '1'} ,  writer='all')


  if(record_name == 'game'):
    for x in record_return:
      print (f'{x.data["name"]} = {x.data["move"]}')

  elif(record_name == 'judgement'):
    for x in record_return:
      print (f'{x.data["winner"]}')

  return record_return



records = query_record_name('Judge_Clarence', 'game')
#records = query_data_record('bruce', None, None)
#records = query_data_record_winner('Judge_Clarence', None, None)
#records = query_data_record_winner('Alicia', None, None)
#records = query_data_record_winner('Bruce', None, None)
#records = query_judgements_and_delete('Judge_Clarence')




