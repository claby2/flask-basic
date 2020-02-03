let input = document.getElementById("input"); //Get input element (textarea)
let submit = document.getElementById("submit"); //Get submit element (button)
let output = document.getElementById("output"); //Get output element (div)

function getCountryAlpha(country){ //Converts country name into ISO 3166-1 alpha-2 code (eg. Singapore -> SG), this communicates with the backend (flask server)
    return fetch('http://localhost:5000/api/country?id=' + country)
    .then(data => data.text())
    .then(data => data)
}

function getIncome(alpha){ //With the ISO 3166-1 alpha-2 code, it communicates with the backend (flask server) to get information about the country
    return fetch('http://localhost:5000/api/income?id=' + alpha)
    .then(data => data.json())
    .then(data => data[1]) //References element index 1, this is where the information we need is at
}

submit.addEventListener("click", ()=>{ //When the submit button is clicked...
    let country = input.value; //Get the output value
    getCountryAlpha(country).then(alpha =>{ //With the name of the country, convert it into ISO 3166-1 alpha-2 code referenced by 'alpha'
        getIncome(alpha).then(info =>{
            let p = document.createElement('p'); //Create a p element (<p></p>)
            p.innerText = country + " - " + info[0].incomeLevel.value; //Format the innertext of the p element to include country name and income level
            output.appendChild(p); //Push the p element into the output div
        })
    })
})