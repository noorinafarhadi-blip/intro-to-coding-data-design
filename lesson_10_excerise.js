// ###### Exercise ########

// Adding up numbers and calculating average

// Define the required variables
let sum = 0;
let numbers = 0;
let average = 0;

// Take input from the user
let user_input = parseInt(prompt("Please enter a number: (negative number stops input)"));

// Do a while loop to run until the user input is < 0
while (user_input >= 0) {

    // Add all positive numbers
    sum = sum + user_input;

    // Increase loop counter
    numbers++;

    // Take input again
    user_input = parseInt(prompt("Please enter a number:"));
}

// Calculate average
if (numbers > 0) {
    average = sum / numbers;
}
else {
    average = 0;
}

// Output into console
console.log("Number of inputs: ", numbers, "Sum: ", sum, "Average: ", average);

console.log("The sum of all inputs is: " + sum + " !");
console.log("The average of all inputs is: " + average + " !");