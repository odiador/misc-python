# MC Names
Some python codes that can verify if a minecraft name is already taken

Those codes use the request python library to go to the minecraft api and if the page doesn't exist, the username is free

It was made aprox. Q2 2022 but one day the api got updated so these codes don't work right now

Maybe in a future it could be updated and improved to the knowledge i have now

Before the api update, if a name was not found, the page doesn't get any response, but now it has

```
{
    "path": "/users/profiles/minecraft/<>",
    "errorMessage": "Couldn't find any profile with name X"
}
```
