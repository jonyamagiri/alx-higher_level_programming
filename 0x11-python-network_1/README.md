## 0x11. Python - Network #1

> This repository contains the tasks for `Python - Network #1` project and a description of what each program or function does:

### Learning Objectives

* How to fetch internet resources with the Python package `urllib`
* How to decode `urllib` body response
* How to use the Python package `requests` #requestsiswaysimplerthanurllib
* How to make HTTP `GET` request
* How to make HTTP `POST`/`PUT`/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service


### Tasks

#### Task: 0-hbtn_status.py
Write a Python script that fetches `https://alx-intranet.hbtn.io/status`
* You must use the package `urllib`
* You are not allowed to import any packages other than `urllib`
* The body of the response must be displayed like the following example (tabulation before `-`)
* You must use a `with` statement

#### Task: 1-hbtn_header.py
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.
* You must use the packages `urllib` and `sys`
* You are not allow to import packages other than `urllib` and `sys`
* The value of this variable is different for each request
* You don’t need to check arguments passed to the script (number or type)
* You must use a `with` statement

#### Task: 2-post_email.py
Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)
* The email must be sent in the `email` variable
* You must use the packages `urllib` and `sys`
* You are not allowed to import packages other than `urllib` and `sys`
* You don’t need to check arguments passed to the script (number or type)
* You must use a `with` statement

#### Task: 3-error_code.py
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).
* You have to manage `urllib.error.HTTPError` exceptions and print: `Error code:` followed by the HTTP status code
* You must use the packages `urllib` and `sys`
* You are not allowed to import packages other than `urllib` and `sys`
* You don’t need to check arguments passed to the script (number or type)
* You must use a `with` statement

#### Task: 4-hbtn_status.py
Write a Python script that fetches `https://alx-intranet.hbtn.io/status`
* You must use the package `requests`
* You are not allow to import packages other than `requests`
* The body of the response must be display like the following example (tabulation before `-`)

#### Task: 5-hbtn_header.py
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header
* You must use the packages `requests` and `sys`
* You are not allow to import other packages than `requests` and `sys`
* The value of this variable is different for each request
* You don’t need to check script arguments (number and type)

#### Task: 6-post_email.py
Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.
* The `email` must be sent in the variable email
* You must use the packages `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`
* You don’t need to error check arguments passed to the script (number or type)

#### Task: 
**Technical interview prep:** 
Write a Python script that takes 2 arguments in order to solve this challenge:
```
Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”.
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/ 
Print all commits by: `<sha>: <author name>` (one by line)
```
* The first argument will be the `repository name`
* The second argument will be the `owner name`
* You must use the packages `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`
* You don’t need to check arguments passed to the script (number or type)

___


