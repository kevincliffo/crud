const nameInput = document.querySelector('input[name=name]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
              .replace(/&/g, '-and-')
              .replace(/[\s\W-]+/g, '-') //replaces spaces and non word chars wirth  single dasj
};
nameInput.addEventListener('keyup', (e) =>{
    slugInput.setAttribute('value', slugify(nameInput.value));
});