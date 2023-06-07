import { get } from "svelte/store";
import Button from "./Button.svelte";

async function getProps() {
    const response = await fetch("/api/main");
	const data = await response.json();
	return data;
}
getProps().then(dict => {
    const app = new Button({
        target: document.getElementById("button-target"),
        props: {
            dict: dict,
        },
    });
});

export default app;