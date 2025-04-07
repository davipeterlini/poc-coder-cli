import argparse
from components import CodeIndexer, CodeGenerator, CodeExplainer, TestGenerator, CommentAdder, CacheManager, GitIntegration, AIInterface

def main():
    parser = argparse.ArgumentParser(description="AI Coding Assistant CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Index command
    subparsers.add_parser("index", help="Index the codebase")

    # Generate code command
    generate_code_parser = subparsers.add_parser("generate_code", help="Generate code")
    generate_code_parser.add_argument("--file", required=True, help="File path")
    generate_code_parser.add_argument("--function", required=True, help="Function name")

    # Explain code command
    explain_parser = subparsers.add_parser("explain", help="Explain code")
    explain_parser.add_argument("--file", required=True, help="File path")
    explain_parser.add_argument("--function", required=True, help="Function name")

    # Generate test command
    generate_test_parser = subparsers.add_parser("generate_test", help="Generate test cases")
    generate_test_parser.add_argument("--file", required=True, help="File path")
    generate_test_parser.add_argument("--function", required=True, help="Function name")

    # Add comment command
    add_comment_parser = subparsers.add_parser("add_comment", help="Add comments")
    add_comment_parser.add_argument("--file", required=True, help="File path")
    add_comment_parser.add_argument("--function", required=True, help="Function name")

    # Cache clear command
    subparsers.add_parser("cache_clear", help="Clear cache")

    # Git status command
    subparsers.add_parser("git_status", help="Show git status")

    args = parser.parse_args()

    if args.command == "index":
        CodeIndexer().index()
    elif args.command == "generate_code":
        CodeGenerator().generate_code(args.file, args.function)
    elif args.command == "explain":
        CodeExplainer().explain(args.file, args.function)
    elif args.command == "generate_test":
        TestGenerator().generate_test(args.file, args.function)
    elif args.command == "add_comment":
        CommentAdder().add_comment(args.file, args.function)
    elif args.command == "cache_clear":
        CacheManager().clear_cache()
    elif args.command == "git_status":
        GitIntegration().status()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()