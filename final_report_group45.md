# Final Report

## Introduction:

Universal Healthcare is one of the most valuable privileges we have in Canada that we often pay little mind to. In many other countries individuals seeking medical support often have the added fear of healthcare debt. This is what drew us to conduct our analysis on the medical costs in the privatized medical industry of the United States. We hoped to understand what factors further exacerbated or alleviated the burden of charges and understand these correlations. Conducive to this we focused our attention specifically on health related attributes such as smoker status and bmi then on situational attributes such as sex, region and parental status. 

## Exploratory Data Analysis:

We started our EDA with a simple exploration of the general details, trends and shape of our data to better understand what we had to work with and how we would utilize it to answer our research question.

<img src ="images/report_eda_1.png" width="400px">

This provided us with a basic understanding of the dataset by giving us the names of its columns and the type of data in each row

<img src ="images/report_eda_2.png" width="400px">

We now had a summary of the important numerical imformation pertinent to answering both our reasearch questions

<img src ="images/report_eda_3.png" width="400px">

This figure shows the distribution charges for varying body mass indexes to help grasp a trend

<img src ="images/report_eda_4.png" width="400px">

From this we see that there is a higher amount of lower charges for both sexes of non smokers and lower amount but higher charges for both sexes of smokers. We will make the assumptiomn that this is due to the lower population of smokers in society over the whole.

<img src ="images/report_eda_5.png" width="400px">

From this plot we see that as the number of children increase the amount of charges actually get lower as opposed to our assumption going into the analysis that it would be the inverse. To understand this we extracted the amount of entries for each amount of children and came to the conclusion that this is due to less people having a greater number of children, providing a smaller sample size. To mitigate this we changed our focus to simply wether the individual was a parent or not. These can all be viewed in our [data analysis for question 2](https://github.com/ubco-W2022T1-cosc301/project-group45/blob/24482e5cb0082479811b7fd7edc6a324238e7a08/notebooks/analysis2.ipynb)

<img src ="images/report_eda_6.png" width="500px">

We then wanted to visualize the correlation between sex/region and charges to know where we could begin wrangling our data. This figure showed us some variances but nothing concrete enough to make a connection to charges. This meant we would need to combine the factor of parenthood to get a concrete trend.

<img src ="images/report_eda_7.png" width="400px">

Finally we used this pairplot to decide on which factors we would each keep when processing our data for the individual research questions. For the second research question The bmi has no significant correlation to how charges change for a parent/guardian as it would not affect their decision making process of seeking expensive medical attention. However bmi was essential to answering our first research question so we decided to create 2 seperate files of processed data to fit the needs of each question.

## Question 1 + Results:

{Clearly state your research question, and include 2-3 visualizations that helped you answer your research question. You can create multi-panel figures, but each of your visualizations must speak directly to your research question, and any insights you were able to get from it should be clearly articulated in the figure caption/description.}

## Question 2 + Results:

**What is the correlation between the number of children or dependants and the amount of charges? Furthermore, how are these trends affected by factors such as sex and/or region?**

<img src ="images/report_q2_1.png" width="300px">

After wrangling my data I was able to create this bar chart that shows the average charges for male and females seperated by each 4 regions southeast, northeast, southwest and northwest. From my EDA which you can access in my [data analysis](https://github.com/ubco-W2022T1-cosc301/project-group45/blob/24482e5cb0082479811b7fd7edc6a324238e7a08/notebooks/analysis2.ipynb) I realized that average charges express a more relevant answer to my question as there are different sample sizes for each region as opposed to using a sum of all charges by region. This analysis does show that regardless of being seperated by region, on average males have higher medical costs than females

<img src ="images/report_q2_2.png" width="300px">

I then included the factor of parental status to conclude on the exact trends of the medical data. I noticed that Males have similar costs in the northeast and south west regions regardless of parental status but male parents have significant jumps in charges in the northwest and southeast regions. Females however have relatively similar costs regardless of status as a parent with an exception to the Northeast which has a significant jump in cost. The situation of Females in the northeast seem to be an anomaly and thus are ignored in determining my conclusion.

<img src ="images/report_q2_3.png" width="300px">

Finally with the above Tableau table you can easily see how the numbers differ across all 16 subgroups. the data shows us that contrary to my assumptions parental status does not have a significant or absolute impact on the number of medical cost charges for an Individual in the United States. When looking at how charges are affected by the number of children each individual cares for, we found no pattern to assert an increase due to more children. Consequently, Male medical costs on average tend to be higher than female medical costs regardless of whether an individual is a parent or not. Furthermore, in half of the regions (northwest & southeast), we see a significant increase in costs for males with children versus males that don't have children. This draws me to conclude that sex and region can indeed have an influence on medical charges for parents but only in very nuanced cases.

## Summary/Conclusion:

{A brief paragraph that highlights your key results and what you learned from doing this project.}

