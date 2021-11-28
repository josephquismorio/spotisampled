# spotisampled
a program that creates a new playlist of samples used by tracks/other tracks sampling tracks in a given spotify playlist using data from a beautifulsoup-facilitated web scrape from whosampled. 

## prior requirements
this program requires the **requests**, **spotipy** and **beautifulsoup** libraries. 

download the requests library using the command line:
```
python -m pip install requests
```
download the spotipy library using the command line:
```
pip install spotipy --upgrade
```
and download the beautifulsoup library using the command line:
```
pip install beautifulsoup4
```

## setup & usage
download this repository using the command line:
```
git pull https://github.com/josephquismorio/spotisampled.git
```
### setting up the secrets file
the file *secrets.py* contains slots for your application client ID, client secret, and your personal spotify username. fill those slots out accordingly. you can create an application at the spotify developer dashboard [here](https://developer.spotify.com/dashboard/).

upon logging in, you are greeted with a... dashboard. click "create an app" and you should see a little menu asking for a name and description for your app - you can name this app whatever you want.

next, find the section labeled "client ID". you should see a link just below it reading "show client secret" - click on it, and the client secret should show. copy both the client ID and client secret and paste it into the *secrets.py* file.

finally, fill in the username slot with your username, and you should be good as far as the secrets go!

### running whosampled
run the *spotisampled.py* file using:
```
python3 spotisampled.py
```
or
```
python spotisampled.py
```
upon running the file, you will be prompted to input a playlist URL (make sure this is in the format "https://open.spotify.com/playlist/playlist-name"):

```
Please enter playlist URL: https://open.spotify.com/playlist/playlist-name
```

after this is completed, you should see a bunch of command lines that lay out all the tracks in your given playlist:
```
Playlist given: 

Dynamite! by The Roots
No More Parties In LA by Kanye West
Crime Pays by Freddie Gibbs
...
```

wait a little bit, and...

<img width="1149" alt="Screen Shot 2021-11-18 at 1 58 18 AM" src="https://user-images.githubusercontent.com/70463608/142375196-38c7a00a-fc72-4f3f-8c9f-43d409a4872d.png">

boom! you should have a new playlist containing all the whosampled-ripped samples that could be found on spotify. there also should be a closing message that gives a list of the songs that were unable to be found by the program:
```
New playlist created! Unable to find:
Indiana by Zoot Sims and Bucky Pizzarelli feat. Buddy Rich
Give Me My Love by Johnny Guitar Watson
Free Spirit by Walt Barr
...
```
