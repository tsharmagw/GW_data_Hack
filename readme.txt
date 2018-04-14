This project is for Gw hippo hacks. 

PROBLEM DEFINITION AND MOTIVATION: Hospital readmissions for Diabetes patients are very expensive since hospitals face severe penalties if the readmission rate is higher than expected.Therefore, in order to ensure better value,more satisfied patients and reduced readmission rates an attempt has been made by the authors to identify the key factors that influence readmission of diabetes patients and predict the probability of diabetic patients’ readmission.The dataset under consideration represents 10 years of clinical care and includes over 50 features representing patient and hospital outcomes.This problem falls under the category of Classification problem and suitable Classification Algorithms like KNN, SVM and Decision Trees are expected to help identify if a patient needs to readmitted or not.It is intuitively expected that the Decision Trees and SVM algorithms will outperform K Nearest Neighbor counterpart.The development of prediction models through three different machine learning approaches is expected to help develop a more lateral understanding of the problem at hand and arrive at suitable recommendations to tackle the problem.Additionally the authors expect to use techniques like Random forests(composed of decision trees) to arrive at a strong classifier.

PROPOSED METHOD: The specific steps involve preprocessing the data with imputation function included,  identifying various modelling techniques suitable to this dataset. The authors propose that the entire dataset be divided into train and test groups based on 70:30 split and deploy the algorithms : Logistic Regression, Decision Tree and Random Forest Algorithms.The parameters for each algorithm will be chosen based on the training set and the performance will be evaluated on the test set.The performance of the machine learning models will be compared and contrasted in order to assess the superiority of these models with the help of Precision-Recall Curve.

Target column  in the data set is readmission, which is a categorical column and has three values >30, <30, NO.
NO means no readmission.                                                                                       
>30 means readmission  after 30 days of discharge.  
<30  means readmission  before 30 days of discharge.

Two use cases for the project:
Use  Case 1:  Converted >30 and <30 to Yes and converted the readmission column to a binary column  and used machine  learning  algorithms to predict  yes or no  for readmission  and find columns  affecting the readmission.

Use Case 2: Used only >30 and <30 . Tried to find if readmission  is True then whether that readmission will be within a month or after a mont h and the factors affecting it.

Conclusion:-
Use Case 1: This gave an accuracy of around 62 percent using Logistic regression.
Use Case 2: This gave an accuracy of around 75.77 percent using Logistic regression.

This  can be used to predict  readmission  for person  diagnosed with  diabetes and help  them  get proper care.  In future,  an app can be made with  the trained model in the  backend. Data regarding thepatient  can be filled in the UI by the doctor itself,  then the data goes through  the machine  learning  pipeline,  to clean and preprocess  it and then  give a result  for  readmission.
If the result it true, it can further classify  whether  the readmission  will be within  30 days or after 30 days. These  results can help both the doctor and patient.

