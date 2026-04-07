import os
import time
import sqlite3
from datetime import datetime

# ==========================================
# SHOCK FRAME STORE - Enterprise Edition
# Architecture: OOP + SQLite Database
# ==========================================

class ShockFrameStore:
    def __init__(self) -> None:
        """Initializes the store cart, business rules, and database connection."""
        self.cart_total: float = 0.0
        self.discount_threshold: float = 100.0
        self.discount_rate: float = 0.20
        self.is_running: bool = True
        self.db_name: str = "store_database.db"
        
        # Initialize database on startup
        self.init_database()

    def init_database(self) -> None:
        """Creates the SQLite database and the sales table if they do not exist."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        # Creating a table to log all successful transactions
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                subtotal REAL,
                discount REAL,
                final_total REAL
            )
        ''')
        conn.commit()
        conn.close()

    def log_transaction(self, subtotal: float, discount: float, final_total: float) -> None:
        """Saves a completed transaction into the local SQLite database."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute('''
            INSERT INTO sales_history (timestamp, subtotal, discount, final_total)
            VALUES (?, ?, ?, ?)
        ''', (current_time, subtotal, discount, final_total))
        
        conn.commit()
        conn.close()

    def clear_screen(self) -> None:
        """Clears the terminal for a cleaner user interface."""
        os.system('clear' if os.name == 'posix' else 'cls')

    def backdoor_reset(self) -> None:
        """Secret Admin Method: Resets the current cart."""
        self.clear_screen()
        print("\n🕵️‍♂️ [ALERT] ADMIN ACCESS GRANTED")
        print("Bypassing security protocols...")
        time.sleep(1)
        self.cart_total = 0.0
        print("Memory wiped. Cart reset to ZERO.\n")

    def backdoor_view_logs(self) -> None:
        """Secret Admin Method: Retrieves and displays the database logs."""
        self.clear_screen()
        print("\n📂 [DATABASE] FETCHING SALES HISTORY...")
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sales_history")
        records = cursor.fetchall()
        
        if not records:
            print("  No transactions recorded yet.")
        else:
            for row in records:
                print(f"  ID: {row[0]} | Date: {row[1]} | Final: ${row[4]:.2f}")
                
        conn.close()
        print("\n")

    def add_item(self, price: float) -> None:
        """Adds an item to the cart or triggers administrative backdoors."""
        if price == -19.0:
            self.backdoor_reset()
        elif price == -99.0:
            self.backdoor_view_logs()
        elif price > 0:
            self.cart_total += price
            print(f"  💾 Item added. Subtotal: ${self.cart_total:.2f}")
        elif price < 0:
            print("  ⚠️ [ERROR] Invalid price. Must be positive.")

    def process_checkout(self) -> None:
        """Calculates final price, applies discounts, and logs to database."""
        if self.cart_total == 0:
            print("\n💻 System Offline. Clean execution.\n")
            self.is_running = False
            return

        self.clear_screen()
        print("\n-----------------------------------")
        print("🧾 INITIALIZING CHECKOUT...")
        
        savings: float = 0.0
        final_price: float = self.cart_total

        if self.cart_total > self.discount_threshold:
            print("🌟 VIP CUSTOMER DETECTED!")
            savings = self.cart_total * self.discount_rate
            final_price = self.cart_total - savings
            print(f"  Automatic 20% discount applied.")
            print(f"  Money saved: ${savings:.2f}")
        
        print(f"✅ FINAL TOTAL: ${final_price:.2f}")
        
        # Save to SQLite Database
        print("💾 Saving transaction to secure database...")
        self.log_transaction(self.cart_total, savings, final_price)
            
        print("-----------------------------------")
        print("💻 System Offline. Clean execution.\n")
        self.is_running = False

    def run_terminal_ui(self) -> None:
        """Main loop for the terminal interface."""
        self.clear_screen()
        print("--- 🎮 SYSTEM ONLINE: SHOCK FRAME STORE 🎮 ---")
        print("Instructions: Enter item price. Type '0' to checkout.")
        
        while self.is_running:
            try:
                user_input: str = input("\n💲 Item Price: ")
                price: float = float(user_input)
                
                if price == 0:
                    self.process_checkout()
                else:
                    self.add_item(price)
            except ValueError:
                print("  ⚠️ [ERROR] Invalid input. Please enter numbers only.")

# --- BOOT SEQUENCE ---
if __name__ == "__main__":
    store = ShockFrameStore()
    store.run_terminal_ui()
