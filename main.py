from datetime import date

today = date.today()
start_date = date.fromisocalendar(2020, 24, 3)
end_date = date.fromisocalendar(2021, 24, 3)

goal_list = {}
goal_index = 0


def store_goal(start_date, end_date, amount_to_save, daily_pledge):
    global goal_index
    goal_list.update({goal_index: [start_date, end_date, amount_to_save, daily_pledge]})
    goal_index = goal_index + 1

store_goal(start_date,end_date,1000,10)
print(repr(goal_list[0]))
