# 📦 IIS ChkTool (Service Status Manager)

## 📑 Description
**IIS ChkTool** is a **portable GUI application** that helps you easily manage the **chk.txt status files (live/off)** used in your IIS services on Windows servers.  
- Automatically finds **chk.txt** or **chk/chk.txt** files.  
- Lists whether they are marked as "LIVE" or "OFF".  
- Allows you to **set selected services to "live" or "off"** with a single click or **rollback** changes.  
- Runs as a **standalone EXE**, no installation required.

---

## 🚀 Features
- ✅ Automatically scans **chk.txt** and **chk/chk.txt** files.
- ✅ Shows **LIVE/OFF status** in a GUI.
- ✅ **Bulk or selective** "live" and "off" operations.
- ✅ **Rollback** support (auto-restore from .bak backup).
- ✅ Fully **portable EXE**, no installation required.

---

## 💻 Usage
### 1. Run the Application
- Double-click `ChkTool.exe` to **run the tool**.
- All services and their current statuses will be listed.
- You can change the status to "OFF" or "LIVE", or rollback changes.

---

### 2. GUI Actions
| Button                      | Description                              |
|---------------------------|-----------------------------------------|
| **Set Selected to OFF**     | Sets selected services to `off`.         |
| **Set Selected to LIVE**    | Sets selected services to `live`.        |
| **Rollback**               | Restores selected services from backup. |
| **Refresh**                 | Refreshes and rescans all services.      |

---

## ⚙️ Configuration (Changing ROOT_DIR)
By default, the tool scans the following directory:
```
C:\inetpub\wwwroot
```

🔑 If you want to scan a **different root directory**:

### 1. Open `config.py`:
```python
ROOT_DIR = r"C:\inetpub\wwwroot"
```

👉 Change the path to your desired directory:
```python
ROOT_DIR = r"D:\MyCustomServices"
```

---

## ⚙️ Building Your Own EXE
If you modify `config.py` and want to **build your own EXE**:

### 1. Update the path in `config.py`.
### 2. Run `build_exe.bat`:
```bash
build_exe.bat
```

📦 This will generate:
```
dist/ChkTool.exe
```

### ✅ Note:
- The generated EXE will **run on any server without Python installed**.
- All dependencies (including PyQt5) are embedded inside the EXE.

---

## 🛑 Development Requirements (Optional for Build)
- Python 3.x
- PyQt5 (for development/build):
```bash
pip install PyQt5
```

---

## 🧩 Project Structure
```
chk_manager_app_advanced/
│
├── app.py              # Main GUI application
├── config.py           # Configuration for scanning directory
├── requirements.txt    # Required Python packages
├── build_exe.bat       # Script to generate EXE
└── dist/               # (Generated EXE will be here)
```

---

## 📬 Contact
For any issues, suggestions, or contributions:  
✉️ [cagrialtinuzengi@gmail.com]

---

> **Note:** Rollback feature automatically creates and uses `.bak` backups for safe operations.

---

## 🔥 Example GUI Output:
```
[ ServiceA  ] [ LIVE ]  | Path: C:\inetpub\wwwroot\Services\ServiceA\chk.txt
[ ServiceB  ] [ OFF  ]  | Path: C:\inetpub\wwwroot\Services\ServiceB\chk\chk.txt
```

---

## 💪 Contributing
Feel free to contribute and open a PR (Pull Request)!

---

## ✨ License
Apache License 2.0