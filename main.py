from datetime import date, timedelta

today = date.today()
start_date = date.fromisocalendar(2020, 24, 3)

goal_list = {}


def store_goal(name, start_date, amount_to_save, daily_pledge):
    end_date = start_date + timedelta(days=round(amount_to_save / daily_pledge))
    goal_list.update({name: [start_date, end_date, amount_to_save, daily_pledge]})


def end_streak(goal):
    global goal_list
    del goal_list[goal]

def streak(goal):
    global goal_list
    current_streak = today - goal_list[goal][0]
    return current_streak

store_goal("car",start_date, 1000, 10)
store_goal("vacation", start_date, 1000, 10)
end_streak("car")
print(repr(goal_list["vacation"]))
print(streak("vacation"))
