import load_client
import e3db
"""
loads and deletes records from client information
"""


def read_record_client_name(client_name, record_id):
    """
    client_name : String to load env var
    record_id : to read from client ID
    """
    client = load_client.load_client(client_name)
    # new_record = client.read(record_id)
    # record_serialized = new_record.to_json()
    # print(f"{record_serialized['data']['winner']} is the winner ")

    try:
        new_record = client.read(record_id)
    except:
        print (f'error loading records' )
    finally:
        return new_record



def read_record_client(client, record_id):
    """
    client :  e3db.Client 
    record_id : to read from client ID
    """
    new_record = None

    try:
        new_record = client.read(record_id)
    except:
        print (f'error loading records' )
    finally:
        return new_record

    
   


def delete_record(client_name, record_id, version):
    """
    client_name : String to load env var
    record_id : to read from client ID
    version: string of record version

    NOTE: Store version to prevent loading
    """
    client = load_client.load_client(client_name)
    print(f"Deleting Record: {record_id}")
    client.delete(record_id, version)




def delete_record_all(client_name, version, record_id):
    """
    client_name : String to load env var
    version: String of record version
    record_id : to read from client ID

    Note: Store version to prevent loading
    """
    client = load_client.load_client(client_name)
    print(f"Deleting Record: {record_id}")
    client.delete(record_id, version)



