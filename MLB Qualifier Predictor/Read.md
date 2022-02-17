# MLB Qualifier Predictor

   **Overview**
        
   * Inspired by the movie *'Moneyball'* which is based on how an algorithm played a major role in strategizing for an underdog team and lead them to victory in a major      Baseball League in America, I decided to make a similar algorithm for predicting whether a particular baseball team can make it to qualifiers or not.
  
   * This is a binary classification problem for which the dataset is available at https://www.kaggle.com/wduckett/moneyball-mlb-stats-19622012
  
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
  
  * The dataset comprised nearly 70 % of missing values in the significant features of 'OOBP' and 'OSLG' which I then filled using **Model Imputation** through **Linear Regression**.
  * The dataset consists the data for two major Baseball leagues in America namely, 'American League' and 'National League'. Hence, the dataset was then split into two sections.
  * Performing EDA and plotting the 'pairplots' revealed various important features which were instrumental in deciding whether a team qualifies or not.  
  * The models used in this instance were **Gradient Boost Decision Tree (GBDT)** and **Logistic Regression**.
  * The metrics used to evaluate and compare the results from both the models were **accuracy**, **confusion matrix** & **f1 score**. 
