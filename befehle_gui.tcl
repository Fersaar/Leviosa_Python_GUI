#############################################################################
# Generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#  Aug 07, 2020 12:10:51 PM CEST  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #ffffff
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ffffff
set vTcl(actual_gui_menu_analog) #ffffff
set vTcl(actual_gui_menu_bg) #ffffff
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ffffff
set vTcl(active_menu_fg) #000000
}




proc vTclWindow.top42 {base} {
    global vTcl
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 824x352+520+339
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 3844 1057
    wm minsize $top 140 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Befehle"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $top.tLa49 \
        -text Sollwerte -width 220 -height 115 
    vTcl:DefineAlias "$top.tLa49" "TLabelframe1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.tLa49
    ttk::entry $site_3_0.tEn51 \
        -font TkTextFont -textvariable nullpunkt_offset -foreground {} \
        -background {} -takefocus {} -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn51" "TEntry1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu52 \
        -command btn_send_nullpunkt_offset -takefocus {} -text Send 
    vTcl:DefineAlias "$site_3_0.tBu52" "TButton_Send_Offset" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_3_0.tLa63 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -text Nullpunkt: 
    vTcl:DefineAlias "$site_3_0.tLa63" "TLabel2" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_3_0.tLa80 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -text {Sollwert: } 
    vTcl:DefineAlias "$site_3_0.tLa80" "TLabel2_15" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn81 \
        -font TkTextFont -textvariable sollwert -foreground {} -background {} \
        -takefocus {} -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn81" "TEntry1_1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu82 \
        -command btn_send_sollwert -takefocus {} -text Send 
    vTcl:DefineAlias "$site_3_0.tBu82" "TButton_Send_Offset_16" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_3_0.tLa45 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -text Bias: 
    vTcl:DefineAlias "$site_3_0.tLa45" "TLabel2_4" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn46 \
        -font TkTextFont -textvariable bias -foreground {} -background {} \
        -takefocus {} -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn46" "TEntry1_5" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu47 \
        -command btn_send_bias -takefocus {} -text Send 
    vTcl:DefineAlias "$site_3_0.tBu47" "TButton_Send_Offset_6" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.tEn51 \
        -in $site_3_0 -x 80 -y 50 -width 66 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tBu52 \
        -in $site_3_0 -x 160 -y 50 -width 48 -height 29 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tLa63 \
        -in $site_3_0 -x 10 -y 50 -anchor nw -bordermode ignore 
    place $site_3_0.tLa80 \
        -in $site_3_0 -x 10 -y 20 -width 67 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn81 \
        -in $site_3_0 -x 80 -y 20 -width 66 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tBu82 \
        -in $site_3_0 -x 160 -y 20 -width 48 -height 29 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tLa45 \
        -in $site_3_0 -x 10 -y 80 -width 67 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn46 \
        -in $site_3_0 -x 80 -y 80 -width 66 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tBu47 \
        -in $site_3_0 -x 160 -y 80 -width 48 -height 29 -anchor nw \
        -bordermode ignore 
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $top.tLa53 \
        -text PID -width 220 -height 185 
    vTcl:DefineAlias "$top.tLa53" "TLabelframe2" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.tLa53
    ttk::label $site_3_0.tLa54 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -text P: 
    vTcl:DefineAlias "$site_3_0.tLa54" "TLabel1" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_3_0.tLa55 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -text I: 
    vTcl:DefineAlias "$site_3_0.tLa55" "TLabel1_1" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_3_0.tLa56 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -text D: 
    vTcl:DefineAlias "$site_3_0.tLa56" "TLabel1_2" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn58 \
        -font TkTextFont -textvariable kp -foreground {} -background {} \
        -takefocus {} -cursor fleur 
    vTcl:DefineAlias "$site_3_0.tEn58" "TEntry_Kp" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn59 \
        -font TkTextFont -textvariable ki -foreground {} -background {} \
        -takefocus {} -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn59" "TEntry_Ki" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn60 \
        -font TkTextFont -textvariable kd -foreground {} -background {} \
        -takefocus {} -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn60" "TEntry_Kd" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TCheckbutton -background $vTcl(actual_gui_bg)
    ttk::style configure TCheckbutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TCheckbutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::checkbutton $site_3_0.tCh61 \
        -variable PoM -takefocus {} -text PoM 
    vTcl:DefineAlias "$site_3_0.tCh61" "TCheckbutton1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu62 \
        -command btn_send_pid_values -takefocus {} -text Send 
    vTcl:DefineAlias "$site_3_0.tBu62" "TButtonSend_PID" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.tLa54 \
        -in $site_3_0 -x 10 -y 30 -anchor nw -bordermode ignore 
    place $site_3_0.tLa55 \
        -in $site_3_0 -x 10 -y 60 -width 15 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tLa56 \
        -in $site_3_0 -x 10 -y 90 -width 25 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tEn58 \
        -in $site_3_0 -x 40 -y 30 -width 126 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tEn59 \
        -in $site_3_0 -x 40 -y 60 -width 126 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tEn60 \
        -in $site_3_0 -x 40 -y 90 -width 126 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tCh61 \
        -in $site_3_0 -x 10 -y 120 -anchor nw -bordermode ignore 
    place $site_3_0.tBu62 \
        -in $site_3_0 -x 20 -y 150 -width 178 -relwidth 0 -height 29 \
        -relheight 0 -anchor nw -bordermode ignore 
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $top.tLa64 \
        -text Overwrite -width 250 -height 215 
    vTcl:DefineAlias "$top.tLa64" "TLabelframe3" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.tLa64
    ttk::label $site_3_0.tLa65 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -text Zone0: 
    vTcl:DefineAlias "$site_3_0.tLa65" "TLabel3" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_3_0.tLa66 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -text Zone1: 
    vTcl:DefineAlias "$site_3_0.tLa66" "TLabel3_6" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_3_0.tLa67 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -text Zone2: 
    vTcl:DefineAlias "$site_3_0.tLa67" "TLabel3_7" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_3_0.tLa68 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -text Zone3: 
    vTcl:DefineAlias "$site_3_0.tLa68" "TLabel3_8" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn69 \
        -font TkTextFont -textvariable overwrite0 -foreground {} \
        -background {} -takefocus {} -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn69" "TEntry_Ovewrite1" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn70 \
        -font TkTextFont -textvariable overwrite1 -foreground {} \
        -background {} -takefocus {} -cursor fleur 
    vTcl:DefineAlias "$site_3_0.tEn70" "TEntry_Ovewrite2" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn71 \
        -font TkTextFont -textvariable overwrite2 -foreground {} \
        -background {} -takefocus {} -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn71" "TEntry_Ovewrite3" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn72 \
        -font TkTextFont -textvariable overwrite3 -foreground {} \
        -background {} -takefocus {} -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn72" "TEntry_Ovewrite4" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu73 \
        -command btn_send_overwrite -takefocus {} -text overwrite 
    vTcl:DefineAlias "$site_3_0.tBu73" "TButton_overwrite" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu74 \
        -command btn_set_automatic -takefocus {} -text automatic 
    vTcl:DefineAlias "$site_3_0.tBu74" "TButton_regelung" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_3_0.tLa43 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -text GND: 
    vTcl:DefineAlias "$site_3_0.tLa43" "TLabel3_2" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn44 \
        -font TkTextFont -textvariable overwrite_gnd -foreground {} \
        -background {} -takefocus {} -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn44" "TEntry_OvewriteGND" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.tLa65 \
        -in $site_3_0 -x 10 -y 20 -anchor nw -bordermode ignore 
    place $site_3_0.tLa66 \
        -in $site_3_0 -x 10 -y 50 -width 46 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tLa67 \
        -in $site_3_0 -x 10 -y 80 -width 46 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tLa68 \
        -in $site_3_0 -x 10 -y 110 -width 46 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn69 \
        -in $site_3_0 -x 70 -y 20 -anchor nw -bordermode ignore 
    place $site_3_0.tEn70 \
        -in $site_3_0 -x 70 -y 50 -width 166 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn71 \
        -in $site_3_0 -x 70 -y 80 -width 166 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn72 \
        -in $site_3_0 -x 70 -y 110 -width 166 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tBu73 \
        -in $site_3_0 -x 20 -y 170 -anchor nw -bordermode ignore 
    place $site_3_0.tBu74 \
        -in $site_3_0 -x 130 -y 170 -width 98 -height 29 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tLa43 \
        -in $site_3_0 -x 10 -y 140 -width 46 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn44 \
        -in $site_3_0 -x 70 -y 140 -width 166 -height 25 -anchor nw \
        -bordermode ignore 
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $top.tLa76 \
        -text sonstiges -width 250 -height 85 
    vTcl:DefineAlias "$top.tLa76" "sonstiges" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.tLa76
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu77 \
        -command btn_send_off -takefocus {} -text aus 
    vTcl:DefineAlias "$site_3_0.tBu77" "TButton1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu78 \
        -command btn_send_offsweep -takefocus {} -text aus(sweep) 
    vTcl:DefineAlias "$site_3_0.tBu78" "TButton1_13" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu79 \
        -command btn_send_fullon -takefocus {} -text full_on 
    vTcl:DefineAlias "$site_3_0.tBu79" "TButton1_14" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.tBu77 \
        -in $site_3_0 -x 10 -y 20 -width 58 -relwidth 0 -height 29 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu78 \
        -in $site_3_0 -x 70 -y 20 -width 88 -relwidth 0 -height 29 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu79 \
        -in $site_3_0 -x 10 -y 50 -width 58 -relwidth 0 -height 29 \
        -relheight 0 -anchor nw -bordermode ignore 
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $top.tLa43 \
        -text sweep -width 220 -height 155 
    vTcl:DefineAlias "$top.tLa43" "TLabelframe2_1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.tLa43
    ttk::label $site_3_0.tLa54 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -text delay: 
    vTcl:DefineAlias "$site_3_0.tLa54" "TLabel1_2" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_3_0.tLa55 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -text dec: 
    vTcl:DefineAlias "$site_3_0.tLa55" "TLabel1_2" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $site_3_0.tLa56 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -text start: 
    vTcl:DefineAlias "$site_3_0.tLa56" "TLabel1_3" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn58 \
        -font TkTextFont -textvariable sweep_delay -foreground {} \
        -background {} -takefocus {} -cursor fleur 
    vTcl:DefineAlias "$site_3_0.tEn58" "TEntry_Kp_4" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn59 \
        -font TkTextFont -textvariable sweep_dec -foreground {} \
        -background {} -takefocus {} -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn59" "TEntry_Ki_5" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $site_3_0.tEn60 \
        -font TkTextFont -textvariable sweep_start -foreground {} \
        -background {} -takefocus {} -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.tEn60" "TEntry_Kd_6" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu62 \
        -command btn_send_sweep_values -takefocus {} -text Send 
    vTcl:DefineAlias "$site_3_0.tBu62" "TButtonSend_sweep" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.tLa54 \
        -in $site_3_0 -x 10 -y 30 -anchor nw -bordermode ignore 
    place $site_3_0.tLa55 \
        -in $site_3_0 -x 10 -y 60 -width 45 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tLa56 \
        -in $site_3_0 -x 10 -y 90 -width 45 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tEn58 \
        -in $site_3_0 -x 60 -y 30 -width 126 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tEn59 \
        -in $site_3_0 -x 60 -y 60 -width 126 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tEn60 \
        -in $site_3_0 -x 60 -y 90 -width 126 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu62 \
        -in $site_3_0 -x 20 -y 120 -width 178 -relwidth 0 -height 29 \
        -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tLa49 \
        -in $top -x 20 -y 10 -width 220 -relwidth 0 -height 115 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa53 \
        -in $top -x 20 -y 130 -width 220 -relwidth 0 -height 185 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa64 \
        -in $top -x 260 -y 10 -width 250 -relwidth 0 -height 215 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa76 \
        -in $top -x 260 -y 230 -width 250 -relwidth 0 -height 85 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa43 \
        -in $top -x 520 -y 10 -width 220 -relwidth 0 -height 155 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

