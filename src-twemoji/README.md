The SVG graphics in this folder come from the [Twemoji project by Twitter](https://github.com/twitter/twemoji), and are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
This means that you can freely reuse these graphics as long as you proper credit to the Twemoji Project

Twemoji in particular is fairly lax about what constitutes proper attribution, stating in the project's README that: 

> As an open source project, attribution is critical from a legal, practical and motivational perspective in our opinion. The graphics are licensed under the CC-BY 4.0 which has [a pretty good guide on best practices for attribution](https://wiki.creativecommons.org/wiki/Best_practices_for_attribution).  
> 
> However, we consider the guide a bit onerous and as a project, will accept a mention in a project README or an 'About' section or footer on a website. In mobile applications, a common place would be in the Settings/About section (for example, see the mobile Twitter application Settings->About->Legal section). We would consider a mention in the HTML/JS source sufficient also.

The zip of SVG files is simply a compressed copy of the [svg folder from Twemoji's asset directory](https://github.com/twitter/twemoji/tree/master/assets/svg). 
Due to the consistent flat style and clean code of Twemoji, I didn't have to modify any images to make them work with nanoemoji.

Please note that this font project is not officially affliated with the Twemoji project.


---

## Other COLR builds of Twemoji

There are actually two other builds of a Twemoji COLRv0 font that I know of.

The first can be found in [Google's experimental colr font repo](https://github.com/googlefonts/color-fonts). The main branch of the repo only has a COLRv1 version of the font, and COLRv1 currently lacks wide support. There is [a branch with a COLRv0 Twemoji font](https://github.com/googlefonts/color-fonts/tree/twemoji-colr_0/fonts), though it isn't completely up to date. The font I built here should be functionally very similar to their 'twemoji-glyf_colr_0.ttf', as it was built using the same [nanoemoji](https://github.com/googlefonts/nanoemoji) tool (albiet a different version of the tool.)

The second can be found in Mozilla's [twemoji-colr](https://github.com/mozilla/twemoji-colr) project, and is built using a javascript plugin called Grunt. In most browsers, I wasn't able to notice any differences between the two generated fonts, but on MacOS, there are noticeable bugs. Of the two the Grunt version has the worse issues, completely failing to render in Firefox or Chrome on MacOS. 


