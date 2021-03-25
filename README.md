# ElectionAnalysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate teh total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
* Data source: election_results.csv
* Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Results
The analysis of the election show that:
* There were 369,711 votes cast in the election.

* The county vote breakdown is as follows:
  * Jefferson: 10.5% (38,855)
  * Denver: 82.8% (306,055)
  * Arapahoe: 6.7% (24,801)
* Denver had the largest number of votes (306,055)
   
* In this election, the candidates, the proportion of votes they received and the number of votes tallied are:
  * Charles Casper Stockham: 23.0% (85,213)
  * Diana DeGette: 73.8% (272,892)
  * Raymon Anthony Doane: 3.1% (11,606)

* Diana DeGette won the election, amassing 272,892 votes (73.8% of the vote)

## Audit summary
This script is very versatile and can be used to analyse the breakdown of votes along candidates and counties
Potential modifications to make this script even more robust so it can be used for other elections:
* Collect the political party affiliations of each voter to break down votes by party affiliation
* Collect the mode of voting: mail in votes, in-person voting to break down votes along these voting methods
