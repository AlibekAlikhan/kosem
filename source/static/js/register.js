document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;


    fetch('/auth/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email,
            password: password,
            username: email
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.access && data.refresh) {
            localStorage.setItem('accessToken', data.access);
            localStorage.setItem('refreshToken', data.refresh);
            document.getElementById('message').style.display = 'block';
            document.getElementById('message').innerText = 'Registration successful!';
            window.location.href = "/auth/login";
        } else {
            document.getElementById('message').style.display = 'block';
            document.getElementById('message').innerText = 'Registration failed.';
            console.error(data);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('message').style.display = 'block';
        document.getElementById('message').innerText = 'An error occurred.';
    });
});




