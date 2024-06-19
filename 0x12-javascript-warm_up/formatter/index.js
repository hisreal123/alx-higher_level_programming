// Import necessary modules
const { exec } = require("child_process");

// Function to add files
const gitAdd = (commitMessage) => {
  exec("git add .", (error, stdout, stderr) => {
    if (error) {
      console.error(`Error adding files: ${error.message}`);
      return;
    }
    if (stderr) {
      console.error(`Git add error: ${stderr}`);
      return;
    }
    console.log(`Files added successfully: ${stdout}`);

    // After adding, commit the changes
    gitCommit(commitMessage);
  });
};

// Function to commit changes
const gitCommit = (commitMessage) => {
  exec(`git commit -m '${commitMessage}'`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error committing changes: ${error.message}`);
      return;
    }
    if (stderr) {
      console.error(`Git commit error: ${stderr}`);
      return;
    }
    console.log(`Changes committed successfully: ${stdout}`);

    // After committing, push changes
    gitPush();
  });
};

// Function to push changes
const gitPush = () => {
  exec("git push", (error, stdout, stderr) => {
    if (error) {
      console.error(`Error pushing changes: ${error.message}`);
      return;
    }
    if (stderr) {
      console.error(`Git push error: ${stderr}`);
      return;
    }
    console.log(`Changes pushed successfully: ${stdout}`);
  });   
};

// Define function to format files using semistandard
const format = (file, commitMessage) => {
  if (!file) {
    console.log("No argument passed for formatting!!");
    return;
  }

  exec(`semistandard --fix ${file}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${error.message}`);
      return;
    }

    if (stderr) {
      console.error(`Stderr: ${stderr}`);
      return;
    }

    console.log(`
      ================ Successfully Fixed File ✅ ==============================
      ${stdout}`);

    // After formatting, commit the changes
    gitAdd(commitMessage);
  });
};

module.exports = format;
