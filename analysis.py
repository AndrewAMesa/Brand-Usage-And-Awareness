import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.patches as patches
 
# Set the seed for random number generators
randomSeed = 1
random.seed(randomSeed)
np.random.seed(randomSeed)
 
# Load a CSV file into a DataFrame
df = pd.read_csv("Haus für Poesie-Survey Data.csv")
#df = pd.read_csv("lyrikline-Survey Data.csv")
 
# Split the 'Sub_Awareness' column into multiple binary columns based on comma-separated values
catSeries = df['Brands they are Aware Of']
awarenessDF = catSeries.str.get_dummies(sep = ",")
awarenessDF = awarenessDF.add_prefix('Awareness_')
 
# Merge the original DataFrame with the new 'awareness' columns
df_combined = pd.merge(df, awarenessDF, left_index=True, right_index=True, how='inner')
 
# Repeat the process for the 'Used' column
catSeries = df['Brands they Use']
usedDF = catSeries.str.get_dummies(sep = ",")
usedDF = usedDF.add_prefix('Used_')
 
# Merge the updated DataFrame with the new 'used' columns
df_combined = pd.merge(df_combined, usedDF, left_index=True, right_index=True, how='inner')
 
# Drop the original 'Sub_Awareness' and 'Used' columns
df_combined.drop(['Brands they are Aware Of', 'Brands they Use'], axis=1, inplace=True)
 
# Assign the final DataFrame to 'df'
df = df_combined
 
# Save the final DataFrame to a new CSV file, used to split values on commas
df.to_csv('split_data_frame.csv', index=False)


# Correlation matrix ------------------------------------------------------------------------

# Selecting only numerical data types
df_numerical = df.select_dtypes(include=['int64', 'float64'])
 
# Calculating the correlation matrix
correlation_matrix = df_numerical.corr(method ='pearson')
 
# Creating a custom colormap
colors = ["white", "#5853a3", "black"]
cmap_name = "custom_colormap"
cm = mcolors.LinearSegmentedColormap.from_list(cmap_name, colors, N=256)
 
# Define a scale multiplier for adjusting visual elements
multiplier = 10
 
# Plotting the correlation matrix with a heatmap
fig, ax = plt.subplots(figsize=(30 + multiplier, 30 + multiplier))
heatmap = sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap=cm, square=True, linewidths=.5, annot_kws={"size": 24 + multiplier})
 
# Adjusting the color bar's label size
cbar = heatmap.collections[0].colorbar
cbar.ax.tick_params(labelsize=28 + multiplier)
 
# Highlighting specific cells with rectangles
for i in range(9):
  Rect = patches.Rectangle((i, 9 + i), 1, 1, linewidth=4, edgecolor='black', facecolor='none')
  ax.add_patch(Rect)
 
# Adjusting font size for ticks on both axes
plt.xticks(fontsize=28 + multiplier)
plt.yticks(fontsize=28 + multiplier)
 
# Adding a title to the heatmap
plt.title('Correlation Matrix with Awareness and Usage of Brands: Haus für Poesie', fontsize=30 + multiplier)
# plt.title('Correlation Matrix with Awareness and Usage of Brands: lyrikline', fontsize=30 + multiplier)
 
# Saving the plotted figure as a PNG image
plt.savefig('correlation_matrix.png', transparent=True)
 
# Display the plot
# plt.show() # Viewing issues arise when not in a jupyter notebook so it is best to view it in the PNG


# bar chart - Haus für Poesie ------------------------------------------------------------------------
 
# Loading survey data from a CSV file into a DataFrame
df = pd.read_csv("Haus für Poesie-Survey Data.csv")
 
# Creating dummy variables for 'Sub_Awareness' category and prefixing new column
catSeries = df['Brands they are Aware Of']
awarenessDF = catSeries.str.get_dummies(sep = ",")
awarenessDF = awarenessDF.add_prefix('Awareness_')
 
# Merging dummy variables back
df_combined = pd.merge(df, awarenessDF, left_index=True, right_index=True, how='inner')
 
# Repeating the process for the 'Used' category
catSeries = df['Brands they Use']
usedDF = catSeries.str.get_dummies(sep = ",")
usedDF = usedDF.add_prefix('Used_')
df_combined = pd.merge(df_combined, usedDF, left_index=True, right_index=True, how='inner')
 
# Dropping original awareness and usage columns
df_combined.drop(['Brands they are Aware Of', 'Brands they Use'], axis=1, inplace=True)
df = df_combined
 
# Filtering data to include only numerical types
df_numerical1 = df.select_dtypes(include=['int64', 'float64'])
df_numerical1 = df_numerical1.iloc[:, :9]
 
# Calculating percentages for these columns relative to the total entries
column_percentages1 = (df_numerical1.sum() / len(df_numerical1)) * 100
 
