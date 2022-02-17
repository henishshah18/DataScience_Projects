# Fake News Detection

  **Overview**
  
  * With an increasing number of people across the world relying on social media as their primary source of news, there is a need to tackle the underlying problem of fake news on those platforms. This project aims to do that by employing techniques of Natural Language Processing (NLP) and cross-references the piece of information entered by the user with the news articles scraped from renowned news websites around a topic. 
  
  * The dataset for this project was scraped from https://abcnews.go.com/ around three pertinent topics namely, Coronavirus, Donald Trump and US Elections. 
  
  **Features**
  
  * Features used in the dataset-
  
        i)   Link      - URL Link to the relevant news articles
        ii)  Title     - Title of the news articles
        iii) Content   - The actual content of the news articles
        iv)  Category  - Categories like International, Health, US, Sports, Politics, etc into which the articles are classified into
        
  **Technical Aspects**
  
  * After the initial data cleaning and pre-processing the 'Content' feature is tokenized so that we can train the **'word2vec'** over it. After training the 'word2vec' and obtaining the vectors, we use **'tsne'** to reduce the dimensionality to 2-D which also helps us visualize the points better. The 'tsne' is run with multiple **perplexity** and **iteration** values in order to find out the optimum parameters. With the help of this plot as well as methods like **'.similarity'** and **'.most_similar'** of gensim's word2vec the user can learn about the top words which are usually associated along with the one's used in the entered string as well as get an overview of  the similarity of words already present in the string. 
  * Equipped with this information, the user can then determine whether the entered data is credible or not. To aid this process, the program also returns the list of top 50 articles around the entered string so that the user can verify the source of this output information. The list is sorted on the basis of maximum number of words of the input corpus appearing in the title, the content of the respective article and the frequency of those words in it.
  * For demonstration purposes, I have scraped around 19k articles. But, more exhaustive the dataset is, the better 'word2vec' will get trained and in-turn yield better results. Ofcourse, the downside to that will be that training the model will take more time accordingly.
  
***Note**: Edit the 'config.json' file to add the path to the 'ChromeDriver' installed on the device and add the name of the topic which you'd like to scrape in the   'search_key' variable. Run the 'NewsWebScraping.py' file to scrape the news website.* 
