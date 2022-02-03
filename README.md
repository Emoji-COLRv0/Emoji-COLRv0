# Emoji-COLRv0
COLRv0 fonts generated from several open-source emoji sets.

These color fonts will work on nearly any browser.


## How do I get the fonts?

Take a look in the 'font' folder. 

TODO


## How do I build the fonts?

On MacOS or Linux:

1. Clone this repo.
2. Navigate to the repo's folder in a command line.
3. Create a [python virtual environment](https://docs.python.org/3/library/venv.html) with `python3 -m venv colrvenv`, where 'colrvenv' can be substituted for whatever you want the path to the virtual environment to be.
4. Activate the virtual environment with `source colrvenv/bin/activate`
5. Install [my fork](https://github.com/Emoji-COLRv0/nanoemoji) of Google's nanoemoji tool into the virtual environment with  
    `pip install git+https://github.com/Emoji-COLRv0/nanoemoji.git`

6. Unzip the .zip file cooresponding to the font you want to build. Navigate into that folder. When you run `ls`, you should see a folder called "svg" and a file called "config.toml".
7. Run nanoemoji with `nanoemoji --config 'config.toml' $(find svg -name '*.svg')`

The script should then start running. It will take a while to complete. If successful, a build folder will be created, and the font file will be inside it.





## Information on the emoji sets:

Further information can be found in the README within each zip file.

### EmojiTwo

The svg files within src-emojitwo come from the EmojiTwo project.

> Emoji artwork is provided by [Emojitwo](https://emojitwo.github.io/), 
> originally released as [Emojione 2.2](https://www.emojione.com) by ~~[Ranks.com](http://www.ranks.com)~~ [Joypixels](https://blog.joypixels.com/emojione-is-now-joypixels/)
> with contributions from the Emojitwo community
> and is licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode).

The font file named 'EmojiTwoCOLRv0.ttf' is built using these graphics.
Please credit both Joypixels and the EmojiTwo community if you use this font elsewhere.


### Twemoji

The svg files within src-twemoji come from the [Twitter Emoji](https://github.com/twitter/twemoji) project, 
and are licensed under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode).

The font file named 'TwemojiCOLRv0.ttf' is built using these graphics.
Please credit the Twemoji project if you use this font elsewhere.



