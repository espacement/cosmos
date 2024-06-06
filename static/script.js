
// const cartItems = document.querySelector('.cart-items');

// Корзина

document.addEventListener("DOMContentLoaded", function() {
    const cartModal = document.getElementById('cart-modal');
    const cartCount = document.getElementById("cart-count");

    document.getElementById('open-cart').addEventListener('click', () => {
        cartModal.style.display = "flex";
    });

    document.querySelector(".close-button").addEventListener("click", () => {
        cartModal.style.display = "none";
    });

    window.addEventListener("click", (event) => {
        if (event.target === cartModal) {
            cartModal.style.display = "none";
        }
    });

    window.addToCart = function(itemId) {
        // const addToCartUrl = document.currentScript.getAttribute('data-add-to-cart-url');

        const csrfTokenInput = document.querySelector('[name=csrfmiddlewaretoken]');
        if (csrfTokenInput) {
            const csrfToken = csrfTokenInput.value;
            // Продолжаем обработку
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = window.addToCartUrl;
            form.innerHTML = `
                <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                <input type="hidden" name="product_id" value="${itemId}">
                <input type="hidden" name="quantity" value="1">
            `;
            document.body.appendChild(form);
            form.submit();
        } else {
            console.error('CSRF token input not found.');
        }
    };
    

    // Обновление количества товаров в корзине
    function updateCartCount() {
        const totalCount = document.querySelectorAll('.cart-item').length;
        cartCount.textContent = totalCount;
    }
    updateCartCount();

    // Владельцы
    const ownerImages = document.querySelectorAll('.owner-img');

    ownerImages.forEach(image => {
        image.addEventListener('click', function () {
            this.classList.toggle('fullscreen');
        });
    });

    
    window.addEventListener('click', function (event) {
        if (event.target.classList.contains('owner-img') && !event.target.classList.contains('fullscreen')) {
            event.target.classList.remove('fullscreen');
        } else if (!event.target.classList.contains('owner-img')) {
            ownerImages.forEach(image => image.classList.remove('fullscreen'));
        }
    });

    
});

// ГАЛЕРЕЯ
document.addEventListener("DOMContentLoaded", function () {
    const galleryImages = document.querySelectorAll('.gallery-img');

    galleryImages.forEach(image => {
        image.addEventListener('click', function () {
            openFullscreen(this.src);
        });
    });

    function openFullscreen(src) {
        const fullscreenDiv = document.createElement('div');
        fullscreenDiv.classList.add('fullscreen');
        fullscreenDiv.innerHTML = `
            <span class="close">&times;</span>
            <img src="${src}" alt="Fullscreen Image">
        `;
        document.body.appendChild(fullscreenDiv);

        const closeBtn = fullscreenDiv.querySelector('.close');
        closeBtn.addEventListener('click', closeFullscreen);

        fullscreenDiv.addEventListener('click', function (event) {
            if (event.target === fullscreenDiv) {
                closeFullscreen();
            }
        });
    }

    function closeFullscreen() {
        const fullscreenDiv = document.querySelector('.fullscreen');
        if (fullscreenDiv) {
            fullscreenDiv.remove();
        }
    }
});
// ФАКЬЮ
document.addEventListener("DOMContentLoaded", function () {
    const faqQuestions = document.querySelectorAll('.faq-question');

    faqQuestions.forEach(question => {
        question.addEventListener('click', function () {
            const answer = this.nextElementSibling;

            // Закрываем все ответы, кроме текущего
            document.querySelectorAll('.faq-answer').forEach(ans => {
                if (ans !== answer) {
                    ans.classList.remove('active');
                }
            });

            // Открываем или закрываем текущий ответ
            answer.classList.toggle('active');
        });
    });
});


