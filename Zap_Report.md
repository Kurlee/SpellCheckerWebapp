
# ZAP Scanning Report




## Summary of Alerts

| Risk Level | Number of Alerts |
| --- | --- |
| High | 4 |
| Medium | 2 |
| Low | 13 |
| Informational | 0 |

## Alert Detail


  
  
  
### SQL Injection
##### High (Medium)
  
  
  
  
#### Description
<p>SQL injection may be possible.</p>
  
  
  
* URL: [http://192.168.7.30:8080/spell_check](http://192.168.7.30:8080/spell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrf_token`
  
  
  * Attack: `ImEzYjY1YjQxOTg5YTEzM2E0ODdhNWUxMTY3MzNkNzI4Y2IzYzZjYTQi.XbITOw.L9IJAUiSO75FhtrfCNduBzlONPY AND 1=1`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Findex+AND+1%3D1](http://192.168.7.30:8080/login?next=%2Findex+AND+1%3D1)
  
  
  * Method: `GET`
  
  
  * Parameter: `next`
  
  
  * Attack: `/index OR 1=1`
  
  
  
  
* URL: [http://192.168.7.30:8080/register](http://192.168.7.30:8080/register)
  
  
  * Method: `POST`
  
  
  * Parameter: `password`
  
  
  * Attack: ` ZAP OR 1=1 -- ' AND '1'='1' -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrf_token`
  
  
  * Attack: `IjYxNGU2YWM5YzJlNzdiZTJiNTBjMzBlZmVmNTU0NmM3Yzk5MDhmZWYi.XbC8WQ.TM4FPbi_zW5-ggkjwVD0OtCebSU OR 1=1 -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/register](http://192.168.7.30:8080/register)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrf_token`
  
  
  * Attack: `ImEzYjY1YjQxOTg5YTEzM2E0ODdhNWUxMTY3MzNkNzI4Y2IzYzZjYTQi.XbITjg.rwaIwtLSVpjjZ-Qi7Oc-3saOGJk" OR "1"="1" -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Fspell_check](http://192.168.7.30:8080/login?next=%2Fspell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `submit`
  
  
  * Attack: `Sign in%'  -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Fspell_check](http://192.168.7.30:8080/login?next=%2Fspell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `password`
  
  
  * Attack: `zakk1989' AND '1'='1' -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Fspell_check](http://192.168.7.30:8080/login?next=%2Fspell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `password`
  
  
  * Attack: `zakk1989%`
  
  
  
  
* URL: [http://192.168.7.30:8080/spell_check](http://192.168.7.30:8080/spell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrf_token`
  
  
  * Attack: `ImEzYjY1YjQxOTg5YTEzM2E0ODdhNWUxMTY3MzNkNzI4Y2IzYzZjYTQi.XbITOw.L9IJAUiSO75FhtrfCNduBzlONPY%'  -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrf_token`
  
  
  * Attack: `IjYxNGU2YWM5YzJlNzdiZTJiNTBjMzBlZmVmNTU0NmM3Yzk5MDhmZWYi.XbC8WQ.TM4FPbi_zW5-ggkjwVD0OtCebSU%`
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `password`
  
  
  * Attack: `zakk1989' OR '1'='1' -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/spell_check](http://192.168.7.30:8080/spell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrf_token`
  
  
  * Attack: `ImEzYjY1YjQxOTg5YTEzM2E0ODdhNWUxMTY3MzNkNzI4Y2IzYzZjYTQi.XbITOw.L9IJAUiSO75FhtrfCNduBzlONPY%"  -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Fspell_check](http://192.168.7.30:8080/login?next=%2Fspell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `password`
  
  
  * Attack: `zakk1989%"  -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/spell_check](http://192.168.7.30:8080/spell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `inputtext`
  
  
  * Attack: `+alert(1)+ OR 1=1 -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/register](http://192.168.7.30:8080/register)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrf_token`
  
  
  * Attack: `ImEzYjY1YjQxOTg5YTEzM2E0ODdhNWUxMTY3MzNkNzI4Y2IzYzZjYTQi.XbITjg.rwaIwtLSVpjjZ-Qi7Oc-3saOGJk' OR '1'='1`
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrf_token`
  
  
  * Attack: `IjYxNGU2YWM5YzJlNzdiZTJiNTBjMzBlZmVmNTU0NmM3Yzk5MDhmZWYi.XbC8WQ.TM4FPbi_zW5-ggkjwVD0OtCebSU' AND '1'='1' -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/spell_check](http://192.168.7.30:8080/spell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `submit`
  
  
  * Attack: `Submit' AND '1'='1`
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `submit`
  
  
  * Attack: `Sign in%'  -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Fspell_check](http://192.168.7.30:8080/login?next=%2Fspell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `submit`
  
  
  * Attack: `Sign in' OR '1'='1' -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/spell_check](http://192.168.7.30:8080/spell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrf_token`
  
  
  * Attack: `ImEzYjY1YjQxOTg5YTEzM2E0ODdhNWUxMTY3MzNkNzI4Y2IzYzZjYTQi.XbITOw.L9IJAUiSO75FhtrfCNduBzlONPY%'  -- `
  
  
  
  
Instances: 105
  
### Solution
<p>Do not trust client side input, even if there is client side validation in place.  </p><p>In general, type check all data on the server side.</p><p>If the application uses JDBC, use PreparedStatement or CallableStatement, with parameters passed by '?'</p><p>If the application uses ASP, use ADO Command Objects with strong type checking and parameterized queries.</p><p>If database Stored Procedures can be used, use them.</p><p>Do *not* concatenate strings into queries in the stored procedure, or use 'exec', 'exec immediate', or equivalent functionality!</p><p>Do not create dynamic SQL queries using simple string concatenation.</p><p>Escape all data received from the client.</p><p>Apply a 'whitelist' of allowed characters, or a 'blacklist' of disallowed characters in user input.</p><p>Apply the principle of least privilege by using the least privileged database user possible.</p><p>In particular, avoid using the 'sa' or 'db-owner' database users. This does not eliminate SQL injection, but minimizes its impact.</p><p>Grant the minimum database access that is necessary for the application.</p>
  
### Other information
<p>The page results were successfully manipulated using the boolean conditions [ImEzYjY1YjQxOTg5YTEzM2E0ODdhNWUxMTY3MzNkNzI4Y2IzYzZjYTQi.XbITOw.L9IJAUiSO75FhtrfCNduBzlONPY AND 1=1] and [ImEzYjY1YjQxOTg5YTEzM2E0ODdhNWUxMTY3MzNkNzI4Y2IzYzZjYTQi.XbITOw.L9IJAUiSO75FhtrfCNduBzlONPY AND 1=2]</p><p>The parameter value being modified was NOT stripped from the HTML output for the purposes of the comparison</p><p>Data was returned for the original parameter.</p><p>The vulnerability was detected by successfully restricting the data originally returned, by manipulating the parameter</p>
  
### Reference
* https://www.owasp.org/index.php/Top_10_2010-A1
* https://www.owasp.org/index.php/SQL_Injection_Prevention_Cheat_Sheet

  
#### CWE Id : 89
  
#### WASC Id : 19
  
#### Source ID : 1

  
  
  
### External Redirect
##### High (Medium)
  
  
  
  
#### Description
<p>URL redirectors represent common functionality employed by web sites to forward an incoming request to an alternate resource. This can be done for a variety of reasons and is often done to allow resources to be moved within the directory structure and to avoid breaking functionality for users that request the resource at its previous location. URL redirectors may also be used to implement load balancing, leveraging abbreviated URLs or recording outgoing links. It is this last implementation which is often used in phishing attacks as described in the example below. URL redirectors do not necessarily represent a direct security vulnerability but can be abused by attackers trying to social engineer victims into believing that they are navigating to a site other than the true destination.</p>
  
  
  
* URL: [http://192.168.7.30:8080/login?next=https%3A%5C%5C4690810286039808771.owasp.org](http://192.168.7.30:8080/login?next=https%3A%5C%5C4690810286039808771.owasp.org)
  
  
  * Method: `POST`
  
  
  * Parameter: `next`
  
  
  * Attack: `https:\\4690810286039808771.owasp.org`
  
  
  * Evidence: `https:\\4690810286039808771.owasp.org`
  
  
  
  
Instances: 1
  
### Solution
<p>Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a whitelist of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. Do not rely exclusively on looking for malicious or malformed inputs (i.e., do not rely on a blacklist). However, blacklists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.</p><p></p><p>When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if you are expecting colors such as "red" or "blue."</p><p></p><p>Use a whitelist of approved URLs or domains to be used for redirection.</p><p></p><p>Use an intermediate disclaimer page that provides the user with a clear warning that they are leaving your site. Implement a long timeout before the redirect occurs, or force the user to click on the link. Be careful to avoid XSS problems when generating the disclaimer page.</p><p></p><p>When the set of acceptable objects, such as filenames or URLs, is limited or known, create a mapping from a set of fixed input values (such as numeric IDs) to the actual filenames or URLs, and reject all other inputs.</p><p></p><p>For example, ID 1 could map to "/login.asp" and ID 2 could map to "http://www.example.com/". Features such as the ESAPI AccessReferenceMap provide this capability.</p><p></p><p>Understand all the potential areas where untrusted inputs can enter your software: parameters or arguments, cookies, anything read from the network, environment variables, reverse DNS lookups, query results, request headers, URL components, e-mail, files, databases, and any external systems that provide data to the application. Remember that such inputs may be obtained indirectly through API calls.</p><p></p><p>Many open redirect problems occur because the programmer assumed that certain inputs could not be modified, such as cookies and hidden form fields.</p>
  
### Other information
<p>The response contains a redirect in its Location header which allows an external Url to be set.</p>
  
### Reference
* http://projects.webappsec.org/URL-Redirector-Abuse
* http://cwe.mitre.org/data/definitions/601.html

  
#### CWE Id : 601
  
#### WASC Id : 38
  
#### Source ID : 1

  
  
  
### SQL Injection - Authentication Bypass
##### High (Medium)
  
  
  
  
#### Description
<p>SQL injection may be possible on a login page, potentially allowing the application's authentication mechanism to be bypassed </p>
  
  
  
* URL: [http://192.168.7.30:8080/login?next=/index](http://192.168.7.30:8080/login?next=/index)
  
  
  * Method: `GET`
  
  
  * Parameter: `next`
  
  
  * Attack: `/index OR 1=1 -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=/spell_check](http://192.168.7.30:8080/login?next=/spell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `next`
  
  
  * Attack: `/spell_check' OR '1'='1' -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=/spell_check](http://192.168.7.30:8080/login?next=/spell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrf_token`
  
  
  * Attack: `ImEzYjY1YjQxOTg5YTEzM2E0ODdhNWUxMTY3MzNkNzI4Y2IzYzZjYTQi.XbIS1A.sD5LkCRn4Hpv1dyr8xuBZiZ67pc" OR "1"="1`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=/spell_check](http://192.168.7.30:8080/login?next=/spell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrf_token`
  
  
  * Attack: `ImEzYjY1YjQxOTg5YTEzM2E0ODdhNWUxMTY3MzNkNzI4Y2IzYzZjYTQi.XbIS1A.sD5LkCRn4Hpv1dyr8xuBZiZ67pc AND 1=1 -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=/spell_check](http://192.168.7.30:8080/login?next=/spell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `submit`
  
  
  * Attack: `Sign in%'  -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=/spell_check](http://192.168.7.30:8080/login?next=/spell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrf_token`
  
  
  * Attack: `ImEzYjY1YjQxOTg5YTEzM2E0ODdhNWUxMTY3MzNkNzI4Y2IzYzZjYTQi.XbIS1A.sD5LkCRn4Hpv1dyr8xuBZiZ67pc" OR "1"="1" -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=/spell_check](http://192.168.7.30:8080/login?next=/spell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrf_token`
  
  
  * Attack: `ImEzYjY1YjQxOTg5YTEzM2E0ODdhNWUxMTY3MzNkNzI4Y2IzYzZjYTQi.XbIS1A.sD5LkCRn4Hpv1dyr8xuBZiZ67pc' AND '1'='1`
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `submit`
  
  
  * Attack: `Sign in AND 1=1 -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrf_token`
  
  
  * Attack: `IjYxNGU2YWM5YzJlNzdiZTJiNTBjMzBlZmVmNTU0NmM3Yzk5MDhmZWYi.XbC8WQ.TM4FPbi_zW5-ggkjwVD0OtCebSU OR 1=1 -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=/spell_check](http://192.168.7.30:8080/login?next=/spell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrf_token`
  
  
  * Attack: `ImEzYjY1YjQxOTg5YTEzM2E0ODdhNWUxMTY3MzNkNzI4Y2IzYzZjYTQi.XbIS1A.sD5LkCRn4Hpv1dyr8xuBZiZ67pc%'  -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=/spell_check](http://192.168.7.30:8080/login?next=/spell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `password`
  
  
  * Attack: `zakk1989%`
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `username`
  
  
  * Attack: `kurlee OR 1=1`
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `submit`
  
  
  * Attack: `Sign in%'  -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrf_token`
  
  
  * Attack: `IjYxNGU2YWM5YzJlNzdiZTJiNTBjMzBlZmVmNTU0NmM3Yzk5MDhmZWYi.XbC8WQ.TM4FPbi_zW5-ggkjwVD0OtCebSU' AND '1'='1' -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=/spell_check](http://192.168.7.30:8080/login?next=/spell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `next`
  
  
  * Attack: `/spell_check" AND "1"="1" -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `password`
  
  
  * Attack: `zakk1989%`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=/index](http://192.168.7.30:8080/login?next=/index)
  
  
  * Method: `GET`
  
  
  * Parameter: `next`
  
  
  * Attack: `/index OR 1=1`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=/spell_check](http://192.168.7.30:8080/login?next=/spell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `next`
  
  
  * Attack: `/spell_check AND 1=1 -- `
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `submit`
  
  
  * Attack: `Sign in' OR '1'='1`
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrf_token`
  
  
  * Attack: `IjYxNGU2YWM5YzJlNzdiZTJiNTBjMzBlZmVmNTU0NmM3Yzk5MDhmZWYi.XbC8WQ.TM4FPbi_zW5-ggkjwVD0OtCebSU AND 1=1 -- `
  
  
  
  
Instances: 47
  
### Solution
<p>Do not trust client side input, even if there is client side validation in place.  </p><p>In general, type check all data on the server side.</p><p>If the application uses JDBC, use PreparedStatement or CallableStatement, with parameters passed by '?'</p><p>If the application uses ASP, use ADO Command Objects with strong type checking and parameterized queries.</p><p>If database Stored Procedures can be used, use them.</p><p>Do *not* concatenate strings into queries in the stored procedure, or use 'exec', 'exec immediate', or equivalent functionality!</p><p>Do not create dynamic SQL queries using simple string concatenation.</p><p>Escape all data received from the client.</p><p>Apply a 'whitelist' of allowed characters, or a 'blacklist' of disallowed characters in user input.</p><p>Apply the principle of least privilege by using the least privileged database user possible.</p><p>In particular, avoid using the 'sa' or 'db-owner' database users. This does not eliminate SQL injection, but minimizes its impact.</p><p>Grant the minimum database access that is necessary for the application.</p>
  
### Reference
* https://www.owasp.org/index.php/Top_10_2010-A1
* https://www.owasp.org/index.php/SQL_Injection_Prevention_Cheat_Sheet

  
#### CWE Id : 89
  
#### WASC Id : 19
  
#### Source ID : 1

  
  
  
### Path Traversal
##### High (Medium)
  
  
  
  
#### Description
<p>The Path Traversal attack technique allows an attacker access to files, directories, and commands that potentially reside outside the web document root directory. An attacker may manipulate a URL in such a way that the web site will execute or reveal the contents of arbitrary files anywhere on the web server. Any device that exposes an HTTP-based interface is potentially vulnerable to Path Traversal.</p><p></p><p>Most web sites restrict user access to a specific portion of the file-system, typically called the "web document root" or "CGI root" directory. These directories contain the files intended for user access and the executable necessary to drive web application functionality. To access files or execute commands anywhere on the file-system, Path Traversal attacks will utilize the ability of special-characters sequences.</p><p></p><p>The most basic Path Traversal attack uses the "../" special-character sequence to alter the resource location requested in the URL. Although most popular web servers will prevent this technique from escaping the web document root, alternate encodings of the "../" sequence may help bypass the security filters. These method variations include valid and invalid Unicode-encoding ("..%u2216" or "..%c0%af") of the forward slash character, backslash characters ("..\") on Windows-based servers, URL encoded characters "%2e%2e%2f"), and double URL encoding ("..%255c") of the backslash character.</p><p></p><p>Even if the web server properly restricts Path Traversal attempts in the URL path, a web application itself may still be vulnerable due to improper handling of user-supplied input. This is a common problem of web applications that use template mechanisms or load static text from files. In variations of the attack, the original URL parameter value is substituted with the file name of one of the web application's dynamic scripts. Consequently, the results can reveal source code because the file is interpreted as text instead of an executable script. These techniques often employ additional special characters such as the dot (".") to reveal the listing of the current working directory, or "%00" NULL characters in order to bypass rudimentary file extension checks.</p>
  
  
  
* URL: [http://192.168.7.30:8080/login?next=login](http://192.168.7.30:8080/login?next=login)
  
  
  * Method: `POST`
  
  
  * Parameter: `next`
  
  
  * Attack: `login`
  
  
  
  
Instances: 1
  
### Solution
<p>Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a whitelist of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. Do not rely exclusively on looking for malicious or malformed inputs (i.e., do not rely on a blacklist). However, blacklists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.</p><p></p><p>When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if you are expecting colors such as "red" or "blue."</p><p></p><p>For filenames, use stringent whitelists that limit the character set to be used. If feasible, only allow a single "." character in the filename to avoid weaknesses, and exclude directory separators such as "/". Use a whitelist of allowable file extensions.</p><p></p><p>Warning: if you attempt to cleanse your data, then do so that the end result is not in the form that can be dangerous. A sanitizing mechanism can remove characters such as '.' and ';' which may be required for some exploits. An attacker can try to fool the sanitizing mechanism into "cleaning" data into a dangerous form. Suppose the attacker injects a '.' inside a filename (e.g. "sensi.tiveFile") and the sanitizing mechanism removes the character resulting in the valid filename, "sensitiveFile". If the input data are now assumed to be safe, then the file may be compromised. </p><p></p><p>Inputs should be decoded and canonicalized to the application's current internal representation before being validated. Make sure that your application does not decode the same input twice. Such errors could be used to bypass whitelist schemes by introducing dangerous inputs after they have been checked.</p><p></p><p>Use a built-in path canonicalization function (such as realpath() in C) that produces the canonical version of the pathname, which effectively removes ".." sequences and symbolic links.</p><p></p><p>Run your code using the lowest privileges that are required to accomplish the necessary tasks. If possible, create isolated accounts with limited privileges that are only used for a single task. That way, a successful attack will not immediately give the attacker access to the rest of the software or its environment. For example, database applications rarely need to run as the database administrator, especially in day-to-day operations.</p><p></p><p>When the set of acceptable objects, such as filenames or URLs, is limited or known, create a mapping from a set of fixed input values (such as numeric IDs) to the actual filenames or URLs, and reject all other inputs.</p><p></p><p>Run your code in a "jail" or similar sandbox environment that enforces strict boundaries between the process and the operating system. This may effectively restrict which files can be accessed in a particular directory or which commands can be executed by your software.</p><p></p><p>OS-level examples include the Unix chroot jail, AppArmor, and SELinux. In general, managed code may provide some protection. For example, java.io.FilePermission in the Java SecurityManager allows you to specify restrictions on file operations.</p><p></p><p>This may not be a feasible solution, and it only limits the impact to the operating system; the rest of your application may still be subject to compromise.</p>
  
### Reference
* http://projects.webappsec.org/Path-Traversal
* http://cwe.mitre.org/data/definitions/22.html

  
#### CWE Id : 22
  
#### WASC Id : 33
  
#### Source ID : 1

  
  
  
### X-Frame-Options Header Not Set
##### Medium (Medium)
  
  
  
  
#### Description
<p>X-Frame-Options header is not included in the HTTP response to protect against 'ClickJacking' attacks.</p>
  
  
  
* URL: [http://192.168.7.30:8080/](http://192.168.7.30:8080/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/index](http://192.168.7.30:8080/index)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2F](http://192.168.7.30:8080/login?next=%2F)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080](http://192.168.7.30:8080)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Findex](http://192.168.7.30:8080/login?next=%2Findex)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Findex](http://192.168.7.30:8080/login?next=%2Findex)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/register](http://192.168.7.30:8080/register)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/register](http://192.168.7.30:8080/register)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/spell_check](http://192.168.7.30:8080/spell_check)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/spell_check](http://192.168.7.30:8080/spell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2F](http://192.168.7.30:8080/login?next=%2F)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Fspell_check](http://192.168.7.30:8080/login?next=%2Fspell_check)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Fspell_check](http://192.168.7.30:8080/login?next=%2Fspell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
Instances: 15
  
### Solution
<p>Most modern Web browsers support the X-Frame-Options HTTP header. Ensure it's set on all web pages returned by your site (if you expect the page to be framed only by pages on your server (e.g. it's part of a FRAMESET) then you'll want to use SAMEORIGIN, otherwise if you never expect the page to be framed, you should use DENY. ALLOW-FROM allows specific websites to frame the web page in supported web browsers).</p>
  
### Reference
* http://blogs.msdn.com/b/ieinternals/archive/2010/03/30/combating-clickjacking-with-x-frame-options.aspx

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### Format String Error
##### Medium (Medium)
  
  
  
  
#### Description
<p>A Format String error occurs when the submitted data of an input string is evaluated as a command by the application. </p>
  
  
  
* URL: [http://192.168.7.30:8080/login?next=ZAP%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%0A](http://192.168.7.30:8080/login?next=ZAP%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%0A)
  
  
  * Method: `POST`
  
  
  * Parameter: `next`
  
  
  * Attack: `ZAP%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s%n%s
`
  
  
  
  
Instances: 1
  
### Solution
<p>Rewrite the background program using proper deletion of bad character strings.  This will require a recompile of the background executable.</p>
  
### Other information
<p>Potential Format String Error.  The script closed the connection on a /%s</p>
  
### Reference
* https://www.owasp.org/index.php/Format_string_attack

  
#### CWE Id : 134
  
#### WASC Id : 6
  
#### Source ID : 1

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [https://snippets.cdn.mozilla.net/us-west/bundles/bundle_210fdae28d0841557b9a21e1db94f3eab06d2b41.json](https://snippets.cdn.mozilla.net/us-west/bundles/bundle_210fdae28d0841557b9a21e1db94f3eab06d2b41.json)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 1
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### Incomplete or No Cache-control and Pragma HTTP Header Set
##### Low (Medium)
  
  
  
  
#### Description
<p>The cache-control and pragma HTTP header have not been set properly or are missing allowing the browser and proxies to cache content.</p>
  
  
  
* URL: [https://snippets.cdn.mozilla.net/us-west/bundles/bundle_210fdae28d0841557b9a21e1db94f3eab06d2b41.json](https://snippets.cdn.mozilla.net/us-west/bundles/bundle_210fdae28d0841557b9a21e1db94f3eab06d2b41.json)
  
  
  * Method: `GET`
  
  
  * Parameter: `Cache-Control`
  
  
  * Evidence: `max-age=2592000`
  
  
  
  
Instances: 1
  
### Solution
<p>Whenever possible ensure the cache-control HTTP header is set with no-cache, no-store, must-revalidate; and that the pragma HTTP header is set with no-cache.</p>
  
### Reference
* https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Web_Content_Caching

  
#### CWE Id : 525
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [http://detectportal.firefox.com/success.txt?ipv6](http://detectportal.firefox.com/success.txt?ipv6)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://detectportal.firefox.com/success.txt?ipv4](http://detectportal.firefox.com/success.txt?ipv4)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 2
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### Incomplete or No Cache-control and Pragma HTTP Header Set
##### Low (Medium)
  
  
  
  
#### Description
<p>The cache-control and pragma HTTP header have not been set properly or are missing allowing the browser and proxies to cache content.</p>
  
  
  
* URL: [https://blocklists.settings.services.mozilla.com/v1/blocklist/3/%7Bec8030f7-c20a-464f-9b0e-13a3a9e97384%7D/69.0.3/Firefox/20191009172106/Darwin_x86_64-gcc3/en-US/release/Darwin%2019.0.0/default/default/1/1/new/](https://blocklists.settings.services.mozilla.com/v1/blocklist/3/%7Bec8030f7-c20a-464f-9b0e-13a3a9e97384%7D/69.0.3/Firefox/20191009172106/Darwin_x86_64-gcc3/en-US/release/Darwin%2019.0.0/default/default/1/1/new/)
  
  
  * Method: `GET`
  
  
  * Parameter: `Cache-Control`
  
  
  
  
* URL: [https://blocklists.settings.services.mozilla.com/v1/blocklist/3/%7Bec8030f7-c20a-464f-9b0e-13a3a9e97384%7D/69.0.3/Firefox/20191009172106/Darwin_x86_64-gcc3/en-US/release/Darwin%2019.0.0/default/default/2/2/1/](https://blocklists.settings.services.mozilla.com/v1/blocklist/3/%7Bec8030f7-c20a-464f-9b0e-13a3a9e97384%7D/69.0.3/Firefox/20191009172106/Darwin_x86_64-gcc3/en-US/release/Darwin%2019.0.0/default/default/2/2/1/)
  
  
  * Method: `GET`
  
  
  * Parameter: `Cache-Control`
  
  
  
  
Instances: 2
  
### Solution
<p>Whenever possible ensure the cache-control HTTP header is set with no-cache, no-store, must-revalidate; and that the pragma HTTP header is set with no-cache.</p>
  
### Reference
* https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Web_Content_Caching

  
#### CWE Id : 525
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### Incomplete or No Cache-control and Pragma HTTP Header Set
##### Low (Medium)
  
  
  
  
#### Description
<p>The cache-control and pragma HTTP header have not been set properly or are missing allowing the browser and proxies to cache content.</p>
  
  
  
* URL: [https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css](https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `Cache-Control`
  
  
  * Evidence: `public, max-age=31536000`
  
  
  
  
Instances: 1
  
### Solution
<p>Whenever possible ensure the cache-control HTTP header is set with no-cache, no-store, must-revalidate; and that the pragma HTTP header is set with no-cache.</p>
  
### Reference
* https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Web_Content_Caching

  
#### CWE Id : 525
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css](https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 1
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [https://tracking-protection.cdn.mozilla.net/analytics-track-digest256/1570824682](https://tracking-protection.cdn.mozilla.net/analytics-track-digest256/1570824682)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://tracking-protection.cdn.mozilla.net/social-track-digest256/1570824682](https://tracking-protection.cdn.mozilla.net/social-track-digest256/1570824682)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://tracking-protection.cdn.mozilla.net/mozstd-trackwhite-digest256/1570824682](https://tracking-protection.cdn.mozilla.net/mozstd-trackwhite-digest256/1570824682)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://tracking-protection.cdn.mozilla.net/allow-flashallow-digest256/1490633678](https://tracking-protection.cdn.mozilla.net/allow-flashallow-digest256/1490633678)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://tracking-protection.cdn.mozilla.net/except-flashsubdoc-digest256/1517935265](https://tracking-protection.cdn.mozilla.net/except-flashsubdoc-digest256/1517935265)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://tracking-protection.cdn.mozilla.net/base-track-digest256/1570824682](https://tracking-protection.cdn.mozilla.net/base-track-digest256/1570824682)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://tracking-protection.cdn.mozilla.net/ads-track-digest256/1570824682](https://tracking-protection.cdn.mozilla.net/ads-track-digest256/1570824682)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://tracking-protection.cdn.mozilla.net/base-cryptomining-track-digest256/1559142673](https://tracking-protection.cdn.mozilla.net/base-cryptomining-track-digest256/1559142673)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://tracking-protection.cdn.mozilla.net/except-flashallow-digest256/1490633678](https://tracking-protection.cdn.mozilla.net/except-flashallow-digest256/1490633678)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://tracking-protection.cdn.mozilla.net/block-flash-digest256/1496263270](https://tracking-protection.cdn.mozilla.net/block-flash-digest256/1496263270)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://tracking-protection.cdn.mozilla.net/except-flash-digest256/1494877265](https://tracking-protection.cdn.mozilla.net/except-flash-digest256/1494877265)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://tracking-protection.cdn.mozilla.net/block-flashsubdoc-digest256/1512160865](https://tracking-protection.cdn.mozilla.net/block-flashsubdoc-digest256/1512160865)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [https://tracking-protection.cdn.mozilla.net/content-track-digest256/1559142673](https://tracking-protection.cdn.mozilla.net/content-track-digest256/1559142673)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 13
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [https://shavar.services.mozilla.com/downloads?client=navclient-auto-ffox&appver=69.0&pver=2.2](https://shavar.services.mozilla.com/downloads?client=navclient-auto-ffox&appver=69.0&pver=2.2)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 1
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### Web Browser XSS Protection Not Enabled
##### Low (Medium)
  
  
  
  
#### Description
<p>Web Browser XSS Protection is not enabled, or is disabled by the configuration of the 'X-XSS-Protection' HTTP response header on the web server</p>
  
  
  
* URL: [http://192.168.7.30:8080/favicon.ico](http://192.168.7.30:8080/favicon.ico)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Findex&zapHudReplaceReq=7c2d2ea7-3a16-4019-851b-8c611b0b3568](http://192.168.7.30:8080/login?next=%2Findex&zapHudReplaceReq=7c2d2ea7-3a16-4019-851b-8c611b0b3568)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://192.168.7.30:8080/index](http://192.168.7.30:8080/index)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://192.168.7.30:8080/register](http://192.168.7.30:8080/register)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://192.168.7.30:8080/register](http://192.168.7.30:8080/register)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Findex](http://192.168.7.30:8080/login?next=%2Findex)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Findex](http://192.168.7.30:8080/login?next=%2Findex)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://192.168.7.30:8080](http://192.168.7.30:8080)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://192.168.7.30:8080/spell_check](http://192.168.7.30:8080/spell_check)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Fspell_check](http://192.168.7.30:8080/login?next=%2Fspell_check)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://192.168.7.30:8080/spell_check](http://192.168.7.30:8080/spell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=ZAP%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%0A](http://192.168.7.30:8080/login?next=ZAP%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%0A)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://192.168.7.30:8080/sitemap.xml](http://192.168.7.30:8080/sitemap.xml)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2F](http://192.168.7.30:8080/login?next=%2F)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2F](http://192.168.7.30:8080/login?next=%2F)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://192.168.7.30:8080/](http://192.168.7.30:8080/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Fspell_check](http://192.168.7.30:8080/login?next=%2Fspell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://192.168.7.30:8080/robots.txt](http://192.168.7.30:8080/robots.txt)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://192.168.7.30:8080/static](http://192.168.7.30:8080/static)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
Instances: 21
  
### Solution
<p>Ensure that the web browser's XSS filter is enabled, by setting the X-XSS-Protection HTTP response header to '1'.</p>
  
### Other information
<p>The X-XSS-Protection HTTP response header allows the web server to enable or disable the web browser's XSS protection mechanism. The following values would attempt to enable it: </p><p>X-XSS-Protection: 1; mode=block</p><p>X-XSS-Protection: 1; report=http://www.example.com/xss</p><p>The following values would disable it:</p><p>X-XSS-Protection: 0</p><p>The X-XSS-Protection HTTP response header is currently supported on Internet Explorer, Chrome and Safari (WebKit).</p><p>Note that this alert is only raised if the response body could potentially contain an XSS payload (with a text-based content type, with a non-zero length).</p>
  
### Reference
* https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet
* https://www.veracode.com/blog/2014/03/guidelines-for-setting-security-headers/

  
#### CWE Id : 933
  
#### WASC Id : 14
  
#### Source ID : 3

  
  
  
### Absence of Anti-CSRF Tokens
##### Low (Medium)
  
  
  
  
#### Description
<p>No Anti-CSRF tokens were found in a HTML submission form.</p><p>A cross-site request forgery is an attack that involves forcing a victim to send an HTTP request to a target destination without their knowledge or intent in order to perform an action as the victim. The underlying cause is application functionality using predictable URL/form actions in a repeatable way. The nature of the attack is that CSRF exploits the trust that a web site has for a user. By contrast, cross-site scripting (XSS) exploits the trust that a user has for a web site. Like XSS, CSRF attacks are not necessarily cross-site, but they can be. Cross-site request forgery is also known as CSRF, XSRF, one-click attack, session riding, confused deputy, and sea surf.</p><p></p><p>CSRF attacks are effective in a number of situations, including:</p><p>    * The victim has an active session on the target site.</p><p>    * The victim is authenticated via HTTP auth on the target site.</p><p>    * The victim is on the same local network as the target site.</p><p></p><p>CSRF has primarily been used to perform an action against a target site using the victim's privileges, but recent techniques have been discovered to disclose information by gaining access to the response. The risk of information disclosure is dramatically increased when the target site is vulnerable to XSS, because XSS can be used as a platform for CSRF, allowing the attack to operate within the bounds of the same-origin policy.</p>
  
  
  
* URL: [http://192.168.7.30:8080/register](http://192.168.7.30:8080/register)
  
  
  * Method: `POST`
  
  
  * Evidence: `<form action="" method="post">`
  
  
  
  
* URL: [http://192.168.7.30:8080/spell_check](http://192.168.7.30:8080/spell_check)
  
  
  * Method: `GET`
  
  
  * Evidence: `<form action="" method="post">`
  
  
  
  
* URL: [http://192.168.7.30:8080/spell_check](http://192.168.7.30:8080/spell_check)
  
  
  * Method: `POST`
  
  
  * Evidence: `<form action="" method="post">`
  
  
  
  
* URL: [http://192.168.7.30:8080/register](http://192.168.7.30:8080/register)
  
  
  * Method: `GET`
  
  
  * Evidence: `<form action="" method="post">`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2F](http://192.168.7.30:8080/login?next=%2F)
  
  
  * Method: `GET`
  
  
  * Evidence: `<form action="" method="post" novalidate>`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2F](http://192.168.7.30:8080/login?next=%2F)
  
  
  * Method: `POST`
  
  
  * Evidence: `<form action="" method="post" novalidate>`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Fspell_check](http://192.168.7.30:8080/login?next=%2Fspell_check)
  
  
  * Method: `POST`
  
  
  * Evidence: `<form action="" method="post" novalidate>`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Fspell_check](http://192.168.7.30:8080/login?next=%2Fspell_check)
  
  
  * Method: `GET`
  
  
  * Evidence: `<form action="" method="post" novalidate>`
  
  
  
  
* URL: [http://192.168.7.30:8080](http://192.168.7.30:8080)
  
  
  * Method: `GET`
  
  
  * Evidence: `<form action="" method="post" novalidate>`
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `GET`
  
  
  * Evidence: `<form action="" method="post" novalidate>`
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `POST`
  
  
  * Evidence: `<form action="" method="post" novalidate>`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Findex](http://192.168.7.30:8080/login?next=%2Findex)
  
  
  * Method: `GET`
  
  
  * Evidence: `<form action="" method="post" novalidate>`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Findex](http://192.168.7.30:8080/login?next=%2Findex)
  
  
  * Method: `POST`
  
  
  * Evidence: `<form action="" method="post" novalidate>`
  
  
  
  
Instances: 13
  
### Solution
<p>Phase: Architecture and Design</p><p>Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid.</p><p>For example, use anti-CSRF packages such as the OWASP CSRFGuard.</p><p></p><p>Phase: Implementation</p><p>Ensure that your application is free of cross-site scripting issues, because most CSRF defenses can be bypassed using attacker-controlled script.</p><p></p><p>Phase: Architecture and Design</p><p>Generate a unique nonce for each form, place the nonce into the form, and verify the nonce upon receipt of the form. Be sure that the nonce is not predictable (CWE-330).</p><p>Note that this can be bypassed using XSS.</p><p></p><p>Identify especially dangerous operations. When the user performs a dangerous operation, send a separate confirmation request to ensure that the user intended to perform that operation.</p><p>Note that this can be bypassed using XSS.</p><p></p><p>Use the ESAPI Session Management control.</p><p>This control includes a component for CSRF.</p><p></p><p>Do not use the GET method for any request that triggers a state change.</p><p></p><p>Phase: Implementation</p><p>Check the HTTP Referer header to see if the request originated from an expected page. This could break legitimate functionality, because users or proxies may have disabled sending the Referer for privacy reasons.</p>
  
### Other information
<p>No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf] was found in the following HTML form: [Form 1: "csrf_token" "uname" "pword" "2fa" "submit" ].</p>
  
### Reference
* http://projects.webappsec.org/Cross-Site-Request-Forgery
* http://cwe.mitre.org/data/definitions/352.html

  
#### CWE Id : 352
  
#### WASC Id : 9
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2F](http://192.168.7.30:8080/login?next=%2F)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080](http://192.168.7.30:8080)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Findex](http://192.168.7.30:8080/login?next=%2Findex)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Findex](http://192.168.7.30:8080/login?next=%2Findex)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2F](http://192.168.7.30:8080/login?next=%2F)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/](http://192.168.7.30:8080/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Fspell_check](http://192.168.7.30:8080/login?next=%2Fspell_check)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/spell_check](http://192.168.7.30:8080/spell_check)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Fspell_check](http://192.168.7.30:8080/login?next=%2Fspell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/spell_check](http://192.168.7.30:8080/spell_check)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/static/style.css](http://192.168.7.30:8080/static/style.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/index](http://192.168.7.30:8080/index)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/register](http://192.168.7.30:8080/register)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://192.168.7.30:8080/register](http://192.168.7.30:8080/register)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 16
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### Application Error Disclosure
##### Low (Medium)
  
  
  
  
#### Description
<p>This page contains an error/warning message that may disclose sensitive information like the location of the file that produced the unhandled exception. This information can be used to launch further attacks against the web application. The alert could be a false positive if the error message is found inside a documentation page.</p>
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Findex](http://192.168.7.30:8080/login?next=%2Findex)
  
  
  * Method: `GET`
  
  
  * Evidence: `HTTP/1.1 500 INTERNAL SERVER ERROR`
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `GET`
  
  
  * Evidence: `HTTP/1.1 500 INTERNAL SERVER ERROR`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=ZAP%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%0A](http://192.168.7.30:8080/login?next=ZAP%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%0A)
  
  
  * Method: `POST`
  
  
  * Evidence: `HTTP/1.1 500 INTERNAL SERVER ERROR`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Findex&zapHudReplaceReq=7c2d2ea7-3a16-4019-851b-8c611b0b3568](http://192.168.7.30:8080/login?next=%2Findex&zapHudReplaceReq=7c2d2ea7-3a16-4019-851b-8c611b0b3568)
  
  
  * Method: `GET`
  
  
  * Evidence: `HTTP/1.1 500 INTERNAL SERVER ERROR`
  
  
  
  
Instances: 4
  
### Solution
<p>Review the source code of this page. Implement custom error pages. Consider implementing a mechanism to provide a unique error reference/identifier to the client (browser) while logging the details on the server side and not exposing them to the user.</p>
  
### Reference
* 

  
#### CWE Id : 200
  
#### WASC Id : 13
  
#### Source ID : 3

  
  
  
### Information Disclosure - Debug Error Messages
##### Low (Medium)
  
  
  
  
#### Description
<p>The response appeared to contain common error messages returned by platforms such as ASP.NET, and Web-servers such as IIS and Apache. You can configure the list of common debug messages.</p>
  
  
  
* URL: [http://192.168.7.30:8080/login?next=ZAP%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%0A](http://192.168.7.30:8080/login?next=ZAP%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%25n%25s%0A)
  
  
  * Method: `POST`
  
  
  * Evidence: `Internal Server Error`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Findex](http://192.168.7.30:8080/login?next=%2Findex)
  
  
  * Method: `GET`
  
  
  * Evidence: `Internal Server Error`
  
  
  
  
* URL: [http://192.168.7.30:8080/login](http://192.168.7.30:8080/login)
  
  
  * Method: `GET`
  
  
  * Evidence: `Internal Server Error`
  
  
  
  
* URL: [http://192.168.7.30:8080/login?next=%2Findex&zapHudReplaceReq=7c2d2ea7-3a16-4019-851b-8c611b0b3568](http://192.168.7.30:8080/login?next=%2Findex&zapHudReplaceReq=7c2d2ea7-3a16-4019-851b-8c611b0b3568)
  
  
  * Method: `GET`
  
  
  * Evidence: `Internal Server Error`
  
  
  
  
Instances: 4
  
### Solution
<p>Disable debugging messages before pushing to production.</p>
  
### Reference
* 

  
#### CWE Id : 200
  
#### WASC Id : 13
  
#### Source ID : 3
