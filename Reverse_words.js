// Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

// Examples
// "This is an example!" ==> "sihT si na !elpmaxe"
// "double  spaces"      ==> "elbuod  secaps"

// - revised attempt
function reverseWords(str)
{
let splitString = str.split(" ");
let wordsReversed = ""
for (var i = 0; i <= splitString.length-1; i++){
    x = splitString[i].split("")
    x = x.reverse().join("")
    wordsReversed+= x + " "
        }
return wordsReversed.trim();
}


console.log(reverseWords("This is an example!"));


// - 1st attempt
function reverseWords1(str) 
    {

    var str_array = str.split(" ");
    var temp_array = []

    for (var i = 0; i <= str_array.length - 1; i++) 
        {
        var temp = "";

        for ( var j = 0; j <= str_array[i].length - 1; j++) 
            {
                temp += str_array[i][str_array[i].length - j -1];
            }

        temp_array.push(temp)

        }
    return temp_array.join(" ");
    }

  console.log(reverseWords1("This is an example!"));


