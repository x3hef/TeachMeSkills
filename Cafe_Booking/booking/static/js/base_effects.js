document.addEventListener('DOMContentLoaded', () => {
    const cursor = document.getElementById('custom-cursor');
    const links = document.querySelectorAll('a, button, input, select');

    document.addEventListener('mousemove', (e) => {
        cursor.style.left = e.clientX - 7 + 'px';
        cursor.style.top = e.clientY - 7 + 'px';
    });

    links.forEach(link => {
        link.addEventListener('mouseenter', () => cursor.classList.add('cursor-active'));
        link.addEventListener('mouseleave', () => cursor.classList.remove('cursor-active'));
    });
});