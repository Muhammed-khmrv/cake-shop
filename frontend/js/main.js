function buyProduct() {
    alert("Товар добавлен в корзину!");
}

function auth() {
    alert("Вы зарегистрировались на сайте!");
}

function signIn() {
    alert("Вы вошли в аккаунт.");
}

function addToCart(productId) {
    alert("Добавлен товар с ID: " + productId);
}

document.querySelectorAll('.like-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        btn.innerText = btn.innerText === "🤍" ? "❤️" : "🤍";
    });
});