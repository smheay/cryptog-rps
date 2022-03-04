import query_data as my_query
import record_information as my_read
import write_to_file as f
import load_client
import write_new_record 

'''
Reads in from game.json
Checks for multiple games
Judges all games that are backed up
Sends result to cloud and local storage
Deletes games locally and in cloud

Note : Refactor needed
'''
def make_judgment():
    
    client = load_client.load_client('judge_Clarence')
    new_list = f.read_file('game.json')

    #Note: Check if list in None
    if new_list == None:
        print("game.json is empty")
        return
    elif len(new_list) == 1:
        print("Not enough games to judge")
        return


    alicia = list()
    bruce = list()

    for x in new_list:
        for y,z in x.items():
            print(f"{y} : {z}")
            if(y == 'Alicia'):
                alicia.append(z)
            if(y == 'Bruce'):
                bruce.append(z)

    #Note: Check if alicia or bruce is None

    send_list = []

    size = min(len(alicia), len(bruce))


    
    for x in range(size):
        send_list.append(alicia[x])
        send_list.append(bruce[x])

    if len(alicia) < 1 or len(bruce) < 1:
        print("Not enough games to judge")
        print(f'{len(alicia) } {len(bruce)}')
        return



    list_of_outcomes = [
        ['Tie', 'Bruce', 'Alicia'],
        ['Alicia', 'Tie', 'Bruce'],
        ['Bruce', 'Alicia', 'Tie']
    ]
    outcomesDic = {
        "rock": '0',
        "papper": '1',
        "scissors": '2'
    }

    decryptAlicia = []
    decryptBruce = []

    print(send_list)
    for x in range(len(send_list)):
        record = my_read.read_record_client(client, send_list[x])

        if record.data['name'].upper() == 'ALICIA':
            decryptAlicia.append(record.data['move'])
        else:
            decryptBruce.append(record.data['move'])

    



    for x in range(len(decryptBruce)):
        print(f'''The Alicia picked: {decryptAlicia[x]}    Bruce: {decryptBruce[x]} 
            \n{list_of_outcomes[int(outcomesDic[decryptAlicia[x]])]  [int(outcomesDic[decryptBruce[x]])]   }
        ''')  
        name_winner = list_of_outcomes[int(outcomesDic[decryptAlicia[x]])]  [int(outcomesDic[decryptBruce[x]])] 

        metadata  = {}
        metadata ['round']= str(x)
        record_type = 'judgement'
        data = {}
        data['winner']= name_winner

        write_new_record.write_new_record('judge_clarence', record_type, metadata , data )
        

    # After judgement sent delete cloud storage
    for x in range(size):
        my_read.delete_record( 'alicia', alicia[x])
        my_read.delete_record( 'bruce',  bruce[x])

    # After judgement sent delete local storage
    send_to_file = {}
    len_Alicia =  len(alicia)
    len_Bruce = len(bruce) 
    if len_Alicia < len_Bruce:
        for x in range(len_Alicia, len_Bruce):
            send_to_file['Bruce'] = bruce[x]
    else: 
        for x in range(len_Bruce, len_Alicia):
            send_to_file['Alicia'] = alicia[x]

    if len(send_to_file) == 0:
        send_to_file = []
    else:
        send_to_file = [send_to_file]
    
    f.write_only_to_file('game.json', send_to_file)

