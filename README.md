MLflow is an open-source platform designed to manage the end-to-end machine learning lifecycle. It provides tools for tracking experiments, packaging code into reproducible runs, and sharing and deploying models across different environments. The primary components of MLflow include Tracking, Projects, Models, and Registry. MLflow supports multiple languages (Python, R, and Java), and its versatility makes it a popular choice for managing machine learning workflows in a collaborative and reproducible manner. In this week's exercise, we aim to learn how to implement MLflow with a simple example.





### Part 1: Creating the Machine Learning Model

The code for creating the machine learning model involves the following steps:

1. **Data Loading and Splitting:**
   - The script loads the Iris dataset using scikit-learn's `datasets.load_iris()` method.
   - It splits the dataset into training and testing sets using `train_test_split`.

2. **Model Training and Prediction:**
   - The logistic regression model is created using `LogisticRegression` from scikit-learn.
   - The model is trained with the training set using the `fit` method.
   - Predictions are made on the test set using the `predict` method.

3. **Model Evaluation:**
   - Accuracy, confusion matrix, and classification report are computed using scikit-learn's evaluation metrics (`accuracy_score`, `confusion_matrix`, `classification_report`).
   - The results are printed to the console.

### Part 2: Using MLflow to Manage the Project

The code integrates MLflow to manage the project and track metrics:

1. **Starting an MLflow Run:**
   - The script uses `mlflow.start_run()` to initiate an MLflow run, creating a new run for the experiment.

2. **Logging Parameters and Metrics:**
   - MLflow's `mlflow.log_param` is used to log parameters, such as the type of the machine learning model.
   - The model's accuracy is logged as a metric using `mlflow.log_metric`.

3. **Saving Confusion Matrix as an Artifact:**
   - The confusion matrix, computed during model evaluation, is saved to a text file using `np.savetxt`.
   - The text file is then logged as an artifact in the MLflow run using `mlflow.log_artifact`.

4. **Viewing Results and Tracking in MLflow:**
   - The results, including accuracy, confusion matrix, and classification report, are printed to the console.
   - The MLflow run information, including parameters, metrics, and artifacts, is viewable in the MLflow UI by navigating to the URL printed at the end of the run.

This division allows for a clear understanding of how the machine learning model is created separately from how MLflow is utilized for project management and metric tracking.