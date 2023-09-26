const base_url = "http://127.0.0.1:8000/";

function fetchTodos() {
	return fetch("http://localhost:8000/todos/")
		.then((response) => response.json())
		.then((data) => data)
		.catch((error) => console.error("Error:", error));
}

function createTodo(title) {
	const csrftoken = document.querySelector("#add-form > input").value;
	console.log(csrftoken);

	return fetch("http://localhost:8000/todos/", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			"X-CSRFToken": csrftoken,
		},
		body: JSON.stringify({ title, completed: false }),
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
