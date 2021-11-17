# whosampled
creates new playlist of samples used by tracks in a given spotify playlist using web scrape from whosampled. an extension of my previous beginner spotipy project [playlist-data](https://github.com/josephquismorio/playlist-data) and build upon cpease00's [spotify-samples](https://github.com/cpease00/Spotify-Samples) repo.

## requirements
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
the file *secrets.py* contains slots for your application client ID, client secret, and your personal spotify username. fill those slots out accordingly. you can create an application at the spotify developer dashboard [here](https://developer.spotify.com/dashboard/).

upon logging in, you are greeted with this menu. click "create an app" and you should be greeted by a little menu asking for a name and description for your app - you can name this app whatever you want.

next, find the section labeled "client ID". you should see a link just below it reading "show client secret" - click on it, and the client secret should show. copy both the client ID and client secret and paste it into the *secrets.py* file.

finally, fill in the username slot with your username, and you should be good as far as the secrets go!

run the *whosampled.py* file using:
```
python3 whosampled.py
```
or
```
python whosampled.py
```
upon running the file, you will be prompted to input a playlist URL. make sure this is in the format "https://open.spotify.com/playlist/playlist-name".

<img width="733" alt="Screen Shot 2021-11-17 at 6 41 57 AM" src="https://user-images.githubusercontent.com/70463608/142202598-b3a699e4-89b4-4cee-8109-54b39edd33b8.png">

next, enter a name for your new playlist. what the name is doesn't matter.

<img width="733" alt="Screen Shot 2021-11-17 at 6 43 51 AM" src="https://user-images.githubusercontent.com/70463608/142202885-d2d9234b-0563-457d-81fe-e42bc0b89be7.png">

after these are completed, you should see a bunch of command lines that lay out all the tracks in your playlist.

<img width="293" alt="Screen Shot 2021-11-17 at 6 45 04 AM" src="https://user-images.githubusercontent.com/70463608/142203055-cb7a5481-f3bd-4247-b8e3-925edfb6ebde.png">

wait a little bit, and...

<img width="790" alt="Screen Shot 2021-11-17 at 6 46 19 AM" src="https://user-images.githubusercontent.com/70463608/142203240-90af85cd-c2b8-4b0f-9421-5e5f76f7bcb3.png">

boom! you should have a new playlist containing all the whosampled-ripped samples that could be found on spotify. there also should be a closing message along the lines of:
```
New playlist "test playlist" created!
```
