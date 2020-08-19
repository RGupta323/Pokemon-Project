//define some variables using DOM functions 
var pokemonContainer = document.querySelector('.pokemon-container'); 
var formEl = document.querySelector("form"); 
var inputEl = document.querySelector("input[type=text]"); 

//add an event listencer to formEl 
formEl.addEventListener("submit", (e) => {
    e.preventDefault(); //stops the page from refreshing 
    pokemonContainer.innerHTML=""; //clear the div html content 
    getPokemon(inputEl.value); //actually calling a function here to reference the 
    //poke api 
})

async function getPokemon(name="bulbasaur"){
    var res = await fetch('https://pokeapi.co/api/v2/pokemon/$(name)'); 
    var pokemon = await res.json(); 
}

var pokemonEl = document.createElement('div'); //creating a div 
pokemonEl.classList.add('pokemon'); //giving the newly created div, with a 
//class of pokemon 

pokemonEl.innerHTML = "<div class='info'> <img src='https://pokeres.bastionbot.org/images/pokemon/${pokemon.id}.png' width='200'> <h2>${pokemon.name}</h2></div>"

pokemonContainer.appendChild(pokemonEl); 
