<script>
    import { onMount } from 'svelte';
    import gsap from 'gsap';
    import { Link } from 'svelte-routing';
    
    let username = '';
    let tg = '';
    let role = 'uxui';
    let about = '';
    let responseData = null;
    let errorMessage = '';

    onMount(() => {
        gsap.from(".page", { duration: 1.7, opacity: 1, y: -10 });
    });

    async function submitForm(event) {
        event.preventDefault();

        const url = `http://team4.itatmisis.ru:8000/docs#/default/get_user_profile_profile__username__get?username=${encodeURIComponent(username)}&tg=${encodeURIComponent(tg)}&role=${encodeURIComponent(role)}&about=${encodeURIComponent(about)}`;

        try {
            const response = await fetch(url, {
                method: 'GET',
            });

            if (response.ok) {
                responseData = await response.json();
                console.log('Ответ сервера:', responseData);
            } else {
                errorMessage = 'Ошибка получения данных';
            }
        } catch (error) {
            errorMessage = 'Произошла ошибка: ' + error.message;
        }
    }
</script>

<main>
    <div class="page">
        <body>
            <div class="registration-form">
                <h1>Заполни анкету и расскажи о себе!</h1>
                <form on:submit={submitForm}>
                    <input 
                        type="text" 
                        id="username" 
                        name="username" 
                        placeholder="ФИО" 
                        bind:value={username} 
                        required
                    >
            
                    <input 
                        type="text" 
                        id="tg" 
                        name="tg" 
                        placeholder="@Telegram" 
                        bind:value={tg} 
                        required
                    >
            
                    <select 
                        id="role" 
                        name="role" 
                        bind:value={role}
                    >
                        <option value="uxui">UX/UI</option>
                        <option value="backend">Backend</option>
                        <option value="frontend">Frontend</option>
                        <option value="manager">Manager</option>
                    </select>
            
                    <textarea 
                        id="about" 
                        name="about" 
                        placeholder="Дополнительная информация" 
                        rows="11"
                        bind:value={about} 
                        required
                    ></textarea>
                    
                    <button type="submit">Отправить</button>
                </form>
                
                {#if responseData}
                    <div>
                        <h2>Полученные данные:</h2>
                        <pre>{JSON.stringify(responseData, null, 2)}</pre>
                    </div>
                {/if}
                
                {#if errorMessage}
                    <div style="color: red;">
                        <p>{errorMessage}</p>
                    </div>
                {/if}
    
                <Link to="/myteams">
                    <button>Перейти к командам</button>
                </Link>
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

    form {
        text-align: center;
    }

    .registration-form {
        width: 700px;
        height: 570px;
        margin: 50px auto;
        padding: 20px;
        background: #2a2a2a;
        border-radius: 12px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    h1 {
        text-align: center;
        color: #fff;
    }

    input[type="text"],
    select,
    textarea {
        width: 100%;
        padding: 10px;
        color: #fff;
        margin-bottom: 20px;
        background-color: #2a2a2a;
        border: 3px solid #5c615d;
        border-radius: 12px;
        box-sizing: border-box;
    }

    button {
        width: 185px;
        height: 53px;
        padding: 10px;
        background-color: #05DA73;
        color: #2a2a2a;
        border: none;
        border-radius: 12px;
        cursor: pointer;
        font-size: 20px;
        font-weight: 700;
    }

    pre {
        background: #333;
        border-radius: 8px;
        padding: 10px;
        color: #fff;
    }
</style>