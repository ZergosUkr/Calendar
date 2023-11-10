import calendar
import datetime
import PySimpleGUI as sg

def display_calendar(year, month):
    cal = calendar.month(year, month)
    return cal

def main():
    today = datetime.date.today()
    year = today.year
    month = today.month

    layout = [
        [sg.Text(f"Сьогоднішня дата: {today.strftime('%d/%m/%Y')}")],
        [sg.Text(f"Календар на {calendar.month_name[month]} {year}:")],
        [sg.Multiline(display_calendar(year, month), size=(30, 10), key='-OUTPUT-', disabled=True)],
        [sg.Button('Вийти')]
    ]

    window = sg.Window('Календар', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Вийти':
            break

    window.close()

if __name__ == "__main__":
    main()
