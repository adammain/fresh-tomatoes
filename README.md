# Fresh Tomatoes Movies Documentation
The Fresh Tomatoes Movies website displays all newly released movies that have a 
current Rotten Tomatoes critic and audience score greater than 
70% ("Certified Fresh").  Displays the movie titles, box art, critic scores, 
audience scores, and trailers (when clicked).

The program uses Python to scrape the Rotten Tomatoes website data and creates 
an html page to display the data.

## Install
Download the directory titled "movie_trailer_website".

## Requirements
- Tested Python version: 2.7.13
- BeautifulSoup4
```
$ pip install beautifulsoup4
```
- Requests
```
$ pip install requests
```
- webbrowser, os, re, unicodedata 

## Usage

To start the program:

1. Open a terminal window
2. Ensure/download all program requirements (above)
3. Navigate to "movie_trailer_website" directory
4. Enter command in terminal:
```
python2.7 entertainment_center.py
```

### Expected Results

Browser window should automatically open and display current "Certified Fresh" 
movie titles, art, critic and audience scores, and trailers (when clicked).

### License
MIT © Adam Main

