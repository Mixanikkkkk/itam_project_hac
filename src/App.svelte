<script>
	import { Router, Route } from 'svelte-routing';
	import Welcome from './welcome.svelte';
	import Login from './login.svelte';
	import Signin from './signin.svelte';
	import Form from './form.svelte';
	import MyTeams from './my-teams.svelte';
</script>

<Router>
	<Route path="/" component={Welcome} />
	<Route path="/login" component={Login} />
	<Route path="/signin" component={Signin} />
	<Route path="/form" component={Form} />
	<Route path="/myteams" component={MyTeams} />
</Router>