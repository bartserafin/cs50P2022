import validators
def main():
    print(validate_email(input("Email: ").strip()))


def validate_email(s):
    """Validate an email address using validator-collection"""
    email_address = validators.email(s)
    if email_address:
        return 'Valid'
    else:
        return 'Invalid'


if __name__ == "__main__":
    main()