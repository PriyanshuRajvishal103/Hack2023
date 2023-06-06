Follow the steps for directly using svelte components inside django template:

run in powershell inside svelte folder "npm install"

Must include {% load django_svelte %} in apps installed

1)Make sure to create a file named main-{file name.js} within the same directory as your new svelte file.

2)Replace all the instances of "App" with your svelte file name.

3)Inside the array at the end of the rollup.config.js, add the name of your svlete file without 'extension'.

Display tag for inside file {% display_svelte "MySpecialComponent.svelte" %}

If you want to create your own:(Within the same path as manage.py)

****************************npx degit thismatters/django-svelte-template svelte


***************************run the commands "npm run dev" and python manage at the same time for svelte reload only.
