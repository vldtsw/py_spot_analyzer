import urwid
from spotify import SpotifyClient


class UI:
    def __init__(self):
        self.text_header = "Spotify Analytics"

        left_column_text = ["Account Name:", "Number of Liked Tracks:"]
        self.left_column = [urwid.Text(line) for line in left_column_text]

        self.account_name_text = urwid.Text("")
        self.num_liked_tracks_text = urwid.Text("")

        self.left_pile = urwid.Pile(
            urwid.Padding(w=w, left=5, right=0) for w in self.left_column
        )
        self.right_pile = urwid.Pile(
            urwid.Padding(w=w, left=0, right=5)
            for w in [self.account_name_text, self.num_liked_tracks_text]
        )

        self.listbox_content = [
            urwid.Columns([self.left_pile, self.right_pile]),
            urwid.Text(markup="Additional Text Widget", align="center"),
        ]

        self.header = urwid.AttrWrap(
            w=urwid.Text(markup=self.text_header, align="center"), attr="header"
        )

        self.listbox = urwid.ListBox(
            body=urwid.SimpleListWalker(self.listbox_content)
        )
        self.body = urwid.AttrWrap(w=self.listbox, attr="body")

        self.frame = urwid.Frame(header=self.header, body=self.body)

        self.palette = [
            ("body", "black", "light gray", "standout"),
        ]

    def update_account_info(self, account_name, num_liked_tracks):
        self.account_name_text.set_text(account_name)
        self.num_liked_tracks_text.set_text(str(num_liked_tracks))

    def run(self):
        urwid.MainLoop(
            widget=self.frame,
            palette=self.palette,
            unhandled_input=self.q_exit
        ).run()

    @staticmethod
    def q_exit(key):
        if key in {"Q", "q"}:
            raise urwid.ExitMainLoop()


class AppUI:
    def __init__(self):
        self.ui = UI()
        self.client = SpotifyClient()

    def run(self):
        account_name = self.client.get_account_name()
        num_liked_tracks = self.client.get_num_liked_tracks()

        self.ui.update_account_info(account_name, num_liked_tracks)
        self.ui.run()
