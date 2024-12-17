# NP2W: Nextcloud Passwords to Bitwarden Vault

Easily convert a Nextcloud Passwords (NP) database to a Bitwarden Vault (BW). 
This script is based on [@monperrus](https://www.github.com/monperrus) work I found [here](https://gist.github.com/monperrus/c671817d53f6fc4bfe8d1773f28262d7).
I wanted to update this script to make it work for my own migration from NP to BW. 

# Set-up
1. Clone repository:
```
https://github.com/godisopensource/np2bw.git
```

2. Ensure you have all necessary dependancies installed:
```
pip install csv json
```
3. Export your Nextcloud passwords as "Predefined csv" and put it in the same folder as this script.
4. Put its path into `csv_file_path` variable
5. The script will then convert your file to a `.json` file (which will be easier for BW to understand) and apply the correct formatting to your database, so it will be easily imported into BW.

---
Many thanks to [Martin Monperrus](https://www.github.com/monperrus) for having provided a base code and having been open to contributions. Feel free to contribute to this project too.