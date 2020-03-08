# intern-code
Github Scraper using Python

# Pre-requisites 

PyGithub - 

run  in terminal/powershell/cmd -

pip install pygithub

Check if the package is installed by importing github in shell if no error is produced the package is installed properly.

# Running the program

run Github_scraper.py

org input - examples include - github,yuzu-emu,google,microsoft

n - top "n" number of forked repos

m - top "m" contributors for each of the n forked repos

# Github-Scraper  

Uses the Github API 3.0 to run through an organisation's github repo and sorts the most forked repositories based on the user input - n.

For each of these repositories, based on user input m displays the top "m" most contributors along with thir commits for the repo.

# Issues  

Since Github's APi for search has rate-limiting implemented, for large organisations with a lot of repos the code fails. 

