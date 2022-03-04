import load_client

#NOTE Error if shared a shared record type multiple times


def share_with_client(record_type, client_name, share_to_client_name):
  client = load_client.load_client(client_name)
  share_to_client_ID = load_client.return_client_id(share_to_client_name)
  client.share(record_type, share_to_client_ID)



def unshare_with_client(record_type, client_name, unshare_to_client_name):
  client = load_client.load_client(client_name)
  unshare_to_client_ID = load_client.return_client_id(unshare_to_client_name)
  client.revoke(record_type, unshare_to_client_ID)




#share_with_client('Bruce','Judge_Clarence')
#unshare_with_client('Bruce', 'Judge_Clarence')
#share_with_client('judgement','Judge_Clarence','Bruce')
#share_with_client('judgement','Judge_Clarence','Alicia')