function loginUser() {
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    fetch('/auth/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email,
            password: password,
        }),
        credentials: 'include', // Позволяет отправлять и принимать куки с запросом
    })
    .then(response => response.json())
    .then(data => {
        if (data.access && data.refresh) {
            // Сохраняем токены в локальном хранилище (LocalStorage)
            localStorage.setItem('accessToken', data.access);
            localStorage.setItem('refreshToken', data.refresh);
            // Перенаправляем пользователя на защищенную страницу или обновляем UI
            window.location.href = "/webapp/category/asd";
        } else {
            console.error('Authentication failed');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

const create_id = document.getElementById('create_id')

create_id.addEventListener('click', loginUser)
