# task 6
def operations_on_dict(dict):
    best = -100
    worst = 102
    loser = ""
    topper = ""
    Totall_score = 0
    #iterate through dict it key value pair 
    for key, value in dict.items():
        Totall_score += value #increase the Totall_score
        # update the best and worst variable and update the loser and topper accoding to that
        if( best < value):
            topper = key
            best = value
        if( worst > value):
            worst = value
            loser = key
    print(f"Average score {Totall_score/len(dict)}")
    print(f"Highest {topper}")
    print(f"Lowest {loser}")

score = {}
# convert the score to dict
score = dict()
score["Mamun"] = 40
score["Rayhan"] = 92
score["Rafi"] = 95
operations_on_dict(score)

