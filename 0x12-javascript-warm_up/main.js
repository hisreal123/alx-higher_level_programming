const format = require("./formatter/index");

// Extract arguments from command line
const arg1 = process.argv[2]; // File name to format
const arg2 = process.argv[3]; // Commit message

// Call the format function with provided arguments
format(arg1, arg2);
