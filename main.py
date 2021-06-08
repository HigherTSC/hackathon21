from datetime import datetime, date
import time

class GoalHandler():
    def __init__(self):
        self.goals={}
        self.today = date.today()

    def store_new_goal(self, start_date, end_date, name, amount_to_save):
        days_saving = (end_date - start_date).days
        daily_pledge = amount_to_save/days_saving
        daily_pledge = round(daily_pledge, 2)
        days = 0
        amount_saved = 0
        isComplete = False

        self.goals[name] = Goal(start_date, end_date, name, amount_saved, amount_to_save, daily_pledge, days, isComplete)
    
    def check_goal(self, name):
        current_goal = self.goals[name]
        if current_goal.isComplete == False:
            return f"The goal has not been complete yet. You have saved {current_goal.amount_saved} of {current_goal.amount_to_save} so far for a {name}."
        else:
            return f"Congrats! You successfully saved up {current_goal.amount_to_save} for a {name}."

    def add_to_goal(self, name, deposit):
        current_goal = self.goals[name]
        new_amount_saved = current_goal.amount_saved + deposit
        if current_goal.isComplete == True:
            message = "That goal is already complete, you can't add to it!"
        if new_amount_saved > current_goal.amount_to_save:
            message = f"Only {current_goal.amount_to_save} was added. You have now reached the goal! Go enjoy your {name}!"
            # i can't remember if python objects update inplace or not, so i wrote it out like this to be safe
            self.goals[name].isComplete = True
        elif new_amount_saved == current_goal.amount_to_save:
            message = f"{current_goal.amount_to_save} was added. You have now reached the goal! Go enjoy your {name}!"
            self.goals[name].isComplete = True
        else:
            self.goals[name].amount_saved += deposit # update amount saved
            days_saving = (current_goal.end_date - current_goal.start_date).days
            remaining_days = days_saving - current_goal.days
            self.goals[name].daily_pledge = (current_goal.amount_to_save - current_goal.amount_saved)/remaining_days
            message = f"{deposit} was added. You now have {current_goal.amount_to_save} left to save for your {name}."
        return message

    def get_goal(self, name):
        if name in self.goals.keys():
            return self.goals[name]
        else:
            return ValueError
    
    def get_goal_streak(self, name):
        if name in self.goals.keys():
            return today - self.goals[name].start_date
        else:
            return ValueError

    def get_max_streak(self):
        all_streak = []
        for name in self.goals.keys():
            all_streak.append(self.get_goal_streak(name))
        return max(all_streak)

    def clean_list(self):
        for name in self.goals.keys():
            if self.goals[name].isComplete == True:
                self.goals.pop(name)


class Goal():
    def __init__(self, start_date, end_date, name, amount_saved, amount_to_save, daily_pledge, days, isComplete):
        self.start_date = start_date
        self.end_date = end_date
        self.name = name
        self.amount_saved = amount_saved
        self.amount_to_save = amount_to_save
        self.daily_pledge = daily_pledge
        self.days = days
        self.isComplete = isComplete

class MilestoneHandler():
    def __init__(self, start_savings=1000):
        self.start_savings = start_savings
        # initialise with 3 basic milestones
        self.milestones = {"first_save": "Yay! You unlocked the first milestone for making your first savings: FIRST SAVE!",
                            "double_savings": "YOU'RE ON A ROLL! You unlocked the second milestone for doubling your savings: DOUBLE TROUBLE!",
                            "savings_veteran":"WOW! You're practically a savings veteran for getting the last milestone: 100,000 MILESTONE!"}
    
    def new_milestone(self, milestone_name, milestone_text):
        self.milestones[milestone_name] = milestone_text

    def check_milestones(self, savings):
        current_milestones = []
        if savings > start_savings:
            #get acheivement
            current_milestones.append(self.milestones["first_save"])
        if savings >= 2*start_savings:
            #get acheivement
            current_milestones.append(self.milestones["double_savings"])
        if savings >= 100000:
            #get acheivement
            current_milestones.append(self.milestones["savings_veteran"])
        if len(current_milestones) == 0:
            return ["No milestones achieved right now."]
        else:
            return current_milestones