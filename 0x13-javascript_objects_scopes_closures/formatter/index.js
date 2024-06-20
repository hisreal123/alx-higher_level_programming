// Import necessary modules
const { exec } = require("child_process");
const gitCommit = async (commitMessage) => {
  exec(
    `git add . && git commit -m "${commitMessage}" && git push origin main`,
    (error, stdout, stderr) => {
      if (error) {
        console.error(`Error pushing latest changes: ${error.message}`);
        return;
      }

      if (stderr) {
        console.error(`Exec stderr: ${stderr}`);
        return;
      }

      console.log(`
      ================ Successfully Committed ✅ ==============================
      ${stdout}`);
    }
  );
};

// Define function to format files using semistandard
const format = async (file, commitMessage) => {
  if (!file) {
    console.log("No argument passed for formatting!!");
    return;
  }

  exec(`semistandard --fix ${file}`, async (error, stdout, stderr) => {
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
    await gitCommit(commitMessage);
  });
};

module.exports = format;
