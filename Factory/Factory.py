class pizza(object): 
    def __init__(self): 
        self._price = None
        
    def get_price(self): 
        return self._price
    
class small(pizza): 
    def __init__(self): 
        self._price = 8.5
            
class med(pizza): 
    def __init__(self): 
        self._price = 10.5
            
class large(pizza): 
    def __init__(self): 
        self._price = 11.5
            
class pizzaFactory(object): 
    @staticmethod 
    def create_pizza(pizza_type): 
        if pizza_type == 'small': 
            return small() 
        elif pizza_type == 'med': 
            return med() 
        elif pizza_type == 'large': 
            return large()
            
if __name__ == '__main__': 
    for pizza_type in ('small', 'med', 'large'): 
            print('Price of {0} is {1}'.format(pizza_type, pizzaFactory.create_pizza(pizza_type).get_price()))