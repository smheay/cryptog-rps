import query_data
def judgement_from_query():
    """
    
    """
    client_name = 'JUDGE_CLARENCE'
    record_name = 'game'

    records = query_data.query_record_name(client_name, record_name)

    alicia_count = []
    bruce_count = []

    for x in records:
        if(x.data["name"].lower() == 'alicia'):
            alicia_count.append({x.data["name"] : x.data["move"]})
        else:
            bruce_count.append({x.data["name"] : x.data["move"]})

    minimum_games = min(bruce_count, alicia_count)

    if(bruce_count == 0 or alicia_count == 0):
        print(f"Not enough games or each player")
        return 

    for x in range(minimum_games):
        print(records[x]['data']["name"])


judgement_from_query()