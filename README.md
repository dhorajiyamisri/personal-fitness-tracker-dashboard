# 🏃 Personal Fitness Tracker Dashboard

<p align="center">

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">

<img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">

<img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white">

<img src="https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=matplotlib&logoColor=white">

<img src="https://img.shields.io/badge/Seaborn-Visualization-0F4C5C?style=for-the-badge">

</p>

<p align="center">

<strong>🏋️ Interactive Fitness Analytics Dashboard built with Python & Streamlit</strong>

</p>

<p align="center">

Track Activities • Analyze Workout Performance • Visualize Fitness Trends

</p>

---

## 🌟 Project Overview

**Personal Fitness Tracker Dashboard** is an interactive data analysis and visualization application built using **Python, Pandas, Matplotlib, Seaborn, and Streamlit**.

The project transforms fitness activity data into an interactive dashboard where users can explore workout patterns, activity duration, calories burned, activity distribution, and relationships between fitness metrics.

Instead of analyzing the dataset only through Python scripts or static charts, this project provides an interactive **Streamlit dashboard** for exploring fitness data.

---

## 🚀 Live Dashboard

🌐 **Live Streamlit App**

👉 https://YOUR-STREAMLIT-URL.streamlit.app/

> Replace the URL above with your actual Streamlit deployment URL.

---

## 🎯 Project Objectives

The main objectives of this project are:

- 🏃 Analyze personal fitness activity data
- ⏱️ Understand workout duration patterns
- 🔥 Analyze calories burned
- 📊 Compare different activity types
- 📈 Visualize fitness trends
- 🔗 Analyze relationships between fitness metrics
- ⚡ Build an interactive Streamlit dashboard
- 🌐 Deploy the dashboard as a live web application

---

## 📊 Dashboard Features

### 🏃 Fitness KPI Dashboard

The dashboard provides important fitness summary metrics:

| Metric | Description |
|---|---|
| 🏃 Total Activities | Total number of recorded activities |
| ⏱️ Total Duration | Total workout duration |
| 🔥 Total Calories | Total calories burned |
| ⏳ Average Duration | Average duration per activity |
| 🔥 Average Calories | Average calories burned per activity |

---

### 🔎 Activity Type Filter

Users can filter the dashboard according to activity type.

Available activities can include:

- Gym
- Running
- Cycling
- Yoga
- Walking
- Swimming
- Other

The dashboard dynamically updates the analysis based on the selected activity.

---

### ⏱️ Duration Analysis

A bar chart displays the total amount of time spent on each activity.

This helps identify which activities contribute the most to overall workout duration.

---

### 🔥 Calories Burned Over Time

A line chart shows how calories burned change across different activity dates.

This helps analyze calorie-burning patterns over time.

---

### 🥧 Activity Distribution

A pie chart visualizes the distribution of recorded fitness activities.

This provides a quick overview of workout types in the dataset.

---

### 📈 Duration vs Calories

A scatter plot analyzes the relationship between:

**Workout Duration → Calories Burned**

This helps explore whether longer workout sessions are associated with higher calorie expenditure.

---

### 🔥 Correlation Analysis

A correlation heatmap analyzes the relationship between numerical fitness variables such as:

- Duration
- Calories Burned

The correlation value helps understand the strength and direction of the relationship between the variables.

---

### 📋 Interactive Data Table

The dashboard displays the underlying fitness activity data so users can directly inspect the records used for analysis.

---

### ➕ Add New Fitness Activity

The dashboard also provides a form for adding a new fitness activity.

Users can enter:

- Date
- Activity Type
- Duration
- Calories Burned

After submission, the new activity is added to the CSV dataset.

---

# 🗂️ Dataset

The project uses:
```text
fitness_activities.csv
```

| Column               | Description                         |
| -------------------- | ----------------------------------- |
| `Date`               | Date of the fitness activity        |
| `Activity Type`      | Type of physical activity           |
| `Duration (Minutes)` | Workout duration in minutes         |
| `Calories Burned`    | Calories burned during the activity |

🔄 Data Analysis Workflow

             Fitness Activity Data
                      │
                      ▼
                CSV Dataset
                      │
                      ▼
                Data Loading
                      │
                      ▼
                Data Cleaning
                      │
                      ▼
              Data Transformation
                      │
                      ▼
             Exploratory Analysis
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Duration    Calories    Activities
          │           │           │
          └───────────┼───────────┘
                      ▼
                Visualization
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
        Bar         Line         Pie
       Chart        Chart       Chart
          │           │           │
          └───────────┼───────────┘
                      ▼
                Scatter Plot
                      │
                      ▼
              Correlation Analysis
                      │
                      ▼
          Interactive Streamlit App

👩‍💻 Author

Misari Dhorajiya

Areas of Interest
📊 Data Science
🤖 Machine Learning
📈 Data Analytics
📊 Data Visualization
🐍 Python          

          


```text
fitness_activities.csv
