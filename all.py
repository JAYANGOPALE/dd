'''assignment 1
Data Wrangling, I
Perform the following operations using Python on any open source dataset (e.g., data.csv)
1. Import all the required Python Libraries.
2. Locate an open source data from the web (e.g. https://www.kaggle.com). Provide a clear
description of the data and its source (i.e., URL of the web site).
3. Load the Dataset into pandas data frame.
4. Data Preprocessing: check for missing values in the data using pandas insult(), describe()
function to get some initial statistics. Provide variable descriptions. Types of variables
etc. Check the dimensions of the data frame.
5. Data Formatting and Data Normalization: Summarize the types of variables by checking
the data types (i.e., character, numeric, integer, factor, and logical) of the variables in the
data set. If variables are not in the correct data type, apply proper type conversions.
6. Turn categorical variables into quantitative variables in Python.
In addition to the codes and outputs, explain every operation that you do in the above steps and
explain everything that you do to import/read/scrape the data set.
'''

import pandas as pd
import numpy as np

df = pd.read_csv("Iris.csv")
df.shape
df.describe()
df.head()
df.tail()
df.duplicated()
df.dtypes
df.isnull()
df.info()
df['Species'].unique()
change = {'Iris-setosa':'IS' , 'Iris-versicolor':'IVE' , 'Iris-virginica':'IVI'}
df['Species'].replace(change, inplace=True)
df['Species'].unique()
df.isnull().sum()
y = df.drop(["PetalLengthCm"], axis=1) # axis=1 column. For row, axis=0
y

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['Species'] = le.fit_transform(df['Species'])

df.head()

df.iloc[:,1:5] = (df.iloc[:,1:5] - df.iloc[:,1:5].min()) / (df.iloc[:,1:5].max() - df.iloc[:,1:5].min())
df.head()


'''assignment 2
Create an “Academic performance” dataset of students and perform the following operations
using Python.
1. Scan all variables for missing values and inconsistencies. If there are missing values
and/or inconsistencies, use any of the suitable techniques to deal with them.
2. Scan all numeric variables for outliers. If there are outliers, use any of the suitable
techniques to deal with them.
3. Apply data transformations on at least one of the variables. The purpose of this
transformation should be one of the following reasons: to change the scale for better
understanding of the variable, to convert a non-linear relation into a linear one, or to
decrease the skewness and convert the distribution into a normal distribution.
Reason and document your approach properly.
'''
import pandas as pd
import numpy as np

df = pd.read_csv('AcademicPerformance.csv')
df.shape
df.describe()
df.head()
df.tail()
missing_values = df.isnull().sum()    #check missing values
print("Missing values:")
missing_values
invalid_attendance = df[(df['Attendance'] < 0) | (df['Attendance'] > 100)]
print("Invalid attendance:")
invalid_attendance
numeric_cols = df.select_dtypes(include=['number'])
mean_values = numeric_cols.mean()
print("\n=== Mean ===")
mean_values
median_values = numeric_cols.median()
print("\n=== Median ===")
median_values
print("\nCGPA Mean:", df["CGPA"].mean())
print("CGPA Median:", df["CGPA"].median())
print("CGPA Mode(s):", df["CGPA"].mode().tolist())

df['Scaled_Attendance'] = ((df['Attendance'] - df['Attendance'].min())) / ((df['Attendance'].max() - df['Attendance'].min()))
print("DataFrame with Min-Max Scaling on 'Attendance':")
print(df[['Attendance', 'Scaled_Attendance']].head(20))



'''assignment 3
Descriptive Statistics - Measures of Central Tendency and variability
Perform the following operations on any open source dataset (e.g., data.csv)
1. Provide summary statistics (mean, median, minimum, maximum, standard deviation) for
a dataset (age, income etc.) with numeric variables grouped by one of the qualitative
(categorical) variable. For example, if your categorical variable is age groups and
quantitative variable is income, then provide summary statistics of income grouped by
the age groups. Create a list that contains a numeric value for each response to the
categorical variable.
2. Write a Python program to display some basic statistical details like percentile, mean,
standard deviation etc. of the species of ‘Iris-setosa’, ‘Iris-versicolor’ and ‘Irisversicolor’ of iris.csv dataset.
Provide the codes with outputs and explain everything that you do in this step.
'''

import pandas as pd
import numpy as np

