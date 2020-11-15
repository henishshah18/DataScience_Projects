# DataScience_Projects
# 1. **Cancer Diagnosis**-

   **Overview**
   
   * Once sequenced, a cancer tumor can have thousands of genetic mutations. Currently this interpretation of genetic mutations is being done manually. This is a very time-consuming task where a clinical pathologist has to manually review and classify every single genetic mutation based on evidence from text-based clinical literature. In order to ease this gruesome process this is a model which can save the clinical pathologists’ several hours of literature review for classifying this mutation.

   * This is a multi-class classification problem for which the data is available at https://www.kaggle.com/c/msk-redefining-cancer-treatment/data
   
  **Features**
  
  * Features used in the dataset-
  
          i)    ID
          ii)   Gene
          iii)  Variation
          iv)   Text -  The clinical texts which the pathologists refer in order to classify a gene's variation as cancerous 
                        or non-cancerous. 
          v)    Class - 9 classes for classifying the mutations into.  
      
      
  **Technical Aspects**
  
  * There are two different datasets for this problem statement. The first one comprising of 'ID', 'Gene', 'Variation' and 'Class', while the second dataset containing 'ID' and 'Text'. The datasets were cleaned and then joined over 'ID' column using the 'left join'. The categorical features of 'Gene' and 'Variation' were vectorised using **Bag of Words**, while the 'Text' column consisting of the important clinical text was vectorised using the **tf-idf** vectorizer.
  * After this vectorizations, the respective features were horizontally stacked and the dataset was then split into train, cross-validation and test sets. Hyper-parameter tuning was carried out for **Logistic Regression**, **Linear SVM** and **Random Forest** to decide the optimum parameters and then the model was trained over those parameters.
  * Finally, the results from each model were compared using **log-loss** and the **mis-classification error**.
  * The model not only classifies the pair into one of the 9 classes but also says the probability with which it ascribes each pair for a particular class.

  
# 2. **Moneyball Project**-

   **Overview**
        
   * Inspired by the movie *'Moneyball'* which is based on how an algorithm played a major role in strategizing for an underdog team and lead them to victory in a major      Baseball League in America, I decided to make a similar algorithm for predicting whether a particular baseball team can make it to qualifiers or not.
  
   * This is a binary classification problem for which the data is available at https://www.kaggle.com/wduckett/moneyball-mlb-stats-19622012
  
  **Features**
  
  * Features used in the dataset-
  
          i)    RS - Total Runs scored 
          ii)   RA - Total Runs allowed
          iii)  OBP - On-base percentage
          iv)   SLG - Slugging Percentage
          v)    RD - Run Difference
          vi)   G - Games Played
          vii)  BA - Batting Average
          viii) OSLG - Overall Slugging percentage 
          ix)   OOBP - Overall On-Base percentage
          x)    W - Total Wins
          xi)   Playoffs - '0' for team not making it to Playoffs or '1' for team making it into Playoffs
      
  **Technical Aspects**
  
  * The dataset comprised nearly 70 % of missing values in the significant features of 'OOBP' and 'OSLG' which were then filled using Model Imputation using Linear Regression.
  * The dataset consists the data for two major Baseball leagues in America namely, 'American League' and 'National League'. Hence, the dataset was then split into two sections.
  * Performing EDA and plotting the 'pairplots' revealed various important features which were instrumental in deciding whether a team qualifies or not.  
  * The models used in this instance were Gradient Boost Decision Tree (GBDT) and Logistic Regression.
  * The metrics used to evaluate and compare the results from both the models were *accuracy*, *confusion matrix* & *f1 score*. 
