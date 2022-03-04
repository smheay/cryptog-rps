import sys
import load_client
import share_with_client
import write_to_file as f

"""" 
argv[1] = Record_type 
argv[2] = Meta
argv[3] = Data
3 ++    = more data
"""

# py write_new_record.py game none=none name=Bruce move=papper round=1


if len(sys.argv) <= 3:
    exit

# Checking if metadata is sent
meta = sys.argv[2].split('=')
metadata = None
if meta[1] != 'none':
    metadata = {}
    metadata[meta[0]] = meta[1]


#Name Should be spilt to load client information
## NOTE did this twice
name = sys.argv[3].split('=')
client = load_client.load_client(name[1])


#Get record name
record_type = sys.argv[1]

#Split multiple data entries into dict
data = {}
x = range(3, len(sys.argv))
for n in x:
  info = sys.argv[n].split('=')
  data[info[0]] = info[1]

#Send information to write
if metadata is None:
    record = client.write(record_type, data)
else:
    record = client.write(record_type, data, metadata)



#Save local files 
send_to_file = {}
send_to_file[name[1].capitalize()] = str(record.meta.record_id )
f.write_to_file('records', send_to_file )

name[1] = name[1].lower()

if name[1] == 'judge_clarence':
    share_with_client.share_with_client(name[1], 'Alicia')
    share_with_client.share_with_client(name[1], 'Bruce')

else:
    share_with_client.share_with_client(name[1], 'judge_clarence')


print (f'Wrote record {record.meta.record_id}')
print (f'{name[1]} summitted {data}')

