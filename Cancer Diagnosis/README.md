# Cancerous Gene Classification

   **Overview**
   
   * Once sequenced, a cancer tumor can have thousands of genetic mutations. Currently this interpretation of genetic mutations is being done manually. This is a very time-consuming task where a clinical pathologist has to manually review and classify every single genetic mutation based on evidence from text-based clinical literature. In order to ease this gruesome process this is a model which can save the clinical pathologists’ several hours of literature review for classifying this mutation.

   * This is a multi-class classification problem for which the dataset is available at https://www.kaggle.com/c/msk-redefining-cancer-treatment/data
   
  **Features**
  
  * Features used in the dataset-
  
          i)    ID
          ii)   Gene
          iii)  Variation
          iv)   Text -  The clinical texts which the pathologists refer in order to classify a gene's 
                        variation as cancerous or non-cancerous. 
          v)    Class - 9 classes for classifying the mutations into.  
      
      
  **Technical Aspects**
  
  * There are two different datasets for this problem statement. The first one comprising of 'ID', 'Gene', 'Variation' and 'Class', while the second dataset containing 'ID' and 'Text'. The datasets were cleaned and then joined over 'ID' column using the 'left join'. The categorical features of 'Gene' and 'Variation' were vectorised using **Bag of Words**, while the 'Text' column consisting of the important clinical text was vectorised using the **tf-idf** vectorizer.
  * After these vectorizations, the respective features were horizontally stacked and the dataset was then split into train, cross-validation and test sets. Hyper-parameter tuning was carried out for **Logistic Regression**, **Linear SVM** and **Random Forest** to decide the optimum parameters and then the model was trained over those parameters.
  * Finally, the results from each model were compared using **log-loss** and the **mis-classification error**.
  * The model not only classifies the pair into one of the 9 classes but also returns the probability with which it ascribes each pair for a particular class.
