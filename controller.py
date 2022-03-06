
import write_new_record
import judgement
import share_with_client
import record_information
import write_to_file as f

'''
This is the main controller for the program
Follow commands to enter games
'''

players = {
    1: "Alicia",
    2: "Bruce"
    }
judge = {
    3: "JUDGE_CLARENCE",
    }
moves = {
    1: "rock",
    2: "papper",
    3: "scissors"
    }
recordType = {
    1: "game",
    2: "judgement"
    }
'''


NOTE: Add way to control and find rounds
'''
def Add_move():
    print('1= Alicia or 2 = Bruce?')
    user_input1 = int(input())
    
    print('1 = Rock. 2 = papper or 3 = scissors?')
    user_input2 = int(input())

    record_type = 'game'
    metadata  = {}
    metadata ['round']= '1'
    data = {}
    data['move']= moves[user_input2]
    data['name']= players[user_input1]

    print(metadata , data)
    write_new_record.write_new_record(players[user_input1], record_type, metadata , data )

    return True

def JudgeRound():
    judgement.make_judgment()
    return True


def share_info():
    

    print('Record name?     1= Game  2=Judgement ')
    user_input1 = int(input())
    record_type = recordType[user_input1]

    print('Who is shareing?     1= Alicia  2=Bruce  3=Judge ')
    user_input1 = int(input())

    if user_input1 != 3 :
        client_name = players[user_input1]
    else:
        client_name = judge[user_input1]

    print('Who is getting access?     1= Alicia  2=Bruce  3=Judge ')
    user_input1 = int(input())

    if user_input1 != 3 :
        share_to_client_name = players[user_input1]
    else:
        share_to_client_name = judge[user_input1]


    share_with_client.share_with_client(record_type, client_name, share_to_client_name)
    return True  


def read_winner():
    
    new_list = f.read_file('judgement.json')
    if new_list == None:
        print("game.json is empty")
        return

    print('1= Alicia or 2 = Bruce?')
    user_input1 = int(input())
    client_name = players[user_input1]

    record = record_information.read_record_client_name( client_name, new_list[-1]['judge_clarence']  )
    print(record._Record__data['winner'])
    return True



def call5():
    return True
def call6():
    return True
def returnFalse():
    
    return False
def default():
    print("Returning to options")
    return True



switcher = {
   1: Add_move,
   2: JudgeRound,
   3: share_info,
   4: read_winner,
   5: call5,
   6: call6,
   7: returnFalse
   }

switcherInfo = {
   1: "Play round",
   2: "Judge round",
   3: "Share record",
   4: "Read Winner",
   5: "....",
   6: "....",
   7: "End"
   }



def switch():
    


    notDone = True
    
    while(notDone):

        print(switcherInfo)
        user_input_main = input()
        if user_input_main.strip().isdigit():
            notDone = switcher.get(int(user_input_main), default)()
       
    


switch()