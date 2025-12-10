import os
import sys

#   Version 1.0
#   MIT License

#   Copyright (c) 2025 Tudor from ipsilo.eu. For more details, contact tudor@ipsilo.eu

#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:

#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.

#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.


csv_file_path="empty"

def main():
    if len(sys.argv) > 1:
        global csv_file_path
        csv_file_path = sys.argv[1]
        print(f"File path received: {csv_file_path}")
        
        try:
            with open(csv_file_path, 'r') as f:
                print(f.read())
        except FileNotFoundError:
            print(f"Error: {csv_file_path} not found.")


if __name__ == "__main__":
    main()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome_message():

    print("\n--- CLL-CSV ---\n")
    print("\nFind out more at https://github.com/ipsilo-eu/cll-csv\n")

    print("Available Commands:\n")
    print("  help - Show this menu.")
    print("  qr - Show the qr code to https://github.com/ipsilo-eu/cll-csv")
    print("  right, left, up, down - Scroll table view.")
    print("  goto <PageNum> or goto <ColLabel> or goto <CellAddress> - Jump.")
    print("  add <v1>,<v2>,... - Append a new row.")
    print("  replace <Addresses> <NewValue> - Update one or more cells/ranges.")
    print("  delete <Address1,Address2,...> - Clear cell contents.")
    print("  clone <destination_filepath> - Save current state to a new file.")
    print("  open <filename> - Open a different file.")
    print("  reload - Re-read the current file.")
    print("  clone <final_address> - Clone the table to another file.")
    print("  delete <cell(s)_loaction> - Delete certain cells.")
    print("  destroy - Delete the file's whole content.")
    print("  get <cell_loaction> - Shows the selected value in terminal.")
    print("  display - Redraw the table.")
    print("  end - Exit the program.")
    print("\n\n")

def qrshow():
    print("Scan the qr code to access https://github.com/ipsilo-eu/cll-csv : \n\n")
    print("████████████████████████████████████████████████████████████████")
    print("█                                                              █")
    print("█  ██████████████  ██    ████  ██████  ██      ██████████████  █")
    print("█  ██          ██  ██████  ██████          ██  ██          ██  █")
    print("█  ██  ██████  ██      ██████  ██    ██    ██  ██  ██████  ██  █")
    print("█  ██  ██████  ██      ██      ██  ██████  ██  ██  ██████  ██  █")
    print("█  ██  ██████  ██  ████████  ████      ██      ██  ██████  ██  █")
    print("█  ██          ██  ██    ██        ██  ██      ██          ██  █")
    print("█  ██████████████  ██  ██  ██  ██  ██  ██  ██  ██████████████  █")
    print("█                  ██  ██████  ████                            █")
    print("█  ██████    ████  ██████    ██████      ██  ████████    ████  █")
    print("█      ██    ██  ████████    ██████████  ██████████      ████  █")
    print("█  ██████████████████    ██      ██      ██    ██████████  ██  █")
    print("█    ██    ████    ████      ██  ██    ██    ██    ████        █")
    print("█  ████  ██    ████████  ██████  ████  ██  ██  ████        ██  █")
    print("█  ████    ████  ██████    ██    ██████  ████  ████      ████  █")
    print("█      ████    ██████      ████████  ██  ██  ████████      ██  █")
    print("█  ██████████          ██████  ██  ██  ██████  ████            █")
    print("█    ████████████            ████  ██      ██████          ██  █")
    print("█    ██  ██  ██  ██          ██████      ██    ████    ██████  █")
    print("█  ████  ████  ██    ██  ██      ██████  ██        ████    ██  █")
    print("█        ██  ██        ██    ██    ██  ██  ██  ██  ██          █")
    print("█  ████    ██  ████████████████    ██      ████████████  ██    █")
    print("█                  ██████  ██    ████  ██  ██      ██████  ██  █")
    print("█  ██████████████    ██    ████████████    ██  ██  ██      ██  █")
    print("█  ██          ██  ████  ████  ██  ██  ██████      ██          █")
    print("█  ██  ██████  ██    ██      ████  ██  ████████████████    ██  █")
    print("█  ██  ██████  ██    ██      ██████████  ██████    ██████  ██  █")
    print("█  ██  ██████  ██  ████  ██      ██          ██    ██    ████  █")
    print("█  ██          ██  ██████    ██  ██    ██  ██    ██████        █")
    print("█  ██████████████  ████████████  ████      ██      ████    ██  █")
    print("█                                                              █")
    print("████████████████████████████████████████████████████████████████")

