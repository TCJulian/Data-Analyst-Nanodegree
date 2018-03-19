### Question 1
I would say the project that most reflects what I would be doing at 8 Rivers would be my project on OpenStreetMap data of the Raleigh-Durham area. OpenStreetMap is pretty much like Google maps, but is completely open source.  In this project, I was tasked with selecting a geographic region and extracting, cleaning, and analyzing the map data using Python and SQL, very similar to the skills needed for this position.

The first step of this project was downloading the raw data in XML form. The data was retrieved from a metro snapshot of the Raleigh-Durham area provided by MapZen. Once the XML data was loaded into Python, the data was converted into CSV data and cleaned programmatically.  

In this cleaning, there were a couple of goals in mind. One was ensuring that the data within the same fields were consistent. A perfect example of a variable that needed to be cleaned was phone numbers.  Many of the numbers were in different formats: some had the country code, others used hyphens, parenthesis, or spaces while others didn’t... it was a mess. I ultimately picked a format that captured the most data and used regular expressions to adapt each record to this format and ensure all the observations within that variable were consistent.

After cleaning was finished, the CSV data was inserted into an SQLite table, where I could easily query the data for analysis. From the analysis, I found some very interesting trends on the user contribution. After aggregating user submissions, some users accounted for over 80% of all contributions, which I found pretty interesting. I decided to further investigate user contribution and found that contributions to the Raleigh-Durham area has decreased steadily since the creation of OpenStreetMap.

Overall, I think this project portrays my ability to work with messy data and cleaning it programmatically. When I first took a shot at this project, I was a little overwhelmed with the scope and programming knowledge required to complete it. However, I am a quick study and love to be challenged. I used a lot of online tutorials alongside my Udacity courses to ultimately complete the project with flying colors. And this is just one project of many! I highly encourage that you check out my portfolio of projects for yourself through my LinkedIn page.

### Question 2
__Part 1:__

_P(OOCC)_ = 1/14 or 0.072

I started off this probability problem by drawing a probabilty tree. After drawing the tree out to four levels, I followed the path _OOCC_ and multiplied the probabilities, giving the result of 1/14 or 0.072.

__Part 2:__

_P(exactly 2 C)_ = 3/7 or 0.429

One method of doing this problem it to collect all of the tree path probabilities that have exactly two _C_'s and then add them together. However, an even faster method is to realize that each tree path probability is the same; the order in which the two _C_'s and two _O_'s occur does not matter. You can use the probability of one tree path with exactly two _C_'s and multiply it my the total number of tree paths with two _C_'s to arrive at the final answer. Interestingly enough, the answer to part one is the probability of a tree with exactly two _C_'s. Multiplying that probability (1/14) by the number of paths with exactly two _C_'s (6) returns the _P(exactly 2 C)_: 3/7 or 0.429.

### Question 3
~~~SQL
  SELECT state, COUNT(*) AS num_active_users FROM users
   WHERE active = TRUE
GROUP BY state
ORDER BY num_active_users DESC
   LIMIT 5;
~~~

The SQL statement first selects the columns needed for the query: `state` and `num_active_users`. `COUNT(*)` is used alongside `GROUP BY` to aggregate the state users together in one column. The `WHERE active = TRUE` clause ensures that only active users are pulled into the query. `ORDER BY num_active_users DESC` and `LIMIT 5` together ensure that the query returns only the top 5 states with the highest users.

### Question 4
~~~Python
def find_unique(s):
    for pos in range(len(s)):
        count = 0
        for letter in s:
            if s[pos] == letter:
                count += 1
        if count == 1:
            return s[pos]
    return None
~~~

This implementation of the function loops over each character in the string, comparing it to every other character to see if it is the only occurence of that character in the string. If it is, the function immediately breaks from the loop and returns the value. In the worst case, the runtime complexity of this implementation is _O(n),_ as the function loops _n * length_ times through the string. Space complexity is _O(1)_, as all calculations are done in place.

I considered using a set or dictionary of the individual characters in the string initially. However, both data structures become problematic due to the importance of the order in which the characters appear in the string. A set or dict does not retain the order of the characters, and thus could not be implemented without increasing the complexity of the code.

### Question 5
Overfitting and underfitting are both terms used to describe how a supervised learning algorithm fits the dataset. These terms go hand-in-hand with the idea of bias vs. variability.

If an algorithm is underfitting a dataset, the algorithm is generalizing the data too much and isn't adjusting enough to the information from the features and the expected outputs. This is known as having high bias.

If an algorithm is overfitting a dataset, the algorithm doesn't generalize enough and often reacts to random noise, getting results that aren't in the expected outputs. This is known as having high variance.

There are several methods to prevent, detect, and resolve over/underfitting. One of the easiest ways to avoid over/underfitting is to ensure that the learning algorithm being used is the most simple for the task at hand. If all of the features are categorical and the features are not too closely correlated, it might be better to implement a Naive Bayes algorithm rather than creating an ensemble of an SVM and a decision tree. Choosing the right algorithm for a machine learning problem is a skill I am constantly working on and hope to continue to cultivate as my experience grows.

One way to detect for fit problems is by looking at the score results from the training and test sets. If the algorithm performs much better on the training set than the test set, it is possible that the data is being overfitted. If the training and testing results are poor, it is possible that the dataset is being underfitted. Cross validation can be used alongside the results to determine how much an algorithm is over or under fitting the data.

Overfitting can be resolved by performing regularization, increasing the amount of data, or reducing the size of the model. Regularization reduces the complexity of the algorithm by adding weights to the estimator in the algorithm. Increasing the amount of data in the training set makes it harder for the algorithm to memorize the training data, which also leads to less overfitting. Reducing the size of the model also decreases the complexity of the algorithm, decreasing variance and increasing bias.

Underfitting is resolved by increasing the complexity of algorithm. This is the opposite of how to treat overfitting. Increasing the complexity of the algorithm can be done by adding more features to the dataset. By adding more features, the algorithm is given more information to predict the results of a datapoint, and leads to less bias and more variance.

### Question 6
There are three overarching goals that I would like to accomplish a year from now while working at 8 Rivers: Gain more Data Science and Financial knowledge, complete a project for a client from start to finish, and meet the team members from all of the unique divisions within 8 Rivers.

Within one year of working at 8 Rivers, I would love to slowly expand my work into areas of data science and machine learning and have an even deeper impact into the creation and implementation of new, globally impactful technologies. This includes expanding my knowledge into advanced data science libraries such as sklearn and nltk, and expanding my understanding of different machine learning algorithms. Learning a NoSQL database system like MongoDB and Big Data management software like Hadoop or Spark are both on my long term goals as well. Along with increasing my abilities in data science, I would also like to become a master of financial and foreign exchange markets, mainly by mentoring under the amazing talent at 8 Rivers.

Beyond my career goals, I want to be familiar with all of the unique people and divisions here at 8 Rivers. One of the reasons I was very interested in applying for this job was that the organization consisted of very knowledgeable and experienced team members from all types of backgrounds. Everyone seems to have extensive knowledge in their respective fields, and they seem like great people to work and grow with.

A longer, 5 year goal would be to play a leadership role in a client project and to participate in the project from start to finish. 8 Rivers has worked on some incredibly high-profile projects, such as the creation of the Allem Cycle for cleaner power plants and Thor Launch Systems for reducing the cost on interplanetary deliveries. I hope to be a much more crucial role in future projects of this scale as I grow in my capabilities as a data scientist.
