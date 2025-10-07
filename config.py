# config.py

# --- Simulation & Data Configuration ---
DATA_FILEPATH = 'data/Superstore.csv'

# A list of specific products to monitor and manage during the simulation.
PRODUCTS_TO_MONITOR = [
    'Staples',
    'Canon imageCLASS 2200 Advanced Copier',
    'Hon Deluxe Fabric Upholstered Stacking Chairs, Rounded Back',
    'Avery Non-Stick Binders',
    'GBC DocuBind P400 Electric Binding System'
]

# The number of days the simulation will run for.
SIMULATION_DAYS = 45

# --- Inventory & Decision Parameters ---
# The initial stock level for each monitored product at the start of the simulation.
INITIAL_STOCK_LEVEL = 60

# The safety stock factor (1.5 means 50% buffer above predicted demand).
SAFETY_STOCK_FACTOR = 1.5

# The number of units to order when a reorder is triggered.
REORDER_QUANTITY = 100

# The number of simulated days it takes for a new order to arrive.
DELIVERY_LEAD_TIME_DAYS = 5

# --- LLM/Generative AI Configuration (For Future Integration - Day 3) ---
# Your local Llama 3.2 settings via LM Studio
LM_STUDIO_BASE_URL = "http://localhost:1234/v1" 
LM_STUDIO_MODEL_NAME = "Llama-3.2-3B-Instruct-Q4_K_S.gguf"