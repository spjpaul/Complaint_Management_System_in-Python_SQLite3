# Complaint_Management_System_in-Python_SQLite3
Basic Complaint Management system written in python with default DB SQLite3.

# Complaints Management System

This is a simple Complaints Management System implemented in Python using SQLite for database management and the `PrettyTable` library for displaying complaint data in a tabular format.

## Prerequisites

Before you begin, ensure you have the following libraries installed:

- `sqlite3`: Included in the Python standard library.
- `prettytable`: You can install it using `pip`:
  ```
  pip install prettytable
  ```

## Usage

1. **Creating the Database Table**

   To initialize the system, the database table needs to be created. This table will store all the complaints. Run the `create_table()` function:

   ```python
   create_table()
   ```

2. **Registering New Complaint**

   To register a new complaint, run the `main()` function. The system will prompt you with a menu of options:

   - Enter '1' to register a new complaint.
   - Enter '2' to view existing complaints.
   - Enter '3' to exit the system.

   Follow the prompts to enter the required details of the complaint. The system will guide you through providing information about the customer, complaint category, service type, and other details.

3. **Viewing Existing Complaints**

   To view existing complaints, select the '2' option from the main menu. This will display all the complaints stored in the database in a tabular format.

## Example

Here's an example of how you can run the system:

```python
# Run the main function
if __name__ == "__main__":
    main()
```

Follow the prompts to register new complaints and view existing ones.

## Important Notes

- Ensure you have write permissions in the directory where the script is located, as the SQLite database file (`complaints.db`) will be created in the same directory.
- The system uses the `PrettyTable` library to display complaints in a tabular format. However, the code for displaying complaints using `PrettyTable` is currently commented out in the provided code. If you wish to use it, uncomment the corresponding sections of code.
- The script's functionality is basic and can be extended to include more features as needed.

## Disclaimer

This script is provided as a basic example of a Complaints Management System and might require further improvements, such as input validation and error handling, to be suitable for production use.
