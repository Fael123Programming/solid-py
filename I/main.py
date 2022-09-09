from I.classes.employee import *

# I for Interface Segregation Principle.

if __name__ == '__main__':
    e1 = Employee('Maria', '1234/56', 'sales', 'secretary', 3000)
    e1.log_in_to_basic_system()
    m1 = Manager('Pamela', '5678/90', 'marketing', '1st manager', 5000)
    m1.log_in_to_basic_system()
    m1.log_in_to_manager_system()
    d1 = Director('Marcus', '1220/11', 'enterprise resources', '2st manager', 4500)
    d1.log_in_to_basic_system()
    d1.log_in_to_director_system()
    c1 = CEO('Jesmmer', '1122/09', 'general administration', '1st president', 30000)
    c1.log_in_to_basic_system()
    c1.log_in_to_director_system()
    c1.log_in_to_ceo_system()

