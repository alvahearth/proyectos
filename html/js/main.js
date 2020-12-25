let num1 = document.getElementById('#value1');
let num2 = document.getElementById('#value2').value;

let sumButton = document.getElementById('calc');
sumButton.addEventListener('click', function() { sumNumbers(num1, num2) });

function sumNumbers(x,y) {
    document.getElementById('result').innerHTML = x + y;
}