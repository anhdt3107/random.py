// Get DOM elements
const todoList = document.getElementById('todo-list');
const completedList = document.getElementById('completed-list');
const addTodoForm = document.getElementById('add-todo');

// Add to-do item
function addTodo(description) {
  // Create to-do item element
  const todoItem = document.createElement('div');
  todoItem.classList.add('todo-item');
  todoItem.innerHTML = `
    <input type="checkbox" class="todo-checkbox">
    <span class="todo-description">${description}</span>
    <button class="todo-delete">Delete</button>
  `;

// Add to-do item to list
todoList.appendChild(todoItem);
  
// Add event listener for delete button
const deleteButton = todoItem.querySelector('.todo-delete');
deleteButton.addEventListener('click', function() {
  todoList.removeChild(todoItem);
});

// Add event listener for checkbox
const checkbox = todoItem.querySelector('.todo-checkbox');
checkbox.addEventListener('change', function() {
  if (checkbox.checked) {
    // Move to-do item to completed list
    completedList.appendChild(todoItem);
  } else {
    // Move to-do item back to to-do list
    todoList.appendChild(todoItem);
  }
});
}

// Add to-do item when form is submitted
addTodoForm.addEventListener('submit', function(event) {
// Prevent form from submitting
event.preventDefault();

// Get to-do description
const description = addTodoForm.querySelector('input').value;

// Add to-do item
addTodo(description);

// Clear input field
addTodoForm.querySelector('input').value = '';
});
