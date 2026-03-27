screen gallery_navigation:
    hbox:
        style_prefix "gallery"
        spacing 100

        xalign 0.5
        xoffset -150
        yalign 0.0
        yoffset 150

        textbutton _("Pomni") action ShowMenu("gallery_b")
        textbutton _("Jax") action ShowMenu("gallery_a")
        textbutton _("Ragatha") action ShowMenu("gallery_c")
        textbutton _("Gangle") action ShowMenu("gallery_d")
        textbutton _("Zooble") action ShowMenu("gallery_e")
        textbutton "Return":
            action Return()
            xoffset 300
        

style gallery_button_text:
    idle_color "#606060"
    hover_color "#cc0066"
    selected_color "#cc0066"
    outlines [ (absolute(2), "#fff", absolute(0), absolute(0)) ]
    size 40
