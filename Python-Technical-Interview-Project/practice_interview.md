1.	I would say the project that most reflects what I would be doing at 8 Rivers would be my project on OpenStreetmap data of the Raleigh-Durham area. OpenStreetMap is pretty much just Google maps but is completely open source for contributions.  In this project, I was tasked with selecting a geographic region and extracting, cleaning, and analyzing the map data using Python and SQL. The first step of this project was downloading the raw data in XML form. From there, the data was converted into csv data and cleaned programmatically. 

In this cleaning, there were a couple of goals in mind. One was ensuring that the data within the same field was consistent. A perfect example of a variable that needed to be cleaned was phone numbers.  Many of the numbers were in different formats: some had the country code, others used hyphens while others didn’t… it was a mess. I ultimately picked a format and used regular expressions to ensure all the observations within that variable were consistent. After cleaning the data, the csv data was inserted into an SQL table, where I could easily access the data for analysis. From the analysis, I found some very interesting trends on the user contribution. After aggregating user submissions, some users accounted for over 80% of all contributions, which I found pretty interesting. 

Overall, I think this project portrays my ability to work with messy data and clean it programmatically. I highly encourage that you check out the project for yourself through my LinkedIn page.
2.	Part 1:
1/14 or 0.072

Part 2:
3/7 or 0.429
3.	Answer:
      SELECT state, COUNT(*) AS num_active_users FROM users
     WHERE active = TRUE
GROUP BY state
 ORDER BY num_active DESC
         LIMIT 5;

Explanation:

~~~
R
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
