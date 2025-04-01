# ZebraTest - Zebra Printer Debug Tool (MVP)

import win32print
import win32ui
import time
import os

TEST_LABEL = """
^XA
^FO50,50^ADN,36,20^FDZebraTest Print Successful^FS
^FO50,100^BCN,100,Y,N,N
^FD1234567890^FS
^XZ
"""

def list_printers():
    printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)
    return [printer[2] for printer in printers]

def find_zebra_printers(printers):
    return [p for p in printers if "zebra" in p.lower()]

def send_test_label(printer_name):
    try:
        hPrinter = win32print.OpenPrinter(printer_name)
        hJob = win32print.StartDocPrinter(hPrinter, 1, ("ZebraTest Label", None, "RAW"))
        win32print.StartPagePrinter(hPrinter)
        win32print.WritePrinter(hPrinter, TEST_LABEL.encode())
        win32print.EndPagePrinter(hPrinter)
        win32print.EndDocPrinter(hPrinter)
        win32print.ClosePrinter(hPrinter)
        return True, "Print sent successfully."
    except Exception as e:
        return False, f"Error: {str(e)}"

def log_result(printer, status, message):
    logline = f"[{time.ctime()}] Printer: {printer} | Status: {status} | Message: {message}\n"
    with open("zebra_debug_log.txt", "a") as logfile:
        logfile.write(logline)
    print(logline)

def main():
    print("\nZebraTest - Zebra Printer Debugger\n------------------------------")
    printers = list_printers()
    zebra_printers = find_zebra_printers(printers)

    if not zebra_printers:
        print("No Zebra printers detected.")
        return

    for zp in zebra_printers:
        print(f"Testing printer: {zp}...")
        success, msg = send_test_label(zp)
        log_result(zp, "Success" if success else "Fail", msg)

if __name__ == "__main__":
    main()
