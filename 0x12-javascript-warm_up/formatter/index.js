// Import necessary modules
const { exec } = require("child_process");

// Define function to commit changes to Git
const gitCommit = (commitMessage) => {
  exec(
    `git add . && git commit -m '${commitMessage}' && git push`,
    (error, stdout, stderr) => {
      if (error) {
        console.error(`Error pushing latest changes: ${error.message}`);
        return;
      }

      if (stderr) {
        console.error(`Git push error: ${stderr}`);
        return;
      }

      console.log(`
      ================ Successfully Committed and Pushed ✅ ==============================
      ${stdout}`);
    }
  );
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
    gitCommit(commitMessage);
  });
};

module.exports = format;
