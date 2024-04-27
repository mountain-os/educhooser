import os
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Vte', '2.91')

from gi.repository import Gtk, Vte
from gi.repository import GLib

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,
                            title='Edu Chooser')
        self.set_default_size(500, 500)
        self.set_icon_from_file("/usr/share/icons/hicolor/scalable/apps/edu.svg")
        
        # Grid
        grid = Gtk.Grid()
        grid.set_row_homogeneous(True)
        grid.set_column_homogeneous(True)
        self.add(grid)

        # Labels
        label = Gtk.Label()
        label.set_markup('''<big><b>Choose what kind of educational programs you want. \n You can change or remove them again later if you want.</b></big>''')
        label.set_halign(Gtk.Align.START)
        label.set_justify(Gtk.Justification.CENTER)
        self.add(label)

        pri_label = Gtk.Label()
        pri_label.set_markup('''<big>Educational tools for children aged 3-11. This includes Gcompris, Scratch, TuxMath and GNOME Paint</big>''')
        pri_label.set_line_wrap(True)
        pri_label.set_justify(Gtk.Justification.CENTER)
        self.add(pri_label)

        sec_label = Gtk.Label()
        sec_label.set_markup('''<big>Educational tools for students aged 11-16. This includes KDevelop, Kalzium, LibreCAD, Kalgebra, KGeography and Marble</big>''')
        sec_label.set_line_wrap(True)
        sec_label.set_justify(Gtk.Justification.CENTER)
        self.add(sec_label)
        
        ter_label = Gtk.Label()
        ter_label.set_markup('''<big>Educational tools for post-16 students. This includes Fritzing, Scilab, LibreCAD, Kig and Chemtool</big>''')
        ter_label.set_line_wrap(True)
        ter_label.set_justify(Gtk.Justification.CENTER)
        self.add(ter_label)

        a_label = Gtk.Label()
        a_label.set_markup('<big>This includes all of the educational programs.</big>')
        a_label.set_justify(Gtk.Justification.CENTER)
        self.add(a_label)

        mr_inf = Gtk.Label()
        mr_inf.set_markup('''<a href=\"mountainlinuxos.wordpress.com/eduice\" title=\"EduIce Editions\">For more information about the different editions follow this link</a>''')
        mr_inf.set_justify(Gtk.Justification.CENTER)
        self.add(mr_inf)

        # Button
        self.pri_button = Gtk.Button(label='Install EduIce Primary')
        self.pri_button.connect('clicked', self.primary)
        self.add(self.pri_button)

        self.sec_button = Gtk.Button(label='Install EduIce Secondary')
        self.sec_button.connect('clicked', self.secondary)
        self.add(self.sec_button)
        
        self.ter_button = Gtk.Button(label='Install EduIce Tertiary')
        self.ter_button.connect('clicked', self.tertiary)
        self.add(self.ter_button)

        self.a_button = Gtk.Button(label='Install EduIce All')
        self.a_button.connect('clicked', self.all)
        self.add(self.a_button)

        # Add buttons
        grid.add(label)
        grid.attach_next_to(self.pri_button, label, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(pri_label, self.pri_button, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.sec_button, self.pri_button, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(sec_label, self.sec_button, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.ter_button, self.sec_button, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(ter_label, self.ter_button, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.a_button, self.ter_button, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(a_label, self.a_button, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(mr_inf, self.a_button, Gtk.PositionType.BOTTOM, 1, 1)

    # Button Function
    def primary(self, widget):
        global tool
        tool = 'EduIce Primary'
        global packages
        packages = ['gnome-paint', 'tuxtype', 'tuxmath', 'kanagram', 'gcompris (flatpak)',
                    'scratch (flatpak)']
        global pkg
        pkg = "eduice-primary"
        dialog = InstallEdu(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            dialog.destroy()
            win = InstallProcess()
            win.show_all()
            win.connect('delete-event', Gtk.main_quit)
            Gtk.main()
        elif response == Gtk.ResponseType.CANCEL:
            dialog.destroy()
    
    def secondary(self, widget):
        global tool
        tool = 'EduIce Secondary'
        global packages
        packages = ['gimp', 'kalgebra', 'inkscape', 'marble', 'kdenlive', 'kdevelop',
                    'kgeography', 'kwave', 'kwordquiz', 'librecad', 'subtitlecomposer', 'fritzing',
                    'chemtool', 'step', 'stellarium', 'kalzium', 'minuet', 'qalculate (flatpak)']
        
        global pkg
        pkg = "eduice-secondary"
        dialog = InstallEdu(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            dialog.destroy()
            win = InstallProcess()
            win.show_all()
            win.connect('delete-event', Gtk.main_quit)
            Gtk.main()
        elif response == Gtk.ResponseType.CANCEL:
            dialog.destroy()
            
    def tertiary(self, widget):
        global tool
        tool = 'EduIce Tertiary'
        global packages
        packages = ['fritzing', 'kdevelop', 'librecad', 'chemtool', 'step', 'scilab', 'rocs', 
                    'labplot', 'qalculate (flatpak)']
        global pkg
        pkg = "eduice-tertiary"
        dialog = InstallEdu(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            dialog.destroy()
            win = InstallProcess()
            win.show_all()
            win.connect('delete-event', Gtk.main_quit)
            Gtk.main()
        elif response == Gtk.ResponseType.CANCEL:
            dialog.destroy()
    
    def all(self, widget):
        global tool
        tool = 'EduIce All'
        global packages
        packages = ['gnome-paint', 'gimp', 'kalgebra', 'inkscape', 'marble', 'kdenlive', 
                    'kdevelop', 'kgeography', 'kwave', 'kwordquiz', 'librecad', 'subtitlecomposer',
                    'fritzing', 'chemtool', 'tuxtype', 'tuxmath', 'step', 'stellarium', 'kalzium',
                    'scilab', 'minuet', 'rocs', 'kig', 'ktechlab', 'labplot', 'kanagram']
        global pkg
        pkg = "eduice-all"
        dialog = InstallEdu(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            dialog.destroy()
            win = InstallProcess()
            win.show_all()
            win.connect('delete-event', Gtk.main_quit)
            Gtk.main()
        elif response == Gtk.ResponseType.CANCEL:
            dialog.destroy()

class InstallEdu(Gtk.Dialog):
    def __init__(self, parent):
        name = 'Install ' + tool
        Gtk.Dialog.__init__(self, name, parent, Gtk.DialogFlags.MODAL, (
            'Cancel', Gtk.ResponseType.CANCEL,
            'Continue', Gtk.ResponseType.OK,         
        ))

        area = self.get_content_area()
        area.add(Gtk.Label('You are about to install ' + tool))
        area.add(Gtk.Label('This will install the following packages: '))
        for i in packages:
            area.add(Gtk.Label(i))
        self.show_all()

class InstallProcess(Gtk.Window):
    def __init__(self):
        ti = 'Installing ' + tool
        Gtk.Window.__init__(self, title=ti)
        self.set_default_size(600, 300)
        self.terminal     = Vte.Terminal()
        self.terminal.spawn_sync(
                Vte.PtyFlags.DEFAULT,
                os.environ['HOME'],
                ["/bin/bash"],
                [],
                GLib.SpawnFlags.DO_NOT_REAP_CHILD,
                None,
                None,
                )
        
        
        com = ""
        if tool == 'EduIce Primary':
            flat = 'flatpak install flathub io.gdevelop.ide -y && flatpak install flathub edu.mit.Scratch -y'
            com = com + flat
        elif tool == 'EduIce Secondary' or 'EduIce Tertiary':
            flat = 'flatpak install flathub io.github.Qalculate -y'
            com = com + flat
        elif tool == 'EduIce All':
            flat = 'flatpak install flathub io.gdevelop.ide -y && flatpak install flathub edu.mit.Scratch -y && flatpak install flathub io.github.Qalculate -y'
        com = str("sudo apt install " + pkg + " -y && " + flat + " && exit \n")
        self.command = com
        command = Gtk.Label("Installing " + tool)
        self.terminal.feed_child(self.command.encode("utf-8"))
        
        # Interface
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.pack_start(command, False, True, 1)
        # Scroll Window
        scroller = Gtk.ScrolledWindow()
        scroller.set_hexpand(True)
        scroller.set_vexpand(True)
        scroller.add(self.terminal)
        box.pack_start(scroller, False, True, 2)
        self.add(box)
        

window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
