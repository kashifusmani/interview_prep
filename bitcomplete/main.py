# We need to write the logic for creating a simple calendar (think Google calendar) in memory.
# You should think of this as APIs that a UI can call to display the calendar.
# The calendar supports the following functionality:

# 1. Create an event:
#   Write a function that takes in such an input,
#   creates an event
#   and stores it in an in-memory data structure.
# 2. Delete an event:
#   Write a function that deletes an event.
# 3. Retrieve events for a given day:
#   Retrieve all the events for a given day.

# The purpose of this exercise is to write clean and testable code.
# Focus on the edge cases and using the right data structures to have reasonable time complexities.



class Calendar:
    def __init__(self):
        self.events = {}
        self.max_ids = {}

'''
self.events = {
  'abc123': '2023-10-12',
  'xyz789': {title: str, dates: ['2023-10-20', '2023-10-20']} # id: list[]
}

self.dates = {
  '2023-10-12': {'abc123'}, # date: list[id]
  '2023-10-11': {'bvn456'}
}
'''


def create(self, date, event_name):
    # Write validations for date and event_name

    if date not in self.max_ids:
        self.max_ids[date] = 0

    else:
        self.max_ids[date] = self.max_ids[date] + 1

    cur_events = self.events.get(date, {})
    cur_events[self.max_ids[date]] = event_name

    self.events[date] = cur_events

def delete(self, date, event_id):
    # Write validations for date and event_name
    del self.events[date][event_id]

def get_events(self, date):
    # Write validations for date and event_name
    return self.events[date]

def create_multi_day_event(self, dates, event_name):
    for date in dates:
        self.create(date, event_name)

def delete_multi_day_event(self, dates, event_ids):
    i = 0
    while i < len(dates):
        self.delete(dates[i], event_ids[i])
        i += 1


cal = Calendar()

cal.create('2023-10-12', 'A')
cal.create('2023-10-12', 'B')

cal.create('2023-10-11', 'C')
cal.create('2023-10-11', 'D')

print(cal.events)

cal.delete('2023-10-12', 0)
cal.delete('2023-10-11', 0)

# cal.delete(event_id)
print(cal.events)

print(cal.get_events('2023-10-12'))
print(cal.get_events('2023-10-11'))

cal.create_multi_day_event(['2023-10-20', '2023-10-21', '2023-10-22'], 'AWS Training')

# cal.create_multi_day_event(start_date, end_date, event_name)
print(cal.events)

cal.delete_multi_day_event(['2023-10-20', '2023-10-21', '2023-10-22'], [0, 0, 0])

#cal.delete_multi_day_event(event_id)
print(cal.events)
