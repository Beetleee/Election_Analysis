# Module 3  Election_Analysis
### by Terra Lasho 
Deliverable 1 
-Election Results printed/delivered to command line:
![](https://github.com/Beetleee/Election_Analysis/blob/main/resources/Election_results_printed_to_command_line.png)
## Overview of Election Audit:
  I am helping Seth and Tom submit an election audit of western Colorado to the election commission.  They asked for additional information including incorporating county-specific information: voter turnout, percentage of votes, and the county with largest turnout.  For this, I wrote specific code which could delineate candidate-specific and county-specific voter information, and provide a printed bottom-line output.
### Election-Audit Results
 - **Total votes cast** The total votes cast in this election was: **369,711**

Specific code and output:
![](https://github.com/Beetleee/Election_Analysis/blob/main/resources/Total_votes.png)
 - **County-specific results**
	* **Jefferson** county has **10.5%** total percent of the vote, with **(38,855)** total votes
	* **Arapahoe** county has **6.7%** total percent of the vote, with **(24,801)** total votes
	* **Denver** county has **82.8** total percent of the vote, with **(306,055)** total votes


Specific code and output:
![](https://github.com/Beetleee/Election_Analysis/blob/main/resources/county_specific.png)
 - **County with largest number of votes**
	  **Denver** county has the largest number of votes with: **306,055**
	

Specific code and output:
![](https://github.com/Beetleee/Election_Analysis/blob/main/resources/Largest%20county.png)
 - **Candidate-specific results**
* Candidate **Charles Casper Stockholm** has **23.0%** of the vote, with **85,213** total votes
	* Candidate **Diana DeGette** has **73.8%** of the vote, with **272,892** total votes
	* Candidate **Raymon Anthony Doane** has **3.1%** of the vote, with **11,606** total votes


Specific code and output:
![]( https://github.com/Beetleee/Election_Analysis/blob/main/resources/Candidate_total_and_percentage_votes.png)
 - **Winning candidate info**
* Candidate **Diana DeGette** won the election!! 


Specific code and output:
![](https://github.com/Beetleee/Election_Analysis/blob/main/resources/winning_candidate.png)


## Election-Audit Summary
I have designed a script which can read raw election results and calculate both candidate-specific and county-specific information on total vote count and percentage of the vote, with a printed final output.  This script is invaluable because not only can it be used to reproduce this information for other elections (including different numbers of candidates, votes, and counties), but can be modified to quantify other variables (such as districts, states, ethnicities, etc…). This would be possible by incorporating new variables (specific to what you are testing for), initializing them to 0, and writing a script (like the one for candidate and counties) which tallies the votes-or other information that has been collected by the polling facility (by looping through the rows of the raw values). The script can also be modified for output, as one could initialize variables to hold the votes and count and introduce any number of formulas to commit calculations for a specific output interest.  
