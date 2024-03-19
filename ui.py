import urwid


class UI:
    palette: list[tuple[str, str, str]] = [
        ("body", "black", "light gray"),
    ]

    COLUMNS_PADDING: int = 2

    def __init__(self):
        self.text_header: str = "Spotify Analytics"

        self.text_exit: urwid.Text = urwid.Text("Press q to exit", align="right")

        left_column_text: list[str] = ["Account Name:", "Number of Liked Tracks:"]
        self.left_column: list[urwid.Text] = [urwid.Text(line) for line in left_column_text]

        self.account_name_text: urwid.Text = urwid.Text("")
        self.num_liked_tracks_text: urwid.Text = urwid.Text("")

        self.left_pile: urwid.Pile = urwid.Pile(
            urwid.Padding(w=w, left=self.COLUMNS_PADDING, right=0)
            for w in self.left_column
        )
        self.right_pile: urwid.Pile = urwid.Pile(
            urwid.Padding(w=w, left=0, right=self.COLUMNS_PADDING)
            for w in [self.account_name_text, self.num_liked_tracks_text]
        )

        self.listbox_content: list = [
            urwid.Padding(w=self.text_exit, left=0, right=self.COLUMNS_PADDING),
            urwid.Columns(widget_list=[self.left_pile, self.right_pile]),
            # urwid.Text(markup="Additional Text Widget", align="center"),
        ]

        self.header: urwid.AttrWrap = urwid.AttrWrap(
            w=urwid.Text(markup=self.text_header, align="center"), attr="header"
        )

        self.listbox: urwid.ListBox = urwid.ListBox(body=urwid.SimpleListWalker(self.listbox_content))
        self.body: urwid.AttrWrap = urwid.AttrWrap(w=self.listbox, attr="body")

        self.frame: urwid.Frame = urwid.Frame(header=self.header, body=self.body)

    def update_account_info(self, account_name: str, num_liked_tracks: int):
        self.account_name_text.set_text(markup=account_name)
        self.num_liked_tracks_text.set_text(markup=str(num_liked_tracks))

    def run(self) -> None:
        urwid.MainLoop(
            widget=self.frame, palette=self.palette, unhandled_input=self.q_exit
        ).run()

    @staticmethod
    def q_exit(key) -> None:
        if key in {"Q", "q"}:
            raise urwid.ExitMainLoop()


class AppUI:
    def __init__(self, client):
        self.ui = UI()
        self.client = client

    def run(self) -> None:
        account_name: str = self.client.get_account_name()
        num_liked_tracks: int = self.client.get_num_liked_tracks()

        self.ui.update_account_info(
            account_name=account_name, num_liked_tracks=num_liked_tracks
        )
        self.ui.run()
