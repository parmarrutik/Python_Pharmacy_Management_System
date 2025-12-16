# 🏥 Pharmacy Management System (Python + MySQL)

A **desktop-based Pharmacy Management System** built using **Python (Tkinter GUI)** and **MySQL**.
This application helps manage medicines, companies, stock details, and provides CRUD operations with a user-friendly interface.

---

## 📌 Features

* 🔐 MySQL Database Integration
* 💊 Add, Update, Delete Medicines
* 🏷️ Medicine Department Management
* 🔎 Search Medicine by:

  * Reference Number
  * Medicine Name
  * Lot Number
* 📋 View All Medicine Records
* 🖥️ Interactive GUI using Tkinter
* 🔄 Auto-refresh Combobox from Database
* 🧾 TreeView Tables for Clear Data Display

---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** – GUI
* **MySQL / MariaDB**
* **Pillow (PIL)** – Image handling
* **mysql-connector-python**

---

## 📂 Project Structure

```
Pharmacy-Management-System/
│
├── Pharamacy.py        # Main Python GUI Application
├── pharmacy.sql        # Database Schema & Sample Data
├── images/             # (Optional) Images used in GUI
└── README.md           # Project Documentation
```

---

## 🗄️ Database Details

**Database Name:** `pharmacy`

### Tables:

#### `meddep` (Medicine Department)

| Column | Type              |
| ------ | ----------------- |
| ref1   | INT (Primary Key) |
| med1   | VARCHAR           |

#### `medinfo` (Medicine Information)

| Column  | Type              |
| ------- | ----------------- |
| ref     | INT (Primary Key) |
| cmp     | VARCHAR           |
| tmed    | VARCHAR           |
| medname | VARCHAR           |
| lot     | INT               |
| issue   | INT               |
| exp     | INT               |
| uses    | VARCHAR           |
| side    | VARCHAR           |
| prec    | VARCHAR           |
| dos     | VARCHAR           |
| tprice  | INT               |
| proq    | INT               |

---

## ⚙️ Installation & Setup

### 1️⃣ Install Required Libraries

```bash
pip install pillow mysql-connector-python
```

### 2️⃣ Setup MySQL Database

* Open **phpMyAdmin** or MySQL CLI
* Create a database named `pharmacy`
* Import the file:

```sql
pharmacy.sql
```

### 3️⃣ Update Database Credentials (if needed)

In `Pharamacy.py`:

```python
mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='pharmacy'
)
```

---

## ▶️ How to Run the Project

```bash
python Pharamacy.py
```

The Pharmacy Management System window will open.

---

## 🖼️ GUI Preview

* Medicine Information Panel
* Medicine Department Panel
* Search & Action Buttons
* Data Display using TreeView

![image alt](https://github.com/parmarrutik/Python_Pharmacy_Management_System/blob/main/Screenshot.png)


---

## 🚀 Future Enhancements

* 🔑 User Login & Authentication
* 📊 Sales & Billing Module
* 📈 Stock Expiry Alerts
* 📄 Invoice Generation (PDF)
* 🌐 Web Version using Flask/Django

---

## 👨‍💻 Author

**Developed by:**
RUTIK PARMAR
🔗 LinkedIn : www.linkedin.com/in/rutik-parmar-9b24b6306




