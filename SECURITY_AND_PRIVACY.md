# Security and privacy boundary

The Git history must not contain patient level prediction tables, private access tokens, credentials, signed data use agreements, or controlled access image data.

Before any public release:

1. replace all author and ethics placeholders in the manuscript;
2. select an explicit source code licence;
3. rerun secret scanning and patient level identifier scanning;
4. confirm every release asset against the dataset licence current at the original source;
5. keep mBRSET, MESA, ARIC, and any other controlled access resource outside the repository.

