# 🖨️ ZebraTest – Zebra Printer Debug Tool

**ZebraTest** is a lightweight Python utility to help IT support teams test and troubleshoot Zebra printers. It auto-detects connected Zebra printers, sends a test ZPL label, and logs the result.

---

## 🚀 Features

- Detects connected printers on Windows
- Filters and targets Zebra brand printers
- Sends a basic ZPL print with text + barcode
- Logs output to `zebra_debug_log.txt`

---

## 📦 Requirements

- Windows OS
- Python 3.8+
- Dependencies:
  ```bash
  pip install pywin32
