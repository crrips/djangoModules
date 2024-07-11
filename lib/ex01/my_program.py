from path import Path


def main():
    try:
        Path.makedirs('some_dir')
    except FileExistsError as e:
        print(e)
    Path.touch('some_dir/some_file')
    f = Path('some_dir/some_file')
    f.write_text('aboba')
    print(f.read_text())


if __name__ == '__main__':
    main()