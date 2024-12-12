<script>
    import { onMount } from 'svelte';
    import gsap from 'gsap';
    import { Link } from 'svelte-routing';

    let username = '';
    let password = '';
    let confirmPassword = '';
    let errorMessage = '';

    onMount(() => {
        gsap.from(".page", { duration: 1.7, opacity: 1, y: -10 });
    });

    async function submitForm(event) {
        event.preventDefault();

        if (password !== confirmPassword) {
            errorMessage = "Пароли не совпадают.";
            return;
        }

        const response = await fetch('http://team4.itatmisis.ru:8000/docs#/default/register_user_register_post', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        });

        if (response.ok) {
            const jsonResponse = await response.json();
            console.log('Успех:', jsonResponse);
        } else {
            errorMessage = 'Ошибка регистрации. Попробуйте снова.';
            console.error('Ошибка:', response.statusText);
        }
    }
</script>

<main>
    <div class="page">
        <body>
            <div class="container">
                <h1>Зарегистрируйтесь:</h1>
                <form on:submit={submitForm}>
                    <div class="form-group">
                        <input type="text" bind:value={username} placeholder="Логин" required />
                    </div>
    
                    <div class="form-group">
                        <input type="password" bind:value={password} placeholder="Пароль" required />
                    </div>
    
                    <div class="form-group">
                        <input type="password" bind:value={confirmPassword} placeholder="Повторите пароль" required />
                    </div>
                    <Link to="/form">
                    <button type="submit" class="btn">Отправить</button>
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
        height: 369px;
        background-color: #2a2a2a;
        text-align: center;
        border-radius: 9px;
        padding: 40px;
    }

    h1 {
        color: #fff;
        text-align: center;
        font-size: 36px;
        margin-bottom: 18px;
    }

    .form-group {
        margin-bottom: 18px;
    }

    .form-group input {
        width: 440px;
        height: 50px;
        font-size: 17px;
        border: 2px solid transparent;
        padding: 8px;
        color: #fff;
        background-color: #2a2a2a;
        border: 3px solid #5c615d;
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