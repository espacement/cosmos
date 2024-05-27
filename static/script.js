const button = document.querySelector('.dropdown');
const dropdown = document.querySelector('.dropdown-content');
const cartItems = document.querySelector('.cart-items');


// window.addEventListener('scroll', function() {
//     var upper = document.querySelector('.upper_container');
//     var header = document.querySelector('header');

//     if(window.scrollY > 0) {
//         upper.style.top = '-45px';
//         header.style.top = '0';
//     } else {
//         upper.style.top = '0';
//         header.style.top = '45px';
//     }
// });

// button.addEventListener('mouseover', function() {
//     dropdown.classList.add('show');
// });

// button.addEventListener('mouseout', function() {
//     dropdown.classList.remove('show');
// });

// Корзина

document.addEventListener("DOMContentLoaded", function () {
    const cart = [];
    const cartModal = document.getElementById('cart-modal');
    const cartItemsList = document.getElementById("cart-items");
    const orderForm = document.getElementById("order-form");
    const cartCount = document.getElementById("cart-count");
    const totalAmountElement = document.getElementById("total-amount");

    document.getElementById('open-cart').addEventListener('click', () => {
        cartModal.style.display = "flex";
        renderCartItems();
    });

    document.querySelector(".close-button").addEventListener("click", () => {
        cartModal.style.display = "none";
    });

    window.addEventListener("click", (event) => {
        if (event.target === cartModal) {
            cartModal.style.display = "none";
        }
    });

    window.addToCart = function (itemName, itemPrice, itemId) {
        const existingItem = cart.find(item => item.name === itemName);
        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            cart.push({ name: itemName, price: itemPrice, quantity: 1 });
        }
        
        renderCartItems();
        updateCartCount();
    };

    function renderCartItems() {
        cartItemsList.innerHTML = "";
        let totalAmount = 0;
        cart.forEach((item, index) => {
            const li = document.createElement("li");
            li.innerHTML = `
                ${item.name} - ₽${item.price} x ${item.quantity}
                <button onclick="updateQuantity(${index}, 'increase')">+</button>
                <button onclick="updateQuantity(${index}, 'decrease')">-</button>
            `;
            cartItemsList.appendChild(li);
            totalAmount += item.price * item.quantity;
        });
        totalAmountElement.textContent = `₽${totalAmount}`;
    }

    window.updateQuantity = function (index, action) {
        if (action === 'increase') {
            cart[index].quantity += 1;
        } else if (action === 'decrease') {
            cart[index].quantity -= 1;
            if (cart[index].quantity === 0) {
                cart.splice(index, 1);
            }
        }
        renderCartItems();
        updateCartCount();
    };

    function updateCartCount() {
        const totalCount = cart.reduce((total, item) => total + item.quantity, 0);
        cartCount.textContent = totalCount;
        console.log(`Cart count updated: ${totalCount}`);
    }

    orderForm.addEventListener("submit", function (event) {
        event.preventDefault();
        const formData = new FormData(orderForm);
        const email = formData.get("email");
        const phone = formData.get("phone");
        const lastname = formData.get("lastname");
        const firstname = formData.get("firstname");
        const middlename = formData.get("middlename");

        console.log("Order Submitted:", {
            email,
            phone,
            lastname,
            firstname,
            middlename,
            cart
        });

        alert("Order submitted successfully!");
        cartModal.style.display = "none";
        orderForm.reset();
        cart.length = 0;
        renderCartItems();
        updateCartCount();
    });
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

    // Слайдер
    let currentSlideIndex = 0;

    window.nextSlide = function () {
        const slides = document.querySelectorAll('.slide');
        slides[currentSlideIndex].style.display = 'none';
        currentSlideIndex = (currentSlideIndex + 1) % slides.length;
        slides[currentSlideIndex].style.display = 'flex';
    };

    window.prevSlide = function () {
        const slides = document.querySelectorAll('.slide');
        slides[currentSlideIndex].style.display = 'none';
        currentSlideIndex = (currentSlideIndex - 1 + slides.length) % slides.length;
        slides[currentSlideIndex].style.display = 'flex';
    };

    // Инициализация первого слайда
    const slides = document.querySelectorAll('.slide');
    slides.forEach((slide, index) => {
        if (index !== currentSlideIndex) {
            slide.style.display = 'none';
        } else {
            slide.style.display = 'flex';
        }
    });

    const slideInterval = setInterval(nextSlide, 5000);

    // Добавить обработчики событий для стрелок
    document.querySelector('.prev').addEventListener('click', () => {
        prevSlide();
        clearInterval(slideInterval);
        setTimeout(() => {
            startSlideShow();
        }, 5000);
    });

    document.querySelector('.next').addEventListener('click', () => {
        nextSlide();
        clearInterval(slideInterval);
        setTimeout(() => {
            startSlideShow();
        }, 5000);
    });

    function startSlideShow() {
        slideInterval = setInterval(nextSlide, 5000);
    }

    // Остановить слайдшоу при наведении мыши
    document.querySelector('.slider').addEventListener('mouseover', () => {
        clearInterval(slideInterval);
    });

    // Запустить слайдшоу при уходе мыши
    document.querySelector('.slider').addEventListener('mouseout', () => {
        startSlideShow();
    });

    // Запустить автоматическую прокрутку при загрузке страницы
    startSlideShow();
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
