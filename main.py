# Theme Park Task

class attraction:
    def __init__(self, name, capacity):
        self._name = name
        self._capacity = capacity
        self._status = "Closed"

    def get_details(self):
        print(f'Attraction: {self._name}\nCapacity: {self._capacity}')
    
    def start(self):
        if self._status == 'Open':
            print('The attraction is starting...')

        else:
            print('Unable to proceed. Plese open the attraction first.')

    def open_attraction(self):
        self._status = 'Open'

    def close_attraction(self):
        self._status = 'Closed'

class thrillRide(attraction):
    def __init__(self, name, capacity, min_height):
        super().__init__(name, capacity)
        self._min_height = min_height
        self._type = 'thrillRide'

    def start(self):
        if self._status == 'Open':
            print(f'Thrill Ride {self._name} is now starting. Hold on tight!')
        else:
            print('Unable to proceed. Plese open the attraction first.')      
    
    def is_eligible(self, height):
        if height < self._min_height:
            return False
        else:
            return True
        
class familyRide(attraction):
    def __init__(self, name, capacity, min_age):
        super().__init__(name, capacity)
        self._min_age = min_age
        self._type = 'familyRide'

    def start(self):
        if self._status == 'Open':
            print(f'Family Ride {self._name} is now starting. Enjoy the fun!')
        else:
            print('Unable to proceed. Plese open the attraction first.')     

    def is_eligible(self, age):
        if age < self._min_age:
            return False
        else:
            return True


class staff:
    def __init__(self, name, role):
        self._name = name
        self._role = role

    def work(self):
        print(f'Staff {self._name} is performing their role: {self._role}')


class manager(staff):
    def __init__(self, name, role):
        super().__init__(name, role)
        self._team = []

    def add_staff(self, staff):
        self._team.append(staff)
    
    def get_team_summary(self):
        count = 1
        for staff in self._team:
            print(f'{count}. {staff._name}     Role: {staff._role}')
            count += 1


class visitor:

    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height
        self._ride_history = []

    def ride(self, attraction):
        if attraction._type == 'thrillRide':
            if attraction.is_eligible(self._height):
                if attraction._status == 'Open':
                    print(f'{self._name} is enjoying the {attraction._name}!')
                    self._ride_history.append(attraction)
                else:
                    print('Unable to proceed. Plese open the attraction first.')
                    return
            else:
                print(f'{self._name} is not eligible for {attraction._name}.')
        
        elif attraction._type == 'familyRide':
            if attraction.is_eligible(self._age):
                if attraction._status == 'Open':
                    print(f'{self._name} is enjoying the {attraction._name}!')
                    self._ride_history.append(attraction)
                else:
                    print('Unable to proceed. Plese open the attraction first.')
                    return
            else:
                print(f'{self._name} is not eligible for {attraction._name}.')

    def view_history(self):
        count = 1
        for ride in self._ride_history:
            print(f'{count}. {ride._name}')
            count += 1



#Task 2
visitor1 = visitor("Alice", 10, 130)
coaster1 = thrillRide("Dragon Coaster", 20, 140)
carousel1 = familyRide("Merry-Go-Round", 30, 4)

coaster1.open_attraction()
carousel1.open_attraction()

visitor1.ride(coaster1)
visitor1.ride(carousel1)

#Task 3
coaster1.start()
carousel1.start()

visitor1.view_history()


