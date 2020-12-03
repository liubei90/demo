```
W7TqKrGws6zMibVOdt5khjuOFhmDOrOoNOdac73g
QXEnImc0YpoyemmMDwKInEFniKwTG3zloWwRcFYJGh9J5DaCE777itvUieNBO2a4DEoATTDUCO5ZnKtfToLs3qJDhct9ycAdsXW8Gj7O3JQrdPXlr9LjBbmF50FT8axz
http://127.0.0.1:8000/noexist/callback

http://127.0.0.1:8000/o/authorize/?response_type=code&client_id=W7TqKrGws6zMibVOdt5khjuOFhmDOrOoNOdac73g&redirect_uri=http://127.0.0.1:8000/noexist/callback

curl -X POST -H "Cache-Control: no-cache" -H "Content-Type: application/x-www-form-urlencoded" "http://127.0.0.1:8000/o/token/" \
  -d "client_id=${ID}" -d "client_secret=W7TqKrGws6zMibVOdt5khjuOFhmDOrOoNOdac73g" -d "code=${CODE}" \
  -d "redirect_uri=http://127.0.0.1:8000/noexist/callback" -d "grant_type=authorization_code"


{
    "access_token": "Szlh8vXuKl8IDdEII8rVOOjYMt0Szq",
    "expires_in": 36000,
    "token_type": "Bearer",
    "scope": "read write",
    "refresh_token": "WKKcvGwXwSnUPTVcXbNCkDHSjanjfd"
}
```