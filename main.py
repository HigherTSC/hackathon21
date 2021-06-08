from datetime import datetime
from datetime import date
import time

#DATE DATASET
start_date_input1 = '2020-06-07'
start_date1 = datetime.strptime(start_date_input1, "%Y-%m-%d")
end_date_input1 = '2020-06-30'
end_date1 = datetime.strptime(end_date_input1, "%Y-%m-%d")
start_date_input2 = '2020-06-07'
start_date2 = datetime.strptime(start_date_input2, "%Y-%m-%d")
end_date_input2 = '2020-12-15'
end_date2 = datetime.strptime(end_date_input2, "%Y-%m-%d")

today = date.today()
goal_list = {}
def store_new_goal(start_date, end_date, name, amount_to_save):

    #calculate daily pledge:
    days_saving = (end_date - start_date).days
    daily_pledge = amount_to_save/days_saving
    daily_pledge = round(daily_pledge, 2)
    days = 0
    amount_saved = 0
    isComplete = False

    #update goal list:
    goal_list.update({name: [start_date, end_date, amount_saved, amount_to_save, daily_pledge, days, isComplete]})

#goal_list[0]-->startdate
#goal_list[1]-->enddate
#goal_list[2]-->amountsaved
#goal_list[3]-->amounttosave
#goal_list[4]-->dailypledge
#goal_list[5]-->days
#goal_list[6]-->siComplete

def check_goal(name):
    global goal_list
    if goal_list[name][6] == False:
        return False
    else:
        #send acheivement
        print('Congrats! You successfully saved up ',goal_list[name][3],' for a ',name,'.')
        return True

def add_to_goal(name, deposit):
    global goal_list
    if (goal_list[name][2] + deposit) > goal_list[name][3]:
        return ValueError
    elif (goal_list[name][2] + deposit) == goal_list[name][3]:
        goal_list[name][6] = True
    else:
        goal_list[name][2] += deposit        #update amount saved
        days_saving = (goal_list[name][1] - goal_list[name][0]).days
        #alternatively, reaminingdays = (end date - today).days
        remaining_days = days_saving - goal_list[name][5]
        #update daily pledge
        goal_list[name][4] = (goal_list[name][3] - goal_list[name][2])/remaining_days
################MILESTONES##########################

#milestone feature
#assume 3 basic milestones
savings = 1000
start_savings = savings
milestones = ["Yay! You unlocked the first milestone \nfor making your first savings: FIRST SAVE!\n",
              "YOU'RE ON A ROLL! You unlocked the second milestone \nfor doubling your savings: DOUBLE TROUBLE!\n",
              "WOW! You're practically a savings veteran \nfor getting the last milestone: 100,000 MILESTONE!\n"]

def check_milestones(savings):
    if savings > start_savings:
        #get acheivement
        print(milestones[0])
    elif savings >= 2*start_savings:
        #get acheivement
        print(milestones[1])
    elif savings >= 100000:
        #get acheivement
        print(milestones[2])

########STREAKS####################################

#streak = get_goal_streak//get_max_streak
#SIMPLY DISPLAY THIS VALUE AS THE STREAK
def get_goal_streak(name):
    global goal_list
    current_streak = today - goal_list[name][0]
    return current_streak

def get_max_streak():
    global goal_list
    all_streak = []
    for name in goal_list.keys():
        all_streak.append((today - goal_list[name][0]).days)
    return max(all_streak)

#################MAINLOOP FOR PROGRESS BARS##################

for name in goal_list.keys():
    if (goal_list[name][2]) >= goal_list[name][3]:
        goal_list[name][6] = True
        savings += goal_list[name][2]
        goal_list.pop(name)
    else:
        days_saving = (goal_list[name][1] - goal_list[name][0]).days
        for x in range(0, days_saving + 1):
            goal_list[name][2] += goal_list[name][4]
            if (goal_list[name][2]) >= goal_list[name][3]:
                goal_list[name][6] = True
                savings += goal_list[name][2]
                goal_list.pop(name)
            time.sleep(86400)#loops every 24 hours