# Repeating the calculation for the next set of 9 columns
df_numerical2 = df.select_dtypes(include=['int64', 'float64'])
df_numerical2 = df_numerical2.iloc[:, 9:18]
column_percentages2 = (df_numerical2.sum() / len(df_numerical2)) * 100
 
# Setting up the figure and specifying the dimensions for clarity in display
plt.figure(figsize=(26, 12))
bar_width = 0.35
 
# Creating indices for the horizontal bar chart
indices = range(len(df_numerical1.columns))
 
# Plotting horizontal bars for the first dataset
plt.barh(indices,column_percentages1, height=bar_width, color='blue', label='Haus für Poesie User Awareness')
 
# Plotting horizontal bars for the second dataset
plt.barh([i +
bar_width for i in indices], column_percentages2, height=bar_width, color='black', label='Haus für Poesie User Usage')
 
# Adding labels and title for the plot
plt.title('Percentage of Haus für Poesie Users that are Aware of vs Use a Brand', fontsize=26, pad=20)
plt.ylabel('Brand', fontsize=22)
plt.xlabel('Awareness & Usage Percentage', fontsize=22, labelpad=20)
 
# Adjusting y-axis ticks
new_labels = [label[10:] if len(label) > 10 else label for label in df_numerical1.columns]
plt.yticks([i + bar_width / 2 for i in indices], labels=new_labels, rotation=45, fontsize=16)
 
# Formatting x-axis ticks
plt.xticks(ticks=[i for i in range(0, 101, 20)], labels=['{}%'.format(i) for i in range(0, 101, 20)], fontsize=16)
 
# Displaying a legend
plt.legend()
 
# Saving the plotted figure
plt.savefig('awareness_haus_horizontal.png', transparent=True)
#plt.show() Viewing issues arise when not in a jupyter notebook so it is best to view it in the PNG


# bar chart - lyrikline ------------------------------------------------------------------------
 
# Loading survey data from a CSV file into a DataFrame
df = df = pd.read_csv("lyrikline-Survey Data.csv")

 
# Creating dummy variables for 'Sub_Awareness' category and prefixing new column
catSeries = df['Brands they are Aware Of']
awarenessDF = catSeries.str.get_dummies(sep = ",")
awarenessDF = awarenessDF.add_prefix('Awareness_')
 
# Merging dummy variables back
df_combined = pd.merge(df, awarenessDF, left_index=True, right_index=True, how='inner')
 
# Repeating the process for the 'Used' category
catSeries = df['Brands they Use']
usedDF = catSeries.str.get_dummies(sep = ",")
usedDF = usedDF.add_prefix('Used_')
df_combined = pd.merge(df_combined, usedDF, left_index=True, right_index=True, how='inner')
 
# Dropping original awareness and usage columns
df_combined.drop(['Brands they are Aware Of', 'Brands they Use'], axis=1, inplace=True)
df = df_combined
 
# Filtering data to include only numerical types
df_numerical1 = df.select_dtypes(include=['int64', 'float64'])
df_numerical1 = df_numerical1.iloc[:, :9]
 
# Calculating percentages for these columns relative to the total entries
Column_percentages1 = (df_numerical1.sum() / len(df_numerical1)) * 100
 
# Repeating the calculation for the next set of 9 columns
df_numerical2 = df.select_dtypes(include=['int64', 'float64'])
df_numerical2 = df_numerical2.iloc[:, 9:18]
Column_percentages2 = (df_numerical2.sum() / len(df_numerical2)) * 100
 
# Setting up the figure and specifying the dimensions for clarity in display
plt.figure(figsize=(26, 12))
bar_width = 0.35
 
# Creating indices for the horizontal bar chart
indices = range(len(df_numerical1.columns))
 
# Plotting horizontal bars for the first dataset
plt.barh(indices,column_percentages1, height=bar_width, color='blue', label='Haus für Poesie User Awareness')
 
# Plotting horizontal bars for the second dataset
plt.barh([i +
bar_width for i in indices], column_percentages2, height=bar_width, color='black', label='Haus für Poesie User Usage')
 
# Adding labels and title for the plot
plt.title('Percentage of lyrikline Users that are Aware of a Brand vs Use a Brand', fontsize=26, pad=20)
plt.ylabel('Brand', fontsize=22)
plt.xlabel('Awareness & Usage Percentage', fontsize=22, labelpad=20)
 
# Adjusting y-axis ticks
new_labels = [label[10:] if len(label) > 10 else label for label in df_numerical1.columns]
plt.yticks([i + bar_width / 2 for i in indices], labels=new_labels, rotation=45, fontsize=16)
 
# Formatting x-axis ticks
plt.xticks(ticks=[i for i in range(0, 101, 20)], labels=['{}%'.format(i) for i in range(0, 101, 20)], fontsize=16)
 
# Displaying a legend
plt.legend()
 
# Saving the plotted figure
plt.savefig('awareness_lyrikline.png', transparent=True)
#plt.show() Viewing issues arise when not in a jupyter notebook so it is best to view it in the PNG
