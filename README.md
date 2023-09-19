# YouTube Comments Spam Detection and Sentimental Analysis

# Motivation

YouTube is the second most popular search engine; it houses many genres like entertainment, education, and lifestyle content. The comment section under any video is where we can understand what the general public feels about the video; it also helps the creator improve the content in line with the audience's requirements. The major problem faced by YouTube today is the increasing number of spam comments, which makes it very difficult for the creator to analyze the comments; also, these spam comments are the primary source of YouTube scams. Thus there is an urgent need to detect and eliminate these spam comments.

It is imperative for a creator to analyze the comments on the videos they create regularly; this becomes very difficult, particularly when the creator has a huge audience, thus tons of comments. Comment analysis can also be helpful to the users as they can get a gist of what the video is about without actually wasting their time in watching the whole video; this becomes important as most of the creators use click-bait captions and thumbnails to force users to consume their content. Recently YouTube has scrapped the dislike counter under the videos, sentimental analysis of the comments sections can be used as an alternative.

# Problem Statement

Extract all the comments of a YouTube video and predict the Spam Comments using the Classification model trained on the spam comments dataset. Then perform a sentimental analysis and generate a Word Cloud to get the hot topics people are talking about after eliminating the spam comments and finding out the number of negative and positive comments to decide whether the content is liked by viewers or not.

# Algorithms and Tools Used

- NLTK (Natural Language Toolkit)
- Sklearn, NumPy, Matplotlib, Pandas
- SVM (Support Vector Machine)
- Logistic Regression
- Text Analytics
- Word Cloud
- NLP (Natural Language Processing)
- Google API Client

# Dataset Used

- [https://www.youtube.com/watch?v=kX3nB4PpJko](https://www.youtube.com/watch?v=kX3nB4PpJko) for **“comments_dataset.csv”** extracted using API.



- [https://www.kaggle.com/datasets/lakshmi25npathi/images](https://www.kaggle.com/datasets/lakshmi25npathi/images) for **“Youtube01-Psy.csv”.**

# Methodology

## Comment Extraction

- A python script *‘comment_extractor.py’* was written to extract all the comments and replies of the video whose ‘*videoId*’ (videoId is the text after “v=” in a YouTube URL, for example in ‘[https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ)’ dQw4w9WgXcQ is the videoId)is given as input.
- To extract the comments, YouTube Data API v3 is used which is routed through the Google API Client. To generate the API key visit: [https://developers.google.com/youtube/v3/getting-started?hl=en_GB](https://developers.google.com/youtube/v3/getting-started?hl=en_GB)
- The main method of the script calls the *‘comment_threads()’* function, which takes videoId as the parameter. The function makes a request to the API which responds with a list of 20 comments (max possible in one request), these are distinguished into comments or replies using the *‘process_comments()’* function and are appended to *‘comments_list’.*
- As only 20 comments can be requested at a time, a While loop is executed until all the comments are extracted and appended to *comments_list’.*
- Finally, all the comments are replies are added to a dataset- ‘*comments_dataset.csv*’ using the *make_csv()* function.
- To execute this script run: `python comment_extractor.py` in the  terminal.

## **Spam Classification**

- A YouTube comments spam classification model was trained using the dataset ‘**Youtube01-Psy’**. This dataset contains columns of - *‘**COMMENT_ID’, ‘AUTHOR’, ‘CONTENT’**,* and ***‘CLASS’***. Column ‘CLASS’ signifies if that content is spam or not. If CLASS is 1 then that content is spam.
- For the classification model, we have used both **Logistic Regression** and **SVM with Linear Kernel**. For this, the dataset was split into training data and test data with a 4:1 ratio respectively. Logistic Regression had an accuracy of 50% while SVM had an accuracy of 87% on the test data. That’s why we went with SVM for our classification model further.
- Now, for our project, the dataset on which we are going to apply our model to classify spam and non-spam comments is **‘comments_dataset’**. This dataset contains columns - *‘**videoId’, ‘textDisplay’, ‘textOriginal’, ‘parentId’, ‘authorDisplayName’, ‘authorProfileImageUrl’, ‘authorChannelUrl’, ‘authorChannelId’, ‘canRate’, ‘viewerRating’, ‘likeCount’, ‘publishedAt’, ‘updatedAt’, ‘commetnId’***.
- After that, some columns have been dropped out from the dataset which is irrelevant for our project purpose and then this dataset was classified by our model, and a new column named **‘spam’** was added to our dataset using the results shown by our classifier model which is equal to 1 if the comment is spam otherwise it is 0. This dataset was named **‘comments_datasetwithspam’.** From this dataset, all those comments were removed which were classified as spam, and then a new dataset was created which contains only non-spam comments. This dataset was named **‘Non_Spam_Comments’.**

## Sentimental Analysis

- Sentiment analysis was performed on this dataset. Word Cloud was formed and displayed.

![image](https://user-images.githubusercontent.com/76249576/204635878-a007d626-ea5f-44c2-a0f7-077f978c57b5.png)


- Text cleaning was performed like removing stop words, lemmatization, removing all the words having length less than 2, etc.,a list of updated stop words can also be custom added. Then again word cloud was formed and displayed for this cleaned data.

![image](https://user-images.githubusercontent.com/76249576/204635925-5b8a0dc9-f8ac-4ece-81ea-1541a30b7b55.png)

- Now for rating the comments as **negative**, **positive**, and **neutral** “VADER” scores are used.
- Finally, total counts of **negative**, **positive**, and **neutral comments** were calculated to gain insight if the viewers liked the content of the user or not. If **negative** counts are greater than **positive** counts, then simply the content of the user is highly disliked by the audience.

# Conclusions and Observations

- SVM has better accuracy than logistic regression.
- Precision, recall, and f-1 scores of the SVM model were found to be**556, 0.513, and 0.533** respectively. If the user wants to analyze as many as possible non-spam comments and does not want to miss any important non-spam comments then he has to need a model with a very high precision which can be obtained by increasing the threshold value of the classifier.
- The confusion matrix obtained for the SVM classifier model looks like this-

![image](https://user-images.githubusercontent.com/76249576/204635970-df854ce9-655c-4be6-b802-7ceb30279520.png)

- A larger dataset will result in better performance or accuracy which means the model is suffering from high bias.
- We are trying to fit non-linear data into a linear model which is resulting into a lesser accuracy.
- The dataset which we have used has very high number of spam comments. This can be reduced if we use a dataset having almost equal amount of spam and non-spam comments.
- In the final results, negative-rated, positive-rated, neutral-rated comments classified on the basis of VADER score are equal to 481, 1655, and 2714 respectively.

![image](https://user-images.githubusercontent.com/76249576/204636035-83c2c807-a712-4f55-9bf3-70879df4d455.png)

# References

- [https://developers.google.com/youtube/v3/docs/commentThreads/list?hl=en_GB#usage](https://developers.google.com/youtube/v3/docs/commentThreads/list?hl=en_GB#usage)
- [https://www.kaggle.com/datasets/lakshmi25npathi/images](https://www.kaggle.com/datasets/lakshmi25npathi/images)

# Contributors

[Yash Bhanushali](https://github.com/Yash-1907)

[Deepak Sharma](https://github.com/deep0505sharma)
