######################################################################

# Insert this code in script.rpy inside an existing init python block

init python:    
    import os

    def get_available_translations():
        tl_path = os.path.join(renpy.config.gamedir, "tl")
        available_translations = []
        if os.path.isdir(tl_path):
            for folder_name in os.listdir(tl_path):
                # Exclude "None" folder and any hidden files
                if folder_name.lower() != "none" and not folder_name.startswith('.'):
                    lang_name = folder_name.lower()
                    available_translations.append(folder_name)
        return available_translations

######################################################################

# Insert this code in screens.rpy inside of your existing screen preferences():


        vbox:
            style_prefix "radio"
            label _("Languages")

            textbutton _("English") action Language(None)

            for lang in get_available_translations():
                textbutton _(f"{lang.capitalize()}") action Language(lang)

            text "{size=-15}{font=NotoSans-Italic.ttf}Place translations in\n directory {font=NotoSans-BoldItalic.ttf}game/tl"

######################################################################

# In gui.rpy Replace this code.....
define gui.text_font = "DejavuSans.ttf"
define gui.name_text_font = "DejavuSans.ttf"
define gui.interface_text_font = "DejavuSans.ttf"


# .......with this code:
default gui.text_font = "NotoSans-Regular.ttf"
default gui.name_text_font = "NotoSans-Regular.ttf"
default gui.interface_text_font = "NotoSans-Regular.ttf"