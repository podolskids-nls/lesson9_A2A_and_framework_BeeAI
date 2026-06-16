"""Mock API рейсов (без авторизации)."""
from __future__ import annotations

MOCK_FLIGHTS: dict[str, dict[str, str]] = {
    "SU-123": {
        "airline": "Аэрофлот",
        "route": "Санкт-Петербург (LED) -> Москва (SVO)",
        "status": "По расписанию",
        "departure_time": "10:30",
        "arrival_time": "12:15",
        "terminal": "B",
        "gate": "12",
    },
    "SU-456": {
        "airline": "Аэрофлот",
        "route": "Москва (SVO) -> Казань (KZN)",
        "status": "Задержан на 45 мин",
        "departure_time": "14:00",
        "arrival_time": "15:50",
        "terminal": "D",
        "gate": "7",
    },
}


def lookup(flight_number: str, date: str) -> str:
    fn = flight_number.strip().upper().replace(" ", "")
    rec = MOCK_FLIGHTS.get(fn)
    if not rec:
        return f"Рейс {fn} на {date}: не найден в mock-базе."
    return (
        f"Рейс: {fn}\nДата: {date}\nАвиакомпания: {rec['airline']}\n"
        f"Маршрут: {rec['route']}\nСтатус: {rec['status']}\n"
        f"Вылет: {rec['departure_time']}\nПрилёт: {rec['arrival_time']}\n"
        f"Терминал: {rec['terminal']}, гейт: {rec['gate']}"
    )
