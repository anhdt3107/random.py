import sqlite3

# Connect to the database
conn = sqlite3.connect('D:\\Python\\my_project\\todolist_web\\todolist.db')

# Create the table (if it doesn't already exist)
conn.execute('''CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, description TEXT NOT NULL, completed BOOLEAN NOT NULL DEFAULT 0)''')

# Insert a new to-do item
description = "Buy milk"
completed = False
conn.execute("INSERT INTO items (description, completed) VALUES (?, ?)", (description, completed))
conn.commit()

# Update an existing to-do item
id = 1
completed = True
conn.execute("UPDATE items SET completed = ? WHERE id = ?", (completed, id))
conn.commit()

# Delete a to-do item
id = 2
conn.execute("DELETE FROM items WHERE id = ?", (id,))
conn.commit()

# Get all to-do items
cursor = conn.execute("SELECT * FROM items")
items = cursor.fetchall()

# Generate HTML for the to-do list
html = ""
for item in items:
  html += f"<div class='todo-item'><input type='checkbox' class='todo-checkbox' {'checked' if item[2] else ''}><span class='todo-description'>{item[1]}</span><button class='todo-delete'>Delete</button></div>"

# Display the to-do list
print(html)

# Close the connection
conn.close()
