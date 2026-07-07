screen options_gen():

    add "gui/options assets/cog.png" at truecenter
    use navigation
    tag menu
    style_prefix "options"
    use options_general
    use tooltips
    add "gui/headers/generalheader.png"

screen options_acc():
    add "gui/options assets/cog.png" at truecenter
    use navigation
    tag menu
    style_prefix "options"
    use options_access
    use tooltips
    add "gui/headers/accessibility.png"

# 1 general
# 2 accessiblity
style skip_radio_button:
    background Transform("gui/options assets/checkbox.png",xalign=1.0,yalign=0.65)
    selected_foreground Transform("gui/options assets/check.png",xalign=1.0,yalign=0.65,xoffset=10)
    focus_mask None
    xalign 0.0
    xfill True
style skip_radio_button_text:
    size 25
    xalign 0.0
    color "#f6f2e4"
    yalign 1.0
    text_align 0.0
default options_menu = 1
style options_label_text:
    size 65
    outlines [ (absolute(4), "#ff7152", absolute(0), absolute(0)), (absolute(2), "#2b2725", absolute(0), absolute(0)) ]
    color "#f6f2e4"
    xalign 0.5
    text_align 0.5
style options_radio_button:
    background Transform("gui/options assets/checkbox.png",xalign=1.0,yalign=0.65)
    selected_foreground Transform("gui/options assets/check.png",xalign=1.0,yalign=0.65,xoffset=10)
    focus_mask None
style options_radio_button_text:
    size 32
    color "#f6f2e4"
    text_align 0.5
    xalign 0.5
    yalign 1.0
style withinoptions_label_text:
    size 32
    color "#f6f2e4"
    xalign 0.5
    text_align 0.5
style withinoptions_button_text:
    size 25
    color "#f6f2e4"
    idle_outlines [ (absolute(2), "#ff715200", absolute(0), absolute(0)), (absolute(1), "#2b2725", absolute(0), absolute(0)) ]
    hover_outlines [ (absolute(2), "#ff715200", absolute(0), absolute(0)), (absolute(1), "#2b2725", absolute(0), absolute(0)) ]
    selected_outlines [ (absolute(2), "#ff7152", absolute(0), absolute(0)), (absolute(1), "#2b2725", absolute(0), absolute(0)) ]
style withinoptions_button:
    background None
    selected_foreground Transform("gui/options assets/check.png",xalign=1.0,yalign=1.0)
    xalign 0.5
    xanchor 0.5
style options_label:
    xalign 0.5

style withinoptions_slider:
    thumb "gui/options assets/slidermid.png"
    thumb_offset 13
    left_bar Frame(VBox(Null(height=10),Solid("#ff7152")),xsize=320,ysize=16)
    top_gutter 15
    left_gutter -3
    right_bar Frame(VBox(Null(height=10),Solid("#f6f2e4")),xsize=320,ysize=16)
