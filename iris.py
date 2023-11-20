# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn import datasets
import mlflow
import mlflow.sklearn
import numpy as np


def train_and_evaluate_model():
    # Load the Iris dataset
    iris = datasets.load_iris()
    X = iris.data  # Features
    y = iris.target  # Target variable

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Start MLflow run
    with mlflow.start_run():

        # Create and train the model (Logistic Regression in this case)
        model = LogisticRegression(max_iter=500)
        model.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = model.predict(X_test)

        # Evaluate the model
        accuracy = accuracy_score(y_test, y_pred)
        conf_matrix = confusion_matrix(y_test, y_pred)
        class_report = classification_report(y_test, y_pred)

        # Log parameters
        mlflow.log_param("model_type", "Logistic Regression")

        # Log metrics
        mlflow.log_metric("accuracy", accuracy)

        # Save confusion matrix to a text file
        conf_matrix_file_path = "confusion_matrix.txt"
        np.savetxt(conf_matrix_file_path, conf_matrix, fmt="%d")

        # Log confusion matrix as an artifact
        mlflow.log_artifact(conf_matrix_file_path, "confusion_matrix.txt")

        print(f"Accuracy: {accuracy}")
        print(f"Confusion Matrix:\n{conf_matrix}")
        print(f"Classification Report:\n{class_report}")


# Call the function to train and evaluate the model with MLflow tracking
def main():
    train_and_evaluate_model()


if __name__ == "__main__":
    main()
