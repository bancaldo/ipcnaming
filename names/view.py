import wx


class ViewChoice(wx.Frame):
    def __init__(self, parent, controller):
        super(ViewChoice, self).__init__(parent=parent,
                                         title="Naming IPC7231-7251")
        self.controller = controller
        # Layout
        self.panel = PanelChoice(parent=self)
        self.SetSize((550, 200))
        # BINDINGS
        self.Bind(wx.EVT_BUTTON, self.on_quit, self.panel.btn_quit)
        self.Bind(wx.EVT_RADIOBOX, self.on_component_type, self.panel.rb_types)
        self.Bind(wx.EVT_COMBOBOX, self.on_component, self.panel.cb_components)
        self.Centre()

    # noinspection PyUnusedLocal
    def on_quit(self, event):
        """Button Quit callback: Destroy the frame"""
        self.Destroy()

    # noinspection PyUnusedLocal
    def on_component_type(self, event):
        """RadioButton callback: decide what dictionary use"""
        choice = self.panel.rb_types.GetStringSelection()
        components = self.controller.get_components_by_type(choice.upper())
        self.panel.cb_components.Clear()
        self.panel.cb_components.AppendItems(components)

    # noinspection PyUnusedLocal
    def on_component(self, event):
        """ComboBox callback: build the second panel with text entries"""
        component_name = self.panel.cb_components.GetStringSelection()
        type_of = self.panel.rb_types.GetStringSelection()
        prefix, description = component_name.split('_')
        component = self.controller.get_component(type_of, prefix, description)
        self.controller.set_pattern(component.pattern)
        args = component.arguments.split(',')
        title = "IPC7251-7351 for '%s'" % component_name
        child = ViewData(self, title, *args)
        child.Show()


class PanelChoice(wx.Panel):
    def __init__(self, parent):
        super(PanelChoice, self).__init__(parent=parent)
        self.parent = parent
        types = ['PTH', 'SMT']
        components = self.parent.controller.get_components_by_type('PTH')
        # RADIO BUTTONS
        self.rb_types = wx.RadioBox(self, -1, "component type", choices=types,
                                    majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.cb_components = wx.ComboBox(self, -1, "", choices=components,
                                         style=wx.CB_DROPDOWN)
        self.btn_quit = wx.Button(self, label='Quit', size=(550, 40))

        # SIZER
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.rb_types, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND)
        sizer.Add(self.cb_components, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND)
        sizer.Add(self.btn_quit, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND)
        self.SetSizer(sizer)


class ViewData(wx.Frame):
    def __init__(self, parent, title, *args):
        super(ViewData, self).__init__(parent=parent, title=title)
        self.parent = parent
        self.controller = parent.controller
        # Layout
        self.panel = PanelData(self, *args)
        self.SetSize((550, 400))
        # BINDINGS
        self.Bind(wx.EVT_BUTTON, self.on_quit, self.panel.btn_quit)
        self.Bind(wx.EVT_BUTTON, self.on_generate, self.panel.btn_generate)
        self.Centre()

    # noinspection PyUnusedLocal
    def on_quit(self, event):
        """Button Quit callback: Destroy the frame"""
        self.Destroy()

    # noinspection PyUnusedLocal
    def on_generate(self, event):
        """Button Generate callback: get the text entries values"""
        data = []
        widgets = [w for w in self.panel.GetChildren()
                   if isinstance(w, wx.TextCtrl)]
        for widget in widgets:
            value = widget.GetValue()
            if not value:
                wx.MessageBox("You must insert all data!", 'Warning',
                              wx.OK | wx.ICON_EXCLAMATION)
                break
            else:
                data.append(value)

        if len(data) == len(widgets):
            name = self.controller.create_name(data)
            dlg = wx.TextEntryDialog(None, "Copy and Paste below",
                                     "IPC7*51 generated name:", name.upper())
            dlg.SetSize((300, 150))
            if dlg.ShowModal() == wx.ID_OK:
                print dlg.GetValue()
            dlg.Destroy()


class PanelData(wx.Panel):
    def __init__(self, parent, *args):
        super(PanelData, self).__init__(parent=parent)
        self.parent = parent
        self.fields = args
        self.btn_quit = wx.Button(self, label='Quit', size=(180, 40))
        self.btn_generate = wx.Button(self, label='Generate', size=(180, 40))
        text_sizer = wx.FlexGridSizer(rows=len(args), cols=2, hgap=5, vgap=5)
        if self.fields:
            for field in self.fields:
                field_name = wx.StaticText(self, label=field)
                field = wx.TextCtrl(self)
                text_sizer.Add(field_name, 0, wx.EXPAND)
                text_sizer.Add(field, wx.EXPAND)
            text_sizer.AddGrowableCol(1)

        # BUTTONS SIZER
        button_sizer = wx.FlexGridSizer(rows=1, cols=2, hgap=5, vgap=5)
        button_sizer.Add(self.btn_generate, 0, wx.EXPAND)
        button_sizer.Add(self.btn_quit, 0, wx.EXPAND)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text_sizer, 0, wx.EXPAND | wx.ALL, 20)
        sizer.Add(button_sizer, 0, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(sizer)
