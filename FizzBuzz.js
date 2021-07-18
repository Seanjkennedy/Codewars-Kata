// Fizz Buzz

// Return an array containing the numbers from 1 to N, where N is the parametered value.

// Replace certain values however if any of the following conditions are met:

// If the value is a multiple of 3: use the value "Fizz" instead
// If the value is a multiple of 5: use the value "Buzz" instead
// If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead
// N will never be less than 1.

// Method calling example:

// fizzbuzz(3) -->  [1, 2, "Fizz"]

function fizzbuzz(n)
{
    let z = [];
    for (let i = 1; i <= n; i++){
        let temp = "";
        if (i % 3 === 0){
            temp += "Fizz";
        }
        if (i % 5 === 0){
            temp += "Buzz";
        }
        if(i % 3 !== 0 && i % 5 !== 0){
            temp = i;
        }
        z.push(temp);
    }
    return z;

}

console.log(fizzbuzz(20))
