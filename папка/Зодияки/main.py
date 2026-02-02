import interface
import zodiac


def p2w():
    day = int(interface.entry.get())
    month = int(interface.entry1.get())
    index = zodiac.define(day, month)
    name = interface.zodiac_names[index]
    file = interface.zodiac_files[index]

    interface.name.config(text=name)
    interface.gif.config(file=f'img/{file}')

interface.button.config(command=p2w)

interface.window.mainloop()

