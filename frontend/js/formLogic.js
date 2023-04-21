let counter = 0;

document.getElementById("add").addEventListener("click", (e) => {
	e.preventDefault();

	let container = document.createElement("div");
	container.setAttribute("class", "input-container");

	let break_el = document.createElement("br");
	let label = document.createElement("label");
	let input = document.createElement("div");

	input.setAttribute("class", "select-container");

	label.innerHTML = "Caffeine Source: ";

	input.innerHTML = `<select name="caffeine-source-${counter}" id="caffeineSources">
                            <option value = "coffee"> Coffee </option>
                            <option value = "tea"> Tea </option>
                            <option value = "energyDrink"> Energy Drink </option>
                            <option value = "softDrink"> Soft Drink </option>
                            <option value = "chocolate"> Chocolate </option>
                            <option value = "other"> Other </option>
                        </select>`;

	let label_time = document.createElement("label");
	let input_time = document.createElement("input");

	input_time.setAttribute("type", "time");
	input_time.setAttribute("required", "true");
	input_time.id = "caffine-consumption-time";
	input_time.name = `caffiene-time-${counter}`;

	label_time.innerHTML = "Time Consumed: ";

	container.appendChild(break_el);
	container.appendChild(label);
	container.appendChild(input);
	container.appendChild(label_time);
	container.appendChild(input_time);

	document.getElementById("form").appendChild(container);
	counter++;
});

document.getElementById("remove").addEventListener("click", (e) => {
	e.preventDefault();
	counter--;

	document.getElementsByClassName("input-container")[0].remove(-1);
});

document.forms[0].addEventListener("submit", async (e) => {
	e.preventDefault();

	const formData = new FormData(document.forms[0]);
	let object = {};
	formData.forEach((value, key) => (object[key] = value));
	auth0.getUser().then(async (user) => {
		object["user"] = user.email;
		let json = JSON.stringify(object);
		console.log(json);
		console.log(...formData);
		const res = await fetch("http://127.0.0.1:5000/post", {
			body: json,
			method: "post",
		});
	});
});
