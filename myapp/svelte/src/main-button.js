import Button from './Button.svelte';
const button = new Button({
	target: document.getElementById("button-target"),
	props: JSON.parse(document.getElementById("button-props").textContent),
});

export default button; 