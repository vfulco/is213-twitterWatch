# is213-twitterWatch

<h4>Requirements: </h4>

Python 3.4  
python-pip  
Mongodb  

You also have to fill out twittercredentials.py with your own credentials.

To install dependencies run: `pip install -r requirements.txt`

To run the application, just run: `python main.py`

Keywords to look for are collected from a mongodb database.

<h4> Troubleshooting: </h4>
There is a bug in Tweepy that on 31.08.15 has not been fixed. If you get: TypeError: Can't convert 'bytes' object to str implicitly  
Go into tweepy/streaming.py and change two lines;  
Line 161 to: `self._buffer += self._stream.read(read_len).decode('ascii')`  
Line 171 to: `self._buffer += self._stream.read(self._chunk_size).decode('ascii')`

Fix from @cozos in issue: https://github.com/tweepy/tweepy/issues/615
