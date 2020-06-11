import math

class Pagination:
    def __init__(self, items=[], page_size=10):
        self.items = items
        self.page_size = page_size
        self.page = 1
    
    def __repr__(self):
        return ''
        
    def get_visible_items(self):
        return self.items[(self.page-1)*self.page_size:self.page*self.page_size]
    
    def prev_page(self):
        self.page -= 1
        return self
    
    def next_page(self):
        self.page += 1
        return self
    
    def first_page(self):
        self.page = 1
        return self
    
    def last_page(self):
        self.page = math.ceil(len(self.items) / self.page_size)
        return self
    
    def go_to_page(self, page_number):
        if page_number > math.ceil(len(self.items) / self.page_size):
            self.last_page()
        elif page_number < 1:
            self.first_page()
        else:
            self.page = page_number
            return self
            
    def get_current_page(self):
        return self.page
    
    def get_page_size(self):
        return len(self.items[(self.page-1)*self.page_size:self.page*self.page_size])
    
    def get_items(self):
        return self.items