screen options_general():
    $ ensureConsistencyBetweenTrophyStateAndSaveDataProgression()
    add "gui/options assets/genbox.png" xalign 0.5 ypos 0.165
    hbox:
        xalign 0.5 ypos 0.123 spacing 40
        vbox:
            spacing 30
            xsize 563 xalign 0.5
            label __("Display") xalign 0.5 xanchor 0.5 background Transform("gui/options assets/displayhead.png",xalign=1.0,ypos=-20,xoffset=60)

            vbox:
                spacing 30
                xalign 0.5
                style_prefix "withinoptions"

                if (not isConsoleVariant() and not renpy.variant("steam_deck")):
                    vbox:
                        xalign 0.5
                        label __("Resolution") xalign 0.5
                        textbutton __("Fullscreen") action Preference("display", "fullscreen") xalign 0.5 tooltip __("Change display resolution.")
                        textbutton __("Windowed (Auto)") action Preference("display", "window") xalign 0.5 tooltip __("Change display resolution.")
                        textbutton __("Windowed 720p") action Preference("display", 0.6666667) xalign 0.5 tooltip __("Change display resolution.")
                        textbutton __("Windowed 540p") action Preference("display", 0.5) xalign 0.5 tooltip __("Change display resolution.")

                    add "gui/options assets/div.png"

                vbox:
                    spacing 30
                    xalign 0.5
                    style_prefix "options_radio"
                    hbox:
                        xsize 210
                        textbutton __("Transitions{space=15}") action Preference("transitions", "toggle") xalign 0.0 text_align 0.0 xfill True text_xalign 0.0 tooltip __("Toggle Transitions On or Off. Toggle Off if experiencing stutter or other performance issues.")
                    if (isR18PatchMounted() and not lewdCompatCheckFailed):
                        hbox:
                            xsize 210
                            textbutton __("R18 Content{space=15}") action ToggleField(persistent, "lewd") xalign 0.0 text_align 0.0 xfill True text_xalign 0.0 tooltip __("Toggle R18 Content On or Off.")
        vbox:
            xsize 563 xalign 0.5 spacing 30
            label __("Game Settings") xalign 0.5 xanchor 0.5 background Transform("gui/options assets/generaltexthead.png",xalign=1.0,ypos=-14,xoffset=25)
            vbox:
                spacing 30
                xalign 0.5
                style_prefix "withinoptions"
                grid 2 1:
                    xspacing 0
                    xalign 0.5
                    vbox:
                        xalign 0.5
                        label __("Language") xalign 0.5
                        textbutton __("{font=gui/fonts/CabinCondensed-Regular.ttf}English{space=10}") action [ Function(setLocalisationToLocalisationID, None), SelectedIf(getCurrentLocalisationID() == None) ] tooltip __("Change language to English.")
                        textbutton __("{font=gui/fonts/SourceHanSans-Regular.otf}中文{/font}{space=10}") at scale86 action [ Function(setLocalisationToLocalisationID, "chinese"), SelectedIf(getCurrentLocalisationID() == "chinese") ] tooltip __("Change language to Simplified Chinese.")
                        textbutton __("{font=gui/fonts/CabinCondensed-Regular.ttf}Español{/font}{space=10}") action [ Function(setLocalisationToLocalisationID, "spanish"), SelectedIf(getCurrentLocalisationID() == "spanish") ] tooltip __("Change language to Spanish.")
                        textbutton __("{font=gui/fonts/CabinCondensed-Regular.ttf}Français{space=10}") action [ Function(setLocalisationToLocalisationID, "fr"), SelectedIf(getCurrentLocalisationID() == "fr") ] tooltip __("Change language to French.")
                        textbutton __("{font=gui/fonts/SourceSans3-Regular.otf}Русский{/font}{space=10}") action [ Confirm("{font=gui/fonts/SourceSans3-Regular.otf}{size=30}Поскольку оригинальный русский перевод был сделан фанатами, нам не удалось получить точный русский перевод нового пользовательского интерфейса, а DLC не был переведен. На данный момент мы использовали машинный перевод, но если вы хотите помочь исправить наши переводы, свяжитесь с нами по адресу melanie@vnstudioelan.com с темой \"Russian TL Fixes.\"\n\nВсе равно поменять язык?{/font}",yes=Function(setLocalisationToLocalisationID, "russian")), SelectedIf(getCurrentLocalisationID() == "russian") ] tooltip __("Change language to Russian.")
                        if (getCurrentLocalisationID() == "duwang" or goofball_mode or realtime):
                            textbutton ("{image=images/ui/duwang.png}"):
                                action [
                                    SelectedIf(Language("duwang"))
                                ]
                    vbox:
                        xalign 0.5
                        label __("Skip") xalign 0.5
                        hbox:
                            xsize 190
                            textbutton __("Unseen Text{space=15}") action Preference("skip", "toggle") style "skip_radio_button" tooltip __("Toggle skipping of unread text.")
                        # textbutton __("Skip Unseen Messages{space=15}") action [Preference("skip", "all"), ToggleField(persistent, "speedlover"),SelectedIf(_preferences.skip_unseen)] style_prefix "options_radio"
                        hbox:
                            xsize 190
                            textbutton __("Begin Skipping{space=15}") action Skip() style "skip_radio_button" tooltip __("Click to exit the menu and begin skipping.")
                add "gui/options assets/div.png"
                vbox:
                    xalign 0.5
                    label __("Auto-Forward Time") xalign 0.5
                    null height (8 if ("SourceHan" in getConfiguredFontFace()) else 0)
                    vbox:
                        xalign .5
                        bar value Preference("auto-forward time") xmaximum 320 tooltip __("Set delay before text advances while on Auto Mode.") xalign .5
                        $ afm_time_adjusted = int((_preferences.afm_time / 250) * 1000)
                        text "[afm_time_adjusted] ms" size 18 xalign 1.0 outlines [(absolute(1), "#ff7152", absolute(0), absolute(0))]
                    textbutton __("Wait for Voice{space=24}") style "options_radio_button" action Preference("wait for voice", "toggle") xalign 0.5 tooltip __("When toggled, Auto-Forward will wait for voice lines to complete before continuing.")
                vbox:
                    xalign 0.5
                    label __("Text Speed") xalign 0.5
                    null height (8 if ("SourceHan" in getConfiguredFontFace()) else 0)
                    vbox:
                        bar value Preference("text speed") xmaximum 320 tooltip __("Set speed of text's typewriter effect.")
                        $ text_speed_adjusted = int(_preferences.text_cps)
                        if text_speed_adjusted == 0:
                            text "Instantaneous" size 18 xalign 1.0 outlines [(absolute(1), "#ff7152", absolute(0), absolute(0))]
                        elif text_speed_adjusted == 1:
                            text "Dangerously slow" size 18 xalign 1.0 outlines [(absolute(1), "#ff7152", absolute(0), absolute(0))]
                        else:
                            text "[text_speed_adjusted] characters/sec" size 18 xalign 1.0 outlines [(absolute(1), "#ff7152", absolute(0), absolute(0))]
        vbox:
            xsize 563 xalign 0.5 spacing 20
            label __("Sound & Voice") xalign 0.5 xanchor 0.5 background Transform("gui/options assets/generalsoundhead.png",xalign=1.0,ypos=-35,xoffset=23)
            vbox:
                xalign 0.5
                style_prefix "withinoptions"
                vbox:
                    xalign 0.5
                    label __("Music Volume") xalign 0.5
                    null height (8 if ("SourceHan" in getConfiguredFontFace()) else 0)
                    vbox:
                        bar value Preference("music volume") xmaximum 320 tooltip __("Set volume of all music.")
                        $ music_percent = int(_preferences.get_volume('music') * 100)
                        text __("[music_percent]%") size 18 xalign 1.0 outlines [(absolute(1), "#ff7152", absolute(0), absolute(0))]
                if ("SourceHan" in getConfiguredFontFace()):
                    null height -10
                elif (getCurrentLocalisationID() == "russian"):
                    null height -12
                vbox:
                    xalign 0.5
                    label __("Sound Volume") xalign 0.5
                    null height (8 if ("SourceHan" in getConfiguredFontFace()) else 0)
                    vbox:
                        bar value Preference("sound volume") xmaximum 320 tooltip __("Set volume of all sound.")
                        $ sound_percent = int(_preferences.get_volume('sfx') * 100)
                        text __("[sound_percent]%") size 18 xalign 1.0 outlines [(absolute(1), "#ff7152", absolute(0), absolute(0))]
                if ("SourceHan" in getConfiguredFontFace()):
                    null height -10
                elif (getCurrentLocalisationID() == "russian"):
                    null height -12
                vbox:
                    xalign 0.5
                    label __("Ambience Volume") xalign 0.5
                    null height (8 if ("SourceHan" in getConfiguredFontFace()) else 0)
                    vbox:
                        bar value MixerValue("ambient") xmaximum 320 tooltip __("Set volume of all ambient sound.")
                        $ amb_percent = int(_preferences.get_volume('ambient') * 100)
                        text __("[amb_percent]%") size 18 xalign 1.0 outlines [(absolute(1), "#ff7152", absolute(0), absolute(0))]
                if ("SourceHan" in getConfiguredFontFace()):
                    null height -10
                elif (getCurrentLocalisationID() == "russian"):
                    null height -12
                vbox:
                    xalign 0.5
                    label __("Master VA Volume") xalign 0.5
                    null height (8 if ("SourceHan" in getConfiguredFontFace()) else 0)
                    vbox:
                        xalign 0.5
                        bar value Preference("voice volume") xmaximum 320 xalign 0.5 tooltip __("Set volume of all voices.")
                        $ voice_percent = int(_preferences.get_volume('voice') * 100)
                        text __("[voice_percent]%") size 18 xalign 1.0 outlines [(absolute(1), "#ff7152", absolute(0), absolute(0))]
                    null height 16
                    hbox:
                        xalign 0.5
                        style_prefix "options_radio"
                        textbutton __("Voice Sustain{space=24}") action Preference("voice sustain", "toggle") xalign 0.5 tooltip __("When toggled, voices continue playing after click until finished, or until another voice replaces it.")
                        textbutton __("Voice Emphasis{space=24}") action Preference("emphasize audio", "toggle") xalign 0.5 tooltip __("When toggled, the volume of sound/music channels will be reduced while voices are playing.")

                null height 2

                vbox:
                    xalign 0.5
                    style_prefix "withinoptions"
                    # label __("Individual Voice Volumes") xalign 0.5
                    spacing 5
                    hbox:
                        spacing 3 xalign 0.5
                        vbox:
                            $ amber_volume = persistent._character_volume.get("amber",1.0)
                            imagebutton idle "gui/voiceicons/amber.png" hover "gui/voiceicons/amber.png" selected_foreground "scarlet_bar_fg" action SetVariable("select_voice","amber") at help_icons tooltip __("Set Amber's voice volume.")
                            text "[amber_volume:.0%]" size 18 xalign 1.0 outlines [(absolute(1), "#ff7152", absolute(0), absolute(0))] ypos -67 xoffset 1
                        vbox:
                            # text
                            $ marina_volume = persistent._character_volume.get("marina",1.0)
                            imagebutton idle "gui/voiceicons/marina.png" hover "gui/voiceicons/marina.png" selected_foreground "scarlet_bar_fg" action SetVariable("select_voice","marina") at help_icons tooltip __("Set Marina's voice volume.")
                            text "[marina_volume:.0%]" size 18 xalign 1.0 outlines [(absolute(1), "#ff7152", absolute(0), absolute(0))] ypos -67 xoffset 1
                        vbox:
                            # text
                            $ mariah_volume = persistent._character_volume.get("mariah",1.0)
                            imagebutton idle "gui/voiceicons/mariah.png" hover "gui/voiceicons/mariah.png" selected_foreground "scarlet_bar_fg" action SetVariable("select_voice","mariah") at help_icons tooltip __("Set Mariah's voice volume.")
                            text "[mariah_volume:.0%]" size 18 xalign 1.0 outlines [(absolute(1), "#ff7152", absolute(0), absolute(0))] ypos -67 xoffset 1
                        vbox:
                            # text
                            $ joe_volume = persistent._character_volume.get("joseph",1.0)
                            imagebutton idle "gui/voiceicons/joe.png" hover "gui/voiceicons/joe.png" selected_foreground "scarlet_bar_fg" action SetVariable("select_voice","joseph") at help_icons tooltip __("Set Joseph's voice volume.")
                            text "[joe_volume:.0%]" size 18 xalign 1.0 outlines [(absolute(1), "#ff7152", absolute(0), absolute(0))] ypos -67 xoffset 1
                        vbox:
                            # text
                            $ tess_volume = persistent._character_volume.get("tess",1.0)
                            imagebutton idle "gui/voiceicons/tess.png" hover "gui/voiceicons/tess.png" selected_foreground "scarlet_bar_fg" action SetVariable("select_voice","tess") at help_icons tooltip __("Set Tess' voice volume.")
                            text "[tess_volume:.0%]" size 18 xalign 1.0 outlines [(absolute(1), "#ff7152", absolute(0), absolute(0))] ypos -67 xoffset 1
                        if renpy.has_label("nextexit_start"):
                            vbox:
                                # text
                                $ cassi_volume = persistent._character_volume.get("cassi",1.0)
                                imagebutton idle "gui/voiceicons/cassi.png" hover "gui/voiceicons/cassi.png" selected_foreground "scarlet_bar_fg" action SetVariable("select_voice","cassi") at help_icons tooltip __("Set Cassi's voice volume.")
                                text "[cassi_volume:.0%]" size 18 xalign 1.0 outlines [(absolute(1), "#ff7152", absolute(0), absolute(0))] ypos -67 xoffset 1
                        vbox:
                            # text
                            $ generic_volume = persistent._character_volume.get("additional_va",1.0)
                            imagebutton idle "gui/voiceicons/generic.png" hover "gui/voiceicons/generic.png" selected_foreground "scarlet_bar_fg" action SetVariable("select_voice","additional_va") at help_icons tooltip __("Set voice volume of additional characters.")
                            text "[generic_volume:.0%]" size 18 xalign 1.0 outlines [(absolute(1), "#ff7152", absolute(0), absolute(0))] ypos -67 xoffset 1

                    if ("SourceHan" in getConfiguredFontFace()):
                        null height -36
                    elif (getCurrentLocalisationID() == "russian"):
                        null height -36
                    else:
                        null height -10

                    if (select_voice == "additional_va"):
                        label __("Additional Voices' Volume") xalign 0.5
                    elif (select_voice == "amber"):
                        label __("Amber's Volume") xalign 0.5
                    elif (select_voice == "marina"):
                        label __("Marina's Volume") xalign 0.5
                    elif (select_voice == "mariah"):
                        label __("Mariah's Volume") xalign 0.5
                    elif (select_voice == "joseph"):
                        label __("Joseph's Volume") xalign 0.5
                    elif (select_voice == "tess"):
                        label __("Tess's Volume") xalign 0.5
                    elif (select_voice == "cassi"):
                        label __("Cassi's Volume") xalign 0.5
                    else:
                        label __("[select_voice!c]'s Volume") xalign 0.5

                    bar value SetCharacterVolume(select_voice) style "withinoptions_slider" xmaximum 320 xalign 0.5 tooltip __("Individual voice volumes are set as a fraction of the Master VA volume.")

