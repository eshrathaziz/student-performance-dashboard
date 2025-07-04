import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Excel data (relative path)
df = pd.read_excel('data/student_scores.xlsx')

# Calculate average marks per student
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)

# Identify at-risk students and low attendance
at_risk = df[df['Average'] < 50]
low_attendance = df[df['Attendance (%)'] < 75]

# Subject-wise average
subject_avg = df[['Math', 'Science', 'English']].mean()

# Plot: Subject-wise average marks
plt.figure(figsize=(6, 4))
subject_avg.plot(kind='bar', color='skyblue')
plt.title('Subject-wise Average Marks')
plt.ylabel('Average Marks')
plt.tight_layout()
plt.savefig('images/subject_avg.png')
plt.close()

# Plot: Attendance vs Performance
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Attendance (%)', y='Average', data=df, hue='Gender')
plt.title('Attendance vs Performance')
plt.tight_layout()
plt.savefig('images/attendance_vs_performance.png')
plt.close()

# Terminal output
print("🔹 Top Performers:")
print(df.sort_values(by='Average', ascending=False).head(3), "\n")

print("⚠️ Students At Risk:")
print(at_risk, "\n")

print("📉 Low Attendance:")
print(low_attendance)
