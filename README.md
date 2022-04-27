# WP Engine Selenium User Portal Access Logs Automator

This Python script uses Selenium and Chromedrive to pull WP Engine Complete Access Logs for last 2 calendar days.
Dependencies: `python3`, `pip`, `selenium`, `chromedriver`

## To Use:

Simply clone the repo and open `init.sh` in your chosen terminal client (Right Click > Open With...) and follow the instructions.

## Authentication

Supports WP Engine internal use with OKTA credentials and appropriate LDAP permission-sets. Also support standard login. Does not support customer MFA or SSO login methods.

It is recommended you create a dedicated user account in the User Portal with the minimum access required for this script with username/password authentication. It is also recommended this account be decomissioned and reprovisioned periodically.
