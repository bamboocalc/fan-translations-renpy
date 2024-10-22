# fan-translations-renpy
Support fan translations in your Ren'Py game without the translators needing to modify your code or redistribute altered versions of your game

This code supports the top 32 most commonly used languages online.

This code also assumes the default language (i.e. language `None`) is English.

Make sure to publically provide translation files on an Itchio page or similar. 

1. Open up your Ren'Py SDK, click "Generate Translations" and type `qliphoth` in the Language field. (This name is a placeholder. The translator will need to do a Find and Replace on all instances of "qliphoth" when doing translations for their desired language)

2. Then click on the checkbox that says `Generate empty strings for translations` 

3. Click on the text button that says `Generate Translations`

4. A new folder should have generated in the `game/tl` directory

**NOTE:** Please consider using Noto Sans as your game's system font. It is an open-source font designed by Google under the SIL Open Font License (OFL) and it looks pleasant enough for most visual novels.

These are download links to all the NotoSans fonts referenced in the code:

* NotoSans: https://fonts.google.com/noto/specimen/Noto+Sans

* NotoSans Japanese: https://fonts.google.com/noto/specimen/Noto+Sans+JP

* NotoSans Korean: https://fonts.google.com/noto/specimen/Noto+Sans+KR

* NotoSans Arabic: https://fonts.google.com/noto/specimen/Noto+Sans+Arabic

* NotoSans Oriya: https://fonts.google.com/noto/specimen/Noto+Serif+Oriya

* NotoSans Simplified Chinese: https://fonts.google.com/noto/specimen/Noto+Sans+SC

* NotoSans Thai: https://fonts.google.com/noto/specimen/Noto+Sans+Thai?query=Thai

* NotoSans Hebrew: https://fonts.google.com/noto/specimen/Noto+Sans+Hebrew?query=Hebrew

* NotoSans Devanagari: https://fonts.google.com/noto/specimen/Noto+Sans+Devanagari?query=Devanagari

Place all fonts in your `game/fonts` directory
