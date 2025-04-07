const { Command } = require('commander');
const inquirer = require('inquirer');
const simpleGit = require('simple-git');
const fs = require('fs');
const path = require('path');

const program = new Command();
const git = simpleGit();

program
  .version('1.0.0')
  .description('A CLI application that replicates the functionalities of Claude Code');

program
  .command('edit <file> <line> <content>')
  .description('Edit a file at a specific line with the provided content')
  .action((file, line, content) => {
    editFile(file, line, content);
  });

program
  .command('explain <file> <functionName>')
  .description('Explain how a specific function works in the given file')
  .action((file, functionName) => {
    explainFunction(file, functionName);
  });

program
  .command('run <command>')
  .description('Run a development command')
  .action((command) => {
    runCommand(command);
  });

program
  .command('git <action> [options...]')
  .description('Perform a git action')
  .action((action, options) => {
    performGitAction(action, options);
  });

program.parse(process.argv);

function editFile(file, line, content) {
  const filePath = path.resolve(file);
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) throw err;
    const lines = data.split('\n');
    lines[line - 1] = content;
    fs.writeFile(filePath, lines.join('\n'), 'utf8', (err) => {
      if (err) throw err;
      console.log(`File ${file} edited successfully at line ${line}`);
    });
  });
}

function explainFunction(file, functionName) {
  const filePath = path.resolve(file);
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) throw err;
    const regex = new RegExp(`function ${functionName}\\s*\\(([^)]*)\\)\\s*{([^}]*)}`, 'g');
    const match = regex.exec(data);
    if (match) {
      console.log(`Function ${functionName} found:\n${match[0]}`);
    } else {
      console.log(`Function ${functionName} not found in file ${file}`);
    }
  });
}

function runCommand(command) {
  const exec = require('child_process').exec;
  exec(command, (err, stdout, stderr) => {
    if (err) {
      console.error(`Error executing command: ${err}`);
      return;
    }
    console.log(`Command output: ${stdout}`);
    if (stderr) {
      console.error(`Command error output: ${stderr}`);
    }
  });
}

function performGitAction(action, options) {
  switch (action) {
    case 'commit':
      git.commit(options[0], options.slice(1))
        .then(() => console.log('Commit successful'))
        .catch((err) => console.error(`Error committing: ${err}`));
      break;
    case 'pull':
      git.pull()
        .then(() => console.log('Pull successful'))
        .catch((err) => console.error(`Error pulling: ${err}`));
      break;
    case 'push':
      git.push()
        .then(() => console.log('Push successful'))
        .catch((err) => console.error(`Error pushing: ${err}`));
      break;
    default:
      console.log(`Unknown git action: ${action}`);
  }
}