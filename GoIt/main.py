from datetime import datetime

def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today_date = datetime.today().date()
        delta = today_date - given_date
        return delta.days
    except ValueError:
        return "Некоректний формат дати. Будь ласка, використовуйте формат YYYY-MM-DD."

print(get_days_from_today("1990-01-28"))
print(get_days_from_today("некоректна дата"))
