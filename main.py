from app import create_app


def main():
    try:
        create_app().run(
            host="127.0.0.1",
            port=8000,
            debug=True
        )
    except KeyboardInterrupt:
        exit(1)


if __name__=='__main__':
    main()