MAX_COL_WIDTH = 20
ROW_NUM_PAD_BASE = 1 
MAX_ROWS_PER_PAGE = 25

current_start_col = 0
current_start_row = 0
all_cols_widths = []
col_labels = []
all_data = []
last_command_executed = ""
last_error_message = ""

print_welcome_message()

if(csv_file_path=="empty"):
    print("Filename: ", end="  ")
    filename=input()
else:
    filename=csv_file_path

def get_terminal_width():
    try:
        return os.get_terminal_size().columns
    except (OSError, AttributeError):
        return 80

def get_cols_per_page():
    terminal_width = get_terminal_width()
    
    max_rows = len(all_data) if all_data else 1
    row_num_padding = len(str(max_rows)) + ROW_NUM_PAD_BASE + 1
    
    cols_per_page = 0
    temp_width = row_num_padding
    
    for w in all_cols_widths:
        col_display_width = w + 2
        if temp_width + col_display_width <= terminal_width:
            cols_per_page += 1
            temp_width += col_display_width
        else:
            break
            
    if cols_per_page == 0 and len(all_cols_widths) > 0:
        return 1
    return cols_per_page


def get_page_info(widths, start_col_index, terminal_width):
    max_rows = len(all_data) if all_data else 1
    row_num_padding = len(str(max_rows)) + ROW_NUM_PAD_BASE + 1
    
    cols_to_show_indices = []
    current_width_used = row_num_padding
    
    if not widths:
        return ([], 0, 1, 1)

    for i in range(start_col_index, len(widths)):
        col_display_width = widths[i] + 2
        if current_width_used + col_display_width <= terminal_width:
            cols_to_show_indices.append(i)
            current_width_used += col_display_width
        else:
            break
            
    if not cols_to_show_indices and start_col_index < len(widths):
        cols_to_show_indices.append(start_col_index)
    
    end_col_index = start_col_index + len(cols_to_show_indices)
    
    cols_per_page = get_cols_per_page()

    total_cols = len(widths)
    total_pages = (total_cols + cols_per_page - 1) // cols_per_page if total_cols > 0 and cols_per_page > 0 else 1
    current_page = (start_col_index // cols_per_page) + 1 if cols_per_page > 0 else 1

    return (cols_to_show_indices, end_col_index, current_page, total_pages)

def get_excel_column_label(n):

    label = ""
    n += 1  
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        label = chr(65 + remainder) + label
    return label

def display_table_page(data, widths, col_labels, start_col_index):


    global current_start_row
    global last_error_message
    terminal_width = get_terminal_width()
    terminal_height = MAX_ROWS_PER_PAGE  
    (cols_to_show_indices, end_col_index, current_h_page, total_h_pages) = \
        get_page_info(widths, start_col_index, terminal_width)

    max_rows = len(data) if data else 1
    row_num_padding = len(str(max_rows)) + ROW_NUM_PAD_BASE + 1
    
    total_rows = len(data)
    end_row_index = min(current_start_row + terminal_height, total_rows)
    current_v_page = (current_start_row // terminal_height) + 1
    total_v_pages = (total_rows + terminal_height - 1) // terminal_height
    
    clear_screen()
    
    print(" --- CLL-CSV --- ")
    print("File Opened:  "+ filename + "\n")
    print(f"--- Last Command: {last_command_executed} ---")
    if last_error_message:
        print(f"\n<< ERROR: {last_error_message} >>\n")
        last_error_message = "" 
    else:
        print("")
    print("\n" + "-" * terminal_width)
    
    if not cols_to_show_indices:
        print("No columns to display.")
        return

    print(f"{'':>{row_num_padding}}", end="")
    for i in cols_to_show_indices:
        width = widths[i]
        print(f"{col_labels[i]:^{width+2}}", end="")
    print()

    row_slice = data[current_start_row:end_row_index]
    
    for row_idx_offset, row in enumerate(row_slice):
        true_row_number = current_start_row + row_idx_offset + 1
        
        print(f"{true_row_number:>{len(str(max_rows))}} ", end="")
        
        for i in cols_to_show_indices:
            effective_width = widths[i]
            display_width = effective_width + 2
            
            display_item = str(row[i]) if i < len(row) else ""

            if len(display_item) > effective_width:
                display_item = display_item[:effective_width - 3] + "..."
            
            print(f"{display_item:^{display_width}}", end="")
            
        print()
    
    if widths:
        first_col_label = col_labels[start_col_index]
        last_col_label = col_labels[end_col_index - 1] 
    else:
        first_col_label = "N/A"
        last_col_label = "N/A"

    footer_text = f"--- Columns {first_col_label} to {last_col_label} | H-Page ({current_h_page}/{total_h_pages}) | Rows ({current_start_row + 1}-{end_row_index} of {total_rows}) | V-Page ({current_v_page}/{total_v_pages}) ---"
    print("\n" + footer_text)
    
    
def down():
    global current_start_row
    global last_error_message
    
    total_rows = len(all_data)
    rows_per_page = MAX_ROWS_PER_PAGE
    next_start = current_start_row + rows_per_page
    
    if next_start >= total_rows:
        last_error_message = "Cannot move down: Already at the last row page."
    else:
        current_start_row = next_start

def up():
    global current_start_row
    global last_error_message

    rows_per_page = MAX_ROWS_PER_PAGE
    new_start = current_start_row - rows_per_page
    
    if new_start < 0:
        last_error_message = "Cannot move up: Already at the first row page."
    else:
        current_start_row = new_start


def left():
    global current_start_col
    global last_error_message
    
    cols_per_page = get_cols_per_page()
    new_start = current_start_col - cols_per_page
    
    if new_start < 0:
        last_error_message = "Cannot move left: Already at the first page."
    else:
        current_start_col = new_start


def right():
    global current_start_col
    global last_error_message
    
    total_cols = len(all_cols_widths)
    cols_per_page = get_cols_per_page()
    next_start = current_start_col + cols_per_page
    
    if next_start >= total_cols:
        last_error_message = "Cannot move right: Already at the last page."
    else:
        current_start_col = next_start


def open_csv_file(filename):
    global all_data, all_cols_widths, col_labels, current_start_col
    global last_error_message


    all_data = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for x in f:
                row = x.strip().split(',') 
                if any(row): 
                    all_data.append(row)

    except FileNotFoundError:
        last_error_message = f"File '{filename}' not found."
        return False

    if not all_data:
        last_error_message = "File is empty or could not be read."
        return False

    max_cols = max(len(row) for row in all_data)
    
    all_cols_widths = []
    for col_index in range(max_cols):
        col_items_lengths = [
            len(str(row[col_index])) for row in all_data if col_index < len(row) and row[col_index].strip()
        ]
        
        if col_items_lengths:
            width = min(max(col_items_lengths), MAX_COL_WIDTH)
        else:
            width = 5
            
        label_width = len(get_excel_column_label(col_index)) 
        final_width = max(width, label_width)
        
        all_cols_widths.append(final_width)

    col_labels = [get_excel_column_label(i) for i in range(len(all_cols_widths))]
    current_start_col = 0
    return True


if open_csv_file(filename):
    display_table_page(all_data, all_cols_widths, col_labels, current_start_col)
    

def handle_goto_command(target_input):
    global current_start_col, current_start_row
    global last_error_message

    
    total_cols = len(all_cols_widths)
    total_rows = len(all_data)
    cols_per_page = get_cols_per_page()
    rows_per_page = MAX_ROWS_PER_PAGE 
    
    if total_rows == 0 or total_cols == 0:
        last_error_message = "Error: No data loaded. >>"
        return
        
    column_label = ""
    row_number_str = ""
    
    for char in target_input:
        if 'A' <= char.upper() <= 'Z':
            column_label += char
        elif '0' <= char <= '9':
            row_number_str += char

    target_col_index = -1
    target_row_index = -1
    
    if column_label and row_number_str:
        try:
            target_col_index = get_column_index_from_label(column_label)
            target_row_index = int(row_number_str) - 1 
            
            if target_row_index < 0 or target_row_index >= total_rows:
                target_row_index = -1
            if target_col_index < 0 or target_col_index >= total_cols:
                target_col_index = -1 

            if target_col_index != -1 and target_row_index != -1:
                if cols_per_page > 0:
                    target_h_page = (target_col_index // cols_per_page) + 1
                    current_start_col = (target_h_page - 1) * cols_per_page
                
                if rows_per_page > 0:
                    target_v_page = (target_row_index // rows_per_page) + 1
                    current_start_row = (target_v_page - 1) * rows_per_page
                
                print(f"\nJumping to Cell {column_label}{row_number_str}.")
                return

        except Exception:
            pass

    if target_input.isdigit():
        try:
            target_row_number = int(target_input)
            target_row_index = target_row_number - 1 
            
            if target_row_index < 0 or target_row_index >= total_rows:
                print(f"\n<< Error: Row {target_row_number} is out of bounds (1 to {total_rows}). >>")
                return

            if rows_per_page > 0:
                target_v_page = (target_row_index // rows_per_page) + 1
                current_start_row = (target_v_page - 1) * rows_per_page
            
            print(f"\nJumping to Row {target_row_number}.")
            return
            
        except Exception:
            pass

    if target_input.isalpha():
        column_label = target_input.upper()
        
        try:
            target_col_index = get_column_index_from_label(column_label)
        except Exception:
             print(f"\n<< Error converting column label '{column_label}'. >>")
             return

        if target_col_index < 0 or target_col_index >= total_cols:
            print(f"\n<< Error: Column {column_label} does not exist (A to {col_labels[-1]}). >>")
            return

        if cols_per_page > 0:
            target_h_page = (target_col_index // cols_per_page) + 1
            current_start_col = (target_h_page - 1) * cols_per_page
        
        print(f"\nJumping to Column {column_label}.")
        return


    print(f"\n<< Invalid 'goto' parameter: '{target_input}'. Use a column (A), row (5), or cell (D5). >>")

def get_column_index_from_label(label):

    index = 0
    multiplier = 1
    for char in reversed(label.upper()):
        value = ord(char) - ord('A') + 1
        index += value * multiplier
        multiplier *= 26
    return index - 1


def _delete_single_cell(cell_address, commit_to_file=True):

    global all_data, filename

    column_label = ""
    row_number_str = ""
    for char in cell_address:
        if 'A' <= char.upper() <= 'Z':
            column_label += char
        elif '0' <= char <= '9':
            row_number_str += char
        else:
            print(f"\n<< Error: Invalid character in cell address '{cell_address}'. >>")
            return False

    if not column_label or not row_number_str:
        print(f"\n<< Error: Malformed cell address '{cell_address}'. Expected format like D5. >>")
        return False

    try:
        row_index = int(row_number_str) - 1
        col_index = get_column_index_from_label(column_label)
    except Exception:
        print(f"\n<< Error processing cell address '{cell_address}'. >>")
        return False

    if row_index < 0 or row_index >= len(all_data):
        print(f"\n<< Error: Row {row_number_str} is out of bounds (1 to {len(all_data)}). >>")
        return False

    if col_index >= len(all_data[row_index]):
        print(f"\nCell {cell_address} is already empty (out of current column bounds).")
        return True

    all_data[row_index][col_index] = ""

    if commit_to_file:
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                for row in all_data:
                    f.write(','.join(row) + '\n')
        except Exception as e:
            print(f"\n<< Error writing to file: {e} >>")
            return False

        open_csv_file(filename)
        print(f"\nCell {cell_address} successfully cleared.")
    
    return True 

def _get_coords_from_address(cell_address):

    column_label = ""
    row_number_str = ""
    for char in cell_address:
        if 'A' <= char.upper() <= 'Z':
            column_label += char
        elif '0' <= char <= '9':
            row_number_str += char
    
    if column_label and row_number_str:
        return column_label.upper(), row_number_str
    return None

def _parse_range_to_addresses(range_string):

    if ':' not in range_string:
        return [range_string]

    start_addr, end_addr = range_string.split(':', 1)
    
    start_coords = _get_coords_from_address(start_addr.strip())
    end_coords = _get_coords_from_address(end_addr.strip())
    
    if not start_coords or not end_coords:
        print(f"\n<< Error: Malformed cell range '{range_string}'. >>")
        return []

    start_col_label, start_row_str = start_coords
    end_col_label, end_row_str = end_coords

    try:
        start_row = int(start_row_str)
        end_row = int(end_row_str)
        start_col_index = get_column_index_from_label(start_col_label)
        end_col_index = get_column_index_from_label(end_col_label)
    except ValueError:
        print(f"\n<< Error: Invalid numbers in range '{range_string}'. >>")
        return []

    addresses = []
    for col_idx in range(min(start_col_index, end_col_index), max(start_col_index, end_col_index) + 1):
        col_label = get_excel_column_label(col_idx)
        for row_num in range(min(start_row, end_row), max(start_row, end_row) + 1):
            addresses.append(f"{col_label}{row_num}")
            
    return addresses

def get_cell_content(cell_address):

    global all_data
    
    column_label = ""
    row_number_str = ""
    for char in cell_address:
        if 'A' <= char.upper() <= 'Z':
            column_label += char
        elif '0' <= char <= '9':
            row_number_str += char
            
    if not column_label or not row_number_str:
        return None, f"<< Error: Malformed cell address '{cell_address}'. Expected format like D5. >>"

    try:
        row_index = int(row_number_str) - 1
        col_index = get_column_index_from_label(column_label)
    except Exception:
        return None, f"<< Error processing cell address '{cell_address}'. >>"

    if row_index < 0 or row_index >= len(all_data):
        return None, f"<< Error: Row {row_number_str} is out of bounds (1 to {len(all_data)}). >>"

    if col_index >= len(all_data[row_index]):
        return "", f"Cell {cell_address} is currently empty (out of current column bounds)."

    content = all_data[row_index][col_index]
    return content, None


def delete_cells(address_string):

    global filename
    global last_error_message

    input_parts = [part.strip() for part in address_string.split(',') if part.strip()]
    
    final_addresses = []
    for part in input_parts:
        if ':' in part:
            final_addresses.extend(_parse_range_to_addresses(part))
        else:
            final_addresses.append(part)
    
    successful_deletions = 0
    total_attempts = len(final_addresses)
    
    if total_attempts == 0:
        last_error_message = "Error: No valid addresses or ranges provided for deletion. >>"
        return False

    for address in final_addresses:
        if _delete_single_cell(address, commit_to_file=False): 
            successful_deletions += 1
            
    if successful_deletions > 0:
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                for row in all_data:
                    while row and not row[-1].strip():
                        row.pop()
                    f.write(','.join(row) + '\n')
            
            open_csv_file(filename)
            
            print(f"\nSuccessfully deleted {successful_deletions} of {total_attempts} cells. File updated.")
            return True
            
        except Exception as e:
            print(f"\n<< Error writing to file after mass delete: {e} >>")
            return False
    else:
        print("\nNo cells were successfully deleted. Check addresses and bounds.")
        return False


def _replace_single_cell(cell_address, new_value, commit_to_file=True):

    global all_data, filename
    global last_error_message

    column_label = ""
    row_number_str = ""
    for char in cell_address:
        if 'A' <= char.upper() <= 'Z':
            column_label += char
        elif '0' <= char <= '9':
            row_number_str += char

    if not column_label or not row_number_str:
        if commit_to_file:
            print(f"\n<< Error: Malformed cell address '{cell_address}'. Expected format like D5. >>")
        return False

    try:
        row_index = int(row_number_str) - 1 
        col_index = get_column_index_from_label(column_label)
    except Exception:
        if commit_to_file:
            print(f"\n<< Error processing cell address '{cell_address}'. >>")
        return False

    if row_index < 0 or row_index >= len(all_data):
        if commit_to_file:
            print(f"\n<< Error: Row {row_number_str} is out of bounds (1 to {len(all_data)}). >>")
        return False

    if col_index >= len(all_data[row_index]):
        if col_index >= MAX_COL_WIDTH * 10:
             if commit_to_file:
                 last_error_message = "Error: Column index is excessively large. >>"
             return False
             
        while len(all_data[row_index]) <= col_index:
            all_data[row_index].append("")

    all_data[row_index][col_index] = new_value

    if commit_to_file:
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                for row in all_data:
                    while row and not row[-1].strip():
                        row.pop()
                    f.write(','.join(row) + '\n')
        except Exception as e:
            print(f"\n<< Error writing to file: {e} >>")
            return False

        open_csv_file(filename)
        print(f"\nCell {cell_address} successfully updated to '{new_value}'.")

    return True 

def replace_cells(address_string, new_value):

    global filename
    global last_error_message
   
    input_parts = [part.strip() for part in address_string.split(',') if part.strip()]
    final_addresses = []
    for part in input_parts:
        final_addresses.extend(_parse_range_to_addresses(part))
    
    successful_replacements = 0
    total_attempts = len(final_addresses)
    
    if total_attempts == 0:
        last_error_message = "Error: No valid addresses or ranges provided for replacement. >>"
        return False

    for address in final_addresses:
        if _replace_single_cell(address, new_value, commit_to_file=False): 
            successful_replacements += 1
            
    if successful_replacements > 0:
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                for row in all_data:
                    while row and not row[-1].strip():
                        row.pop()
                    f.write(','.join(row) + '\n')
            
            open_csv_file(filename)
            
            print(f"\nSuccessfully replaced {successful_replacements} of {total_attempts} cells with '{new_value}'. File updated.")
            return True
            
        except Exception as e:
            print(f"\n<< Error writing to file after mass replace: {e} >>")
            return False
    else:
        print("\nNo cells were successfully replaced. Check addresses and bounds.")
        return False

def replace_cells(address_string, new_value):

    global filename
    global last_error_message
    
    input_parts = [part.strip() for part in address_string.split(',') if part.strip()]
    final_addresses = []
    for part in input_parts:
        final_addresses.extend(_parse_range_to_addresses(part))
    
    successful_replacements = 0
    total_attempts = len(final_addresses)
    
    if total_attempts == 0:
        last_error_message = "Error: No valid addresses or ranges provided for replacement. >>"
        return False

    for address in final_addresses:
        if _replace_single_cell(address, new_value, commit_to_file=False): 
            successful_replacements += 1
            
    if successful_replacements > 0:
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                for row in all_data:
                    f.write(','.join(row) + '\n')
            
            open_csv_file(filename)
            
            print(f"\nSuccessfully replaced {successful_replacements} of {total_attempts} cells with '{new_value}'. File updated.")
            return True
            
        except Exception as e:
            print(f"\n<< Error writing to file after mass replace: {e} >>")
            return False
    else:
        print("\nNo cells were successfully replaced. Check addresses and bounds.")
        return False



inp=""
while(inp!="end"):
    print("\n>>>", end="  ")

    inp=input()
    last_command_executed = inp 

    inpt=inp.split(" ")
    
    command = inpt[0].lower() 

    match command:
        case "add":
            wrtdata="\n"
            for i in inpt:
                if(i!="add"):
                    if(wrtdata!="\n"):
                        wrtdata=wrtdata+ "," +i
                    else:
                        wrtdata="\n"+i

            with open(filename, "a") as f:
                f.write(wrtdata)
            
            open_csv_file(filename) 
            display_table_page(all_data, all_cols_widths, col_labels, current_start_col)


        case "right":
            right()
            display_table_page(all_data, all_cols_widths, col_labels, current_start_col)

        case "left":
            left()
            display_table_page(all_data, all_cols_widths, col_labels, current_start_col)

        case "down":
            down()
            display_table_page(all_data, all_cols_widths, col_labels, current_start_col)

        case "up":
            up()
            display_table_page(all_data, all_cols_widths, col_labels, current_start_col)

        case "get":
            if len(inpt) == 2:
                cell_address = inpt[1].strip()
                
                content, error_message = get_cell_content(cell_address)
                
                if error_message:
                    print(error_message)
                else:
                    display_table_page(all_data, all_cols_widths, col_labels, current_start_col)
                    print("------------------------------------------")
                    print(f"--- Content of Cell {cell_address.upper()} ---")
                    print(f"'{content}'")
                    print("------------------------------------------")
            else:
                print("Usage: get <CellAddress>")



        case "clone":
            if len(inpt) > 1:
                destination_filepath = inpt[1]
                
                try:
                    with open(destination_filepath, 'w', encoding='utf-8') as f:
                        for row in all_data:
                            temp_row = list(row) 
                            while temp_row and not temp_row[-1].strip():
                                temp_row.pop()
                            f.write(','.join(temp_row) + '\n')
                    
                    print(f"\nFile successfully cloned from '{filename}' to '{destination_filepath}'.")
                    display_table_page(all_data, all_cols_widths, col_labels, current_start_col)
                
                except Exception as e:
                    print(f"\n<< Error cloning file: {e} >>")
            else:
                print("Usage: clone <destination_filepath>")


        case "replace":
            if len(inpt) >= 3:
                address_string = inpt[1] 
                new_value = " ".join(inpt[2:]) 
                
                replace_cells(address_string, new_value)
            else:
                print("Usage: replace <Addresses> <NewValue>")  
            display_table_page(all_data, all_cols_widths, col_labels, current_start_col)


        case "goto":
            if len(inpt) > 1:
                handle_goto_command(inpt[1])
            else:
                print("Usage: goto <ColumnLabel>, goto <RowNumber>, or goto <CellAddress>")
            display_table_page(all_data, all_cols_widths, col_labels, current_start_col)


        case "delete":
            if len(inpt) >= 2:
                address_string = " ".join(inpt[1:])
                delete_cells(address_string) 
            else:
                print("Usage: delete <CellAddress> or delete <Address1,Address2,...>")
            display_table_page(all_data, all_cols_widths, col_labels, current_start_col) 


        case "open":
            if len(inpt) > 1:
                filename=inpt[1]
                print("Opening: "+filename)
                if open_csv_file(filename):
                    display_table_page(all_data, all_cols_widths, col_labels, current_start_col)
            else:
                print("Usage: open <filename>")
                display_table_page(all_data, all_cols_widths, col_labels, current_start_col)

        case "reload":
            print("Reloading: "+filename)
            if open_csv_file(filename):
                display_table_page(all_data, all_cols_widths, col_labels, current_start_col)

        case "qr":
            clear_screen()
            qrshow()

        case "help":
            print_welcome_message()

        case "end":
            print("File closed and program ended!")
            break

        case "destroy":
            print("Are you sure you want to DELETE the whole file's contents for " +filename +" ?")
            input_check=input("delete_file_contents / abort >>> ")
            if(input_check=="delete_file_contents"):
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write('')
                    print(filename+" succesfully cleared of contents.")
                    clear_screen()
            else:
                print("\nDeletion ABORTED!")

        case "display":
            display_table_page(all_data, all_cols_widths, col_labels, current_start_col)

        case _:
            print(f"Unknown command: {command}")
