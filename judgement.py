import query_data as my_query
import record_information as my_read
import write_to_file as f
import load_client
import write_new_record 
import query_data

'''
Reads in from game.json
Checks for multiple games
Judges all games that are backed up
Sends result to cloud and local storage
Deletes games locally and in cloud


NOTE : Refactor needed
'''




def make_judgment():
    
    client = load_client.load_client('judge_Clarence')
    new_list = f.read_file('game.json')
    start_judgements = query_data.query_data_record_last_judged('judge_Clarence')

    #Note: Check if list in None
    if new_list == None:
        print("game.json is empty")
        return
    elif len(new_list) == 1:
        print("Not enough games to judge")
        return

 

    alicia = []
    bruce = []


    for x in new_list:
        if 'Alicia' in x:
            alicia.append(x)
        else:
            bruce.append(x)

    
    #NOTE: Check if alicia or bruce is None
    if(len(bruce) == 0 or len(alicia) == 0  ):
        print("One player has 0 games to judge")
        return

    size = min(len(alicia), len(bruce))

    send_list = []

    for x in range(size):
        if  start_judgements < int(alicia[x]['round']):
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


    record_list = []
    for x in range(len(send_list)):
        if 'Alicia' in send_list[x]:
            record = my_read.read_record_client(client, send_list[x]['Alicia'])
            record_list.append(record)
            decryptAlicia.append(record.data['move'])
        else:
            record = my_read.read_record_client(client, send_list[x]['Bruce'])
            decryptBruce.append(record.data['move'])

     


    for x in range(len(decryptBruce)):
        print(f'Alicia picked: {decryptAlicia[x]}         Bruce picked: {decryptBruce[x]}')  

        name_winner = list_of_outcomes[int(outcomesDic[decryptAlicia[x]])]  [int(outcomesDic[decryptBruce[x]])] 

        metadata  = {}
        metadata ['round']= record_list[x].meta.plain['round']
        record_type = 'judgement'
        data = {}
        data['winner']= name_winner

        write_new_record.write_new_record('judge_clarence', record_type, metadata , data )
        


    # After judgement sent delete cloud storage
    
    # for x in range(len(alicia)-1):
    #     my_read.delete_record( 'Alicia', alicia[x]['Alicia'],  bruce[x]['version'])
    # for x in range(len(bruce)-1):
    #     my_read.delete_record( 'Bruce',  bruce[x]['Bruce'],  bruce[x]['version'])


    # After judgement sent delete local storage
    
    if size == 1:
        f.write_only_to_file('game.json', new_list)

    
    send_to_file = []
    len_Alicia =  len(alicia)
    len_Bruce = len(bruce) 
    if len_Alicia < len_Bruce:
        for x in range(len_Alicia-1, len_Bruce):
            send_to_file.append(bruce[x])
        send_to_file.append(alicia[-1])
    else: 
        for x in range(len_Bruce-1, len_Alicia):
            send_to_file.append(alicia[x])
        send_to_file.append(bruce[-1])

    f.write_only_to_file('game.json', send_to_file)

