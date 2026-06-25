from pathlib import Path

import toga

active_switch_index = 0


def build(app):
    box = toga.Box(direction="column", margin=20, width=400, height=60)
    open_data_path_button = toga.Button("Open")
    edit_data_path_button = toga.Button("Edit")
    data_path_input = toga.TextInput(
        value=str(Path().absolute()),
        readonly=True,
        flex=1,
    )
    data_frame_content = toga.Box(
        direction="column",
        children=[
            data_path_input,
            toga.Box(
                direction="row",
                children=[
                    open_data_path_button,
                    edit_data_path_button,
                ],
                gap=10,
            ),
        ],
        margin=(3, 10, 0),
        align_items="center",
        gap=2,
        flex=1,
    )
    frame = toga.Frame(
        title="Data folder",
        content=data_frame_content,
        flex=1,
        height=95,
        font_weight="bold",
    )

    def increase_height(widget):
        box.style.height += 5

    def increase_font(widget):
        frame.style.font_size += 1

    box.add(frame)
    box.add(
        toga.Button("Height", on_press=increase_height),
        toga.Button("Font", on_press=increase_font),
    )

    return box


def main():
    return toga.App(
        "First App",
        "org.beeware.toga.examples.tutorial",
        startup=build,
    )


if __name__ == "__main__":
    main().main_loop()
