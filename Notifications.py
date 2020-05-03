# Based on https://www.protechtraining.com/blog/post/tutorial-the-observer-pattern-in-python-879

class NotificationSubscriber:
    
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
    def update(self, leave_type):
        if self.role == 'manager':
            print(f'{self.name}, you have a request for your approval: {leave_type}')
        elif self.role == 'supervisor':
            print(f'{self.name}, you have a request to add to the calendar: {leave_type}')
        elif self.role == 'employee':
            print(f'{self.name}, your {leave_type} has been updated')
    
        
class NotificationPublisher:
    def __init__(self, events):
        # maps event names to subscribers
        # str -> dict
        self.events = { event : dict()
                          for event in events }
        
    def get_subscribers(self, event):
        return self.events[event]
    
    def register(self, event, who, callback=None):
        if callback == None:
            callback = getattr(who, 'update')
        self.get_subscribers(event)[who] = callback
        
    def unregister(self, event, who):
        del self.get_subscribers(event)[who]
        
    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)
            
            
