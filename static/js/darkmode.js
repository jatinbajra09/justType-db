//  --- dark mode js ---

const toggle = document.querySelector('.toggle');
const body = document.body;

// Check if the theme preference is already set in sessionStorage
const selectedTheme = sessionStorage.getItem('theme');

// If the theme preference is not set, default to dark mode
const isDarkMode = selectedTheme === null ? true : selectedTheme === 'dark';

// Apply the appropriate theme class and update the toggle accordingly
body.classList.add('dark-mode', isDarkMode);
toggle.checked = isDarkMode;

// Update the sessionStorage with the current theme preference
sessionStorage.setItem('theme', isDarkMode ? 'dark' : 'light');

toggle.addEventListener('change', function () {
    body.classList.toggle('dark-mode');
    const isDarkMode = body.classList.contains('dark-mode')
        sessionStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
});

window.addEventListener('load', function () {
    const selectedTheme = sessionStorage.getItem('theme');
    if (selectedTheme === 'dark') {
        body.classList.add('dark-mode');
        toggle.checked = true;
    }
});
