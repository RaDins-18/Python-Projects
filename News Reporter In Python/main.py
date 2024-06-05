# QUESTION:

# Use the NewsAPI and the requests module to fetch the daily news related to different topics. Go to: https://newsapi.org/ and explore the various options to build you application.



# SOLUTION:

# Importing request module.
import requests

# API key from News API website, Create your News API account and get your key.
API_KEY = 'fb3a5891a786455bb898f36e92b09f24'

# Add API key in the header.
headers = {
    'X-Api-Key': API_KEY,  # KEY in header to hide it from url.
  }

# While loop for continuosly running the script.
while True:

  # Get topic from user.
  topic = input("Topic: ")
  
  # Let choose user between top-headline or everything about news.
  userChoice = int(input("1 = top-headlines or 2 = everything: "))
  
  # If user choice is not 1 or 2 then print a message.
  if(userChoice not in [1, 2]):
    # Tell user to specify clearly.
    print("Please specify clearly what you want")
    # Repeat the loop.
    continue
  # If user choice is 1 or 2 then execute esle block code below.
  else:
    # If user choice is 1 then run below code.
    if(userChoice == 1):
      # Set news mod to "top-headlines".
      newsMod = "top-headlines"
    # If user choice is 2 then run below code.
    else:
      # Set news mod to "everything".
      newsMod = "everything"

  # Set params dictionary with below properties.
  params = {
      'q': topic,
      # 'source': 'bbc-news',
      'sortBy': 'publishedAt',
      'language': 'hi',
      # 'category': 'business',
      # 'country': 'us',
      # 'apiKey': API_KEY,
    }
  
  # If news mod is equal to "top-headlines" then reset language property in params.
  if(newsMod == "top-headlines"):
    params['language'] = ''
  
  # Define url of the API.
  url = f'https://newsapi.org/v2/{newsMod}?'
  
  # Add properties to request.
  response = requests.get(url, params=params, headers=headers)
  # Request News-API for news.
  data = response.json()
  
  # Sorting totalResult data from data.
  totalResults = data["totalResults"]
  # Print total results.
  print(f"Total Results: {totalResults}")
  
  # Sorting article data from data.
  articles = data["articles"] 
  # Make a dictionary with the name of results that has all data that is needed for app.
  results = [[arr["title"] for arr in articles], [pub["publishedAt"] for pub in articles], [des["description"]for des in articles], [ur["url"]for ur in articles]]
  
  # Assign n variable with initial value of 0.
  n = 0
  # For loop for print each news seperately from results dictionary.
  for arr, pub, des, ur in zip(results[0], results[1], results[2], results[3]):
      # Increase value of n variable.
      n = n + 1
      # Print n variable.
      print(n)
      # Print title and publish date of news.
      print(f"Title: {arr} - {pub[0:10]} \n")
      # Print description of news.
      print(f"Description: {des} \n")
      # Print url of news.
      print(f"URL: {ur} \n")
      # Print dashes for showing each news seperately.
      print("---------------------------------\n")