# Generate data
data = {
    'age': [25, 30, 22, 40, 55, 60, 33, 28, 45, 50],
    'income': [50000, 60000, 45000, 70000, 80000, 90000, 65000, 62000, 75000, 85000],
    'age_group': ['20-30', '30-40', '20-30', '40-50', '50-60', '50-60', '30-40', '20-30', '40-50', '50-60']
}

# Define data in DataFrame
df = pd.DataFrame(data)

# Group the data by age_group and compute summary statistics for 'income'
summary_stats = df.groupby('age_group')['income'].describe()

# Print summary
print(summary_stats)

# Group the data by age_group; Select income column for each of the groups created; Calculate median for income
median_income = df.groupby('age_group')['income'].median()

# Print dat median
print("Median Income by Age Group:")
print(median_income)

print("Column Names:", df.columns)

# Modified dataset with repeated values
data = {
    'age': [25, 30, 25, 40, 55, 60, 33, 28, 45, 50, 25, 30, 28, 30, 25],
    'income': [50000, 60000, 50000, 70000, 80000, 90000, 65000, 62000, 75000, 85000, 50000, 60000, 62000, 70000, 75000],
    'age_group': ['20-30', '30-40', '20-30', '40-50', '50-60', '50-60', '30-40', '20-30', '40-50', '50-60', '20-30', '30-40', '20-30', '30-40', '20-30']
}

# Define data in DataFrame
df = pd.DataFrame(data)

# Calculate the mode for each column
mode_age = df['age'].mode()
mode_income = df['income'].mode()
print(f"Mode of Age: {mode_age.values}")
print(f"Mode of Income: {mode_income.values}")

df = pd.read_csv('Iris.csv')

# Group the data by species and display summary statistics
summary_stats_species = df.groupby('Species').describe()

# Compute specific percentiles and statistics
percentiles = df.groupby('Species').quantile([0.25, 0.5, 0.75])

# Display summary statistics and percentiles
summary_stats_species = df.groupby('Species').describe()

print("\nPercentiles by Species:")
percentiles

# Group the data by variety; Select sepal.width column for each of the groups created; Display summary statistics
summary_stats_species = df.groupby('Species')['SepalWidthCm'].describe()

print("\nSummary Statistics by Species for Sepal Width:")
summary_stats_species


# Group by variety and compute the median for numeric columns
median_values = df.groupby('Species').median()

print("Median Values by Species:")
median_values

# Group the data by variety; Select sepal.width column for each of the groups created; Display median
median_sepal_length = df.groupby('Species')['SepalLengthCm'].median()
print("Median Sepal Length by Species:")
median_sepal_length

# Calculate & print mode for sepal.width
mode_width = df['SepalWidthCm'].mode()
print("Mode of Width:")
mode_width




'''assignment 4
Data Analytics I
Create a Linear Regression Model using Python/R to predict home prices using Boston Housing
Dataset (https://www.kaggle.com/c/boston-housing). The Boston Housing dataset contains
information about various houses in Boston through different parameters. There are 506 samples
and 14 feature variables in this dataset.
The objective is to predict the value of prices of the house using the given features.

'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

df = pd.read_csv('BostonHousing.csv')
df.columns
df.info()
df.describe()
df.isnull().sum()
X = df.iloc[:,0:13]
y = df.iloc[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,random_state=42)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
model = make_pipeline(StandardScaler(with_mean=False), LinearRegression())
model.fit(X_train, y_train)
model.score(X_test,y_test)






'''assignment 5
Data Analytics II
1. Implement logistic regression using Python/R to perform classification on
Social_Network_Ads.csv dataset.
2. Compute Confusion matrix to find TP, FP, TN, FN, Accuracy, Error rate, Precision,
Recall on the given dataset.
'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

df = pd.read_csv('Social_Network_Ads.csv')

df.head()

df.columns

df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

# Features and Target
X = df[['Gender', 'Age', 'EstimatedSalary']]
y = df['Purchased']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Train the model
classifier = LogisticRegression()
classifier.fit(X_train, y_train)
# Make predictions
y_pred = classifier.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Extract values
TN, FP, FN, TP = cm.ravel()

