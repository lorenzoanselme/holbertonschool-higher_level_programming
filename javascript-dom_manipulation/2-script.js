const Header = document.querySelector('header');
const redHeader = document.querySelector('#red_header');

redHeader.addEventListener('click', () => {
    Header.classList.add('red');
});