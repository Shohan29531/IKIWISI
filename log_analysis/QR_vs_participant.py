import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True

# Load the DataFrame
df = pd.read_csv('../Logs/trimmed_logs/all.csv')

# Calculate 'quality of rating'
df['quality of rating'] = df['F1-Base'] - df['score']

# Specify the order of participants
participant_order = ['P1', 'P4', 'P5', 'P11', 'P12', 'P14', 'P15', 'P2', 'P3', 'P6', 'P7', 'P8', 'P9', 'P10', 'P13']

# Convert 'participant' column to a categorical type with the specified order
df['participant'] = pd.Categorical(df['participant'], categories=participant_order, ordered=True)

# Specify the order of expertise levels if necessary
expertise_order = ['Expert', 'Non-Expert']

# Convert 'expertise' column to a categorical type with the specified order
df['expertise'] = pd.Categorical(df['expertise'], categories=expertise_order, ordered=True)

# Increase overall font sizes by 4 using plt.rc
plt.rc('font', size=18)  # Increase base font size
plt.rc('axes', titlesize=20 + 4)  # Increase axes title font size
plt.rc('axes', labelsize=20 + 4)  # Increase axes labels font size
plt.rc('xtick', labelsize=12 + 4)  # Increase xtick labels font size
plt.rc('ytick', labelsize=12 + 4)  # Increase ytick labels font size
plt.rc('legend', fontsize=12 + 4)  # Increase legend font size

# Setting the plot size
plt.figure(figsize=(14, 8))

# Plotting boxplots for 'quality of rating' for each participant, colored by 'expertise'
sns.boxplot(x='participant', y='quality of rating', data=df, hue='expertise', palette='gray')

plt.title(r'Deviation of User Rating from $F_{1}^{\mathcal{D}*}$ for Each Participant')
plt.xlabel('Participant')
plt.ylabel(r'$F_{1}^{\mathcal{D}*}$ - User Rating')
plt.xticks(rotation=45)  # Rotate participant labels for better readability
plt.legend(title='Participant Expertise', title_fontsize='13')

# Optional: Adjust ylim if necessary to better visualize the boxplots
plt.ylim(-1, 1)

plt.axvline(x=6.5, color='black', linestyle='-', linewidth=3, zorder=10)  # After 8 bars

plt.tight_layout()  # Adjust layout
plt.savefig('../paper_files_latex/QR_vs_participant.pdf')  # Save the plot as a PDF file
plt.show()


from scipy.stats import mannwhitneyu

# Filter the DataFrame to separate the expert and non-expert groups
expert_ratings = df[df['expertise'] == 'Expert']['quality of rating']
non_expert_ratings = df[df['expertise'] == 'Non-Expert']['quality of rating']

# Perform the Mann-Whitney U test
u_stat, p_value = mannwhitneyu(expert_ratings, non_expert_ratings, alternative='two-sided')

# Print the results
print(f"Mann-Whitney U test result: U-statistic = {u_stat}, p-value = {p_value}")

# Evaluate the statistical significance
alpha = 0.05  # Common threshold for significance
if p_value < alpha:
    print("The difference between expert and non-expert groups is statistically significant.")
else:
    print("No significant difference was found between expert and non-expert groups.")
