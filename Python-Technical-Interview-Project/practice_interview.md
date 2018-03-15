### Question 1
I would say the project that most reflects what I would be doing at 8 Rivers would be my project on OpenStreetmap data of the Raleigh-Durham area. OpenStreetMap is pretty much just Google maps but is completely open source for contributions.  In this project, I was tasked with selecting a geographic region and extracting, cleaning, and analyzing the map data using Python and SQL. The first step of this project was downloading the raw data in XML form. From there, the data was converted into CSV data and cleaned programmatically. 

In this cleaning, there were a couple of goals in mind. One was ensuring that the data within the same fields were consistent. A perfect example of a variable that needed to be cleaned was phone numbers.  Many of the numbers were in different formats: some had the country code, others used hyphens, parenthesis, or spaces while others didn’t... it was a mess. I ultimately picked a format that captured the most data and used regular expressions to adapt each record and ensure all the observations within that variable were consistent. After cleaning was finished, the CSV data was inserted into SQLite, where I could easily query the data for analysis. From the analysis, I found some very interesting trends on the user contribution. After aggregating user submissions, some users accounted for over 80% of all contributions, which I found pretty interesting. 

Overall, I think this project portrays my ability to work with messy data and clean it programmatically. I highly encourage that you check out the project for yourself through my LinkedIn page.

### Question 2	
__Part 1:__

_P(OOCC)_ = 1/14 or 0.072

I started off this probability problem by drawing a probabilty tree. After going down the tree by four levels, I followed the path _OOCC_ and mulitpled the probabilities, giving the result of 1/14 or 0.072.

__Part 2:__

_P(exactly 2 C)_ = 3/7 or 0.429

One method of doing this problem it to collect all of the tree path probabilities that have exactly two _C_'s and then add them together. However, an even faster method is to realize that each tree path probability is the same; the order in which the two _C_'s occur does not matter. You can use the probabilty of one tree path with exactly two _C_'s and multiply it my the total number of tree paths with two _C_'s to arrive at the final answer, which is 3/7 or 0.429.

### Question 3
~~~SQL
  SELECT state, COUNT(*) AS num_active_users FROM users
   WHERE active = TRUE
GROUP BY state
ORDER BY num_active_users DESC
   LIMIT 5;
~~~

The SQL statement first selects the columns needed for the query: `state` and `num_active_users`. `COUNT(*)` is used alongside `GROUP BY` to aggregate the state users together in one column. The `WHERE active = TRUE` clause ensures that only active users to pulled into the query. `ORDER BY num_active_users DESC` and `LIMIT 5` together ensure that the query only the top 5 states with the highest users is returned.

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


### Question 6
