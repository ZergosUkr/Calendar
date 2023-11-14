import calendar
import datetime
import PySimpleGUI as sg

class CalendarDisplay:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def get_today_date(self):
        return datetime.date.today()

    def display_calendar(self):
        cal = calendar.month(self.year, self.month)
        return cal

    def show_calendar(self):
        today = self.get_today_date()

        layout = [
            [sg.Text(f"Сьогоднішня дата: {today.strftime('%d/%m/%Y')}")],
            [sg.Text(f"Календар на {calendar.month_name[self.month]} {self.year}:")],
            [sg.Multiline(self.display_calendar(), size=(30, 10), key='-OUTPUT-', disabled=True)],
            [sg.Button('Вийти')]
        ]

        window = sg.Window('Календар', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Вийти':
                break

        window.close()

def main():
    today = datetime.date.today()
    year = today.year
    month = today.month

    calendar_display = CalendarDisplay(year, month)
    calendar_display.show_calendar()

if __name__ == "__main__":
    main()
