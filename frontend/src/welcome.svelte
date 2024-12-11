<script>
    import { onMount } from 'svelte';
    import gsap from 'gsap';
    import { Link } from 'svelte-routing';

    onMount(() => {
        gsap.from(".page", { duration: 3, opacity: 0, y: -50 });
    });
</script>

<main>
    <div class="page">
        <body>
            <div class="container">
                <div class="text-block">
                    <h1>Добро пожаловать! TEST!</h1>
                    <p>Здесь вы можете создать учетную запись или войти в уже существующую.</p>
                </div>
                <div class="button-group">
                    <Link to="/login">
                        <button id="loginBtn">Вход</button>
                    </Link>
                    <Link to='/signin'>
                        <button id="registerBtn">Регистрация</button>
                    </Link>
                </div>
            </div>
        </body>
    </div>
</main>

<style>
	body {
		font-family: 'Manrope', sans-serif;
		background-image: url('/assets/images/background.png');
		background-size: 100% 100%;
		height: 100vh;
		width: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.container {
		width: 430px;
		height: 277px;
		background-color: #2a2a2a;
		text-align: center;
		border-radius: 9px;
		padding: 40px;
	}

	.text-block h1 {
		font-size: 36px;
		color: #ffffff;
		margin-bottom: 20px;
	}

	.text-block p {
		font-size: 20px;
		margin-bottom: 30px;
		color: #ffffff;
	}

	#registerBtn {
		background-color: #2a2a2a;
		width: 390px;
		height: 53px;
		color: #05DA73;
		border-color: #05DA73;
		border-radius: 12px;
		padding: 10px 20px;
		font-size: 16px;
		font-weight: 700;
		cursor: pointer;
	}

	#loginBtn {
		background-color: #05DA73;
		width: 390px;
		height: 53px;
		color: #2a2a2a;
		border: none;
		border-radius: 12px;
		padding: 10px 20px;
		font-size: 16px;
		font-weight: 700;
		cursor: pointer;
	}
</style>