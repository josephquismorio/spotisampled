# whosampled
a program that creates a new playlist of samples used by tracks/other tracks sampling tracks in a given spotify playlist using data from a beautifulsoup-facilitated web scrape from whosampled. an extension of my previous beginner spotipy project [playlist-data](https://github.com/josephquismorio/playlist-data) and build upon cpease00's [spotify-samples](https://github.com/cpease00/Spotify-Samples) repo.

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
git pull https://github.com/josephquismorio/samplepy.git
```
### setting up the secrets file
the file *secrets.py* contains slots for your application client ID, client secret, and your personal spotify username. fill those slots out accordingly. you can create an application at the spotify developer dashboard [here](https://developer.spotify.com/dashboard/).

upon logging in, you are greeted with a... dashboard. click "create an app" and you should see a little menu asking for a name and description for your app - you can name this app whatever you want.

next, find the section labeled "client ID". you should see a link just below it reading "show client secret" - click on it, and the client secret should show. copy both the client ID and client secret and paste it into the *secrets.py* file.

finally, fill in the username slot with your username, and you should be good as far as the secrets go!

### running whosampled
run the *whosampled.py* file using:
```
python3 whosampled.py
```
or
```
python whosampled.py
```
upon running the file, you will be prompted to input a playlist URL (make sure this is in the format "https://open.spotify.com/playlist/playlist-name"):

```
Please enter playlist URL: https://open.spotify.com/playlist/blahblahblah
```

next, enter a name for your new playlist:

```
Please enter a name for the sample playlist: test playlist
```

after these are completed, you should see a bunch of command lines that lay out all the tracks in your playlist.
```
Playlist given: 

Dynamite! by The Roots
No More Parties In LA by Kanye West
Crime Pays by Freddie Gibbs
Runnin' by The Pharcyde
Pennyroyal by Joey Bada$$
Doomsday by MF DOOM
Accordion by Madvillain
Potholderz feat. Count Bass D by MF DOOM
Snakes by Joey Bada$$
THAT'S THAT by MF DOOM
Raid by Madvillain
All Caps by Madvillain
Fancy Clown by Madvillain
```

wait a little bit, and...

<img width="790" alt="Screen Shot 2021-11-17 at 6 46 19 AM" src="https://user-images.githubusercontent.com/70463608/142203240-90af85cd-c2b8-4b0f-9421-5e5f76f7bcb3.png">

boom! you should have a new playlist containing all the whosampled-ripped samples that could be found on spotify. there also should be a closing message along the lines of:
```
New playlist "test playlist" created!
```
