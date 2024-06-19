const { exec, spawn } = require("child_process");
const { stderr } = require("process");


// new commit mesage
const gitCommit = (commitMessage) => {
  exec(
    `git add . && git commit -m ${commitMessage} && git push`,
    (error, stdout, stderr) => {
      if (error) {
        console.error(`Error pushing latest changes ${error.message}`);
        return;
      }

      if (stderr) {
        console.error(`Exec stderr: ${stderr}`);
        return;
      }

      console.log(`
      ================ Successfully Committed ✅  ==============================: 
      ================ Successfully Committed ✅  ==============================: ,
      ${stdout}`);
    }
  );
};
const format = (arg1, arg2) => {
  if (!arg1) return console.log("No arguement passed for formatting !!");

  exec(`semistandard --fix ${arg1} `, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${error.message}`);
      return;
    }

    if (stderr) {
      console.error(`Stderr: ${stderr}`);
      return;
    }

    console.log(
      `================ Successfully fix file ✅  ==============================: ${stdout} commiting code now  ⏳`
    );

    gitCommit(arg2);
  });
};

module.exports = format;
