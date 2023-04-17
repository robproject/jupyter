from ics import Calendar, Event
from datetime import datetime, timedelta
import pytz

def create_event(name, start_time, end_time, day, week_start):
    event = Event()
    event.name = name
    event.begin = week_start + timedelta(days=day, hours=start_time[0], minutes=start_time[1])
    if end_time is not None:
        event.end = week_start + timedelta(days=day, hours=end_time[0], minutes=end_time[1])
    return event


def main():
    # Initialize calendar and starting date
    calendar = Calendar()
    pst = pytz.timezone('US/Pacific')
    week_start = datetime(2023, 4, 9, tzinfo=pst)

    # Define schedule as (name, start_time, end_time, day)
    schedule = [
        ("Morning routine", (7, 0), (8, 0), 0, week_start),
        ("Classes/study", (8, 0), (13, 0), 0, week_start),
        ("Lunch", (13, 0), (14, 0), 0, week_start),
        ("Classes/study", (14, 0), (17, 0), 0, week_start),
        ("Exercise/relax/hobby", (17, 0), (18, 0), 0, week_start),
        ("Dinner", (18, 0), (19, 0), 0, week_start),
        ("Part-time job/study", (19, 0), (21, 0), 0, week_start),
        ("Relax and unwind", (21, 0), (22, 0), 0, week_start),
        ("Evening routine", (22, 0), (23, 0), 0, week_start)
    ]

    # Add events for weekdays (Monday-Friday)
    for day in range(0, 5):
        for item in schedule:
            event = create_event(item[0], item[1], item[2], day, week_start)
            calendar.events.add(event)

    # Add events for Saturday
    schedule_saturday = [
        ("Morning routine", (8, 0), (9, 0), 5, week_start),
        ("Study/catch up", (9, 0), (12, 0), 5, week_start),
        ("Lunch", (12, 0), (13, 0), 5, week_start),
        ("Errands", (13, 0), (16, 0), 5, week_start),
        ("Exercise/hobby", (16, 0), (18, 0), 5, week_start),
        ("Dinner", (18, 0), (19, 0), 5, week_start),
        ("Socialize/relax", (19, 0), None, 5, week_start)
    ]

    for item in schedule_saturday:
        event = create_event(item[0], item[1], item[2], item[3], week_start)
        calendar.events.add(event)

    # Add events for Sunday
    schedule_sunday = [
        ("Morning routine", (8, 0), (9, 0), 6, week_start),
        ("Study/catch up", (9, 0), (12, 0), 6, week_start),
        ("Lunch", (12, 0), (13, 0), 6, week_start),
        ("Leisure activities", (13, 0), (16, 0), 6, week_start),
        ("Meal prep", (16, 0), (18, 0), 6, week_start),
        ("Dinner", (18, 0), (19, 0), 6, week_start),
        ("Relax/prepare for the week", (19, 0), None, 6, week_start)
    ]

    for item in schedule_sunday:
        event = create_event(item[0], item[1], item[2], item[3], week_start)
        calendar.events.add(event)

    # Save calendar to an iCal file
    with open('schedule.ics', 'w') as f:
        f.writelines(calendar)

if __name__ == '__main__':
    main()

