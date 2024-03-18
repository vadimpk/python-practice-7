import app.io.input as input
import app.io.output as output


def main():
    console_text = input.read_from_console()
    output.print_to_console(console_text)
    output.write_to_file_builtin('data/output.txt', console_text)

    file_text = input.read_from_file_builtin('data/sample.txt')
    output.print_to_console(file_text)
    output.write_to_file_builtin('data/output2.txt', file_text)

    df = input.read_from_file_pandas('data/sample.csv')
    output.print_to_console(df.head().to_string())


if __name__ == "__main__":
    main()
