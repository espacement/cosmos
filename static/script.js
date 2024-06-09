const button = document.querySelector('.dropdown');
const dropdown = document.querySelector('.dropdown-content');
const cartItems = document.querySelector('.cart-items');

// Корзина

document.addEventListener("DOMContentLoaded", function () {
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


