function getTodos() {
	return fetch("http://localhost:8000/todos/")
		.then((response) => response.json())
		.then((data) => data)
		.catch((error) => console.error("Error:", error));
}

function createTodo(title) {
	return fetch("http://localhost:8000/todos/", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({ title }),
	})
		.then((response) => response.json())
		.then((data) => data)
		.catch((error) => console.error("Error:", error));
}

function addTodo() {
	// Add new todo to the list
	this.todos.push({
		id: Math.random(), // Generate a unique id (you may use a real id in your backend)
		title: this.newTodo,
		completed: false,
	});
	this.newTodo = ""; // Clear the input field
}
