const portalScene = document.querySelector('.portal-scene');
const bg = document.querySelector('.main-bg');

document.addEventListener('mousemove', (e) => {
    const x = (window.innerWidth / 2 - e.pageX) / 70;
    const y = (window.innerHeight / 2 - e.pageY) / 70;

    // Двигаем весь портал целиком вместе с персонажами[cite: 5]
    if (portalScene) {
        portalScene.style.transform = `translate(${x}px, ${y}px)`;
    }

    // Легкий параллакс фона[cite: 5]
    if (bg) {
        bg.style.transform = `translate(${-x/2}px, ${-y/2}px) scale(1.05)`;
    }
});