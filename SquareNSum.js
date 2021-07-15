// Square(n) Sum

// Complete the square sum function so that it squares each number passed into it and then sums the results together.

// For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

function squareSum(numbers)
  {
    if (numbers.length)
    {
    let numSquared =  numbers.map(x => x*x)
    return numSquared.reduce(function(a, b) {
      return a + b;})
    } 
    else
    {
      return 0;
    }
  }
  
  
  console.log(squareSum([0, 3, 4, 5]));
  console.log(squareSum([]));
