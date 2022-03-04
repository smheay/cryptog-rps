import e3db
import load_client



def read_record_client_name(client_name, record_id):
    client = load_client.load_client(client_name)
    new_record = client.read(record_id)
    print(type(new_record.data))
    print (f"Record: {new_record.data}")
    return new_record


def read_record_client(client, record_id):
    new_record = client.read(record_id)
    #print(new_record.status_code)
    print(type(new_record.data))
    print (f"Record: {new_record.data}")
    return new_record


def delete_record(client_name, record_id):
    client = load_client.load_client(client_name)
    new_record = client.read(record_id)
    record_serialized = new_record.to_json()
    print(record_serialized)


    client.delete(record_id, record_serialized['meta']['version'])