import { get } from "svelte/store";
import Home from "./Home.svelte";

async function getProps() {
    const response = await fetch("/api/main");
	const data = await response.json();
	return data;
}
getProps().then(dict => {
    const app = new Home({
        target: document.getElementById("home-target"),
        props: {
            dict: dict,
        },
    });
});

export default app;
