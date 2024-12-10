<script>
    import { onMount } from 'svelte';
    import gsap from 'gsap';

    onMount(() => {
        gsap.from(".page", { duration: 1.7, opacity: 1, y: -10 });
    });
</script>

<main>
    <div class="page">
        <body>
            <div class="container">
                <div class="head">
                    <h1 class="header">Мои команды:</h1>
                </div>
                <div class="card">
                    <h2>Крутая команда</h2>
                    <p>Описание очень крутой команды</p>
                    <div class="for-role"><p>Твоя роль: <span class="role">UX/UI</span></p></div>
                </div>
                <div class="card">
                    <h2>Очень крутая команда</h2>
                    <p>Описание очень крутой команды</p>
                    <div class="for-role-manager"><p>Твоя роль: <span class="role selected">Владелец</span></p></div>
                </div>
                <div class="card">
                    <h2>Сильно крутая команда</h2>
                    <p>Описание сильно крутой команды</p>
                    <div class="for-role"><p>Твоя роль: <span class="role">Backend</span></p></div>
                </div>
                <div class="card">
                    <h2>Ещё одна крутая команда</h2>
                    <p>Описание ещё одной крутой команды</p>
                    <div class="for-role"><p>Твоя роль: <span class="role">Frontend</span></p></div>
                </div>
                <div class="footer">
                    <button class="btn">Уведомления</button>
                    <button class="btn">Моя анкета</button>
                    <button class="btn">Новая команда</button>
                    <button class="btn">Список анкет</button>
                </div>
            </div>
        </body>
    </div>
</main>

<style>    
    body {
        overflow: hidden;
        position: relative;
        font-family: 'Manrope', sans-serif;
        background-image: url('/assets/images/background.png');
        background-size: 100% 100%;
        color: white;
        height: 100vh;
        display: flex;
        justify-content: center;
        margin: 0;
        padding: 0;
    }

    h2 {
        font-size: 36px;
    }

    p {
        font-size: 20px;
    }

    .container {
        width: 900px;
        overflow: hidden;
        overflow-y: hidden;
        overflow-x: hidden;
        height: 100%;
        position: relative;
        overflow-y: auto;
        border-radius: 9px;
        color: #fff;
    }

    .head {
        top: 0;
        width: 900px;
        height: 70px;
        background-color: #2b2b2b;
        border-radius: 10px;
    }

    .header {
        margin-top: 0;
        text-align: center;
        margin-bottom: 1px;
    }

    .card {
        text-align: center;
        margin-top: 30px;
        background-color: #2b2b2b;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 30px;
        transition: 0.2s;
    }

    .card:hover {
        box-shadow: 1px 1px 50px rgba(255, 255, 255, 0.674);
    }

    .role {
        font-weight: bold;
    }

    .role.selected {
        color: #4CAF50;
    }

    .footer {
        display: flex;
        justify-content: space-between;
    }

    .btn {
        width: 225px;
        height: 85px;
        background-color: #2a2a2a;
        color: white;
        border-radius: 12px;
        cursor: pointer;
        transition: background 0.3s;
    }

    .btn:hover {
        background-color: #343641;
    }

    .for-role {
        border: 2px solid #fff;
        border-radius: 12px;
    }

    .for-role-manager {
        border: 2px solid #05DA73;
        border-radius: 12px;
    }
</style>