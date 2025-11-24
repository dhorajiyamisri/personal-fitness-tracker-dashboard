import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

CSV_FILE = "fitness_activities.csv"

# 1️ Check CSV exists
if not os.path.exists(CSV_FILE):
    print(f"{CSV_FILE} not found! Please create it with your fitness data.")
    exit()

class FitnessTracker:

    def __init__(self):
        self.df = pd.read_csv(CSV_FILE)
        
    # METHOD 1: Log New Activity
   
    def log_activity(self, date, activity_type, duration, calories):
        """
        Appends new activity to the CSV file.
        """
        new_row = {
            "Date": date,
            "Activity Type": activity_type,
            "Duration (Minutes)": duration,
            "Calories Burned": calories
        }

        self.df.loc[len(self.df)] = new_row
        self.df.to_csv(CSV_FILE, index=False)
        print("Activity logged successfully!")

    # METHOD 2: Calculate Metrics
   
    def calculate_metrics(self):
        """
        Returns average duration, average calories,
        total time, and total calories.
        """
        metrics = {
            "Average Duration": np.mean(self.df["Duration (Minutes)"]),
            "Average Calories": np.mean(self.df["Calories Burned"]),
            "Total Duration": np.sum(self.df["Duration (Minutes)"]),
            "Total Calories Burned": np.sum(self.df["Calories Burned"])
        }
        return metrics

    # METHOD 3: Filter Activities
 
    def filter_activities(self, column, value):
        """
        Filters the DataFrame based on column-value match.
        """
        if column not in self.df.columns:
            print("Invalid column!")
            return None
        
        return self.df[self.df[column] == value]

    # METHOD 4: Generate Report
   
    def generate_report(self):
        """
        Displays full dataset + metrics summary.
        """
        print("\nFITNESS REPORT\n")
        print(self.df)
        
        print("\nMETRICS")
        metrics = self.calculate_metrics()
        for key, val in metrics.items():
            print(f"{key}: {val}")
#3 Visualizations

class FitnessVisualizer:

    def __init__(self, df):
        self.df = df

    # Bar Chart
    def bar_chart(self):
        plt.figure(figsize=(8, 5))
        sns.barplot(data=self.df, x="Activity Type", y="Duration (Minutes)")
        plt.title("Time Spent on Each Activity Type")
        plt.show()

    # Line Chart
    def line_chart(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.df["Date"], self.df["Calories Burned"], marker="o")
        plt.xticks(rotation=45)
        plt.title("Calories Burned Over Time")
        plt.xlabel("Date")
        plt.ylabel("Calories Burned")
        plt.tight_layout()
        plt.show()

    # Pie Chart
    def pie_chart(self):
        plt.figure(figsize=(6, 6))
        counts = self.df["Activity Type"].value_counts()
        plt.pie(counts, labels=counts.index, autopct="%1.1f%%")
        plt.title("Activity Distribution")
        plt.show()

    # Heatmap
    def heatmap(self):
        plt.figure(figsize=(6, 5))
        sns.heatmap(self.df[["Duration (Minutes)", "Calories Burned"]].corr(), annot=True)
        plt.title("Correlation Heatmap")
        plt.show()

    def show_all_charts(self):
        print("\nShowing all visualizations...")
        self.bar_chart()
        self.line_chart()
        self.pie_chart()
        self.heatmap()
        
# 4. Main Menu

def main_menu():

    tracker = FitnessTracker()

    while True:
        print("\n===== PERSONAL FITNESS TRACKER =====")
        print("1. Log Activity")
        print("2. View Full Report")
        print("3. Filter Activities")
        print("4. Visualizations")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            date = input("Enter Date (YYYY-MM-DD): ")
            activity = input("Enter Activity Type: ")
            duration = int(input("Enter Duration (Minutes): "))
            calories = int(input("Enter Calories Burned: "))
            tracker.log_activity(date, activity, duration, calories)

        elif choice == "2":
            tracker.generate_report()

        elif choice == "3":
            column = input("Filter by column (Activity Type / Date): ")
            value = input("Enter value to match: ")
            print(tracker.filter_activities(column, value))

        elif choice == "4":
            vis = FitnessVisualizer(tracker.df)
            vis.show_all_charts()
            vis.bar_chart()
            vis.line_chart()
            vis.pie_chart()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")
main_menu()