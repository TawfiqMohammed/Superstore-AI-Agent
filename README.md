# 🚀 Smart Superstore AI Team: An Autonomous Multi-Agent Inventory System

🛒 **Smart Superstore AI Team**

This is an **Autonomous Multi-Agent System** designed to revolutionize inventory management in a retail environment. It showcases a modern **Agentic AI architecture** where specialized, collaborating agents perceive data, reason about trends, and autonomously execute decisions to maintain optimal stock levels.

**Key Features & Focus:**
* **Multi-Agent Collaboration:** Demonstrates clear communication and workflow between the Sales Forecaster, Inventory Manager, and Reorder Analyst.
* **Intelligent Decision Logic:** Uses predicted demand and safety stock factors to dynamically calculate reorder thresholds.
* **Modular Architecture:** Built for scalability and clear separation of concerns (Perception, Analysis, Orchestration).
* **Future Generative AI Integration:** Roadmap includes using **Llama 3.2** for external **Market Intelligence** synthesis and automated supplier communication.

**Built to demonstrate advanced concepts in AI/ML engineering, system architecture, and practical business automation.**

---

## 🏗️ Current Progress: The Foundation (Rule-Based Agentic PoC)

The core, rule-based multi-agent system is fully implemented, modularized, and successfully demonstrated through a 45-day simulation. It effectively mimics an intelligent operations team making data-driven inventory decisions.

### **The Three Collaborating Agents:**

The system is built upon a clear, modular architecture, enabling each agent to focus on its specialized task while seamlessly communicating with others.

1.  **📊 Sales Forecaster Agent (`agents/sales_forecaster.py`):**
    * **Role:** The Analyst. Responsible for predictive analytics.
    * **Functionality:** Analyzes historical sales data (from `Superstore.csv`) to calculate average monthly demand, projecting a **predicted demand** for a specified future period (e.g., 30 days). This provides the foresight needed for proactive inventory management.

2.  **📦 Inventory Manager Agent (`agents/inventory_manager.py`):**
    * **Role:** The Watcher. Manages the system's state and execution of physical actions.
    * **Functionality:** Tracks real-time stock levels, accurately processes sales, monitors pending deliveries (including simulating lead times for arrival), and updates inventory upon receipt of new stock.

3.  **🧠 Reorder Analyst Agent (`agents/reorder_analyst.py`):**
    * **Role:** The Orchestrator and Decision Maker.
    * **Functionality:** Acts as the central intelligence. It queries the `Inventory Manager` for current stock and the `Sales Forecaster` for predicted demand. Using a dynamic **reorder threshold** (predicted demand multiplied by a safety stock factor), it autonomously decides whether a reorder is necessary, preventing both stockouts and overstock situations. Crucially, it avoids duplicate orders for items already en route.

### **Simulation Highlights (45-Day Run):**

The simulation successfully demonstrates the agents collaborating in real-time. Key observations include:

* **Proactive Monitoring:** Agents continuously monitor stock levels and sales activities.
* **Intelligent Decision-Making:** The `Reorder Analyst` correctly determines when stock falls below the calculated threshold, factoring in predicted demand and safety stock.
* **Order Placement:** When a reorder is triggered (e.g., for 'GBC DocuBind P400 Electric Binding System' on Day 25, 'Staples' on Day 26, 'Canon imageCLASS 2200 Advanced Copier' on Day 28), the `Inventory Manager` accurately logs the pending delivery with an expected arrival date.
* **Delivery Processing:** New stock is seamlessly integrated into inventory upon its simulated arrival (e.g., 'GBC DocuBind P400 Electric Binding System' on Day 30), bringing stock levels back to optimal ranges.
* **Duplicate Order Prevention:** The system intelligently recognized an existing order for 'Staples' on Day 29, preventing unnecessary reordering.

This output clearly validates the foundational agentic architecture and decision-making logic.

---

## 🚀 Future Roadmap: Elevating with Generative AI (Llama 3.2 Integration)

The next crucial phase will integrate **Generative AI (Llama 3.2)** to enhance the system's intelligence from purely quantitative to a blend of quantitative and qualitative, alongside enabling advanced communication.

| Future Agent | Role | Generative AI Function | Impact |
| :--- | :--- | :--- | :--- |
| **Market Intelligence Agent** | **Contextual Reasoner.** | Will utilize Llama 3.2 to synthesize external data (e.g., simulated news articles, competitor announcements, seasonal trends) and output a **dynamic risk/demand adjustment factor.** | Moves beyond historical data to anticipate future market shifts, making reorder decisions *smarter and more adaptive*. |
| **Action Agent** | **Communication Specialist.** | Will use Llama 3.2 to **generate** professional, context-aware, and actionable reorder emails/messages to suppliers, including all necessary order details and custom notes. | Automates critical communication, saving time and ensuring clarity in supplier interactions. |

This integration will transform the "Smart Superstore AI Team" into a truly intelligent, adaptive, and communicative autonomous system.

---

## **Setup & Execution:**

1.  **Repository Structure:**
    ```
    job-market-ai-agent/
    ├── agents/
    │   ├── sales_forecaster.py
    │   ├── inventory_manager.py
    │   └── reorder_analyst.py
    ├── data/
    │   └── Superstore.csv        # Your dataset (e.g., from Kaggle)
    ├── config.py                 # Configuration for agents and simulation
    ├── main.py                   # Main simulation runner
    ├── README.md                 # This file
    └── requirements.txt          # Required Python packages
    ```

2.  **Dependencies:** Ensure you have Python 3.9+ installed. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: `langchain`, `openai`, `python-dotenv` are listed in `requirements.txt` for future LLM integration.)*

3.  **Data:** Place your `Superstore.csv` file inside the `data/` directory.

4.  **Run Simulation:**
    ```bash
    python main.py
    ```
    Observe the agents collaborating through the detailed console logs as the 45-day (or `SIMULATION_DAYS` defined in `config.py`) simulation unfolds.

---