// Build Tower

// Build Tower by the following given argument:
// number of floors (integer and always greater than 0).

// Tower block is represented as *

// Python: return a list;
// JavaScript: returns an Array;
// C#: returns a string[];
// PHP: returns an array;
// C++: returns a vector<string>;
// Haskell: returns a [String];
// Ruby: returns an Array;
// Lua: returns a Table;

// for example, a tower of 3 floors looks like below

// [
//   '  *  ', 
//   ' *** ', 
//   '*****'
// ]
// and a tower of 6 floors looks like below

// [
//   '     *     ', 
//   '    ***    ', 
//   '   *****   ', 
//   '  *******  ', 
//   ' ********* ', 
//   '***********'
// ]

function towerBuilder(nFloors) {

    let length = (nFloors * 2) -1;
    let towerArray = [];
    let temp;

    for (let i = 1; i <= nFloors; i++)
        {
            stars = (i * 2) -1;
            let numberSpaces = Math.ceil((length - stars) / 2);
            let spaces = " ".repeat(numberSpaces);
            let numberStars = "*".repeat(stars);
            temp = `${spaces}${numberStars}${spaces}`;
            towerArray.push(temp);
            
        }
    return towerArray;
    }
console.log(towerBuilder(5));
