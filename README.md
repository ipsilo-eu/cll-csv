## CLL-CSV: Command Line CSV Viewer and Editor

CLL-CSV is a lightweight, command-line interface (CLI) tool for viewing and editing CSV files directly in your terminal. It offers a screen-based table display with scrolling, cell-level modifications, and file management functions.

### Key Features

  * **Terminal Display:** Shows a paginated, formatted view of the CSV data, adapting to your terminal width.
  * **Navigation:** Scroll horizontally and vertically using simple commands (`right`, `left`, `up`, `down`).
  * **Jumping:** Navigate directly to a specific row, column, or cell using the `goto` command (e.g., `goto 10`, `goto C`, `goto E12`).
  * **Data Manipulation:**
      * `add`: Append a new row with comma-separated values.
      * `replace`: Update the content of one or more cells or ranges (e.g., `replace A1:B5 NewValue`).
      * `delete`: Clear the content of one or more cells or ranges.
  * **File Management:**
      * `open`: Load a different CSV file.
      * `clone`: Save the current table state to a new file.
      * `reload`: Re-read the current file from disk.
      * `destroy`: Clear all contents from the current file.
  * **Cell Inspection:** Use `get <CellAddress>` to display the raw content of a specific cell.

-----

## Installation and Setup (Windows Executable)

CLL-CSV is available as a single, compiled Windows executable (`cll-csv.exe`), requiring no Python setup. The easiest way to install it and make it runnable from anywhere is using the PowerShell installer script.

### Option 1: One-Line PowerShell Installation (Recommended for Windows)

This command downloads the user-specific installer script, runs it to download `cll-csv.exe`, places it in your **user**'s `PATH`.

1.  Open **PowerShell** (not Command Prompt).
2.  Paste and run the following single command:

<!-- end list -->

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass; Invoke-WebRequest -Uri "https://raw.githubusercontent.com/ipsilo-eu/cll-csv/main/install/.exe/install-cll-csv-user.ps1" -UseBasicParsing | Invoke-Expression
```

3.  After installation completes, **open a new PowerShell or Command Prompt window** to use the `cll-csv` command.

### Option 2: Manual Download (For any OS)

The executable can be downloaded directly, or the Python script can be run manually.

  * **Windows Executable:** Download the `.exe` file directly:
    [/.exe/cll-csv.exe](https://raw.githubusercontent.com/ipsilo-eu/cll-csv/main/.exe/cll-csv.exe)
  * **Python File:** Download the `.py` file directly (requires Python to be installed):
    [/.py/cll-csv.py](https://raw.githubusercontent.com/ipsilo-eu/cll-csv/main/.py/cll-csv.py)

-----

## Usage

### Running CLL-CSV

Once installed via Option 1, or if running the Python script, you can launch the program:

**Option A: Specify file at launch**

```bash
cll-csv your_data.csv
```

**Option B: Enter file at prompt**

```bash
cll-csv
>>> Filename: my_data.csv
```

### Available Commands

Once the file is loaded, the table view will be displayed, and the prompt `>>>` will appear.

| Command | Description | Example |
| :--- | :--- | :--- |
| `help` | Show the list of available commands. | `help` |
| `qr` | Display the QR code for the GitHub repository. | `qr` |
| `right` | Scroll the table view one page to the right. | `right` |
| `left` | Scroll the table view one page to the left. | `left` |
| `up` | Scroll the table view one page up. | `up` |
| `down` | Scroll the table view one page down. | `down` |
| `goto` | Jump to a specific row number, column label, or cell address. | `goto 10`, `goto D`, `goto C5` |
| `add` | Append a new row with the specified values. | `add Value1,Value2,Value3` |
| `replace` | Update one or more cells/ranges with a `<NewValue>`. | `replace A1:C10,E2 MyNewData` |
| `delete` | Clear the content of specified cells or ranges. | `delete B2,C4:D7` |
| `get` | Shows the raw value of a specific cell in the terminal. | `get A1` |
| `clone` | Save the current data state to a new file. | `clone backup.csv` |
| `open` | Open and load a different file. | `open another.csv` |
| `reload` | Re-read the current file from disk. | `reload` |
| `destroy` | Permanently delete the file's whole content (requires confirmation). | `destroy` |
| `display` | Redraw the table view. | `display` |
| `end` | Exit the program. | `end` |

### Data Entry Note

  * When using the **`add`** command, the values must be comma-separated:
    `>>> add NewItem,19.99,Notes`
  * For the **`replace`** command, the new value can contain spaces and will be treated as a single string:
    `>>> replace A1 This is the new header`

### Cell Addressing

The tool uses standard Excel-style addressing:

  * **Column Labels:** A, B, C, ...
  * **Row Numbers:** 1, 2, 3, ...
  * **Cell Address:** Column Label + Row Number (e.g., A1, D5)
  * **Cell Range:** StartCell:EndCell (e.g., A1:B5)

-----

## Licensing

This project is licensed under the MIT License.

Copyright (c) 2025 Tudor from ipsilo.eu. For more details, contact tudor@ipsilo.eu
