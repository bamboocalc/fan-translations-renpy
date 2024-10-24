# Support for (unofficial) fan translations in a Ren'Py game without further modification to the game files
Support fan translations in your Ren'Py game without the translators needing to modify your code or redistribute altered versions of your game.

Once you've integrated this code into your Ren'Py project, any folders dropped in the `tl` directory will appear as language options in the Preferences menu.

We will use NotoSans, which is an open-source font designed by Google under the SIL Open Font License (and it looks pleasant enough for most visual novels).

* NotoSans: https://fonts.google.com/noto/specimen/Noto+Sans

Place this font in your `game/fonts` directory

**PLEASE NOTE:**
* This code currently only supports languages covered by the base NotoSans font.
  * English, Spanish, French, German, Italian, Portuguese, Dutch, Swedish, Norwegian, Danish, Finnish, Icelandic, Irish, Polish, Czech, Slovak, Slovenian, Croatian, Bosnian, Serbian, Albanian, Romanian, Hungarian, Turkish, Estonian, Latvian, Lithuanian, Maltese, Afrikaans, Swahili, Filipino, Indonesian, Malay, Vietnamese, Zulu, Xhosa, Welsh, Galician, Catalan, Basque, Luxembourgish, Frisian, Latin, Greek, Russian, Ukrainian, Bulgarian, Belarusian, Serbian, Macedonian, Kazakh, Kyrgyz, Tajik, Mongolian, Bashkir, Tatar 
* This code assumes the game's default language (i.e. language `None`) is English.
* This code assumes that any and all folders inside the `game/tl` directory contain translation scripts.


**IMPORTANT:** Make sure to publically provide translation files for your game, otherwise this code will be near-useless. 

1. Open up your Ren'Py SDK, click "Generate Translations" and type `qliphoth` in the Language field. (This name is a placeholder. The translator will need to do a Find and Replace on all instances of "qliphoth" when doing translations for their desired language)

2. Then click on the checkbox that says `Generate empty strings for translations` 

3. Click on the text button that says `Generate Translations`

4. A new folder should have generated in the `game/tl` directory

5. Zip and upload this folder to your Itchio page, or figure out some way to allow fans to download it from you

