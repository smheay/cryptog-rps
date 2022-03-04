
import write_new_record
import judgement

players = {
    1: "Alicia",
    2: "Bruce"
    }
moves = {
    1: "rock",
    2: "papper",
    3: "scissors"
    }


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


def call3():
    return True  


def call4():
    return True
def call5():
    return True
def call6():
    return True
def returnFalse():
    return False
def default():
    return False

switcher = {
   1: Add_move,
   2: JudgeRound,
   3: call3,
   4: call4,
   5: call5,
   6: call6,
   7: returnFalse
   }

switcherInfo = {
   1: "Play round",
   2: "Judge round",
   3: "....",
   4: "....",
   5: "....",
   6: "....",
   7: "End"
   }



def switch():
    


    notDone = True
    
    while(notDone):

        print(switcherInfo)
        user_input = int(input())
        notDone = switcher.get(user_input, False)()
    


switch()