# Metrics
accuracy = accuracy_score(y_test, y_pred)
error_rate = 1 - accuracy
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f"True Positives (TP): {TP}")
print(f"False Positives (FP): {FP}")
print(f"True Negatives (TN): {TN}")
print(f"False Negatives (FN): {FN}")
print(f"Accuracy: {accuracy:.2f}")
print(f"Error Rate: {error_rate:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()





'''assignment 6
Data Analytics III
1. Implement Simple Naïve Bayes classification algorithm using Python/R on iris.csv
dataset.
2. Compute Confusion matrix to find TP, FP, TN, FN, Accuracy, Error rate, Precision,
Recall on the given dataset.
'''

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

df = pd.read_csv("Iris.csv")
df.head()

# Set independent and dependent variables
X = df.drop('Species', axis=1) # Independent variable
y = df['Species'] # Dependent variable

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Naive Bayes model
model = GaussianNB()
model.fit(X_train_scaled, y_train)

# Predict
y_pred = model.predict(X_test_scaled)

# Evaluate the model
cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
cm_df = pd.DataFrame(cm, index=model.classes_, columns=model.classes_)

# Plot Confusion Matrix
sns.heatmap(cm_df, annot=True, cmap='Blues', fmt='d')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
error_rate = 1 - accuracy

print(f"Accuracy: {accuracy:.2f}")
print(f"Error Rate: {error_rate:.2f}")
print(f"Precision (Macro): {precision:.2f}")
print(f"Recall (Macro): {recall:.2f}")






'''assignment 7
Text Analytics
1. Extract Sample document and apply following document preprocessing methods:
Tokenization, POS Tagging, stop words removal, Stemming and Lemmatization.
2. Create representation of document by calculating Term Frequency and Inverse Document
Frequency.
'''

import nltk
from nltk.tokenize import *
from nltk.corpus import *
from nltk.stem import *
import re

nltk.download('punkt') # For splitting text into sentences or words
nltk.download('stopwords') # Common stop words
nltk.download('wordnet') # Synonyms
nltk.download('averaged_perceptron_tagger') # part-of-speech (POS) tagger
nltk.download('punkt_tab') # For tokenizing text that is formatted in tabular form

text = "Hello everyone! I am jayan gopale. I am a loyal Git user all the way from Nashik. I have considerable knowledge about life, Python, C++, Java, Rust, Golang and Blockchain. For every smart contract, I lose one strand of my hair. In my free time, which by the way, I barely get, I like to swim."

var1 = sent_tokenize(text)
print(var1)

var2 = word_tokenize(text)
print(var2)

text = re.sub('[^a-zA-Z]',' ',text)
print("After removing punctuation from text:\n", text)

var3 = set(stopwords.words('english'))
print("Stop words:\n", var3)
print("==============================================================")
tokens = word_tokenize(text.lower())
filtered_text = []
for word in tokens:
  if word not in var3:
    filtered_text.append(word)
print("Tokenized Sentence:\n", tokens)
print("\nFiltered Sentence:\n", filtered_text)

var = ["write", "writing", "wrote", "writes","reading","reads"]
ps = PorterStemmer() # brings word to its root form
for w in var:
  root_word = ps.stem(w)
  print(root_word)

  nltk.download('omw-1.4')

wordnet_lemmatizer = WordNetLemmatizer()
text = "studies studying cries cry"
tt = nltk.word_tokenize(text)
print("Text is:\t", tt)
for w in tt:
  print("Lemma for {} is {}".format(w, wordnet_lemmatizer.lemmatize(w)))



text = "Hello everyone this is a sample text! Earth."
text = nltk.word_tokenize(text)
nltk.pos_tag(text)


# TF-IDF (Term Frequency & Inverse Document Frequency)
from sklearn.feature_extraction.text import TfidfVectorizer

new_sentence = "This is an example of term frequency. Meow meow meow meow meow!"

def calculate_tfIdf(document):
    tokenizer = TfidfVectorizer()
    tf_matrix = tokenizer.fit_transform(document)
    features_names = tokenizer.get_feature_names_out()
    return tf_matrix, features_names

# Wrap the new_sentence in a list
document = [new_sentence]
tf_matrix, feature_names = calculate_tfIdf(document)

print('TF-IDF')
print(feature_names, tf_matrix.toarray())




'''assignment 8
Data Visualization I
1. Use the inbuilt dataset 'titanic'. The dataset contains 891 rows and contains information
about the passengers who boarded the unfortunate Titanic ship. Use the Seaborn library
to see if we can find any patterns in the data.
2. Write a code to check how the price of the ticket (column name: 'fare') for each
passenger is distributed by plotting a histogram.
'''


import seaborn as sns
from matplotlib import pyplot as plt

df=sns.load_dataset('titanic')

df.head()

plt.figure(figsize=(6,4))
sns.displot(df['age']) # Use sns.distplot(df['age']) for older versions of seaborn library
plt.show()

plt.figure(figsize=(5,3))
bp = sns.boxplot(x='class',y='age',palette='pastel',data=df)
plt.show()
df.describe().transpose()

plt.figure(figsize=(5,4))
vp = sns.violinplot(x='class',y='age',palette='rainbow',data=df)
plt.show()

plt.figure(figsize=(5,4))
pq = sns.histplot(x='fare',bins=10,data=df,hue='survived',kde=False)
for i in pq.containers:
  pq.bar_label(i)
plt.show()

plt.figure(figsize=(5,4))
st=sns.scatterplot(x='age',y='fare',data=df)
plt.show()

plt.figure(figsize=(5,4))
kl=sns.scatterplot(x='age',y='fare',data=df,hue='survived')
plt.show()







'''assignmnt 9
Data Visualization II
1. Use the inbuilt dataset 'titanic' as used in the above problem. Plot a box plot for
distribution of age with respect to each gender along with the information about whether
they survived or not. (Column names : 'sex' and 'age')
2. Write observations on the inference from the above statistics.
'''


import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

df= sns.load_dataset('titanic')
df.head()
# Describe
df.describe()
# Describe - transposed, i.e. rows and columns swapped
df.describe().transpose()
# Mean, median, mode
age_data = df['age'].dropna() # Drop missing values in age & store in age_data var

sorted_age_data = sorted(age_data) # Store sorted age_data
n = len(sorted_age_data) # Store length of age_data

# Calculate mean
mean_age = sum(age_data) / len(age_data)

# Calculate median
if n % 2 == 1:  # odd
    median_age = sorted_age_data[n // 2]
else:  # even
    median_age = (sorted_age_data[n // 2 - 1] + sorted_age_data[n // 2]) / 2

# Calculate mode
age_counts = Counter(age_data)  # Count occurrences of each age
mode_age = age_counts.most_common(1)[0][0]  # Get the most common value

# Print
print(f"The mean age is: {mean_age}")
print(f"The median age is: {median_age}")
print(f"The mode age is: {mode_age}")

plt.figure(figsize=(8,4)) # 8 by 4 inches
sns.boxplot(x="sex", y="age", hue="survived", data= df, palette="viridis")
plt.title("Distribution of age with respect to each gender and survival Status")
plt.xlabel("Sex")
plt.ylabel("Age")
plt.show()

sns.violinplot(x='sex',y='age',data=df, hue= 'survived')

sns.catplot(x="sex", hue="survived", data=df, kind="count")





'''assignment 10
Data Visualization III
Download the Iris flower dataset or any other dataset into a DataFrame. (e.g.,
https://archive.ics.uci.edu/ml/datasets/Iris ). Scan the dataset and give the inference as:
1. List down the features and their types (e.g., numeric, nominal) available in the dataset.
2. Create a histogram for each feature in the dataset to illustrate the feature distributions.
3. Create a box plot for each feature in the dataset.
4. Compare distributions and identify outliers
'''


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Iris.csv")

df.head()

df.info()

df.dtypes

plt.hist(df['SepalLengthCm'])
plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()

plt.hist(df['SepalWidthCm'])
plt.title("Histogram of Sepal Width")
plt.xlabel("Sepal Width")
plt.ylabel("Frequency")
plt.show()

plt.hist(df['PetalLengthCm'])
plt.title("Histogram of Petal Length")
plt.xlabel("Petal Length")
plt.ylabel("Frequency")
plt.show()

plt.hist(df['PetalWidthCm'])
plt.title("Histogram of Petal Width")
plt.xlabel("Petal Width")
plt.ylabel("Frequency")
plt.show()

plt.boxplot(df['SepalLengthCm'])
plt.title("Boxplot of Sepal Length")
plt.show()

plt.boxplot(df['SepalWidthCm'])
plt.title("Boxplot of Sepal Width")
plt.show()

plt.boxplot(df['PetalLengthCm'])
plt.title("Boxplot of Petal Length")
plt.show()

plt.boxplot(df['PetalWidthCm'])
plt.title("Boxplot of Petal Width")
plt.show()

df.describe()















