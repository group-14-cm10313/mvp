let auth0 = null;

window.onload = async () => {
	await configureClient();
	await processLoginState();
	updateUI();
};

const configureClient = async () => {
	auth0 = await createAuth0Client({
		domain: "dev-s3azzbxk6y2nn64s.uk.auth0.com",
		client_id: "AoJSPiimBtdQP2qAmlhHOGiecQKlsyqH",
	});
};

const processLoginState = async () => {
	// Check code and state parameters
	const query = window.location.search;
	if (query.includes("code=") && query.includes("state=")) {
		// Process the login state
		await auth0.handleRedirectCallback();
		// Use replaceState to redirect the user away and remove the querystring parameters
		window.history.replaceState(
			{},
			document.title,
			window.location.pathname
		);
	}
};

const updateUI = async () => {
	document.body.classList.toggle("hidden");
	const isAuthenticated = await auth0.isAuthenticated();
	document.getElementById("btn-logout").disabled = !isAuthenticated;
	document.getElementById("btn-login").disabled = isAuthenticated;
	if (isAuthenticated) {
		auth0.getUser().then((user) => {
			console.log(user);
			document.getElementById("btn-login").classList.toggle("hidden");
			document
				.getElementById("welcome-message-container")
				.classList.toggle("hidden");
			document.getElementById("gated-content").classList.remove("hidden");
			document.getElementById("ipt-user-profile").innerHTML =
				user.given_name;
			document.getElementById("caffeine-form").classList.toggle("hidden");
		});
	} else {
		document.getElementById("btn-logout").classList.toggle("hidden");

		document.getElementById("gated-content").classList.add("hidden");
	}
};

const login = async () => {
	console.log(window.location.href);
	await auth0.loginWithRedirect({
		redirect_uri: "http://localhost:5500",
	});
};

const logout = () => {
	auth0.logout({
		returnTo: window.location.href,
	});
};
