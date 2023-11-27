/*Theme Toggle*/

// Check if the user has a theme preference in localStorage
const storedTheme = localStorage.getItem('theme');
if (storedTheme) {
  document.body.classList.add(storedTheme);
  updateButton(storedTheme);
}

// Toggle dark mode
document.getElementById('theme-toggle').addEventListener('click', function () {
  document.body.classList.toggle('dark-mode');
  // Update localStorage with the current theme choice
  const currentTheme = document.body.classList.contains('dark-mode') ? 'dark-mode' : '';
  localStorage.setItem('theme', currentTheme);
  updateButton(currentTheme);
});

// Function to update the button text based on the theme
function updateButton(theme) {
  const buttonElement = document.getElementById('theme-toggle');
  // Update the button text based on the theme
  buttonElement.innerText = theme === 'dark-mode' ? '🌞 Day Mode' : '🌙 Night Mode';
}