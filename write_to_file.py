import json
from pathlib import Path


def read_file(filename):
    
    # NOTE ADD ERROR CHECKS
    # ADD MULTIPLE CALL LOCATION 
    read_from_file_test_null(filename)

    data = None

    with open(filename, "r") as file:
        try:
            data = json.load(file)
        except json.decoder.JSONDecodeError:
            pass
   
    return data


def write_only_to_file(filename, write_to_file):
    
    # NOTE ADD ERROR CHECKS
    # ADD MULTIPLE CALL LOCATION 
    filename = f'{filename}'

    read_from_file_test_null(filename)
    
    with open(filename, "w") as file:
        try:
            json.dump(write_to_file, file, indent=1)
        except json.decoder.JSONDecodeError:
            pass
   
    

def write_to_file(filename, write_to_file):
    
    # NOTE ADD ERROR CHECKS
    # ADD MULTIPLE CALL LOCATION 
    
    read_from_file_test_null(filename)
    
   
    entry = write_to_file
    data = []

    with open(filename, "r") as file:
        try:
            data = json.load(file)
        except json.decoder.JSONDecodeError:
            pass
   
    data.append(entry)
 
    with open(filename, "w") as file:
        json.dump(data, file, indent=1)



def write_to_env(new_user, configs):
    """
    Writes to text file for env vars to be copied over
    #configs['names'][0]['version']
    """

    filename = f'test.txt'

    read_from_file_test_null(filename)

    if not Path(filename):
        with open(filename, 'a+'): pass

    new_user = new_user.upper()
    
    write_to_file = {
        f'{new_user}_CLIENT_ID': configs['names'][0]['client_id'],
        f'{new_user}_API_KEY_ID': configs['names'][0]['api_key_id'],
        f'{new_user}_API_SECRET': configs['names'][0]['api_secret'],
        f'{new_user}_PUBLIC_KEY': configs['names'][0]['public_key'],
        f'{new_user}_PRIVATE_KEY': configs['names'][0]['private_key']
    }

    with open('test.txt', 'a+') as f:
        json.dump(write_to_file, f, indent=0 ,separators=('','='))
        





def write_new_user_to_file(new_user, configs):

    filename = f'local_user_list.json'

    read_from_file_test_null(filename)

    data= {}

    new_user = new_user.upper()
    with open('local_user_list.json', 'r') as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            pass
        
 
    write_to_file = {
            'user_name': new_user,
            'version': configs['names'][0]['version'],
            'client_id': configs['names'][0]['client_id'],
            'api_key_id': configs['names'][0]['api_key_id'],
            'api_secret': configs['names'][0]['api_secret'],
            'client_email': configs['names'][0]['client_email'],
            'public_key': configs['names'][0]['public_key'],
            'private_key': configs['names'][0]['private_key'],
            'public_signing_key': configs['names'][0]['public_signing_key'],
            'private_signing_key': configs['names'][0]['private_signing_key'],
            'api_url': configs['names'][0]['api_url']
        }
    
    if len(data) == 0:
        size = 0
        data['users'] = list()
        data['users'].append({})
       


    else:
        size =  len(data['users'][0].keys())
        
    data ['users'][0][size] = write_to_file
    

    with open('local_user_list.json', 'w') as f:
        json.dump(data, f, indent=4 ,separators=(',',':'))

   




def remove_json_indents():
    read_from_file_test_null('local_user_list.json')

    data = {}
    with open('local_user_list.json', 'r') as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            pass
    
    # Note to add format

    with open('no_indent_users.json', 'w') as f:
        json.dump(data, f, indent=0 ,separators=(',',':'))






def read_from_file_test_null(filename):
    myfile = Path(filename)
    myfile.touch(exist_ok =True)


