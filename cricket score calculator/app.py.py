# import required 
# from collections import deque
import pandas as pd
# required variables
# balls=6
team_dhurandar=["abc","def"]
team_sikandar=["ghi","jkl"]
over=[]
striker=[]
non_striker=[]
bowler=[]

match_types=["t20","odi","test"]
tournaments=["IPL","world cup odi","t20 world cup ","champions trophy","asia cup"]
recognisations=["international","national","state","institute","club"]
gender=["men","women"]

ball_types=["normal","wide","noball","dismiss"]
# balls=[]

# normal match basic logics
def over_inputs():
    # global ball_type,run
    ball_type=input("Enter the ball type [normal, wide, noball, dismiss] : ")
    wicket=input("wicket taken? (y/n)")
    if wicket=="n":
        run=int(input("enter runs: "))
    elif wicket=="y":
        out_logic(wicket)
    return ball_type,run,wicket



def batsman_logic(balltype,run,wicket):
    # when striker hits odd run, non striker becomes striker
    # when over completes striker changes
    # when any batsman gets out new batsman replaced with the respected striking position 
    batsman_run=0
    striker=["plr1",batsman_run]
    non_striker=""
    if balltype=="wide":
        pass
    elif balltype=="normal" and run==1:
        striker[1]+=run
        striker=""
    print("")
def out_logic(wicket):
    if wicket=="y":
        print("hi")

# khichdi in an over
def an_over(batting_team,fielding_team):
    # updating normal scores of an over
    ball_count=6
    # lists and variables for normal scores of an over
    runs_in_over=[]
    ball_types_in_over=[]
    wickets=[]

    # lists and variables for extra scores of an over
    extra_ball_index=[]

    extra_runs_in_over=[]
    extra_ball_types_in_over=[]
    # extra_runs=[]
    batsman=batting_team[1]
    # run a loop for an over 
    for ball in range(ball_count):
        

        # take inputs : type of ball and runs 
        ball_type,run,wicket=over_inputs()
        # conditions of deliveries in an over
        # when its a straight free hit alarm
        if ball_type == "noball":
            print("free hit")
            wicket=False
        # when its a wide or invalids
        def invalid():
            extra_ball_index.append(ball)
            print("Extra Ball:")
            # take user input for extras and save in extras dataframe
            extra_ball_type,extra_run,wicket_in_extra=over_inputs() # input of extras taken 

            # storing input of extras in respected lists
            extra_ball_types_in_over.append(extra_ball_type) 
            extra_runs_in_over.append(extra_run)
            wickets.append(wicket_in_extra)
            # if extras also needs extras condition
            if extra_ball_type=="wide" or extra_ball_type=="noball":
                extra_run+=1
                invalid()
            return extra_ball_type ,extra_run, wicket_in_extra

        if ball_type == "wide" or ball_type == "noball":
            run+=1
            extra_ball_type,extra_run,wicket_in_extra=invalid()
        elif (ball_type=="n" or ball_type=="normal"):
            if wicket=="n":
                runs_in_over.append(run)
            elif wicket=="y":
                print("batsman out")
        

        # storing input of an over in respected lists
        ball_types_in_over.append(ball_type)
        wickets.append(wicket)
        # batsman_logic(striker,nonstriker,ball_type,run,wicket)

    over=pd.DataFrame(zip(runs_in_over,ball_types_in_over,wickets))
    extras=pd.DataFrame(zip(extra_ball_index,extra_ball_types_in_over,extra_runs_in_over,wickets))
    over_score=0
    for i in range(len(runs_in_over)):
        over_score=runs_in_over[i]+over_score
        print(f" {i} {over_score}")
    # insert extras into the over
    # over.insert()

    print(f"fair overs{over}")
    print(f"extras{extras}")
    return over_score
# ^^--- an_over()

# match basic logics
# types of tournaments and their logics
def innings(noi,no_o_overs,batting,fielding):
    print(f"Starting of {noi} inning")
    # no_o_overs=
    # if first_in_sc!=0: 
    #     target=first_in_sc+1
    print(f"Now batting: {batting} team \nNow bowling {fielding} team")
    # if noi=="1st":
    #     print("")
    # elif noi=="2nd":
    #     pass
    combined_score=0
    print(f"match started : total overs ={no_o_overs}")
    for over_count in range(no_o_overs):
        over_score=an_over(batting,fielding)
        # print(f"{}")
        combined_score+=over_score
        print(f"{over_count+1} overs completed current over's score is {over_score} and overal score is {combined_score}\n")
    print(f"{noi} inning completed")
    
    print(f"total score of {noi} inning is {combined_score}.")
    return combined_score

def a_match(total_overs):
    if rules=="gully":
        print("Gully mode")
    #  first innings
    team_1b=teams[0]
    team_1f=teams[1]
    print(f"This {recognisation} {tournament} {match_type} tournament is between {teams[0]} and {teams[1]} live from {stadium}")
    print(f"this team has won the toss and choose to bat/ball.")
    noi="1st"
    first_in_sc=innings(noi,total_overs,team_1b,team_1f)
    target=first_in_sc+1
    
    # second innings
    team_2b=team_1f
    team_2f=team_1b
    noi="2nd"
    # innings(noi,total_overs,team_2b,team_2f,score)
    second_in_sc=innings(noi,total_overs,team_2b,team_2f)
    if second_in_sc>=target:
        print(f"Match completed {team_2b} won the match")
    else:
        print(f"Match completed {team_2f} won the match")

# ==================================================================================================================================================
match_type="t20"
tournament="IPL"
recognisation="international"
stadium="melborne"
# gather team infos
team_1=team_dhurandar.copy()
team_2=team_sikandar.copy()
teams=[team_1,team_2]

# main part / func calling part / display part
print("ipl score update")

# input part :
# select tournament type
print("Available Tournaments : t20 , 2over , my")
tournament_type=input("Enter tournament type: ")

if tournament_type=="t20":
    total_overs=20
elif tournament_type=="2over":
    total_overs=2
elif tournament_type=="my":
    total_overs=1
    rules="gully"

else:
    print(f"No Tournament named'{tournament_type}' found ")

a_match(total_overs)

# output part



