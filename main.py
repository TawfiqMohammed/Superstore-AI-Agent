# main.py
import random
import time
import os

# Import agent classes from the 'agents' folder
from agents.sales_forecaster import SalesForecaster
from agents.inventory_manager import InventoryManager
from agents.reorder_analyst import ReorderAnalyst

# Import configuration from the config file
import config

# Create the agents folder if it doesn't exist to ensure imports work
# We're simulating running the main loop from the project root
if not os.path.exists('agents'):
    print("WARNING: 'agents' folder not found. Please create it and place agent files inside.")

def run_simulation():
    """Initializes agents and runs the main simulation loop."""
    print("--- Initializing Smart Superstore AI Team ---")
    
    # 1. Initialize all agents
    forecaster = SalesForecaster(config.DATA_FILEPATH)
    inventory = InventoryManager()
    analyst = ReorderAnalyst(inventory, forecaster, config.SAFETY_STOCK_FACTOR)
    
    # 2. Set up the initial inventory
    inventory.setup_initial_inventory(config.PRODUCTS_TO_MONITOR, config.INITIAL_STOCK_LEVEL)
    
    print(f"\n--- Starting {config.SIMULATION_DAYS}-Day Business Simulation ---")
    print("=" * 70)
    
    # 3. Run the simulation loop for each day
    for day in range(1, config.SIMULATION_DAYS + 1):
        # time.sleep(0.05) # Uncomment for a slower, more visible simulation flow
        print(f"\n--- SIMULATION DAY {day} ---")
        
        # At the start of the day, check if any deliveries have arrived
        inventory.check_and_process_deliveries(day)
        
        # Simulate a random sale for a random product
        product_sold = random.choice(config.PRODUCTS_TO_MONITOR)
        quantity_sold = random.randint(1, 15)
        
        # The Inventory Manager processes the sale
        print(f"[Simulation]: A sale of {quantity_sold} units of '{product_sold}' occurred.")
        inventory.process_sale(product_sold, quantity_sold)
        
        # The Reorder Analyst runs its check and makes a decision
        if analyst.check_and_decide(product_sold):
            # If the analyst decides to reorder, the inventory manager places the order
            inventory.place_reorder(
                product_name=product_sold,
                quantity=config.REORDER_QUANTITY,
                order_day=day,
                lead_time=config.DELIVERY_LEAD_TIME_DAYS
            )
            # NOTE: FUTURE STEP: The ActionAgent will be called here to generate the email.

if __name__ == "__main__":
    run_simulation()