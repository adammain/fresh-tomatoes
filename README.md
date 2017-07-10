# Fresh Tomatoes Movies Documentation
The Fresh Tomatoes Movies website displays all newly released movies that have a
current Rotten Tomatoes critic and audience score greater than
70% ("Certified Fresh").  Displays the movie titles, box art, critic scores,
audience scores, and trailers (when clicked).

The program uses Python to scrape the Rotten Tomatoes website data and creates
an html page to display the data.

## How to install on computer
```
# Clone this git repo:
git clone git@github.com:amtruenorth/fresh-tomatoes.git

cd fresh-tomatoes/
```


## Requirements
- Tested Python version: 2.7.13
```
$ pip install beautifulsoup4

$ pip install requests
```
- webbrowser, os, re, unicodedata

## Usage

1) Confirm requirements (above) are installed
2) Navigate to project directory ```fresh-tomatoes/```

From project directory:
```
python2.7 entertainment_center.py
```

### Expected Results

Browser window should automatically open and display current "Certified Fresh"
movie titles, art, critic and audience scores, and trailers (when clicked).

### License
MIT © Adam Main
