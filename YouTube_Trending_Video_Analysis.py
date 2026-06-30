# =====================================================
# YouTube Trending Video Analysis
# Data Science Internship Project
# =====================================================

# Step 1: Import Required Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set chart style
sns.set_style("whitegrid")


# =====================================================
# Step 2: Load Dataset
# =====================================================

df = pd.read_csv("youtube.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())


# =====================================================
# Step 3: Basic Data Cleaning
# =====================================================

# Remove duplicate rows
df = df.drop_duplicates()

# Convert required columns to numeric values
df["views"] = pd.to_numeric(df["views"], errors="coerce")
df["likes"] = pd.to_numeric(df["likes"], errors="coerce")
df["dislikes"] = pd.to_numeric(df["dislikes"], errors="coerce")
df["comment_count"] = pd.to_numeric(df["comment_count"], errors="coerce")

# Fill missing numeric values with 0
df["views"] = df["views"].fillna(0)
df["likes"] = df["likes"].fillna(0)
df["dislikes"] = df["dislikes"].fillna(0)
df["comment_count"] = df["comment_count"].fillna(0)

print("\nConclusion: Dataset loaded and basic cleaning completed.")


# =====================================================
# Step 4: Category Analysis
# =====================================================

category_count = df["category_id"].value_counts()

print("\nVideos in Each Category:")
print(category_count)

plt.figure(figsize=(10, 6))
category_count.plot(kind="bar", color="skyblue")
plt.title("Number of Videos in Each Category")
plt.xlabel("Category ID")
plt.ylabel("Number of Videos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\nConclusion: This chart shows which category_id has the most trending videos.")


# =====================================================
# Step 5: Views Trend Analysis
# =====================================================

top_views = df.sort_values(by="views", ascending=False).head(10)

print("\nTop 10 Videos with Highest Views:")
print(top_views[["title", "channel_title", "views"]])

plt.figure(figsize=(12, 6))
sns.barplot(data=top_views, x="views", y="title", color="orange")
plt.title("Top 10 Most Viewed Videos")
plt.xlabel("Views")
plt.ylabel("Video Title")
plt.tight_layout()
plt.show()

print("\nConclusion: These are the videos that received the highest number of views.")


# =====================================================
# Step 6: Likes vs Dislikes Analysis
# =====================================================

average_likes = df["likes"].mean()
average_dislikes = df["dislikes"].mean()

print("\nAverage Likes:", average_likes)
print("Average Dislikes:", average_dislikes)

plt.figure(figsize=(10, 6))
plt.scatter(df["likes"], df["dislikes"], color="green", alpha=0.6)
plt.title("Likes vs Dislikes")
plt.xlabel("Likes")
plt.ylabel("Dislikes")
plt.tight_layout()
plt.show()

print("\nConclusion: The scatter plot helps compare likes and dislikes on videos.")


# =====================================================
# Step 7: Comment Analysis
# =====================================================

top_comments = df.sort_values(by="comment_count", ascending=False).head(10)

print("\nTop 10 Videos by Comment Count:")
print(top_comments[["title", "channel_title", "comment_count"]])

plt.figure(figsize=(12, 6))
sns.barplot(data=top_comments, x="comment_count", y="title", color="purple")
plt.title("Top 10 Videos by Comments")
plt.xlabel("Comment Count")
plt.ylabel("Video Title")
plt.tight_layout()
plt.show()

print("\nConclusion: These videos have the highest audience discussion through comments.")


# =====================================================
# Step 8: Country Analysis
# =====================================================

country_count = df["publish_country"].value_counts().head(10)

print("\nTop Publishing Countries:")
print(country_count)

plt.figure(figsize=(10, 6))
country_count.plot(kind="bar", color="teal")
plt.title("Top Publishing Countries")
plt.xlabel("Country")
plt.ylabel("Number of Videos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\nConclusion: This chart shows the countries with the highest number of published trending videos.")


# =====================================================
# Step 9: Published Day Analysis
# =====================================================

day_count = df["published_day_of_week"].value_counts()

print("\nVideos Uploaded on Each Weekday:")
print(day_count)

plt.figure(figsize=(10, 6))
day_count.plot(kind="bar", color="coral")
plt.title("Videos Uploaded by Weekday")
plt.xlabel("Day of Week")
plt.ylabel("Number of Videos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\nConclusion: This analysis shows which weekdays have more video uploads.")


# =====================================================
# Step 10: Correlation Analysis
# =====================================================

num_data = df[["views", "likes", "dislikes", "comment_count"]]

print("\nCorrelation Matrix:")
print(num_data.corr())

plt.figure(figsize=(10, 6))
sns.heatmap(num_data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

print("\nConclusion: The heatmap shows the relationship between views, likes, dislikes and comments.")


# =====================================================
# Step 11: Distribution Graph
# =====================================================

plt.figure(figsize=(10, 6))
plt.hist(df["views"], bins=30, color="lightgreen", edgecolor="black")
plt.title("Distribution of Views")
plt.xlabel("Views")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

print("\nConclusion: The histogram shows how views are distributed in the dataset.")


# =====================================================
# Step 12: Pie Chart of Top 5 Publish Countries
# =====================================================

top_countries = df["publish_country"].value_counts().head(5)

plt.figure(figsize=(8, 8))
plt.pie(top_countries, labels=top_countries.index, autopct="%1.1f%%", startangle=90)
plt.title("Top 5 Publish Countries")
plt.tight_layout()
plt.show()

print("\nConclusion: The pie chart shows the share of videos from the top 5 countries.")


# =====================================================
# Step 13: Final Simple Conclusions
# =====================================================

print("\nFinal Conclusions:")
print("1. Category analysis shows which category_id appears most in trending videos.")
print("2. Top viewed videos are the most popular videos based on views.")
print("3. Likes and dislikes help understand audience reaction.")
print("4. Comment count shows audience engagement.")
print("5. Country analysis shows which countries publish more trending videos.")
print("6. Weekday analysis shows upload patterns by day.")
print("7. Correlation analysis shows relationships between numerical columns.")
print("8. Views distribution shows that some videos get very high views compared to others.")

print("\nProject Completed Successfully")
