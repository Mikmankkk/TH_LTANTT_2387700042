import argparse
from securecrypto import aes_utils

def main():
    parser = argparse.ArgumentParser(description="SecureCrypto CLI")
    parser.add_argument('--encrypt', help='Encrypt file')
    parser.add_argument('--decrypt', help='Decrypt file')
    parser.add_argument('--password', help='Password for AES encryption/decryption')
    parser.add_argument('--key', help='Base64 Key for AES decryption')
    args = parser.parse_args()

    if args.encrypt:
        if not args.password:
            print("Error: --password is required for encryption")
            return
        res = aes_utils.encrypt_file_aes(args.encrypt, args.password)
        print(res)
    elif args.decrypt:
        # Hỗ trợ cả key truyền trực tiếp hoặc password
        key = args.key or args.password
        if not key:
            print("Error: --key or --password (key base64) is required for decryption")
            return
        out = aes_utils.decrypt_file_aes(args.decrypt, key)
        print(f"Decrypted. Output: {out}")

if __name__ == '__main__':
    main()
