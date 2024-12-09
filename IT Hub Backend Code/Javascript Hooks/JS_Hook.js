const { spawn } = require('child_process');

function callPythonFunction(functionName, args) {
    // Prepare the input for the Python script
    const input = JSON.stringify({ function: functionName, args });


    //Path of the Python DataBaseFetch.py
    //The \\ are needed for the path
    const path = "C:\\Users\\milan\\OneDrive\\Desktop\\IT-Database-Code\\IT Hub Backend Code\\Python\\DataBaseFetch.py";

    // Spawn the Python process
    const pythonProcess = spawn('py', [path, input]);

    // Capture the output from Python
    pythonProcess.stdout.on('data', (data) => {
        
        const result = JSON.parse(data.toString());

        if (result.error) {
            console.error(`Error: ${result.error}`);
        } else {
            console.log(`Result: ${result.result}`);
        }
    });

    // Capture errors
    pythonProcess.stderr.on('data', (data) => {
        console.error(`Python error: ${data}`);
    });
}

// Example usage
  // Calls multiply_by_two(5)
// callPythonFunction('greet', ['Alice']);      // Calls greet('Alice')
console.log(typeof(callPythonFunction('getEmpInfoPackage')));

