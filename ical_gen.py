# Testing ical generation via ChatGPT

from datetime import datetime, timedelta
from icalendar import Calendar, Event

def create_event(summary, dtstart, duration):
    event = Event()
    event.add('summary', summary)
    event.add('dtstart', dtstart)
    event.add('duration', duration)
    return event

def main():
    cal = Calendar()

    # Fixed times
    bedtime = datetime(2023, 3, 26, 21, 0)
    wake_time = datetime(2023, 3, 27, 5, 0)
    sleep_duration = timedelta(hours=8)

    # Work
    work_start = datetime(2023, 3, 28, 7, 0)
    work_duration = timedelta(hours=8)
    commute_duration = timedelta(hours=1)

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    work_days = [False, True, False, True, False, False, False]
    homework_hours = 2
    internship_hours = 1

    # Gym
    gym_duration = timedelta(hours=1)
    gym_days = [True, False, True, False, True, False, False]

    # Meal planning
    meal_planning_duration = timedelta(hours=2)

    # Piano practice
    piano_duration = timedelta(minutes=30)

    # Reading
    reading_duration = timedelta(minutes=30)

    for i in range(7):
        day = datetime(2023, 3, 26) + timedelta(days=i)
        work_day = work_days[i]
        gym_day = gym_days[i]

        if work_day:
            cal.add_component(create_event('Work', work_start, work_duration))
            cal.add_component(create_event('Commute', work_start - commute_duration, commute_duration))
            cal.add_component(create_event('Commute', work_start + work_duration, commute_duration))

        cal.add_component(create_event('Homework', wake_time + timedelta(hours=i * homework_hours), timedelta(hours=homework_hours)))
        cal.add_component(create_event('Internship efforts', wake_time + timedelta(hours=i * internship_hours), timedelta(hours=internship_hours)))

        if gym_day:
            cal.add_component(create_event('Gym', wake_time + timedelta(hours=7), gym_duration))

        if i == 0:  # Sunday
            cal.add_component(create_event('Meal planning', wake_time + timedelta(hours=7), meal_planning_duration))

        cal.add_component(create_event('Piano practice', bedtime - piano_duration - reading_duration, piano_duration))
        cal.add_component(create_event('Reading', bedtime - reading_duration, reading_duration))
        cal.add_component(create_event('Sleep', bedtime, sleep_duration))

        bedtime += timedelta(days=1)
        wake_time += timedelta(days=1)
        work_start += timedelta(days=1)

    with open('optimal_schedule.ics', 'wb') as f:
        f.write(cal.to_ical())

if __name__ == '__main__':
    main()
