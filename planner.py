import datetime

class Planner:
    def init(self):
        self.events = []

    def add_event(self, name, date, time):
        event = {'name': name, 'date': date, 'time': time}
        self.events.append(event)

    def remove_event(self, name):
        for event in self.events:
            if event['name'] == name:
                self.events.remove(event)

    def get_next_event(self):
        now = datetime.datetime.now()
        for event in self.events:
            event_time = datetime.datetime.strptime(event['date'] + ' ' + event['time'], '%Y-%m-%d %H:%M')
        if event_time > now:
            return event
        return None

planner = Planner()


planner.add_event('Meeting with client', '2022-05-01', '14:00')

next_event = planner.get_next_event()
print(next_event) # {'name': 'Meeting with client', 'date': '2022-05-01', 'time': '14:00'}

planner.remove_event('Meeting with client')

next_event = planner.get_next_event()
print(next_event) # None