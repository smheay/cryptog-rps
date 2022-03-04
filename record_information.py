import load_client
"""
loads and deletes records from client information
"""


def read_record_client_name(client_name, record_id):
    """
    client_name : String to load env var
    record_id : to read from client ID
    """
    client = load_client.load_client(client_name)
    new_record = client.read(record_id)
    record_serialized = new_record.to_json()
    print(f"{record_serialized['data']['winner']} is the winner ")


def read_record_client(client, record_id):
    """
    client_name :  e3db.Client 
    record_id : to read from client ID
    """
    new_record = client.read(record_id)
    print (f"Record: {new_record.data}")
    return new_record


def delete_record(client_name, record_id):
    """
    client_name : String to load env var
    record_id : to read from client ID

    Note: Store version to prevent loading
    """
    client = load_client.load_client(client_name)
    new_record = client.read(record_id)
    record_serialized = new_record.to_json()
    #print(record_serialized)
    client.delete(record_id, record_serialized['meta']['version'])