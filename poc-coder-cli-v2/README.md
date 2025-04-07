# AI Coding Assistant CLI

AI Coding Assistant CLI is a command-line tool designed to assist developers by providing AI-powered code generation, explanation, test generation, and more. It integrates seamlessly with Git projects and supports monorepos.

## Features

- **Code Indexing:** Index the codebase to understand the structure and content of the files.
- **Code Generation:** Generate code snippets based on user specifications.
- **Code Explanation:** Provide explanations for specific code segments.
- **Test Generation:** Generate test cases for specified functions.
- **Comment Addition:** Add comments to specified functions or code segments.
- **Cache Management:** Manage caching of indexed data and AI responses for performance.
- **Git Integration:** Integrate with Git to understand the project structure and changes.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ai-coding-assistant-cli.git
    cd ai-coding-assistant-cli
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Index the Codebase
```sh
ai-assist index
```
Output: "Indexing complete. Indexed 120 files."

### Generate Code
```sh
ai-assist generate_code --file <file_path> --function <function_name>
```
Output: "Generated code for <function_name> in <file_path>."

### Explain Code
```sh
ai-assist explain --file <file_path> --function <function_name>
```
Output: "The function <function_name> in <file_path> does X, Y, and Z."

### Generate Tests
```sh
ai-assist generate_test --file <file_path> --function <function_name>
```
Output: "Generated test cases for <function_name> in <file_path>."

### Add Comments
```sh
ai-assist add_comment --file <file_path> --function <function_name>
```
Output: "Added comments to <function_name> in <file_path>."

### Clear Cache
```sh
ai-assist cache_clear
```
Output: "Cache cleared."

### Check Git Status
```sh
ai-assist git_status
```
Output: "On branch main. Your branch is up to date with 'origin/main'."

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.