# Emoji-COLRv0
COLRv0 fonts generated from several open-source emoji sets.

These color fonts will work on nearly any browser.


## How do I get the fonts?

TODO

## How do I build the fonts?

On MacOS or Linux:

1. Clone this repo.
2. Navigate to the repo's folder in a command line.
3. Create a [python virtual environment](python3 -m venv /path/to/new/virtual/environment) with `python3 -m venv colrvenv`, where 'colrvenv' can be substituted for whatever you want the path to the virtual environment to be.
4. Activate the virtual environment with `source colrvenv/bin/activate`
5. Install [my fork](https://github.com/Emoji-COLRv0/nanoemoji) of Google's nanoemoji tool into the virtual environment with  
    `pip install git+https://github.com/Emoji-COLRv0/nanoemoji.git`

6. Unzip the .zip file cooresponding to the font you want to build. Navigate into that folder. When you run `ls`, you should see a folder called "svg" and a file called "config.toml".
7. Run nanoemoji with `nanoemoji --config 'config.toml' $(find svg -name 'emoji_u270d*.svg')`

The script should then start running. If successful, a build folder will be craeted, and the font file will be inside it.





## Information on the emoji sets:



