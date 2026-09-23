import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Personal Fitness Tracker",
    page_icon="🏃",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🏃 Personal Fitness Tracker Dashboard")

st.write(
    "Interactive fitness activity analysis and visualization dashboard"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

CSV_FILE = "fitness_activities.csv"


@st.cache_data
def load_data():
    df = pd.read_csv(CSV_FILE)

    # Convert date column
    df["Date"] = pd.to_datetime(df["Date"])

    # Clean activity names
    df["Activity Type"] = (
        df["Activity Type"]
        .str.strip()
        .str.title()
    )

    return df


df = load_data()

# --------------------------------------------------
# DATA INFORMATION
# --------------------------------------------------

st.subheader("📋 Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Activities",
        len(df)
    )

with col2:
    st.metric(
        "Activity Types",
        df["Activity Type"].nunique()
    )

with col3:
    st.metric(
        "Total Duration",
        f"{df['Duration (Minutes)'].sum()} min"
    )

# --------------------------------------------------
# KPI METRICS
# --------------------------------------------------

st.subheader("📊 Fitness Summary")

total_duration = df["Duration (Minutes)"].sum()
total_calories = df["Calories Burned"].sum()

average_duration = df["Duration (Minutes)"].mean()
average_calories = df["Calories Burned"].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "⏱️ Total Duration",
        f"{total_duration:.0f} min"
    )

with col2:
    st.metric(
        "🔥 Total Calories",
        f"{total_calories:.0f}"
    )

with col3:
    st.metric(
        "⏳ Avg Duration",
        f"{average_duration:.1f} min"
    )

with col4:
    st.metric(
        "🔥 Avg Calories",
        f"{average_calories:.1f}"
    )

# --------------------------------------------------
# SIDEBAR FILTER
# --------------------------------------------------

st.sidebar.header("🔎 Filter Activities")

activity_options = ["All"] + sorted(
    df["Activity Type"].unique().tolist()
)

selected_activity = st.sidebar.selectbox(
    "Select Activity Type",
    activity_options
)

if selected_activity == "All":
    filtered_df = df.copy()
else:
    filtered_df = df[
        df["Activity Type"] == selected_activity
    ]

# --------------------------------------------------
# FILTERED DATA SUMMARY
# --------------------------------------------------

st.subheader("🎯 Selected Activity Analysis")

if len(filtered_df) > 0:

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Activities",
            len(filtered_df)
        )

    with col2:
        st.metric(
            "Duration",
            f"{filtered_df['Duration (Minutes)'].sum():.0f} min"
        )

    with col3:
        st.metric(
            "Calories",
            f"{filtered_df['Calories Burned'].sum():.0f}"
        )

# --------------------------------------------------
# ACTIVITY SUMMARY
# --------------------------------------------------

st.subheader("🏋️ Activity Summary")

activity_summary = (
    filtered_df
    .groupby("Activity Type")
    .agg(
        Activities=("Activity Type", "count"),
        Total_Duration=("Duration (Minutes)", "sum"),
        Total_Calories=("Calories Burned", "sum"),
        Average_Calories=("Calories Burned", "mean")
    )
    .reset_index()
)

st.dataframe(
    activity_summary,
    use_container_width=True
)

# --------------------------------------------------
# CHART 1 - DURATION BY ACTIVITY
# --------------------------------------------------

st.subheader("⏱️ Time Spent on Each Activity")

duration_summary = (
    filtered_df
    .groupby("Activity Type")["Duration (Minutes)"]
    .sum()
    .sort_values(ascending=False)
)

fig1, ax1 = plt.subplots(figsize=(10, 5))

duration_summary.plot(
    kind="bar",
    ax=ax1
)

ax1.set_title("Total Duration by Activity Type")
ax1.set_xlabel("Activity Type")
ax1.set_ylabel("Duration (Minutes)")

plt.xticks(rotation=0)
plt.tight_layout()

st.pyplot(fig1)

# --------------------------------------------------
# CHART 2 - CALORIES OVER TIME
# --------------------------------------------------

st.subheader("🔥 Calories Burned Over Time")

fig2, ax2 = plt.subplots(figsize=(10, 5))

sorted_df = filtered_df.sort_values("Date")

ax2.plot(
    sorted_df["Date"],
    sorted_df["Calories Burned"],
    marker="o"
)

ax2.set_title("Calories Burned Over Time")
ax2.set_xlabel("Date")
ax2.set_ylabel("Calories Burned")

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig2)

# --------------------------------------------------
# CHART 3 - ACTIVITY DISTRIBUTION
# --------------------------------------------------

st.subheader("🥧 Activity Distribution")

activity_counts = (
    filtered_df["Activity Type"]
    .value_counts()
)

fig3, ax3 = plt.subplots(figsize=(7, 7))

ax3.pie(
    activity_counts,
    labels=activity_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

ax3.set_title("Fitness Activity Distribution")

st.pyplot(fig3)

# --------------------------------------------------
# CHART 4 - DURATION VS CALORIES
# --------------------------------------------------

st.subheader("📈 Duration vs Calories Burned")

fig4, ax4 = plt.subplots(figsize=(10, 5))

ax4.scatter(
    filtered_df["Duration (Minutes)"],
    filtered_df["Calories Burned"]
)

ax4.set_title(
    "Relationship Between Duration and Calories Burned"
)

ax4.set_xlabel("Duration (Minutes)")
ax4.set_ylabel("Calories Burned")

plt.tight_layout()

st.pyplot(fig4)

# --------------------------------------------------
# CHART 5 - CORRELATION HEATMAP
# --------------------------------------------------

st.subheader("🔥 Correlation Analysis")

correlation_data = filtered_df[
    ["Duration (Minutes)", "Calories Burned"]
].corr()

fig5, ax5 = plt.subplots(figsize=(6, 4))

sns.heatmap(
    correlation_data,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    ax=ax5
)

ax5.set_title("Duration vs Calories Correlation")

st.pyplot(fig5)

# --------------------------------------------------
# RAW DATA
# --------------------------------------------------

st.subheader("📋 Fitness Activity Data")

st.dataframe(
    filtered_df.sort_values("Date"),
    use_container_width=True
)

# --------------------------------------------------
# LOG NEW ACTIVITY
# --------------------------------------------------

st.subheader("➕ Log New Fitness Activity")

with st.form("activity_form"):

    date = st.date_input("Date")

    activity = st.selectbox(
        "Activity Type",
        [
            "Gym",
            "Running",
            "Cycling",
            "Yoga",
            "Walking",
            "Swimming",
            "Other"
        ]
    )

    duration = st.number_input(
        "Duration (Minutes)",
        min_value=1,
        max_value=1000,
        value=30
    )

    calories = st.number_input(
        "Calories Burned",
        min_value=1,
        max_value=5000,
        value=200
    )

    submitted = st.form_submit_button(
        "Add Activity"
    )

    if submitted:

        new_row = pd.DataFrame({
            "Date": [date],
            "Activity Type": [activity],
            "Duration (Minutes)": [duration],
            "Calories Burned": [calories]
        })

        new_row.to_csv(
            CSV_FILE,
            mode="a",
            header=False,
            index=False
        )

        st.success(
            "✅ Activity added successfully!"
        )

        st.cache_data.clear()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "🏃 Personal Fitness Tracker | "
    "Built with Python, Pandas, Matplotlib, Seaborn & Streamlit"
)