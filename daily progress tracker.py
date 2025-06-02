from datetime import datetime

def add_habit(habits, habit):
    habits[habit] = datetime.now().date()
    return habits

def view_habits(habits):
    if not habits:
        print("No habits tracked.")
    else:
        for habit, date in habits.items():
            print(f"Habit: {habit}, Last Completed: {date}")

if __name__ == "__main__":
    habits = {}
    while True:
        print("\n1. Add Habit\n2. View Habits\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            habit = input("Enter your habit: ")
            habits = add_habit(habits, habit)
        elif choice == '2':
            view_habits(habits)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
