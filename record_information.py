import e3db
import load_client



def read_record_client_name(client_name, record_id):
    client = load_client.load_client(client_name)
    new_record = client.read(record_id)
    record_serialized = new_record.to_json()
    print(f"{record_serialized['data']['winner']} is the winner ")


def read_record_client(client, record_id):
    new_record = client.read(record_id)
    print (f"Record: {new_record.data}")
    return new_record


def delete_record(client_name, record_id):
    client = load_client.load_client(client_name)
    new_record = client.read(record_id)
    record_serialized = new_record.to_json()

    #print(record_serialized)


    client.delete(record_id, record_serialized['meta']['version'])