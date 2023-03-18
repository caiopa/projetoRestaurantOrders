import analyze_log as analyze
from collections import Counter
class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        return self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        return analyze.most_common_food(self.orders, customer)

    def get_never_ordered_per_customer(self, customer):
        return analyze.never_ask(self.orders, customer)

    def get_days_never_visited_per_customer(self, customer):
        return analyze.never_went(self.orders, customer)

    def count_by_days(self):
        days_list = [item[2] for item in self.orders]
        most_common = Counter(days_list).most_common()
        return most_common

    def get_busiest_day(self):
        most_common = self.count_by_days()
        return most_common[0][0]

    def get_least_busy_day(self):
        most_common = self.count_by_days()
        return most_common[-1][0]
    
