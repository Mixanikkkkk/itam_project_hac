<script>
    import { onMount } from 'svelte';
    import gsap from 'gsap';
    import { Link } from 'svelte-routing';

    onMount(() => {
        gsap.from(".page", { duration: 1.7, opacity: 1, y: -10 });
    });
</script>

<main>
    <div class="page">
        <body>
            <div class="registration-form">
                <h1>Заполни анкету и расскажи о себе!</h1>
                <form>
                    <input type="text" id="username" name="username" placeholder="ФИО" required>
        
                    <input type="tg" id="tg" name="tg" placeholder="@Telegram" required>
        
                    <select id="role" name="role" placeholder="Выберите вашу роль:">
                        <option value="uxui">UX/UI</option>
                        <option value="backend">Backend</option>
                        <option value="frontend">Frontend</option>
                        <option value="manager">Manager</option>
                    </select>
        
                    <textarea id="about" name="about" placeholder="Дополнительная информация" rows="11" required></textarea>
                    
                    <!-- svelte-ignore missing-declaration -->
                    <Link to="/myteams">
                        <button type="submit">Отправить</button>
                    </Link>
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
    input[type="tg"],
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
</style>