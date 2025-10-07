# agents/reorder_analyst.py

class ReorderAnalyst:
    """Agent 3: Collaborates with other agents to make reordering decisions."""
    
    def __init__(self, inventory_manager, sales_forecaster, safety_stock_factor):
        print("[Reorder Analyst]: Initializing. Establishing connections to other agents...")
        self.inventory_manager = inventory_manager
        self.sales_forecaster = sales_forecaster
        self.safety_stock_factor = safety_stock_factor
        print(f"[Reorder Analyst]: Ready to work. Safety stock factor set to {self.safety_stock_factor}.")

    def check_and_decide(self, product_name, forecast_period=30):
        """
        The core logic where agents collaborate. Returns True if a reorder is needed.
        """
        print(f"\n[Reorder Analyst]: === Starting analysis for '{product_name}' ===")
        
        # 1. Check if an order is already pending to avoid duplicates (TALKING TO INVENTORY MANAGER)
        if self.inventory_manager.is_order_pending(product_name):
            print(f"[Reorder Analyst]: An order for '{product_name}' is already on its way. No action needed.")
            print("=" * 70)
            return False

        # 2. Talk to the Inventory Manager
        print(f"[Reorder Analyst] -> [Inventory Manager]: What is the current stock level for '{product_name}'?")
        current_stock = self.inventory_manager.get_stock_level(product_name)
        print(f"    [Inventory Manager]: We currently have {current_stock} units.")
        
        # 3. Talk to the Sales Forecaster
        print(f"[Reorder Analyst] -> [Sales Forecaster]: What is the predicted demand for the next {forecast_period} days?")
        predicted_demand = self.sales_forecaster.predict_demand(product_name, forecast_period)
        
        # 4. Apply the business logic
        reorder_threshold = predicted_demand * self.safety_stock_factor
        print(f"[Reorder Analyst]: Calculating reorder threshold (predicted demand * safety factor): {predicted_demand} * {self.safety_stock_factor} = {reorder_threshold:.1f}")
        
        # 5. Make and return the decision
        if current_stock < reorder_threshold:
            print(f"[Reorder Analyst]: FINAL DECISION: TRIGGER REORDER. Stock ({current_stock}) is below threshold ({reorder_threshold:.1f}).")
            decision = True
        else:
            print(f"[Reorder Analyst]: FINAL DECISION: NO ACTION NEEDED. Stock level ({current_stock}) is sufficient.")
            decision = False

        print("=" * 70)
        return decision