# intern-code
Github Scraper using Python

# Pre-requisites 

1) PyGithub - 

   run  in terminal/powershell/cmd -

   pip install pygithub

   Check if the package is installed by importing github in shell if no error is produced the package is installed properly.

2) Obtain user token i.e - ACCESS_TOKEN  to run the program by following steps from encoded-token-list.txt

3) Update value for ACCESS_TOKEN in Github_Scraper.py 

# Running the program

run Github_scraper.py

org input - examples include - amzn(amazon),westerndigitalcorporation(WD),github(Github),google(Google),microsoft(Microsoft)

n - top "n" number of forked repos

m - top "m" contributors for each of the n forked repos

# Github-Scraper  

Uses the Github API 3.0 to run through an organisation's github repo and sorts the most forked repositories based on the user input - n.

For each of these repositories, based on user input m displays the top "m" most contributors along with their commit counts for the repo.

# Issues  

Since Github's API for search has rate-limiting of 5000 requests per hour implemented, for large organisations with a lot of repos the code fails. 

When trying to run the program for various test cases in short intervals of time, if the program pops an error as shown in error1.jpg refer to encoded-token-list.txt to bypass this restriction.

Few possible solutions to bypass the rate-limiting can be found at https://stackoverflow.com/questions/13394077/is-there-a-way-to-increase-the-api-rate-limit-or-to-bypass-it-altogether-for-git