image scarlet_bar_fg:
    Transform(Solid("#ff7152",xsize=51,ysize=3),xalign=0.5,yalign=1.1)
default select_voice = "amber"
screen options_access():

    add "gui/options assets/accessbox.png" xalign 0.5 ypos .309
    hbox:
        xalign 0.5 ypos 0.267
        vbox:
            xalign 0.5 xsize 566 ysize (320 if not ("SourceHan" in getConfiguredFontFace()) else 360)
            label __("Text") xalign 0.5 background Transform("gui/options assets/texthead.png",xalign=1.0,ypos=-20,xoffset=30)
            vbox:
                xsize 540
                style_prefix "withinoptions"
                hbox:
                    xfill True
                    xalign .5

                    vbox:
                        xalign 0.5
                        label __("Color") xalign 0.5
                        textbutton __("Low Contrast{space=10}") action SetField(persistent,"text_contrast",False):
                            text_color darktheme_text[0] xalign 0.5
                            tooltip __("The default dialogue text. An off-white color in the dark theme, or an off-black color in the light theme.")
                        textbutton __("High Contrast{space=10}") action SetField(persistent,"text_contrast",True):
                            text_color darktheme_text[3] xalign 0.5
                            tooltip __("Extra contrast for dialogue text. Text will be white in the dark theme, and black in the light theme.")

                    if (not "SourceHan" in getConfiguredFontFace() and not "russian" in str(getCurrentLocalisationID())):
                        vbox:
                            xalign 0.5
                            label __("Font") xalign 0.5
                            textbutton "{font=gui/fonts/CabinCondensed-Regular.ttf}Cabin Condensed{/font}{space=10}" action [ Function(setFontToFontAtPath, "gui/fonts/CabinCondensed-Regular.ttf"), SelectedIf(getConfiguredFontFace() == "gui/fonts/CabinCondensed-Regular.ttf") ] xalign 0.5 tooltip __("Change the font of dialogue text.")
                            textbutton "{font=gui/fonts/OpenDyslexic-Regular.otf}{size=-6}OpenDyslexic{/size}{/font}{space=10}" action [ Function(setFontToFontAtPath, "gui/fonts/OpenDyslexic-Regular.otf"), SelectedIf(getConfiguredFontFace() == "gui/fonts/OpenDyslexic-Regular.otf") ] xalign 0.5 tooltip __("Change the font of dialogue text.")
                            textbutton "{font=gui/fonts/Martel-Bold.ttf}{size=-6}Martel{/size}{/font}{space=10}" action [ Function(setFontToFontAtPath, "gui/fonts/Martel-Bold.ttf"), SelectedIf(getConfiguredFontFace() == "gui/fonts/Martel-Bold.ttf") ] xalign 0.5 tooltip __("Change the font of dialogue text.")

                    vbox:
                        xalign 0.5
                        label __("Size") xalign 0.5
                        textbutton __("Regular{space=10}") action [ Function(setFontSizePreset, "regular"), SelectedIf(getConfiguredFontSizePreset() == "regular") ] xalign 0.5 tooltip __("Change the size of dialogue text.")
                        textbutton __("Large{space=10}") action [ Function(setFontSizePreset, "large"), SelectedIf(getConfiguredFontSizePreset() == "large") ] xalign 0.5 tooltip __("Change the size of dialogue text.")

                null height 0

                vbox:
                    yalign 1.0 xalign 0.5
                    label __("Text Spacing") xalign 0.5
                    bar value FieldValue(persistent, 'pref_text_kerning', 1.0, max_is_zero=False, offset=0, step=.2) style "withinoptions_slider" xmaximum 320 xalign 0.5 yalign 1.0 tooltip __("Change the kerning between characters of the dialogue text.")

        vbox:
            xalign 0.5 xsize 566 ysize (320 if not ("SourceHan" in getConfiguredFontFace()) else 360)
            label __("Textbox") xalign 0.5 background Transform("gui/options assets/textboxhead.png",xalign=1.0,ypos=-20,xoffset=60)
            vbox:
                style_prefix "withinoptions"
                xalign 0.5
                vbox:
                    xalign 0.5 ypos -10
                    label __("Theme") xalign 0.5
                    textbutton __("Dark{#Dark colors}{space=10}") action SetField(persistent,"theme","dark") xalign 0.5 tooltip __("The default dark theme features light text on a dark background.")
                    textbutton  __("Light{#Light colors}{space=10}") action SetField(persistent,"theme","light") xalign 0.5 tooltip __("The light theme features dark text on a light background.")
                null height 5
                vbox:
                    yalign 1.0 xalign 0.5
                    label __("Textbox Opacity") xalign 0.5
                    bar value FieldValue(persistent,"say_window_alpha",1.0) style "withinoptions_slider" xmaximum 320 xalign 0.5 yalign 1.0 tooltip __("Change the transparency of the dialogue window.")

        vbox:
            xalign 0.5 xsize 566
            label __("Sound") xalign 0.5 background Transform("gui/options assets/soundhead.png",xalign=1.0,ypos=-20,xoffset=60)
            vbox:
                style_prefix "withinoptions" xalign 0.5
                # label __("Audio Aid Toggles") xalign 0.5
                vbox:
                    style_prefix "options_radio" xalign 0.5
                    hbox:
                        xsize (280 if (getCurrentLocalisationID() != "fr" and getCurrentLocalisationID() != "russian") else 360)
                        textbutton __("Music Cues{space=15}") action persistentToggle("music_cues") xfill True text_align 0.0 text_xalign 0.0 tooltip __("Toggle On and music changes will be indicated by displaying the new track title in the corner of the screen.")
                    hbox:
                        xsize (280 if (getCurrentLocalisationID() != "fr" and getCurrentLocalisationID() != "russian") else 360)
                        textbutton __("Sound Cues{space=15}") action persistentToggle("sound_cues") xfill True text_align 0.0 text_xalign 0.0 tooltip __("Toggle On and sound effects will have a text description in the corner of the screen.")
                    hbox:
                        xsize (280 if (getCurrentLocalisationID() != "fr" and getCurrentLocalisationID() != "russian") else 360)
                        textbutton __("Text to Speech{space=15}") action Preference("self voicing","toggle") xfill True text_align 0.0 text_xalign 0.0 tooltip __("Toggle On to activate computer self-voicing.")
                    # hbox:
                    #     xsize (280 if (getCurrentLocalisationID() != "fr" and getCurrentLocalisationID() != "russian") else 360)
                    #     textbutton __("VFX Descriptions{space=15}") action persistentToggle("visual_text_help") xfill True text_align 0.0 text_xalign 0.0 tooltip __("Toggle On and additional narration will describe visual effects of the game when necessary.")
            frame:
                background Solid("#241e1c")
                xsize 350 ysize 24 xalign 1.0 ypos 3.5 xpadding 0 top_padding 13 bottom_padding 0 xmargin 0 ymargin 0
                textbutton __("{image=gui/options assets/additional.png} Additional Options") text_size 24 action ToggleScreen("_accessibility") xalign 0.0 yalign 1.0 background None text_align 0.0 yoffset 4 tooltip __("View even more accessibility options. These features are unsupported.")
