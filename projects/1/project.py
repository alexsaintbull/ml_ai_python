from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from Tree import *

if __name__ == "__main__":

    # loading dataset
    iris = load_iris()
    
    #defining training and testing set
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)
    
    # Create and train the classifier
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    
    # Make predictions
    y_pred = clf.predict(X_test)

    # Calculate accuracy
    accuracy = np.sum(y_pred == y_test) / len(y_test)
    
    print(f"Accuracy: {accuracy}")