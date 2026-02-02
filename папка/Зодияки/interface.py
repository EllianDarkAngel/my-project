from tkinter import *

window = Tk()
window.title('Зодияки')
window.geometry('300x500')

gif = PhotoImage(file='img/start.gif')

zodiac_names = ['Неправильная дата рождения!',
       'Козерог', 'Водолей', 'Рыбы', 'Овен', 'Телец', 'Близнецы',
           'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец']
zodiac_files = ['start.gif',
'capricorn.gif', 'aquaris.gif', 'pisces.gif', 'aries.gif', 'taurus.gif', 'gemini.gif',
   'cancer.gif', 'leo.gif', 'virgo.gif', 'libra.gif', 'scorpio.gif', 'sagittarius.gif']

frame1 = LabelFrame(text='Дата рождения')
frame1.pack(fill=X)
label1 = Label(frame1, text='Введите день')
label1.grid(column=0, row=0, sticky=E, padx=5, pady=5)
entry = Entry(frame1)
entry.grid(column=1, row=0, sticky=E, padx=5, pady=5)
label2 = Label(frame1, text='Введите месяц')
label2.grid(column=0, row=1, sticky=E, padx=5, pady=5)
entry1 = Entry(frame1)
entry1.grid(column=1, row=1, sticky=E, padx=5, pady=5)
button = Button(frame1, text='Определить знак')
button.grid(column=1, row=2, padx=5, pady=5)

name = Label(text='Сначала введите дату рождения')
name.pack(anchor=CENTER, padx=5, pady=5)
image = Label(image=gif)
image.pack(padx=5, pady=5)

if __name__ == '__main__':
    window.mainloop()