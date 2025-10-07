# agents/sales_forecaster.py
import pandas as pd
import os

class SalesForecaster:
    """Agent 1: Analyzes historical data to predict future sales demand."""
    
    def __init__(self, data_filepath):
        print("[Sales Forecaster]: Initializing. Loading historical data...")
        try:
            # Added error handling for data loading
            self.sales_data = pd.read_csv(data_filepath, encoding='latin1')
            self.sales_data['Order Date'] = pd.to_datetime(self.sales_data['Order Date'], dayfirst=True, errors='coerce')
            self.sales_data = self.sales_data.dropna(subset=['Order Date']) 
            self.sales_data['OrderMonth'] = self.sales_data['Order Date'].dt.to_period('M')
            
            self.total_days_of_history = (self.sales_data['Order Date'].max() - self.sales_data['Order Date'].min()).days
            if self.total_days_of_history == 0: self.total_days_of_history = 1 # Avoid division by zero
            
            print(f"[Sales Forecaster]: Data loaded. History covers {self.total_days_of_history} days.")
        except FileNotFoundError:
            print(f"[Sales Forecaster]: ERROR! Data file not found at '{data_filepath}'. Forecasts will be zero.")
            self.sales_data = pd.DataFrame({'Quantity': [], 'Product Name': [], 'OrderMonth': []})
            self.total_days_of_history = 1

    def predict_demand(self, product_name, days_to_predict=30):
        """Predicts demand based on average monthly sales for the specific product."""
        
        product_data = self.sales_data[self.sales_data['Product Name'] == product_name]
        
        if product_data.empty:
            # print(f"    [Sales Forecaster]: No historical data for '{product_name}'. Assuming zero demand.")
            return 0
        
        total_quantity_sold = product_data['Quantity'].sum()
        num_months_sold = product_data['OrderMonth'].nunique()
        
        # Ensure num_months_sold is at least 1 to avoid division by zero if there's data
        num_months_sold = max(1, num_months_sold)

        # Calculate the average sales for the months the product was active.
        avg_monthly_sales = total_quantity_sold / num_months_sold
        
        # Scale the monthly average to the forecast period (default 30 days)
        predicted_demand = round(avg_monthly_sales * (days_to_predict / 30.0))
        
        print(f"    [Sales Forecaster]: Prediction for next {days_to_predict} days: {predicted_demand} units (based on {avg_monthly_sales:.1f} avg monthly sales).")
        return predicted_demand