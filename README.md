WebSockets Sample App
====

``WebSocketsSample`` is an app intended to demonstrate how websockets work, use as a starting point for a new websockets app, or help one learn more about websockets.  This implementation uses the [FastAPI|https://fastapi.tiangolo.com/] framework as it is replacing Flask.  My goal with the project was to learn more about FastAPI, ASGI, uvicorn, and websockets. The websockets code is based on the FastAPI [Docs|https://fastapi.tiangolo.com/advanced/websockets/].  This code is not intended for production use.

**ToDo:**
- [ ] Add real websockets client frontend with React, Angular, or X
- [ ] Research application security implications with websockets

## Getting Started

### Prerequisites
Make sure you have Docker and Python 3.x installed

### Clone the repo
```bash
git@github.com:dRy3vd/WebSocketsSample.git
```


### Build the container image
```bash
docker build -t wssimage .
```
* Run the container:

```bash
docker run -d --name wsscontainer -p 8000:80 wssimage
```

You should now be able to access the application:
http://localhost:8000

## License

This project is licensed under the terms of the MIT license.
