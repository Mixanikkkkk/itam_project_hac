<script>
    import { onMount } from 'svelte';
    import gsap from 'gsap';
    import { Link } from 'svelte-routing';

    onMount(() => {
        gsap.from(".page", { duration: 1.3, opacity: 1, y: -10 });
    });
</script>

<main>
    <div class="page">
        <body>
            <div class="container">
                <h1>Авторизируйтесь:</h1>
                <form id="authForm">
                    <div class="form-group">
                        <input type="text" id="username" name="username" placeholder="Логин" required>
                    </div>

                    <div class="form-group">
                        <input type="password" id="password" name="password" placeholder="Пароль" required>
                    </div>

                    <!-- svelte-ignore missing-declaration -->
                    <Link to="/myteams">
                        <button id="auth-btn" type="submit" class="btn">Отправить</button>
                    </Link>

                    <div id="error-message" class="error"></div>
                </form>
            </div>
            <script src="authorization_script.js"></script>
        </body>
    </div>
</main>

<style>
    body {
    font-family: 'Manrope', sans-serif;
    background-image: url('/assets/images/background.png');
    background-size: 100% 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
    }

	.container {
		width: 480px;
		height: 301px;
		background-color: #2a2a2a;
		text-align: center;
		border-radius: 9px;
		padding: 40px;
	}

    h1 {
        text-align: center;
        color: #fff;
        font-size: 36px;
        margin-bottom: 18px;
    }

    .form-group {
        margin-bottom: 18px;
    }

    .form-group input {
        width: 440px;
        height: 58px;
        font-size: 17px;
        padding: 8px;
        color: #fff;
        border: 3px solid #5c615d;
        background-color: #2a2a2a;
        border-radius: 12px;
    }

    .btn {
        margin: 0 auto;
        background-color: #05DA73;
        color: #2a2a2a;
        width: 185px;
        height: 53px;
        padding: 10px;
        border: none;
        border-radius: 12px;
        font-weight: 700;
        cursor: pointer;
    }

    .error {
        color: red;
        text-align: center;
        margin-top: 10px;
    }
</style>