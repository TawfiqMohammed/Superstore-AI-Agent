# agents/inventory_manager.py

class InventoryManager:
    """Agent 2: Manages real-time stock and pending deliveries."""
    
    def __init__(self):
        print("[Inventory Manager]: Initializing. Inventory database is empty.")
        self.inventory = {}
        self.pending_deliveries = [] # Tracks incoming orders

    def setup_initial_inventory(self, product_list, initial_stock_level):
        """Sets an initial stock level for monitored products."""
        print(f"[Inventory Manager]: Setting initial stock to {initial_stock_level} for monitored products.")
        for product in product_list:
            self.inventory[product] = initial_stock_level
        print("[Inventory Manager]: Initial inventory setup is complete.")

    def process_sale(self, product_name, quantity):
        """Processes a sale and decrements stock."""
        if product_name in self.inventory:
            # Ensure stock doesn't go below zero
            self.inventory[product_name] = max(0, self.inventory[product_name] - quantity)
            # Log only the new stock level for cleaner output
        else:
            print(f"[Inventory Manager]: WARNING! Sale processed for an unmonitored product: '{product_name}'.")

    def get_stock_level(self, product_name):
        """Returns the current stock level for a product."""
        return self.inventory.get(product_name, 0)

    def is_order_pending(self, product_name):
        """Checks if there is an incoming delivery for a product."""
        for delivery in self.pending_deliveries:
            if delivery['product'] == product_name:
                return True
        return False

    def place_reorder(self, product_name, quantity, order_day, lead_time):
        """Places a new order and adds it to the pending deliveries list."""
        arrival_day = order_day + lead_time
        self.pending_deliveries.append({
            'product': product_name,
            'quantity': quantity,
            'arrival_day': arrival_day
        })
        print(f"[Inventory Manager]: Reorder placed for {quantity} units of '{product_name}'. Expected arrival on Day {arrival_day}.")

    def check_and_process_deliveries(self, current_day):
        """Checks for and processes deliveries scheduled for the current day."""
        deliveries_arrived = []
        for delivery in self.pending_deliveries:
            if delivery['arrival_day'] == current_day:
                product = delivery['product']
                quantity = delivery['quantity']
                self.inventory[product] += quantity
                print(f"[Inventory Manager]: DELIVERY ARRIVED! {quantity} units of '{product}' added to stock. New level: {self.inventory[product]}.")
                deliveries_arrived.append(delivery)
        
        # Remove the deliveries that have been processed
        self.pending_deliveries = [d for d in self.pending_deliveries if d not in deliveries_arrived]