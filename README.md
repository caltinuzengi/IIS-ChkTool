# IIS ChkTool (Service Status Manager)

## 📑 Description
**IIS ChkTool** is a **portable GUI application** that helps you easily manage the **chk.txt status files (live/off)** used in your IIS services on Windows servers.  
- Automatically finds **chk.txt** or **chk/chk.txt** files.  
- Lists whether they are marked as "LIVE" or "OFF".  
- Allows you to **set selected services to "live" or "off"** with a single click or **rollback** changes.  
- Runs as a **standalone EXE**, no installation required.  
- **Root directory selection is now interactive via GUI.**

---

## 🚀 Features
- ✅ Automatically scans **chk.txt** and **chk/chk.txt** files.
- ✅ **Dynamic root directory selection** on startup via GUI.
- ✅ Shows **LIVE/OFF status** in a GUI.
- ✅ **Bulk or selective** "live" and "off" operations.
- ✅ **Rollback** support (auto-restore from .bak backup).
- ✅ Fully **portable EXE**, no installation required.

---

## 💻 Usage
### 1. Run the Application
- Double-click `ChkTool.exe` to **run the tool**.
- At startup, a **window will ask you to select a root directory**:
  - You can choose from:
    - `C:\inetpub\wwwroot`
    - `C:\Ecommerce`
    - **Or enter a custom path manually.**
- Once the path is selected, all services and their current statuses will be listed.
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

## ⚙️ Configuration (Root Directory)
No need to edit any file!  
- You **choose the root directory via GUI on startup**.
- Default options are:
  - `C:\inetpub\wwwroot`
  - `C:\Ecommerce`
- You can **enter any custom path** if needed.

---

## ⚙️ Building Your Own EXE
If you want to **build your own EXE** (for development or modifying default directories):

### 1. (Optional) Adjust default directories in `root_selector.py` if needed.
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
chk_manager_app_with_root_selector/
│
├── app.py              # Main GUI application
├── root_selector.py   # GUI for selecting root directory
├── requirements.txt    # Required Python packages
├── build_exe.bat       # Script to generate EXE
└── dist/               # (Generated EXE will be here)
```

---

## 📬 Contact
For any issues, suggestions, or contributions:  
✉️ cagrialtinuzengi@gmail.com

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