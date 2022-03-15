# load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as mplp
from sklearn import model_selection
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC



# file location
location="/laboratory/python/machine learning/iris/resources/iris.data"
# define variable names as column name
columnName=['sepal-length','sepal-width','petal-length','petal-width','class']
# create dataset
dataset=pandas.read_csv(location,columnName)

print(dataset.shape)