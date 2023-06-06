import { get } from "svelte/store";
import App from "./App.svelte";

async function getProps() {
    const response = await fetch("http://127.0.0.1:8000/api/main");
	const data = await response.json();
	return data;
}
getProps().then(dict => {
    const app = new App({
        target: document.getElementById("app-target"),
        props: {
            dict: dict,
        },
    });
});

export default app;
