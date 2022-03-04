import e3db
import sys
import write_to_file as f

from os import environ as env
from dotenv import load_dotenv

load_dotenv()

'''
Creates new users and adds key to test.txt to copy env vars and saves json of the clients made 
to local_user_list.json
'''

# NOTE: ADD CHECK FOR MULTIPLE USERS 

if len(sys.argv) == 2:
    exit

token = env['API_TOKEN']
client_name = sys.argv[1]

public_key, private_key = e3db.Client.generate_keypair()

# Register your client
client_info = e3db.Client.register(token, client_name, public_key)

config = e3db.Config(
    client_info.client_id,
    client_info.api_key_id,
    client_info.api_secret,
    public_key,
    private_key
)

# To save this Configuration to disk, do the following:
#config.write()


configs = config.__call__()
## Fixing uuid error in configs.client id returned as function call
item = str(configs['client_id'])
#newString = item[18:-1]
configs['client_id'] = item
#After converting to string is why it is that way in source to sanitize errors like uuid call


##Set up file format
list1 = []
list1.append(configs)
dic2 = {}
dic2['names'] = list1
dic2['names'].append(configs)

f.write_to_env(client_name, dic2)
f.write_new_user_to_file(client_name, dic2)

