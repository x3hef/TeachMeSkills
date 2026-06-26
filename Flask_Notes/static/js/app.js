document.addEventListener("DOMContentLoaded", () => {

    const btn = document.getElementById("themeToggle");

    const icon = btn?.querySelector(".icon");

    function setTheme(isDark) {
        document.body.classList.toggle("dark", isDark);
        localStorage.setItem("theme", isDark ? "dark" : "light");
        if (icon) icon.textContent = isDark ? "☀️" : "🌙";
    }

    setTheme(localStorage.getItem("theme") === "dark");

    btn?.addEventListener("click", () => {
        setTheme(!document.body.classList.contains("dark"));
    });

    window.openModal = function (e) {
        if (e) e.preventDefault();
        document.getElementById("modal")?.classList.add("active");
    };

    window.closeModal = function () {
        document.getElementById("modal")?.classList.remove("active");
    };

    document.querySelectorAll(".note-card").forEach((card, i) => {
        card.style.opacity = "0";
        card.style.transform = "translateY(10px)";

        setTimeout(() => {
            card.style.transition = "0.4s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, i * 70);
    });

});

async function getWeather() {
    const city = document.getElementById("cityInput");
    const result = document.getElementById("weatherResult");

    if (!city || !result) return;

    const name = city.value.trim();

    if (!name) {
        result.innerText = "Введите город";
        return;
    }

    try {
        const geo = await fetch(
            `https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(name)}`
        ).then(r => r.json());

        if (!geo.results?.length) {
            result.innerText = "Город не найден";
            return;
        }

        const { latitude, longitude } = geo.results[0];

        const weather = await fetch(
            `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current_weather=true`
        ).then(r => r.json());

        result.innerText = `🌡 ${weather.current_weather.temperature}°C`;

    } catch {
        result.innerText = "Ошибка загрузки погоды";
    }
}


async function getRate() {
    const result = document.getElementById("rateResult");

    if (!result) return;

    try {
        const data = await fetch("https://open.er-api.com/v6/latest/USD")
            .then(r => r.json());

        const rate = data?.rates?.EUR;

        if (!rate) {
            result.innerText = "Ошибка курса";
            return;
        }

        result.innerText = `1 USD = ${rate.toFixed(2)} EUR`;

    } catch {
        result.innerText = "Ошибка загрузки курса";
    }
}


function calc() {
    const input = document.getElementById("calcInput");
    const result = document.getElementById("calcResult");

    if (!input || !result) return;

    try {
        const expr = input.value.trim();

        if (!expr) {
            result.innerText = "Введите выражение";
            return;
        }

        // безопасный eval
        const value = Function(`"use strict"; return (${expr})`)();
        result.innerText = `= ${value}`;

    } catch {
        result.innerText = "Ошибка";
    }
}

document.addEventListener("mousemove", (e) => {
    const x = (e.clientX / window.innerWidth) * 100;
    const y = (e.clientY / window.innerHeight) * 100;

    document.body.style.setProperty("--x", x + "%");
    document.body.style.setProperty("--y", y + "%");
});

function openEditModal(id, title, content) {
    const modal = document.getElementById("editModal");
    const form = document.getElementById("editForm");

    document.getElementById("editTitle").value = title;
    document.getElementById("editContent").value = content;

    form.action = `/posts/${id}/edit`;

    modal.classList.add("active");
}

function closeEditModal() {
    document.getElementById("editModal").classList.remove("active");
}
document.addEventListener("DOMContentLoaded", () => {

    const searchInput = document.getElementById("searchInput");

    if (!searchInput) return;

    searchInput.addEventListener("input", function () {
        const value = this.value.toLowerCase().trim();

        document.querySelectorAll(".note-card").forEach(card => {

            const titleEl = card.querySelector(".note-title");
            const textEl = card.querySelector(".note-text");

            const title = titleEl?.innerText || "";
            const text = textEl?.innerText || "";

            const match =
                title.toLowerCase().includes(value) ||
                text.toLowerCase().includes(value);

            card.style.display = match ? "block" : "none";

            // очистка старой подсветки
            if (titleEl) titleEl.innerHTML = title;
            if (textEl) textEl.innerHTML = text;

            // подсветка
            if (value && match) {
                if (titleEl) {
                    titleEl.innerHTML = highlightText(title, value);
                }
                if (textEl) {
                    textEl.innerHTML = highlightText(text, value);
                }
            }
        });
    });

    function highlightText(text, query) {
        if (!query) return text;

        const regex = new RegExp(`(${escapeRegExp(query)})`, "gi");

        return text.replace(
            regex,
            `<span class="highlight">$1</span>`
        );
    }

    function escapeRegExp(string) {
        return string.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    }

});