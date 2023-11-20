## MLflow Project Management Example

[![MLflow Workflow](https://github.com/nogibjj/lisa-mini-project-12/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/lisa-mini-project-12/actions/workflows/cicd.yml)

### Overview

MLflow, an open-source platform, facilitates comprehensive management of the machine learning lifecycle. Offering tools for experiment tracking, reproducible code packaging, and model sharing, MLflow ensures seamless collaboration and deployment across various environments. Its versatile support for multiple languages, including Python, R, and Java, makes it a preferred choice for orchestrating machine learning workflows. In this week's exercise, we delve into implementing MLflow through a simple example.



### Goal

This MLflow project aims to make machine learning (ML) project management easy and effective. The main goals are:

1. **MLflow Introduction:**
   - Learn about MLflow and how it helps manage the entire ML process.

2. **Hands-on Model Building:**
   - Build a simple ML model using a common dataset like Iris.

3. **MLflow in Action:**
   - See MLflow in action by using it for experiment tracking, code packaging, and deploying models.

4. **Track Everything:**
   - Learn how to use MLflow to track important details like parameters, metrics, and even save useful artifacts.


### Part 1: Creating the Machine Learning Model

The machine learning model creation involves the following steps:

1. **Data Loading and Splitting:**
   - Load the Iris dataset using scikit-learn's `datasets.load_iris()` method.
   - Split the dataset into training and testing sets using `train_test_split`.

2. **Model Training and Prediction:**
   - Create a logistic regression model using `LogisticRegression` from scikit-learn.
   - Train the model with the training set using the `fit` method.
   - Make predictions on the test set using the `predict` method.

3. **Model Evaluation:**
   - Compute accuracy, confusion matrix, and classification report using scikit-learn's evaluation metrics (`accuracy_score`, `confusion_matrix`, `classification_report`).
   - Print the results to the console.

### Part 2: Using MLflow to Manage the Project

Integrate MLflow to manage the project and track metrics:

1. **Starting an MLflow Run:**
   - Use `mlflow.start_run()` to initiate an MLflow run, creating a new run for the experiment.

2. **Logging Parameters and Metrics:**
   - Log parameters, such as the type of the machine learning model, using MLflow's `mlflow.log_param`.
   - Log the model's accuracy as a metric using `mlflow.log_metric`.

3. **Saving Confusion Matrix as an Artifact:**
   - Save the confusion matrix, computed during model evaluation, to a text file using `np.savetxt`.
   - Log the text file as an artifact in the MLflow run using `mlflow.log_artifact`.

4. **Viewing Results and Tracking in MLflow:**
   - Print results, including accuracy, confusion matrix, and classification report, to the console.
   - View MLflow run information, including parameters, metrics, and artifacts, in the MLflow UI by navigating to the URL provided at the end of the run.

### Outputs

<img width="942" alt="Screenshot 2023-11-19 at 9 10 06 PM" src="https://github.com/nogibjj/lisa-mini-project-12/assets/46847817/bb3373a3-a9c2-4873-b84f-37abf5b403eb">
* Artifacts can also be found under the `mlruns` folder.
