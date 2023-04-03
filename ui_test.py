import urwid


def q_exit(key):
    if key in {'Q', 'q'}:
        raise urwid.ExitMainLoop()


text_header = "Spotify analytics"

# Define the text for the left and right columns
left_column_text = ["Left Column Text Line 1", "Left Column Text Line 2", "Left Column Text Line 3"]
right_column_text = ["Right Column Text Line 1", "Right Column Text Line 2", "Right Column Text Line 3"]

# Define the widgets for the left and right columns using the text
# left_column = urwid.ListBox(urwid.SimpleListWalker([urwid.Text(line) for line in left_column_text]))
# right_column = urwid.ListBox(urwid.SimpleListWalker([urwid.Text(line) for line in right_column_text]))

# Combine the left and right columns into a Columns widget
# columns = urwid.Columns(widget_list=[left_column, right_column])

listbox_content = [
    urwid.Columns(
        [
            urwid.Padding(urwid.Text(left_column_text), left=2, right=0, min_width=20),
            urwid.Padding(urwid.Text(right_column_text), left=0, right=2, min_width=20)
        ],
    )
]

header = urwid.AttrWrap(urwid.Text(text_header), "header")
listbox = urwid.ListBox(urwid.SimpleListWalker(listbox_content))
frame = urwid.Frame(urwid.AttrWrap(listbox, "body"), header=header)

# Define a palette to set the background color
palette = [
    ("body", "black", "light gray", "standout"),
]

# Set the palette and run the event loop to display the columns
urwid.MainLoop(
    widget=frame,
    palette=palette,
    unhandled_input=q_exit
).run()
