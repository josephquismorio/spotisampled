import requests
import base64
import json
import spotipy
from spotipy import util
from bs4 import BeautifulSoup
from secrets import clientID
from secrets import clientSecret
from secrets import username

# endpoint #
authURL = "https://accounts.spotify.com/api/token" 

# authorization header for credential specification #
authHeader = {}

# hold grant type for access token #
authData = {}

# base64 encoder for app client ID and secret #
def accessToken(clientID, clientSecret):
    message = f"{clientID}:{clientSecret}" 
    messageBytes = message.encode('ascii')
    base64bytes = base64.b64encode(messageBytes)
    base64message = base64bytes.decode('ascii')

    # create authorization tag for header with encoded message #
    authHeader['Authorization'] = "Basic " + base64message

    # create grant type tag #
    authData['grant_type'] = "client_credentials"

    # !!! be sure to have requests library installed correctly !!! #
    # !!! have cacert.pem copied to your certifications folder !!! #
    res = requests.post(authURL, headers=authHeader, data=authData)

    # print(base64message) 

    # print(res)

    # create access token #
    resObj = res.json()

    token = resObj['access_token']
    
    return token


def playlistInfo(token, playlistID):
    # referenced from API endpoint reference #
    playlist = f"https://api.spotify.com/v1/playlists/{playlistID}"
    
    # get authorization header #
    getHeader = {"Authorization": "Bearer " + token}
    
    res = requests.get(playlist, headers=getHeader)
    
    playlistObj = res.json()
    
    return playlistObj

# API request #
token = accessToken(clientID, clientSecret)

playlistURL = input("Enter playlist URL: ")

playlistID = playlistURL.replace("https://open.spotify.com/playlist/", "")

tracklist = playlistInfo(token, playlistID)

# write data into json file for extraction later #
with open('tracklist.json', 'w') as f:
    json.dump(tracklist, f)

# extract data from json file #
def exportFormattedPlaylist(tracklist):
    titleList = []
    artistList = []
    for track in tracklist['tracks']['items']:
        artist = track['track']['artists'][0]['name']
        artistList.append(artist)
        title = track['track']['name']
        titleList.append(title)
    return titleList, artistList

titles, artists = exportFormattedPlaylist(tracklist)

def checkSampled(a, t):
    query = f"{a.replace(' ', '%20')}%20-%20{t.replace(' ', '%20')}"
    url = 'https://www.whosampled.com/search/tracks/?q={}'.format(query)
    page = requests.get(url, headers={"User-Agent":"Mozilla/5.0"})
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.findAll('li', attrs={'class': "listEntry"})
    if result:
        link = [i.a for i in result][0].get('href')
        return link
#    else:
#       print(f'{a} - {t} not found on WhoSampled') 

def getSamples(t, link):
    samples = []
    sampledBy = []
    url = f"https://www.whosampled.com{link}"
    page = requests.get(url, headers={"User-Agent":"Mozilla/5.0"})
    soup = BeautifulSoup(page.content, 'html.parser')
    listed = [i.text for i in soup.findAll('div', attrs={'class':'list bordered-list'})]
    if len(listed) == 2:
        sampledOut = [i.split('\n') for i in list(filter(None, listed[0].split('\t')))][:-1]
        sampledIn = [i.split('\n') for i in list(filter(None, listed[1].split('\t')))][:-1]
        for j in sampledIn:
            sampledBy.append({'query':t, 'type':j[-7], 'genre':j[-6], 'title':j[-3], 'artist':j[-2].replace('by ', '').split(' (')[0], 'year': j[-2].replace('by ', '').split(' (')[1].replace(')', '')})
    else:
        sampledOut = [i.split('\n') for i in list(filter(None, listed[0].split('\t')))][:-1]
    for i in sampledOut:
        samples.append({'query':t, 'type':i[-7], 'genre':i[-6], 'title':i[-3], 'artist':i[-2].replace('by ', '').split(' (')[0], 'year': i[-2].replace('by ', '').split(' (')[1].replace(')', '')})
    return samples, sampledBy

def sampleCompiler(a, t):
    link = checkSampled(a, t)
    if link:
        samples, sampledBy = getSamples(t, link)
        return samples, sampledBy
    else:
        return None, None
    
def samplesPlaylist(titleList, artistList):
    samples = []
    samplesPlaylist = []
    print('SPOTIFY PLAYLIST DISCOVERED: \n')
    for i in range(0, len(titleList)):
        print(titleList[i]+' by '+ artistList[i])
    for i in range(0, len(artistList)):
        samples, sampledBy = sampleCompiler(artistList[i], titleList[i])
        if samples:
            samplesPlaylist.append(samples)
    newList = [i for j in samplesPlaylist for i in j]
    return newList


def findSamplesSpotify(newList):
    ccm = util.prompt_for_user_token(username, scope='playlist-modify-public', client_id=clientID, client_secret=clientSecret, redirect_uri='http://127.0.0.1.8080/')
    sp = spotipy.Spotify(auth=ccm)
    found = []
    notFound = []
    for track in newList:
        subList = []
        artist = track['artist'].lower()
        result = sp.search(track['title'], limit=50)['tracks']['items']
        for i in result:
            if i['artists'][0]['name'].lower() == artist:
                subList.append(i['id'])
                break
        if subList:
#           print(f"Found {track['title']} by {track['artist']} on Spotify")
            found.append(subList[0])
        else:
            notFound.append((track['title'] + ' by ' + track['artist']))
    location_rate = 1 - len(notFound)/len(newList)
    return {'ids': found, 'unfound': notFound, 'rate': location_rate}


def setupNewPlaylist(newList, playlistName):
    ccm = util.prompt_for_user_token(username, scope='playlist-modify-public', client_id=clientID, client_secret=clientSecret, redirect_uri='http://127.0.0.1.8080/')
    sp = spotipy.Spotify(auth=ccm)
    allSamples = findSamplesSpotify(newList) 
    desc = f"Enjoy! I was unable to find: {len(allSamples['unfound'])} samples."
    playlist = sp.user_playlist_create(username, playlistName, public=True, description=desc)
    playlistID = sp.user_playlists(user=username)['items'][0]['id']
    sp.user_playlist_add_tracks(username, playlistID, allSamples['ids'], None)
    pass

def createNewPlaylist(newList, playlistName):
    ccm = util.prompt_for_user_token(username, scope='playlist-modify-public', client_id=clientID, client_secret=clientSecret, redirect_uri='http://127.0.0.1.8080/')
    sp = spotipy.Spotify(auth=ccm)
    samples = findSamplesSpotify(newList)
    new_playlist = setupNewPlaylist(newList, playlistName)
    print(f'New playlist "{playlistName}" created!')
    pass

def run():
    name = input('Please enter the name of the sample playlist\n')
    createNewPlaylist(samplesPlaylist(titles, artists), name)
    
run()