# 🎮 Shock Frame Store - POS System

A lightweight, terminal-based Point of Sale (POS) system built with Python. Designed with a strict Object-Oriented Programming (OOP) architecture and native SQLite integration for data persistence.

---

## 🚀 Tech Stack & Architecture
- **Language:** Python 3
- **Paradigm:** Object-Oriented Programming (OOP)
- **Database:** SQLite (Native, serverless)
- **UI:** Clean Terminal / Command Line Interface

## 🛠️ Core Features
- **Dynamic Checkout:** Real-time subtotal calculation and robust error handling for invalid inputs.
- **Business Rules:** Automatic VIP discount (20% off) applied to purchases over $100.
- **Data Persistence:** Every completed transaction is permanently logged into a local `store_database.db` SQLite file.

## 🕵️‍♂️ Admin Backdoors (Easter Eggs)
This system includes hidden administrative commands that can be executed directly from the price input prompt:
* `Type -19`: **Emergency Reset**. Bypasses security, wipes the current cart memory, and resets the subtotal to zero.
* `Type -99`: **Database Fetch**. Bypasses the storefront UI and prints the entire sales history directly from the SQLite database.

## 📥 Usage

No external libraries required. Runs entirely on standard Python 3.

```bash
# Clone the repository
git clone [https://github.com/ortiz10m/Tienda-Gamer-Python.git](https://github.com/ortiz10m/Tienda-Gamer-Python.git)

# Enter the directory
cd Tienda-Gamer-Python

# Run the store
python3 store.py


## 🤝 Support & Connect
If you found this architecture useful, consider giving this repository a ⭐!

* 🎥 **Follow the journey:** For discipline, motivation, and the stoic mindset needed to build great things (in code and in life), join the community on my YouTube channel: **DavOS**. Let's build efficiently.
