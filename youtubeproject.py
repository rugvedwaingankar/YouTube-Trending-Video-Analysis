import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("youtube.csv")

print(df.head())

# Number of Videos & Total Columns & Names
print(df.columns)

# total number of videos
print("Number of Videos =", df.shape[0])

# missing values
print(df.isnull().sum())

# Average Views
print(df['views'].mean())

# Average Likes
print(df['likes'].mean())

# Maximum Views
print(df['views'].max())

# minimum Views
print(df['views'].min())

# Maximum Likes
print(df['likes'].max())

# minimum likes
print(df['likes'].min())


# Difference between likes and dislikes
df['like_dislike_difference'] = df['likes'] - df['dislikes']
print(df[['title', 'likes', 'dislikes', 'like_dislike_difference']].head())


# Views vs Likes
df['view_like_difference'] = df['views'] - df['likes']
print(df[['title', 'views', 'likes', 'view_like_difference']].head())


# Videos with Comments Disabled vs Enabled
comments_disabled = len(df[df['comments_disabled'] == True])
comments_enabled = len(df[df['comments_disabled'] == False])
print("Comments Enabled Videos =", comments_enabled)
print("Comments Disabled Videos =", comments_disabled)




# Ratings Disabled vs Enabled
ratings_disabled = len(df[df['ratings_disabled'] == True])
ratings_enabled = len(df[df['ratings_disabled'] == False])

print("Ratings Enabled Videos =", ratings_enabled)
print("Ratings Disabled Videos =", ratings_disabled)


# # Bar graph
labels = ['Comments Enabled', 'Comments Disabled']
values = [comments_enabled, comments_disabled]

plt.bar(labels, values)
plt.xlabel("Category")
plt.ylabel("Number of Videos")
plt.title("Comments Enabled vs Disabled")
plt.show()


# Most Common Publish Country
print(df['publish_country'].value_counts())
# Videos Published by Day
print(df['published_day_of_week'].value_counts())


# Bar graph
df['published_day_of_week'].value_counts().plot(kind='bar')
plt.xlabel("Day")
plt.ylabel("Count")
plt.title("Videos Published Per Day")
plt.show()

# Top 10 Most Viewed Videos
top10 = df.nlargest(10, 'views')
print(top10[['title','views']])

# Line graph
df['views'].head(100).plot()
plt.xlabel("Video Number")
plt.ylabel("Views")
plt.title("Views Analysis")
plt.show()

# Likes Analysis
print(df['likes'].mean())
# Histrogram
plt.hist(df['likes'], bins=20)
plt.xlabel("Likes")
plt.ylabel("Frequency")
plt.title("Likes Distribution")
plt.show()


# Comment analysis
print(df['comment_count'].mean())
# Box plot
plt.boxplot(df['comment_count'])
plt.title("Comment Analysis")
plt.show()


# Heatmap
plt.figure(figsize=(8,6))

sns.heatmap(
    df[['views','likes','dislikes','comment_count']].corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")
plt.show()

# Tabel
table = df[['views','likes','comment_count']].mean()
print(table)





# Summary
# Summary
print("----- YOUTUBE DATASET SUMMARY -----")
print("Total Number of Videos :", len(df))
print("Total Number of Columns :", len(df.columns))
print("Column Names :")
print(df.columns.tolist())

print("\nMissing Values :")
print(df.isnull().sum().sum())

print("\nAverage Views :", df['views'].mean())
print("Average Likes :", df['likes'].mean())
print("Average Dislikes :", df['dislikes'].mean())
print("Average Comments :", df['comment_count'].mean())

print("\nMaximum Views :", df['views'].max())
print("Maximum Likes :", df['likes'].max())
print("Maximum Comments :", df['comment_count'].max())

print("\nMost Common Publish Country :")
print(df['publish_country'].mode()[0])

print("\nMost Common Publishing Day :")
print(df['published_day_of_week'].mode()[0])