document.addEventListener("DOMContentLoaded", () => {

    // 1. Анимация появления при скролле (Scroll Reveal)
    const revealElements = document.querySelectorAll('.page-header, .glass-card, .item-card, .table-info-box');

    // Добавляем базовый класс для скрытия
    revealElements.forEach(el => el.classList.add('reveal'));

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Добавляем класс active, когда элемент появляется на экране
                entry.target.classList.add('active');
                // Перестаем следить за элементом после его появления
                observer.unobserve(entry.target);
            }
        });
    }, {
        root: null,
        rootMargin: '0px 0px -50px 0px', // Срабатывает чуть раньше, чем дойдет до низа экрана
        threshold: 0.1
    });

    // Применяем наблюдатель и добавляем небольшую задержку для эффекта лесенки (каскада)
    revealElements.forEach((el, index) => {
        el.style.transitionDelay = `${(index % 4) * 0.1}s`;
        revealObserver.observe(el);
    });

    // 2. Анимация хедера при скролле
    const header = document.querySelector('.header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.style.padding = '10px 0';
            header.style.background = 'rgba(5, 5, 5, 0.95)';
        } else {
            header.style.padding = '0';
            header.style.background = 'rgba(5, 5, 5, 0.9)';
        }
    });

    // 3. Кастомный конфирм для удаления
    const deleteForms = document.querySelectorAll("form[action*='delete']");
    deleteForms.forEach(form => {
        form.addEventListener('submit', (e) => {
            if(!confirm('ОТМЕНА ВИЗИТА: Вы уверены, что хотите освободить стол?')) {
                e.preventDefault();
            }
        });
    });
});