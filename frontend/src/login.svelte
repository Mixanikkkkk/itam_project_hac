<script>
    import { onMount } from 'svelte';
    import gsap from 'gsap';
    import { Link } from 'svelte-routing';

    let username = '';
    let password = '';
    let errorMessage = '';

    onMount(() => {
        gsap.from(".page", { duration: 1.3, opacity: 0, y: -10 });
    });

    async function submitForm(event) {
        event.preventDefault();

        const response = await fetch('http://team4.itatmisis.ru:8000/docs#/default/login_login_post', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        });

        if (response.ok) {
            const data = await response.json();
            console.log('Аутентификация успешна:', data);
        } else {
            const errorData = await response.json();
            errorMessage = errorData.message || 'Ошибка авторизации.';
        }
    }
</script>

<main>
    <div class="page">
        <body>
            <div class="container">
                <h1>Авторизируйтесь:</h1>
                <form id="authForm" on:submit={submitForm}>
                    <div class="form-group">
                        <input type="text" id="username" bind:value={username} placeholder="Логин" required>
                    </div>
    
                    <div class="form-group">
                        <input type="password" id="password" bind:value={password} placeholder="Пароль" required>
                    </div>
                    <Link to="/my-teams">
                        <button id="auth-btn" type="submit" class="btn">Отправить</button>
                    </Link>
    
                    {#if errorMessage}
                        <div class="error">{errorMessage}</div>
                    {/if}
                </form>
            </div>
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
        height: auto;
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