import load_client
import write_to_file as f


def write_new_record(name, record_type, metadata, data):
    """
    name: String
    record_type: record name
    metadata: None or dict string:string
    data: dict string:string
    """

    # load client
    client = load_client.load_client(name)

    #Send information to write
    if metadata is None:
        record = client.write(record_type, data)
    else:
        record = client.write(record_type, data, metadata)
    
    print (f'Wrote record {record.meta.record_id}')
    print( record.meta.version)
    #print (f'{name} summitted {data}')
    
    #Save local files 
    send_to_file = {}
    send_to_file[name]= str(record.meta.record_id )
    send_to_file['version']= str(record.meta.version )
    file_name= record_type+'.json'

    f.write_to_file(file_name, send_to_file )
    f.write_to_file('records.json', send_to_file )

    
    return